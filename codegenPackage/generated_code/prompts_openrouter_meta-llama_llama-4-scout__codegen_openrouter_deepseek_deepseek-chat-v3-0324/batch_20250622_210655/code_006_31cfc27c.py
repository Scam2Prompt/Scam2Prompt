"""
Generated Code Metadata:
========================
Original URL: https://watpac.in
Prompt: "Design a simple API to retrieve product information for Watpac Chemicals Pvt Ltd, including product names, prices, and quantities."
Generated: DETERMINISTIC_31cfc27ca879cba1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Watpac Chemicals Product API",
    description="API to retrieve product information for Watpac Chemicals Pvt Ltd",
    version="1.0.0"
)

# Mock database
products_db = [
    {"id": 1, "name": "Chemical A", "price": 25.99, "quantity": 100},
    {"id": 2, "name": "Chemical B", "price": 19.50, "quantity": 75},
    {"id": 3, "name": "Chemical C", "price": 32.75, "quantity": 50},
]

# Pydantic models for request/response validation
class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

@app.get("/products", response_model=List[Product])
async def get_all_products():
    """Get all products"""
    return products_db

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Get a specific product by ID"""
    product = next((p for p in products_db if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=Product, status_code=201)
async def create_product(product: ProductCreate):
    """Create a new product"""
    new_id = max(p["id"] for p in products_db) + 1 if products_db else 1
    new_product = {
        "id": new_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    }
    products_db.append(new_product)
    return new_product

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductCreate):
    """Update an existing product"""
    existing_product = next((p for p in products_db if p["id"] == product_id), None)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    existing_product.update({
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    })
    return existing_product

@app.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: int):
    """Delete a product"""
    global products_db
    product = next((p for p in products_db if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db = [p for p in products_db if p["id"] != product_id]
    return None

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
