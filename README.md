# 🧠 RAG Chat System (Fully Local + Free)

A **full-stack Retrieval-Augmented Generation (RAG) application** that allows users to query their documents using a local LLM powered by Hugging Face Transformers.

Built with a production-style architecture using **FastAPI, ChromaDB, and a custom RAG pipeline** — no paid APIs required.

---

## 🚀 Features

* 📄 **Document Ingestion Pipeline**

  * PDF → Chunking → Embeddings → Vector DB
* 🔍 **Semantic Search (ChromaDB)**
* 🤖 **Local LLM (Hugging Face Transformers)**
* 🧠 **Query Rewriting for Better Retrieval**
* 💬 **Conversational Memory (Chat History)**
* 🌐 **FastAPI Backend**
* 🎨 **Dark Themed Frontend (HTML + Tailwind + JS)**
* ⚡ **Fully Free & Runs Locally**

---

## 🏗️ Architecture

```
User Query
   ↓
Query Rewriting
   ↓
Vector Search (ChromaDB)
   ↓
Top-K Retrieval
   ↓
Context + Chat History
   ↓
LLM (TinyLlama / HF Model)
   ↓
Final Answer
```

---

## 📁 Project Structure

```
rag-system/
│
├── app/
│   ├── main.py              # FastAPI backend
│   ├── ingest.py            # Document ingestion pipeline
│   ├── rag_pipeline.py      # RAG logic (retrieval + LLM)
│   ├── config.py            # Configurations
│
├── frontend/
│   ├── index.html           # UI (Tailwind)
│   ├── script.js            # API calls
│
├── data/                    # Input PDFs
├── chroma_db/               # Vector database
│
├── pyproject.toml
├── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone repo

```
git clone <your-repo-url>
cd rag-system
```

---

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

OR (recommended with uv):

```
uv add langchain langchain-community langchain-huggingface langchain-chroma transformers sentence-transformers chromadb fastapi uvicorn pypdf torch
```

---

## 📥 Ingest Documents

Add PDFs to:

```
data/
```

Run:

```
python -m app.ingest
```

---

## ▶️ Run Backend

```
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Run Frontend

Open:

```
frontend/index.html
```

(Or use Live Server)

---

## 🧪 Example Query

```
What skills are mentioned?
```

---

## 🔥 Tech Stack

* **LLM:** Hugging Face Transformers (TinyLlama / Mistral)
* **Embeddings:** Sentence Transformers
* **Vector DB:** ChromaDB
* **Backend:** FastAPI
* **Frontend:** HTML + Tailwind CSS + JavaScript
* **Pipeline:** LangChain (modular usage)

---

## 🧠 Key Concepts Implemented

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Query Rewriting
* Context Filtering
* Prompt Engineering
* Conversational Memory

---

## ⚠️ Limitations

* In-memory chat history (resets on restart)
* No authentication
* Basic UI (can be improved)

---

## 🚀 Future Improvements

* Persistent memory (database)
* Hybrid search (BM25 + vector)
* Streaming responses
* Deployment (Docker / Cloud)
* Advanced UI (React)

---

## 💡 Why This Project Matters

This project demonstrates:

* End-to-end LLM application design
* Backend + AI integration
* Real-world system architecture
* Ability to work without paid APIs

---

## 👨‍💻 Author

**Harkirat Singh**
Generative AI Engineer

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to fork!
