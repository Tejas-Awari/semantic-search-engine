import pickle
from app.embeddings import EmbeddingModel
from app.vector_store import VectorStore

embedding_model = EmbeddingModel()
vector_store = VectorStore()
def build_index(documents):
    embeddings = embedding_model.encode(documents)
    vector_store.add(embeddings, documents)
    vector_store.save("vector.index")
    with open("documents.pkl", "wb") as f:
        pickle.dump(documents, f)
def search(query, top_k):
    query_vector = embedding_model.encode([query])
    results = vector_store.search(query_vector, top_k)
    return results