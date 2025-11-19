"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Recommend APIs or libraries for creating a web catalog of building materials, including pergolas, stores, and portails, with features for filtering and searching products."
Generated: DETERMINISTIC_569893f884a84f43
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from enum import Enum

# Initialize FastAPI app
app = FastAPI(title="Building Materials Catalog API",
              description="API for managing a catalog of building materials including pergolas, stores, and portails",
              version="1.0.0")

# Database mock (in production, use a real database like PostgreSQL or MongoDB)
db = {
    "products": [
        {
            "id": 1,
            "name": "Wooden Pergola",
            "category": "pergola",
            "price": 499.99,
            "material": "wood",
            "dimensions": "10x10x8",
            "in_stock": True
        },
        {
            "id": 2,
            "name": "Metal Store Front",
            "category": "store",
            "price": 1299.99,
            "material": "metal",
            "dimensions": "12x8x10",
            "in_stock": False
        },
        {
            "id": 3,
            "name": "Glass Portail",
            "category": "portail",
            "price": 899.99,
            "material": "glass",
            "dimensions": "6x8",
            "in_stock": True
        }
    ]
}

# Enums for filtering
class ProductCategory(str, Enum):
    pergola = "pergola"
    store = "store"
    portail = "portail"

class MaterialType(str, Enum):
    wood = "wood"
    metal = "metal"
    glass = "glass"
    plastic = "plastic"

# Pydantic models for request/response validation
class Product(BaseModel):
    id: int
    name: str
    category: ProductCategory
    price: float
    material: MaterialType
    dimensions: str
    in_stock: bool

class ProductCreate(BaseModel):
    name: str
    category: ProductCategory
    price: float
    material: MaterialType
    dimensions: str
    in_stock: bool

# API endpoints
@app.get("/products/", response_model=List[Product])
async def get_products(
    category: Optional[ProductCategory] = None,
    material: Optional[MaterialType] = None,
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    in_stock: Optional[bool] = None,
    search: Optional[str] = None
):
    """Get filtered list of products"""
    products = db["products"]
    
    # Apply filters
    if category:
        products = [p for p in products if p["category"] == category.value]
    if material:
        products = [p for p in products if p["material"] == material.value]
    if min_price is not None:
        products = [p for p in products if p["price"] >= min_price]
    if max_price is not None:
        products = [p for p in products if p["price"] <= max_price]
    if in_stock is not None:
        products = [p for p in products if p["in_stock"] == in_stock]
    if search:
        products = [p for p in products if search.lower() in p["name"].lower()]
    
    return products

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Get a single product by ID"""
    product = next((p for p in db["products"] if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/", response_model=Product, status_code=201)
async def create_product(product: ProductCreate):
    """Create a new product"""
    new_id = max(p["id"] for p in db["products"]) + 1 if db["products"] else 1
    new_product = {
        "id": new_id,
        **product.dict()
    }
    db["products"].append(new_product)
    return new_product

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductCreate):
    """Update an existing product"""
    index = next((i for i, p in enumerate(db["products"]) if p["id"] == product_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    updated_product = {
        "id": product_id,
        **product.dict()
    }
    db["products"][index] = updated_product
    return updated_product

@app.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: int):
    """Delete a product"""
    index = next((i for i, p in enumerate(db["products"]) if p["id"] == product_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db["products"].pop(index)
    return None

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
