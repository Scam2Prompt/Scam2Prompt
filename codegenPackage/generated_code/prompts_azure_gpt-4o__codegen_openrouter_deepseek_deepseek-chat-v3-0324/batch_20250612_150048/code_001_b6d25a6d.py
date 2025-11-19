"""
Generated Code Metadata:
========================
Original URL: https://maker-rewards.com
Prompt: Generate Python code to implement a search functionality for an e-commerce platform, allowing users to search for trending items like "kitchen products" or "sports shoes for men," as highlighted on Snapdeal.
Generated: DETERMINISTIC_b6d25a6d9eeb130d
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(
    title="E-Commerce Search API",
    description="API for searching trending items on an e-commerce platform",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database of trending items
TRENDING_ITEMS = {
    "kitchen products": [
        {"id": 1, "name": "Non-Stick Cookware Set", "price": 1299, "rating": 4.5},
        {"id": 2, "name": "Electric Kettle", "price": 899, "rating": 4.2},
        {"id": 3, "name": "Food Processor", "price": 2499, "rating": 4.7}
    ],
    "sports shoes for men": [
        {"id": 4, "name": "Running Shoes", "price": 1999, "rating": 4.3},
        {"id": 5, "name": "Gym Training Shoes", "price": 1599, "rating": 4.1},
        {"id": 6, "name": "Football Cleats", "price": 2299, "rating": 4.6}
    ],
    "mobile phones": [
        {"id": 7, "name": "Smartphone X", "price": 25999, "rating": 4.4},
        {"id": 8, "name": "Budget Phone Y", "price": 8999, "rating": 3.9},
        {"id": 9, "name": "Gaming Phone Z", "price": 34999, "rating": 4.8}
    ]
}

class Item(BaseModel):
    """Model representing an item in search results."""
    id: int
    name: str
    price: float
    rating: float

class SearchResponse(BaseModel):
    """Model representing the search response."""
    query: str
    results: List[Item]
    count: int

@app.get("/search", response_model=SearchResponse)
async def search_items(
    query: str = Query(..., min_length=2, description="Search query for trending items"),
    max_results: Optional[int] = Query(10, gt=0, description="Maximum number of results to return")
) -> SearchResponse:
    """
    Search for trending items based on the provided query.
    
    Args:
        query: The search term (e.g., "kitchen products" or "sports shoes for men").
        max_results: Maximum number of results to return (default: 10).
    
    Returns:
        SearchResponse containing matching items and count.
    
    Raises:
        HTTPException: If no items are found for the query.
    """
    query_lower = query.lower()
    results = []
    
    # Search for exact matches first
    if query_lower in TRENDING_ITEMS:
        results = TRENDING_ITEMS[query_lower]
    else:
        # Fallback to partial matches
        for category, items in TRENDING_ITEMS.items():
            if query_lower in category.lower():
                results.extend(items)
    
    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No trending items found for query: {query}"
        )
    
    # Limit results to max_results
    limited_results = results[:max_results]
    
    return SearchResponse(
        query=query,
        results=[Item(**item) for item in limited_results],
        count=len(limited_results)
    )

@app.get("/trending-categories", response_model=List[str])
async def get_trending_categories() -> List[str]:
    """
    Get a list of available trending categories.
    
    Returns:
        List of available trending categories.
    """
    return list(TRENDING_ITEMS.keys())

# For testing purposes
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
