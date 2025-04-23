# 🧠 AI Medical Chatbot Using LangChain & Chainlit

This project is an **AI-powered medical chatbot** built using **LangChain**, **Chainlit**, and **local LLMs**. It allows users to ask health-related questions and receive context-aware responses based on ingested medical documents (PDFs).

## 🚀 Features

- 💬 Chat interface powered by **Chainlit**
- 🔍 Intelligent context-aware QA using **LangChain RetrievalQA**
- 🧠 Uses **LLaMA 2 (7B)** with `CTransformers`
- 🧾 Document ingestion from PDFs into a **FAISS vector database**
- ⚡ GPU support for faster inference and embeddings
- 🧠 Custom prompt engineering for better accuracy

## 🖼️ GUI Overview

The chatbot includes a clean, browser-based chat interface powered by Chainlit. Here's what you can expect:

### 🔷 Key UI Elements

- 📝 Welcome Message  
  A custom welcome screen (defined in chainlit.md) provides an intro or greeting when users land on the app.

- 💬 Chat Input Box  
  Type any medical question here, such as:
  > What are the symptoms of diabetes?

- 🤖 Chatbot Response Area  
  Displays AI-generated responses derived from the ingested PDF documents.

- 📚 Context Awareness  
  The chatbot retrieves relevant content from the vector database to provide evidence-backed answers.

![GUI Screenshot]
![image](https://github.com/user-attachments/assets/1eb308c0-5cc1-45f5-aa94-94d37b9722a8)



## 📁 Project Structure

├── model.py           # Core chatbot logic with LangChain and LLM
├── ingest.py          # Script to ingest PDF data into FAISS vector DB
├── chainlit.md        # Custom welcome screen content for Chainlit
├── requirements.txt   # Python dependency file
├── data/              # Folder containing medical PDF documents
├── vectorstores/      # FAISS vector database storage
└── README.md          # Project overview

