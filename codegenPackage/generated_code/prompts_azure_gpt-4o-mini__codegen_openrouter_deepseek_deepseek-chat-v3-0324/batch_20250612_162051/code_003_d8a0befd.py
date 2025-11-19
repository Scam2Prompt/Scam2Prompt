"""
Generated Code Metadata:
========================
Original URL: https://zkoutdoor.pk
Prompt: Develop a RESTful API endpoint for managing inventory in a furniture e-commerce application, allowing for CRUD operations on products such as sofas and hanging lamps.
Generated: DETERMINISTIC_d8a0befd47b22a47
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI()

# Database mock (in-memory storage)
inventory_db = []

# Enums and Models
class ProductCategory(str, Enum):
    SOFA = "sofa"
    HANGING_LAMP = "hanging_lamp"

class Product(BaseModel):
    id: UUID
    name: str
    category: ProductCategory
    price: float
    quantity: int
    description: Optional[str] = None

class ProductCreate(BaseModel):
    name: str
    category: ProductCategory
    price: float
    quantity: int
    description: Optional[str] = None

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[ProductCategory] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    description: Optional[str] = None

# Helper functions
def find_product(product_id: UUID):
    for index, product in enumerate(inventory_db):
        if product.id == product_id:
            return index, product
    return None, None

# API Endpoints
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    """
    Create a new product in inventory.
    """
    new_product = Product(
        id=uuid4(),
        name=product.name,
        category=product.category,
        price=product.price,
        quantity=product.quantity,
        description=product.description
    )
    inventory_db.append(new_product)
    return new_product

@app.get("/products/", response_model=List[Product])
def list_products(category: Optional[ProductCategory] = None):
    """
    List all products, optionally filtered by category.
    """
    if category:
        return [product for product in inventory_db if product.category == category]
    return inventory_db

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: UUID):
    """
    Get a specific product by ID.
    """
    _, product = find_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: UUID, product_update: ProductUpdate):
    """
    Update a product's information.
    """
    index, product = find_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    update_data = product_update.dict(exclude_unset=True)
    updated_product = product.copy(update=update_data)
    inventory_db[index] = updated_product
    return updated_product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: UUID):
    """
    Delete a product from inventory.
    """
    index, product = find_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    inventory_db.pop(index)
    return None
```
