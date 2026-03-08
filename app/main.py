from fastapi import FastAPI
from app.schemas import SearchRequest, SearchResponse
from app.services import search, build_index

app = FastAPI(title="Semantic Search Engine")

with open("data/documents.txt") as f:
    documents = [line.strip() for line in f if line.strip()]
build_index(documents)

@app.post("/search", response_model=SearchResponse)
def search_endpoint(request: SearchRequest):
    results = search(request.query, request.top_k)
    return {"results": results}