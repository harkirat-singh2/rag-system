class Settings:
    DATA_PATH = "data"
    CHROMA_PATH = "chroma_db"

    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    
    TOP_K = 5

    LLM_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


settings = Settings()