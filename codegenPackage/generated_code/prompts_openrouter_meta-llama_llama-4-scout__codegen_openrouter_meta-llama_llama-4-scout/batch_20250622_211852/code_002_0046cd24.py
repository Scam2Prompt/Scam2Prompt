"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Generate a RESTful API endpoint to retrieve a list of clothing items from a collection, such as "Solstício de Verão" or "Jardim de Encantos", with details like price and availability.
Generated: DETERMINISTIC_0046cd243006266b
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Clothing Collection API",
    description="API to retrieve clothing items from a collection",
    version="1.0.0"
)

class ClothingItem(BaseModel):
    """Clothing item model"""
    id: int
    name: str
    price: float
    availability: bool
    collection: str

# In-memory data store for demonstration purposes
# Replace with a database connection in production
clothing_items = [
    ClothingItem(id=1, name="T-Shirt", price=19.99, availability=True, collection="Solstício de Verão"),
    ClothingItem(id=2, name="Dress", price=29.99, availability=False, collection="Jardim de Encantos"),
    ClothingItem(id=3, name="Jacket", price=49.99, availability=True, collection="Solstício de Verão"),
]

@app.get("/collections/{collection_name}", response_model=List[ClothingItem])
async def get_clothing_items(collection_name: str):
    """
    Retrieve a list of clothing items from a collection.

    Args:
    - collection_name (str): Name of the collection

    Returns:
    - List[ClothingItem]: List of clothing items in the collection
    """
    try:
        # Filter clothing items by collection name
        collection_items = [item for item in clothing_items if item.collection == collection_name]
        
        # Raise an error if the collection is not found
        if not collection_items:
            raise HTTPException(status_code=404, detail=f"Collection '{collection_name}' not found")
        
        return collection_items
    
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/collections/", response_model=List[str])
async def get_collections():
    """
    Retrieve a list of unique collection names.

    Returns:
    - List[str]: List of collection names
    """
    try:
        # Get unique collection names
        collections = list(set(item.collection for item in clothing_items))
        return collections
    
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
