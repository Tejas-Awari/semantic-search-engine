from fastapi import FastAPI
from app.schemas import SearchRequest, SearchResponse
from app.services import search

app = FastAPI(title="Semantic Search Engine")

@app.post("/search", response_model=SearchResponse)
def search_endpoint(request: SearchRequest):
    results = search(request.query, request.top_k)
    return {"results": results}