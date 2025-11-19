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
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="Product Collections API",
    description="A REST API for managing product collections in an online store",
    version="1.0.0"
)

# Database simulation
class Database:
    def __init__(self):
        self.collections = []
        self.products = []

db = Database()

# Models
class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    price: float
    sku: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Premium Widget",
                "description": "A high-quality widget for all your needs",
                "price": 29.99,
                "sku": "WIDGET-001"
            }
        }

class Collection(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    products: List[UUID] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Summer Collection",
                "description": "Products perfect for summer",
                "products": []
            }
        }

class CollectionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Updated Summer Collection",
                "description": "Updated description"
            }
        }

# Helper functions
def get_collection(collection_id: UUID) -> Collection:
    """Retrieve a collection by ID or raise 404 if not found"""
    for collection in db.collections:
        if collection.id == collection_id:
            return collection
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Collection with id {collection_id} not found"
    )

def get_product(product_id: UUID) -> Product:
    """Retrieve a product by ID or raise 404 if not found"""
    for product in db.products:
        if product.id == product_id:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} not found"
    )

# Endpoints
@app.post("/collections/", response_model=Collection, status_code=status.HTTP_201_CREATED)
def create_collection(collection: Collection):
    """Create a new product collection"""
    db.collections.append(collection)
    return collection

@app.get("/collections/", response_model=List[Collection])
def list_collections():
    """List all product collections"""
    return db.collections

@app.get("/collections/{collection_id}", response_model=Collection)
def get_collection_by_id(collection_id: UUID):
    """Get a specific collection by ID"""
    return get_collection(collection_id)

@app.put("/collections/{collection_id}", response_model=Collection)
def update_collection(collection_id: UUID, collection_update: CollectionUpdate):
    """Update a collection's details"""
    collection = get_collection(collection_id)
    
    if collection_update.name is not None:
        collection.name = collection_update.name
    if collection_update.description is not None:
        collection.description = collection_update.description
    
    collection.updated_at = datetime.utcnow()
    return collection

@app.delete("/collections/{collection_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_collection(collection_id: UUID):
    """Delete a collection"""
    collection = get_collection(collection_id)
    db.collections.remove(collection)

@app.post("/collections/{collection_id}/products/{product_id}", response_model=Collection)
def add_product_to_collection(collection_id: UUID, product_id: UUID):
    """Add a product to a collection"""
    collection = get_collection(collection_id)
    product = get_product(product_id)
    
    if product.id in collection.products:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product already exists in collection"
        )
    
    collection.products.append(product.id)
    collection.updated_at = datetime.utcnow()
    return collection

@app.delete("/collections/{collection_id}/products/{product_id}", response_model=Collection)
def remove_product_from_collection(collection_id: UUID, product_id: UUID):
    """Remove a product from a collection"""
    collection = get_collection(collection_id)
    product = get_product(product_id)
    
    if product.id not in collection.products:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product not found in collection"
        )
    
    collection.products.remove(product.id)
    collection.updated_at = datetime.utcnow()
    return collection

@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    """Create a new product"""
    db.products.append(product)
    return product

@app.get("/products/", response_model=List[Product])
def list_products():
    """List all products"""
    return db.products

@app.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: UUID):
    """Get a specific product by ID"""
    return get_product(product_id)
```
