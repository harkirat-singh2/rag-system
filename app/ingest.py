from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from app.config import settings


def load_documents(file_path: str):
    """Load documents from a PDF file."""
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


def split_documents(documents):
    """Split documents into smaller chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(documents)
    return chunks


def create_embeddings():
    """Initialize embedding model."""
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL
    )


def store_in_vector_db(chunks, embeddings):
    """Store chunks into Chroma vector database."""
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=settings.CHROMA_PATH,
    )
    return db


def ingest(file_path: str):
    """Full ingestion pipeline."""
    print(f"📄 Loading: {file_path}")

    documents = load_documents(file_path)
    print(f"Loaded {len(documents)} documents")

    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    embeddings = create_embeddings()
    print("Embeddings model initialized")

    store_in_vector_db(chunks, embeddings)
    print("✅ Data stored in vector DB")


if __name__ == "__main__":
    data_path = Path(settings.DATA_PATH)

    for file in data_path.glob("*.pdf"):
        ingest(str(file))