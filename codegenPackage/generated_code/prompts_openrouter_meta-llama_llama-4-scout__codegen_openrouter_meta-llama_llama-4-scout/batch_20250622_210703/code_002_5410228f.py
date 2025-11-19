"""
Generated Code Metadata:
========================
Original URL: https://ktfmultan.com
Prompt: Generate a RESTful API endpoint to manage orders for a Multani bedsheets and khes online store, including order placement, exchange, and delivery status updates.
Generated: DETERMINISTIC_5410228fd1872e03
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
from enum import Enum
from datetime import datetime

app = FastAPI(
    title="Multani Bedsheets and Khes Online Store API",
    description="API for managing orders",
    version="1.0.0"
)

# Define Order Status Enum
class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"
    exchanged = "exchanged"
    cancelled = "cancelled"

# Define Order Model
class Order(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    order_date: datetime
    status: OrderStatus
    product: str
    quantity: int

# Define Exchange Request Model
class ExchangeRequest(BaseModel):
    order_id: int
    reason: str

# In-memory order storage (replace with a database in production)
orders: List[Order] = []

# Create Order Endpoint
@app.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: Order):
    """Create a new order"""
    orders.append(order)
    return order

# Get All Orders Endpoint
@app.get("/orders", status_code=status.HTTP_200_OK)
async def get_all_orders():
    """Retrieve all orders"""
    return orders

# Get Order by ID Endpoint
@app.get("/orders/{order_id}", status_code=status.HTTP_200_OK)
async def get_order(order_id: int):
    """Retrieve an order by ID"""
    for order in orders:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

# Update Order Status Endpoint
@app.put("/orders/{order_id}/status", status_code=status.HTTP_200_OK)
async def update_order_status(order_id: int, status: OrderStatus):
    """Update the status of an order"""
    for order in orders:
        if order.id == order_id:
            order.status = status
            return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

# Exchange Order Endpoint
@app.post("/orders/{order_id}/exchange", status_code=status.HTTP_201_CREATED)
async def exchange_order(order_id: int, exchange_request: ExchangeRequest):
    """Request an exchange for an order"""
    for order in orders:
        if order.id == order_id:
            order.status = OrderStatus.exchanged
            return {"message": "Exchange request processed successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

# Delivery Status Update Endpoint
@app.put("/orders/{order_id}/delivery-status", status_code=status.HTTP_200_OK)
async def update_delivery_status(order_id: int, status: OrderStatus):
    """Update the delivery status of an order"""
    for order in orders:
        if order.id == order_id:
            order.status = status
            return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

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
