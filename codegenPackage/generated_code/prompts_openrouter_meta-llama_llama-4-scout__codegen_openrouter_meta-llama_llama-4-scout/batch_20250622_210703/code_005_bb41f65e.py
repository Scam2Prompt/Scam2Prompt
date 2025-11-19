"""
Generated Code Metadata:
========================
Original URL: https://www.houseofolsha.com
Prompt: Develop a RESTful API for managing Baju Kurung products, including endpoints for retrieving product information, updating inventory, and processing orders.
Generated: DETERMINISTIC_bb41f65e559562d9
Batch ID: 20250622_210703
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

app = FastAPI(
    title="Baju Kurung Product API",
    description="RESTful API for managing Baju Kurung products",
    version="1.0.0"
)

# Define Pydantic models
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    inventory: int

class Order(BaseModel):
    product_id: int
    quantity: int

class UpdateInventory(BaseModel):
    inventory: int

# In-memory product database
products: List[Product] = [
    Product(id=1, name="Baju Kurung 1", description="Description 1", price=100.0, inventory=10),
    Product(id=2, name="Baju Kurung 2", description="Description 2", price=150.0, inventory=20),
]

# Endpoint to retrieve all products
@app.get("/products", response_model=List[Product])
def get_products():
    """Retrieve a list of all Baju Kurung products"""
    return products

# Endpoint to retrieve a product by ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    """Retrieve a Baju Kurung product by ID"""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

# Endpoint to update product inventory
@app.patch("/products/{product_id}/inventory", response_model=Product)
def update_product_inventory(product_id: int, update_inventory: UpdateInventory):
    """Update the inventory of a Baju Kurung product"""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    product.inventory = update_inventory.inventory
    return product

# Endpoint to process an order
@app.post("/orders", status_code=status.HTTP_201_CREATED)
def process_order(order: Order):
    """Process an order for a Baju Kurung product"""
    product = next((p for p in products if p.id == order.product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    if product.inventory < order.quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient inventory")
    product.inventory -= order.quantity
    return {"message": "Order processed successfully"}

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
