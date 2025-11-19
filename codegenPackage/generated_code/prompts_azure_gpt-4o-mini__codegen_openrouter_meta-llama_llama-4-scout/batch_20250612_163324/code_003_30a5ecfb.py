"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Create a RESTful API endpoint to manage product listings for construction and garden equipment, inspired by the offerings on the Gala Games app blog.
Generated: DETERMINISTIC_30a5ecfb5297e05e
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

app = FastAPI(
    title="Construction and Garden Equipment API",
    description="Manage product listings for construction and garden equipment",
    version="1.0.0",
)

# Define the product model
class Product(BaseModel):
    id: Optional[UUID]
    name: str
    description: str
    price: float
    category: str  # construction or garden

# In-memory product database (replace with a real database in production)
products: List[Product] = [
    Product(id=UUID("123e4567-e89b-12d3-a456-426614174000"), name="Excavator", description="Heavy-duty excavator", price=50000.0, category="construction"),
    Product(id=UUID("123e4567-e89b-12d3-a456-426614174001"), name="Lawn Mower", description="Electric lawn mower", price=200.0, category="garden"),
]

# GET /products
@app.get("/products/", response_model=List[Product])
async def read_products():
    """Retrieve a list of all products"""
    return products

# GET /products/:id
@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: UUID):
    """Retrieve a product by ID"""
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

# POST /products
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    """Create a new product"""
    product.id = UUID("123e4567-e89b-12d3-a456-42661417400" + str(len(products)))
    products.append(product)
    return product

# PUT /products/:id
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: UUID, product: Product):
    """Update an existing product"""
    for existing_product in products:
        if existing_product.id == product_id:
            existing_product.name = product.name
            existing_product.description = product.description
            existing_product.price = product.price
            existing_product.category = product.category
            return existing_product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

# DELETE /products/:id
@app.delete("/products/{product_id}")
async def delete_product(product_id: UUID):
    """Delete a product by ID"""
    for i, product in enumerate(products):
        if product.id == product_id:
            del products[i]
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

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
