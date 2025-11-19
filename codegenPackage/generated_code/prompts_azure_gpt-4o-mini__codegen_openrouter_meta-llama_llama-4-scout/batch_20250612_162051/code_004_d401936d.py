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

**Hair and Beard Care Products API**
=====================================

**models.py**
```python
from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    benefits: str
    usage: str
    price: float
    category: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Beard Oil",
                "description": "A nourishing oil for beard care",
                "benefits": "Moisturizes and conditions beard and skin",
                "usage": "Apply 2-3 drops daily",
                "price": 19.99,
                "category": "Beard Care"
            }
        }

class ProductDB:
    def __init__(self):
        self.products = [
            Product(id=1, name="Beard Oil", description="A nourishing oil for beard care", benefits="Moisturizes and conditions beard and skin", usage="Apply 2-3 drops daily", price=19.99, category="Beard Care"),
            Product(id=2, name="Shampoo", description="A gentle shampoo for hair care", benefits="Cleans and nourishes hair", usage="Use 1-2 times a week", price=14.99, category="Hair Care"),
            # Add more products here...
        ]

    def get_product(self, product_id: int) -> Optional[Product]:
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def get_products(self) -> list[Product]:
        return self.products

    def create_product(self, product: Product) -> Product:
        self.products.append(product)
        return product

    def update_product(self, product_id: int, product: Product) -> Optional[Product]:
        for existing_product in self.products:
            if existing_product.id == product_id:
                existing_product.name = product.name
                existing_product.description = product.description
                existing_product.benefits = product.benefits
                existing_product.usage = product.usage
                existing_product.price = product.price
                existing_product.category = product.category
                return existing_product
        return None

    def delete_product(self, product_id: int) -> bool:
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                return True
        return False
```

**main.py**
```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from models import Product, ProductDB

app = FastAPI()
product_db = ProductDB()

# GET all products
@app.get("/products/", response_model=list[Product])
async def read_products():
    return product_db.get_products()

# GET product by ID
@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    product = product_db.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

# POST create new product
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    return product_db.create_product(product)

# PUT update existing product
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product):
    updated_product = product_db.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return updated_product

# DELETE product by ID
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int):
    if not product_db.delete_product(product_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
```

**requirements.txt**
```
fastapi
pydantic
uvicorn
```

**Run with:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
