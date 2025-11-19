"""
Generated Code Metadata:
========================
Original URL: https://zellerscanada.ca
Prompt: Develop a REST API endpoint for managing product collections in an online store, inspired by the Zellers catalog structure.
Generated: DETERMINISTIC_088aaa820a10c8e1
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

app = FastAPI(
    title="Product Collection API",
    description="Manage product collections in an online store",
    version="1.0.0"
)

# Data models
class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float

class Collection(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    products: List[Product]

# In-memory data store (replace with a database in production)
collections: dict[UUID, Collection] = {}
products: dict[UUID, Product] = {}

# Create a new product
@app.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    # Check for duplicate product ID
    if product.id in products:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product with this ID already exists")

    products[product.id] = product
    return product

# Get a product by ID
@app.get("/products/{product_id}")
async def get_product(product_id: UUID):
    product = products.get(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

# Create a new collection
@app.post("/collections", status_code=status.HTTP_201_CREATED)
async def create_collection(collection: Collection):
    # Check for duplicate collection ID
    if collection.id in collections:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Collection with this ID already exists")

    # Validate products in collection
    for product in collection.products:
        if product.id not in products:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Product {product.id} not found")

    collections[collection.id] = collection
    return collection

# Get a collection by ID
@app.get("/collections/{collection_id}")
async def get_collection(collection_id: UUID):
    collection = collections.get(collection_id)
    if not collection:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collection not found")
    return collection

# Update a collection
@app.put("/collections/{collection_id}")
async def update_collection(collection_id: UUID, updated_collection: Collection):
    if collection_id not in collections:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collection not found")

    # Validate products in collection
    for product in updated_collection.products:
        if product.id not in products:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Product {product.id} not found")

    collections[collection_id] = updated_collection
    return updated_collection

# Delete a collection
@app.delete("/collections/{collection_id}")
async def delete_collection(collection_id: UUID):
    if collection_id not in collections:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collection not found")

    del collections[collection_id]
    return {"message": "Collection deleted"}

# Add product to collection
@app.post("/collections/{collection_id}/products")
async def add_product_to_collection(collection_id: UUID, product_id: UUID):
    if collection_id not in collections:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collection not found")

    if product_id not in products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    collection = collections[collection_id]
    collection.products.append(products[product_id])
    collections[collection_id] = collection
    return collection

# Remove product from collection
@app.delete("/collections/{collection_id}/products/{product_id}")
async def remove_product_from_collection(collection_id: UUID, product_id: UUID):
    if collection_id not in collections:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collection not found")

    collection = collections[collection_id]
    collection.products = [product for product in collection.products if product.id != product_id]
    collections[collection_id] = collection
    return collection
```
