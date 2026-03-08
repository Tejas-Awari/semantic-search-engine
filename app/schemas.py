from pydantic import BaseModel
from typing import List

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
class SearchResult(BaseModel):
    text: str
    score: float
class SearchResponse(BaseModel):
    results: List[SearchResult]