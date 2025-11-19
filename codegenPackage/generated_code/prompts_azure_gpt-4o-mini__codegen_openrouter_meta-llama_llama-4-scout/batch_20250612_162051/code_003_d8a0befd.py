"""
Generated Code Metadata:
========================
Original URL: https://zkoutdoor.pk
Prompt: Develop a RESTful API endpoint for managing inventory in a furniture e-commerce application, allowing for CRUD operations on products such as sofas and hanging lamps.
Generated: DETERMINISTIC_d8a0befd47b22a47
Batch ID: 20250612_162051
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
from typing import List
from uuid import UUID

app = FastAPI(
    title="Furniture E-commerce Inventory API",
    description="API for managing inventory in a furniture e-commerce application",
    version="1.0.0",
)

# Define a Pydantic model for Product
class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    quantity: int

# In-memory inventory storage (replace with a database in production)
inventory: List[Product] = [
    Product(id="123e4567-e89b-12d3-a456-426614174000", name="Sofa", description="Comfortable sofa", price=999.99, quantity=10),
    Product(id="123e4567-e89b-12d3-a456-426614174001", name="Hanging Lamp", description="Modern hanging lamp", price=99.99, quantity=20),
]

# GET /products
@app.get("/products/", response_model=List[Product])
async def read_products():
    """Retrieve a list of all products in the inventory"""
    return inventory

# GET /products/{product_id}
@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: UUID):
    """Retrieve a product by ID"""
    product = next((p for p in inventory if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

# POST /products
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    """Create a new product"""
    if any(p.id == product.id for p in inventory):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product with this ID already exists")
    inventory.append(product)
    return product

# PUT /products/{product_id}
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: UUID, product: Product):
    """Update an existing product"""
    existing_product = next((p for p in inventory if p.id == product_id), None)
    if existing_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.quantity = product.quantity
    return existing_product

# DELETE /products/{product_id}
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: UUID):
    """Delete a product"""
    product = next((p for p in inventory if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    inventory.remove(product)

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
# uvicorn app:app --host 0.0.0.0 --port 8000
```
