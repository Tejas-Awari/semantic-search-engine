from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    VECTOR_DIM: int = 384
    TOP_K: int = 5
    INDEX_PATH: str = "faiss.index"

    class Config:
        env_file = ".env"


settings = Settings()