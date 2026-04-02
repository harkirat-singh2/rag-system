from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline


from app.config import settings


def load_vector_db():
    """Load existing Chroma vector database."""
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL
    )

    db = Chroma(
        persist_directory=settings.CHROMA_PATH,
        embedding_function=embeddings
    )

    return db


def create_retriever(db):
    """Create retriever from DB."""
    return db.as_retriever(
        search_kwargs={"k": settings.TOP_K}
    )


def load_llm():
    """Load HuggingFace LLM."""
    pipe = pipeline(
        "text-generation",
        model=settings.LLM_MODEL,
        max_new_tokens=256,
        temperature=0.3
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    return llm


def build_rag():
    db = load_vector_db()
    retriever = create_retriever(db)
    llm = load_llm()

    return retriever, llm


if __name__ == "__main__":
    retriever, llm = build_rag()

while True:
    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    # 🔹 Step 1: Rewrite query (better retrieval)
    rewrite_prompt = f"""
Rewrite this question to be more specific for document search.

Question: {query}
Rewritten:
"""
    better_query = llm.invoke(rewrite_prompt).strip()

    # 🔹 Step 2: Retrieve documents
    docs = retriever.invoke(better_query)

    # 🔹 Step 3: Filter noisy chunks
    docs = [doc for doc in docs if len(doc.page_content) > 50]
    docs = docs[:3]

    # 🔹 Step 4: Build context (limit size)
    context = "\n\n".join([doc.page_content[:300] for doc in docs])

    # 🔹 Step 5: Strong prompt
    prompt = f"""
You are an expert assistant.

Strict rules:
- Answer ONLY from the given context
- Do NOT add extra knowledge
- If answer not found → say "I don't know"
- Keep answer concise and structured

Context:
{context}

Question: {query}

Answer in bullet points:
"""

    # 🔹 Step 6: Generate answer
    result = llm.invoke(prompt).strip()
    result = result.replace("Answer:", "").strip()

    # 🔹 Step 7: Output
    print("\n🧠 Answer:")
    print(result)