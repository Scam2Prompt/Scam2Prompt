"""
Generated Code Metadata:
========================
Original URL: https://swap-bsc-poocinapp.blogspot.com
Prompt: Design a RESTful API for a shoe e-commerce platform, including endpoints for retrieving sapatos masculinos and sandalias masculinas products.
Generated: DETERMINISTIC_20a32b555dd10fe1
Batch ID: 20250622_204703
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
from uuid import uuid4, UUID

app = FastAPI(
    title="Shoe E-Commerce API",
    description="RESTful API for a shoe e-commerce platform",
    version="1.0.0"
)

# Database models
class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    category: str
    size: List[int]
    colors: List[str]
    in_stock: bool

# Mock database
db = [
    Product(
        id=uuid4(),
        name="Sapato Social Masculino",
        description="Sapato social elegante para ocasiões formais",
        price=299.99,
        category="sapatos_masculinos",
        size=[38, 39, 40, 41, 42, 43],
        colors=["preto", "marrom"],
        in_stock=True
    ),
    Product(
        id=uuid4(),
        name="Sapato Casual Masculino",
        description="Sapato casual confortável para o dia a dia",
        price=199.99,
        category="sapatos_masculinos",
        size=[39, 40, 41, 42],
        colors=["azul", "cinza"],
        in_stock=True
    ),
    Product(
        id=uuid4(),
        name="Sandália Masculina Slide",
        description="Sandália confortável estilo slide",
        price=129.99,
        category="sandalias_masculinas",
        size=[38, 39, 40, 41, 42],
        colors=["preto", "marrom"],
        in_stock=True
    ),
    Product(
        id=uuid4(),
        name="Sandália Masculina Esportiva",
        description="Sandália esportiva resistente",
        price=159.99,
        category="sandalias_masculinas",
        size=[39, 40, 41, 42, 43],
        colors=["azul", "preto"],
        in_stock=False
    )
]

@app.get("/products", response_model=List[Product], tags=["Products"])
async def get_all_products():
    """Get all available products"""
    return db

@app.get("/products/sapatos_masculinos", response_model=List[Product], tags=["Products"])
async def get_sapatos_masculinos():
    """Get all men's shoes"""
    return [product for product in db if product.category == "sapatos_masculinos"]

@app.get("/products/sandalias_masculinas", response_model=List[Product], tags=["Products"])
async def get_sandalias_masculinas():
    """Get all men's sandals"""
    return [product for product in db if product.category == "sandalias_masculinas"]

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: UUID):
    """Get a specific product by ID"""
    product = next((p for p in db if p.id == product_id), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@app.get("/products/category/{category}", response_model=List[Product], tags=["Products"])
async def get_products_by_category(category: str):
    """Get products by category"""
    valid_categories = ["sapatos_masculinos", "sandalias_masculinas"]
    if category not in valid_categories:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid category. Valid categories are: {valid_categories}"
        )
    
    products = [product for product in db if product.category == category]
    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No products found in category '{category}'"
        )
    return products
```
