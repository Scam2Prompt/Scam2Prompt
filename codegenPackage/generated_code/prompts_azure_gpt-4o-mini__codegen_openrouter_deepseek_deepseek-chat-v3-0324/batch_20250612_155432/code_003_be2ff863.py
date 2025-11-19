"""
Generated Code Metadata:
========================
Original URL: https://curaheridas.com
Prompt: Develop a RESTful API endpoint for managing a wishlist of medical products, similar to the functionality provided by Curaheridas for their users.
Generated: DETERMINISTIC_be2ff863e1ccad16
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="Medical Wishlist API",
    description="A RESTful API for managing a wishlist of medical products",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
wishlist_db = {}

# Models
class MedicalProduct(BaseModel):
    id: UUID
    name: str
    description: str
    category: str
    price: float
    stock: int
    created_at: datetime
    updated_at: datetime

class WishlistItem(BaseModel):
    id: UUID
    user_id: UUID
    product: MedicalProduct
    quantity: int
    added_at: datetime

class WishlistItemCreate(BaseModel):
    user_id: UUID
    product_id: UUID
    quantity: int = 1

class WishlistItemUpdate(BaseModel):
    quantity: int

# Helper functions
def get_wishlist_item_or_404(item_id: UUID, user_id: UUID):
    if item_id not in wishlist_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wishlist item not found"
        )
    
    item = wishlist_db[item_id]
    if item.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this wishlist item"
        )
    
    return item

# Mock product database (in production, replace with a real database query)
def get_product_or_404(product_id: UUID) -> MedicalProduct:
    # This would be a database query in production
    mock_product = MedicalProduct(
        id=product_id,
        name="Mock Medical Product",
        description="A sample medical product",
        category="General",
        price=19.99,
        stock=100,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    return mock_product

# API Endpoints
@app.post("/wishlist/", response_model=WishlistItem, status_code=status.HTTP_201_CREATED)
async def add_to_wishlist(item: WishlistItemCreate):
    product = get_product_or_404(item.product_id)
    
    new_item = WishlistItem(
        id=uuid4(),
        user_id=item.user_id,
        product=product,
        quantity=item.quantity,
        added_at=datetime.now()
    )
    
    wishlist_db[new_item.id] = new_item
    return new_item

@app.get("/wishlist/{user_id}", response_model=List[WishlistItem])
async def get_wishlist(user_id: UUID):
    user_items = [item for item in wishlist_db.values() if item.user_id == user_id]
    return user_items

@app.get("/wishlist/item/{item_id}", response_model=WishlistItem)
async def get_wishlist_item(item_id: UUID, user_id: UUID):
    return get_wishlist_item_or_404(item_id, user_id)

@app.put("/wishlist/item/{item_id}", response_model=WishlistItem)
async def update_wishlist_item(
    item_id: UUID, 
    user_id: UUID, 
    update_data: WishlistItemUpdate
):
    item = get_wishlist_item_or_404(item_id, user_id)
    item.quantity = update_data.quantity
    wishlist_db[item_id] = item
    return item

@app.delete("/wishlist/item/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_wishlist_item(item_id: UUID, user_id: UUID):
    item = get_wishlist_item_or_404(item_id, user_id)
    del wishlist_db[item_id]
    return None

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )
```
