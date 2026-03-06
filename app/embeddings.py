from sentence_transformers import SentenceTransformer
from app.config import settings


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(settings.MODEL_NAME)

    def encode(self, texts):
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings