"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Develop a RESTful API to manage orders and inventory for a medical equipment e-commerce platform, including endpoints for creating, reading, updating, and deleting orders and products.
Generated: DETERMINISTIC_869fa20c4aac6f92
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

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from uuid import UUID
from enum import Enum

# Initialize FastAPI app
app = FastAPI(
    title="Medical Equipment E-commerce Platform API",
    description="API for managing orders and inventory",
    version="1.0.0"
)

# Define product status enum
class ProductStatus(str, Enum):
    in_stock = "in_stock"
    out_of_stock = "out_of_stock"
    discontinued = "discontinued"

# Define product model
class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    status: ProductStatus

# Define order status enum
class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

# Define order item model
class OrderItem(BaseModel):
    product_id: UUID
    quantity: int

# Define order model
class Order(BaseModel):
    id: UUID
    customer_name: str
    order_items: List[OrderItem]
    status: OrderStatus

# In-memory data store for products and orders
products = []
orders = []

# Create product endpoint
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    # Check for duplicate product
    for p in products:
        if p.id == product.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product already exists")
    products.append(product)
    return product

# Read products endpoint
@app.get("/products/", response_model=List[Product])
async def read_products():
    return products

# Read product endpoint
@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: UUID):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

# Update product endpoint
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: UUID, product: Product):
    for p in products:
        if p.id == product_id:
            p.name = product.name
            p.description = product.description
            p.price = product.price
            p.status = product.status
            return p
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

# Delete product endpoint
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: UUID):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

# Create order endpoint
@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order: Order):
    # Check for valid products
    for item in order.order_items:
        product_found = False
        for product in products:
            if product.id == item.product_id and product.status == ProductStatus.in_stock:
                product_found = True
                break
        if not product_found:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid product or product is out of stock")
    orders.append(order)
    return order

# Read orders endpoint
@app.get("/orders/", response_model=List[Order])
async def read_orders():
    return orders

# Read order endpoint
@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: UUID):
    for order in orders:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

# Update order endpoint
@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: UUID, order: Order):
    for o in orders:
        if o.id == order_id:
            o.customer_name = order.customer_name
            o.order_items = order.order_items
            o.status = order.status
            return o
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

# Delete order endpoint
@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: UUID):
    for order in orders:
        if order.id == order_id:
            orders.remove(order)
            return {"message": "Order deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
```

```python
# main.py

import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
