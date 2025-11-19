"""
Generated Code Metadata:
========================
Original URL: https://www.matinshop.dk
Prompt: Design a RESTful API that provides information about various hair and beard care products, ensuring it includes details on their benefits and usage, similar to the descriptions found on Matin Shop.
Generated: DETERMINISTIC_d401936db630a909
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
from uuid import uuid4, UUID

app = FastAPI(
    title="Hair & Beard Care Products API",
    description="A RESTful API providing information about various hair and beard care products, including their benefits and usage.",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@haircareapi.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database mock (in a real application, this would be a proper database)
products_db = []

# Models
class ProductBase(BaseModel):
    name: str
    brand: str
    category: str  # e.g., shampoo, conditioner, beard oil
    description: str
    benefits: List[str]
    usage_instructions: str
    ingredients: Optional[List[str]] = None
    price: float
    size: str  # e.g., "100ml", "8oz"

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: UUID

# Helper function to find product by ID
def get_product_by_id(product_id: UUID):
    for product in products_db:
        if product["id"] == product_id:
            return product
    return None

# Endpoints
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    """
    Create a new hair or beard care product entry.
    """
    product_data = product.dict()
    product_data["id"] = uuid4()
    products_db.append(product_data)
    return product_data

@app.get("/products/", response_model=List[Product])
def read_products(category: Optional[str] = None, brand: Optional[str] = None):
    """
    Get a list of all products, optionally filtered by category or brand.
    """
    filtered_products = products_db
    if category:
        filtered_products = [p for p in filtered_products if p["category"].lower() == category.lower()]
    if brand:
        filtered_products = [p for p in filtered_products if p["brand"].lower() == brand.lower()]
    return filtered_products

@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: UUID):
    """
    Get detailed information about a specific product by its ID.
    """
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: UUID, product: ProductCreate):
    """
    Update an existing product's information.
    """
    existing_product = get_product_by_id(product_id)
    if not existing_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    update_data = product.dict(exclude_unset=True)
    for field in update_data:
        existing_product[field] = update_data[field]
    
    return existing_product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: UUID):
    """
    Delete a product from the database.
    """
    global products_db
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    products_db = [p for p in products_db if p["id"] != product_id]
    return None

# Sample data initialization
@app.on_event("startup")
def startup_event():
    sample_products = [
        {
            "id": uuid4(),
            "name": "Argan Oil Shampoo",
            "brand": "Matin",
            "category": "shampoo",
            "description": "Nourishing shampoo with argan oil for healthy hair",
            "benefits": ["Hydrates hair", "Reduces frizz", "Adds shine"],
            "usage_instructions": "Apply to wet hair, massage, and rinse thoroughly.",
            "ingredients": ["Argan oil", "Aloe vera", "Vitamin E"],
            "price": 24.99,
            "size": "250ml"
        },
        {
            "id": uuid4(),
            "name": "Beard Growth Oil",
            "brand": "Matin",
            "category": "beard oil",
            "description": "Promotes beard growth and conditions facial hair",
            "benefits": ["Stimulates growth", "Softens beard", "Reduces itchiness"],
            "usage_instructions": "Apply a few drops to beard and massage into skin.",
            "ingredients": ["Jojoba oil", "Peppermint oil", "Vitamin B"],
            "price": 19.99,
            "size": "30ml"
        }
    ]
    products_db.extend(sample_products)
```
