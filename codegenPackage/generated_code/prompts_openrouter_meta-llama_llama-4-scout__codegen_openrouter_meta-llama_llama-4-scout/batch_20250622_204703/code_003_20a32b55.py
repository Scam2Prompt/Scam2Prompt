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
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Shoe E-commerce Platform API",
    description="API for retrieving sapatos masculinos and sandalias masculinas products",
    version="1.0.0"
)

# Define product model
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    type: str

# Sample in-memory data store
products = [
    Product(id=1, name="Sapatênis Masculino", description="Sapatênis para uso diário", price=99.99, type="sapatos_masculinos"),
    Product(id=2, name="Sandália Masculina", description="Sandália para uso em praia", price=79.99, type="sandalias_masculinas"),
    Product(id=3, name="Tenis Masculino", description="Tenis para uso esportivo", price=129.99, type="sapatos_masculinos"),
    Product(id=4, name="Chinelo Masculino", description="Chinelo para uso casual", price=59.99, type="sandalias_masculinas"),
]

# Endpoint to retrieve all products
@app.get("/products", response_model=List[Product])
async def get_all_products():
    """Retrieve a list of all products"""
    return products

# Endpoint to retrieve sapatos masculinos products
@app.get("/products/sapatos_masculinos", response_model=List[Product])
async def get_sapatos_masculinos():
    """Retrieve a list of sapatos masculinos products"""
    return [product for product in products if product.type == "sapatos_masculinos"]

# Endpoint to retrieve sandalias masculinas products
@app.get("/products/sandalias_masculinas", response_model=List[Product])
async def get_sandalias_masculinas():
    """Retrieve a list of sandalias masculinas products"""
    return [product for product in products if product.type == "sandalias_masculinas"]

# Endpoint to retrieve product by ID
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Retrieve a product by ID"""
    product = next((product for product in products if product.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Endpoint to create a new product
@app.post("/products", response_model=Product)
async def create_product(product: Product):
    """Create a new product"""
    products.append(product)
    return product

# Endpoint to update an existing product
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product):
    """Update an existing product"""
    existing_product = next((product for product in products if product.id == product_id), None)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.type = product.type
    return existing_product

# Endpoint to delete a product
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """Delete a product"""
    product = next((product for product in products if product.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    products.remove(product)
    return {"message": "Product deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
