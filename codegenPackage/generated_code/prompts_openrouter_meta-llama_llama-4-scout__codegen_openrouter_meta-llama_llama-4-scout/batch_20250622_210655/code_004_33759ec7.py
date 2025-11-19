"""
Generated Code Metadata:
========================
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Design a RESTful API for managing hot tub and spa inventory, including endpoints for retrieving product information and pricing, inspired by the Country Leisure Mfg product offerings.
Generated: DETERMINISTIC_33759ec7c457d0a3
Batch ID: 20250622_210655
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
    title="Hot Tub and Spa Inventory API",
    description="API for managing hot tub and spa inventory",
    version="1.0.0"
)

# Define a model for Product
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

# Define a model for ProductResponse
class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

# In-memory data store for products (replace with a database in production)
products: List[Product] = [
    Product(id=1, name="Spa Package 1", description="Basic spa package", price=999.99, quantity=10),
    Product(id=2, name="Spa Package 2", description="Deluxe spa package", price=1999.99, quantity=5),
    Product(id=3, name="Hot Tub 1", description="Small hot tub", price=799.99, quantity=8),
]

# Endpoint to retrieve all products
@app.get("/products", response_model=List[ProductResponse])
async def get_products():
    """Retrieve a list of all products"""
    return [{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products]

# Endpoint to retrieve a product by ID
@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    """Retrieve a product by ID"""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"id": product.id, "name": product.name, "description": product.description, "price": product.price}

# Endpoint to create a new product
@app.post("/products", response_model=ProductResponse)
async def create_product(product: Product):
    """Create a new product"""
    products.append(product)
    return {"id": product.id, "name": product.name, "description": product.description, "price": product.price}

# Endpoint to update an existing product
@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: Product):
    """Update an existing product"""
    existing_product = next((p for p in products if p.id == product_id), None)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.quantity = product.quantity
    return {"id": existing_product.id, "name": existing_product.name, "description": existing_product.description, "price": existing_product.price}

# Endpoint to delete a product
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """Delete a product"""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    products.remove(product)
    return {"message": "Product deleted successfully"}

# Endpoint to retrieve product pricing
@app.get("/products/{product_id}/price")
async def get_product_price(product_id: int):
    """Retrieve the price of a product"""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"price": product.price}

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
# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
