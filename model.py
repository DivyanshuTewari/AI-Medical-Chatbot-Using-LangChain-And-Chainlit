from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl
import torch  # For checking GPU availability

DB_FAISS_PATH = "vectorstores/db_faiss"

custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, please just say that you don't know the answer, don't try to make up
an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vector store.
    """
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt

def load_llm():
    # Check for GPU and use it if available
    device = "cuda" if torch.cuda.is_available() else "cpu"

    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5,
        device=device  # Set device to GPU (cuda) or CPU
    )
    return llm  

def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )
    return qa_chain

def qa_bot():
    # Check for GPU and use it for embeddings
    device = "cuda" if torch.cuda.is_available() else "cpu"

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', 
                                      model_kwargs={'device': device})  # Use GPU if available

    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)
    return qa  

def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response

## Chainlit ##
@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome to the Medical Bot. What is your query?"
    await msg.update()
    # Set the chain object in user session with the correct value
    cl.user_session.set("chain", chain)
    
@cl.on_message
async def main(message):
    # Get the chain object from user session
    chain = cl.user_session.get("chain")
    
    # Extract the text content from the message object
    user_message = message.content  # Use .content instead of .text
    
    # Prepare the callback handler
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens={"FINAL", "ANSWER"}
    )
    cb.answer_reached = True
    
    # Pass the user message (as a string) to the chain
    res = await chain.acall({"query": user_message}, callbacks=[cb])  # Pass as a dictionary with the 'query' key
    
    answer = res["result"]
    
    
    
    
    # Send the answer back to the user
    await cl.Message(content=answer).send()


