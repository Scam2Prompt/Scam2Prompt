"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Suggest an API for managing inventory of products like "شارژر فندکی Ldnio مدل C104" and "مبدل بلوتوث لایتنینگ به جک هدفون اپل" from the website, including stock tracking and price updates.
Generated: DETERMINISTIC_aa5adee4cc9a33b7
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Inventory Management API",
    description="Manage inventory of products",
    version="1.0.0"
)

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

class ProductUpdate(BaseModel):
    price: float | None
    stock: int | None

# In-memory product database (replace with a real database in production)
products: dict[int, Product] = {
    1: Product(id=1, name="شارژر فندکی Ldnio مدل C104", price=50.0, stock=100),
    2: Product(id=2, name="مبدل بلوتوث لایتنینگ به جک هدفون اپل", price=20.0, stock=50)
}

@app.get("/products/")
async def get_products():
    """Get a list of all products"""
    return list(products.values())

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """Get a product by ID"""
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/")
async def create_product(product: Product):
    """Create a new product"""
    if product.id in products:
        raise HTTPException(status_code=400, detail="Product already exists")
    products[product.id] = product
    return product

@app.put("/products/{product_id}")
async def update_product(product_id: int, product_update: ProductUpdate):
    """Update a product"""
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if product_update.price is not None:
        product.price = product_update.price
    if product_update.stock is not None:
        product.stock = product_update.stock
    return product

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """Delete a product"""
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    del products[product_id]
    return {"message": "Product deleted"}

@app.get("/products/{product_id}/stock")
async def get_product_stock(product_id: int):
    """Get the stock of a product"""
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"stock": product.stock}

@app.put("/products/{product_id}/stock")
async def update_product_stock(product_id: int, stock: int):
    """Update the stock of a product"""
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product.stock = stock
    return {"stock": product.stock}

@app.get("/products/{product_id}/price")
async def get_product_price(product_id: int):
    """Get the price of a product"""
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"price": product.price}

@app.put("/products/{product_id}/price")
async def update_product_price(product_id: int, price: float):
    """Update the price of a product"""
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product.price = price
    return {"price": product.price}
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("inventory_api:app", host="0.0.0.0", port=8000, reload=True)
```
