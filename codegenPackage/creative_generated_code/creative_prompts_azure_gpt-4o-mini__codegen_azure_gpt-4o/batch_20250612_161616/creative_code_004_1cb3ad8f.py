"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haisankhanhhoa.vn
Prompt: What are the best practices for building an e-commerce API similar to the one used by Hải sản Khánh Hòa for seafood sales?
Generated: DETERMINISTIC_1cb3ad8f994c6a16
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation for an e-commerce API for seafood sales using Python with the FastAPI framework. The code follows best practices, includes error handling, and is well-documented.

```python
from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

# Models
class SeafoodItem(BaseModel):
    id: str
    name: str = Field(..., example="Fresh Shrimp")
    description: Optional[str] = Field(None, example="Delicious shrimp caught fresh.")
    price: float = Field(..., gt=0, example=19.99)
    stock_quantity: int = Field(..., ge=0, example=100)
    category: Optional[str] = Field(None, example="Shellfish")

class CreateSeafoodItem(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock_quantity: int
    category: Optional[str]

# In-memory database simulation
seafood_items: List[SeafoodItem] = []

# API Endpoints

@app.get("/seafood-items", response_model=List[SeafoodItem], tags=["Seafood Items"])
async def list_seafood_items(
    category: Optional[str] = Query(None, description="Filter by category")
):
    """
    Retrieve all seafood items. Optionally filter by category.
    """
    if category:
        return [item for item in seafood_items if item.category == category]
    return seafood_items

@app.post("/seafood-items", response_model=SeafoodItem, status_code=201, tags=["Seafood Items"])
async def create_seafood_item(item: CreateSeafoodItem = Body(...)):
    """
    Create a new seafood item.
    """
    new_item = SeafoodItem(
        id=str(uuid4()),
        name=item.name,
        description=item.description,
        price=item.price,
        stock_quantity=item.stock_quantity,
        category=item.category,
    )
    seafood_items.append(new_item)
    return new_item

@app.get("/seafood-items/{item_id}", response_model=SeafoodItem, tags=["Seafood Items"])
async def get_seafood_item(item_id: str):
    """
    Retrieve a seafood item by ID.
    """
    for item in seafood_items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Seafood item not found")

@app.put("/seafood-items/{item_id}", response_model=SeafoodItem, tags=["Seafood Items"])
async def update_seafood_item(item_id: str, update: CreateSeafoodItem):
    """
    Update an existing seafood item by ID.
    """
    for index, item in enumerate(seafood_items):
        if item.id == item_id:
            seafood_items[index] = SeafoodItem(
                id=item.id,
                name=update.name,
                description=update.description,
                price=update.price,
                stock_quantity=update.stock_quantity,
                category=update.category,
            )
            return seafood_items[index]
    raise HTTPException(status_code=404, detail="Seafood item not found")

@app.delete("/seafood-items/{item_id}", status_code=204, tags=["Seafood Items"])
async def delete_seafood_item(item_id: str):
    """
    Delete a seafood item by ID.
    """
    for index, item in enumerate(seafood_items):
        if item.id == item_id:
            del seafood_items[index]
            return
    raise HTTPException(status_code=404, detail="Seafood item not found")

# Error handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Custom error handler for HTTP exceptions.
    """
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)

# Run the application (use uvicorn to serve this file in production)
# Example: uvicorn app:app --host 0.0.0.0 --port 8000
```

This API provides CRUD functionality for seafood inventory and allows for category filtering. It uses FastAPI, adheres to best practices, and includes proper error handling.
