# 📘 AI Medical Chatbot — Setup & Usage Instructions

This guide will help you install, configure, and run the AI Medical Chatbot on your local machine.

---

## ✅ Prerequisites

- Python 3.8 or higher
- Git (optional, for cloning the repository)
- Internet connection (for initial model downloads)

---


## 🛠️ Setup Instructions

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Add your medical PDFs** to the `data/` directory.

4. **Generate vector database**:
    ```bash
    python ingest.py
    ```

5. **Start the chatbot using Chainlit**:
    ```bash
    chainlit run model.py -w
    ```

6. Open your browser at `http://localhost:8000` to interact with the bot!

## 🧠 Model Used

- **LLM**: `llama-2-7b-chat.ggmlv3.q8_0.bin` via `CTransformers`
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Store**: FAISS

> Make sure the LLaMA model file is downloaded and placed in your working directory or correctly referenced.

## 🔍 Example Query

> **User**: "What are the symptoms of diabetes?"
>
> **Bot**: "The common symptoms of diabetes include increased thirst, frequent urination, extreme fatigue, and blurred vision..."

## 📚 Resources

- [LangChain Documentation](https://docs.langchain.com/)
- [Chainlit Documentation](https://docs.chainlit.io)
- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)

---

🧑‍💻 Built with ❤️ by [Divyanshu Tewari]


