"""
Generated Code Metadata:
========================
Original URL: https://issowork.com
Prompt: "Create a RESTful API for managing clothing inventory, including endpoints for adding, updating, and deleting products, inspired by ISSO's product offerings."
Generated: DETERMINISTIC_37c0f795ecd163c6
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Clothing Inventory API",
    description="A RESTful API for managing clothing inventory",
    version="1.0.0",
)

class Product(BaseModel):
    """Product model"""
    id: int
    name: str
    description: str
    price: float
    quantity: int

# In-memory product database
products: List[Product] = [
    Product(id=1, name="T-Shirt", description="Basic T-Shirt", price=19.99, quantity=100),
    Product(id=2, name="Jeans", description="Classic Jeans", price=49.99, quantity=50),
]

@app.get("/products/")
async def read_products():
    """Retrieve a list of all products"""
    return products

@app.get("/products/{product_id}")
async def read_product(product_id: int):
    """Retrieve a product by ID"""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/")
async def create_product(product: Product):
    """Create a new product"""
    existing_product = next((p for p in products if p.id == product.id), None)
    if existing_product:
        raise HTTPException(status_code=400, detail="Product with this ID already exists")
    products.append(product)
    return product

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    """Update an existing product"""
    existing_product = next((p for p in products if p.id == product_id), None)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.quantity = product.quantity
    return existing_product

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """Delete a product"""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    products.remove(product)
    return {"message": f"Product {product_id} deleted successfully"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return {"error": exc.detail}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
