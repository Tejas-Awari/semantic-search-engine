import faiss
import numpy as np
from app.config import settings

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(settings.VECTOR_DIM)
        self.documents = []
    def add(self, embeddings, docs):
        embeddings = np.array(embeddings).astype("float32")
        if embeddings.ndim == 1:
            embeddings = embeddings.reshape(1, -1)
        self.index.add(embeddings)
        self.documents.extend(docs)
    def search(self, query_vector, top_k):
        query_vector = np.array(query_vector).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)
        results = []
        for idx, doc_index in enumerate(indices[0]):
            results.append({
                "text": self.documents[doc_index],
                "score": float(distances[0][idx])
            })
        return results