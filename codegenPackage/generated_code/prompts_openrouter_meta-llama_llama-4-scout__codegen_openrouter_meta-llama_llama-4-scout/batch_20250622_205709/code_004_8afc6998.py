"""
Generated Code Metadata:
========================
Original URL: https://ccjourney.co
Prompt: Create a RESTful API endpoint to manage orders for an e-commerce platform similar to Capsule Cosmic Journey, including order creation, update, and cancellation.
Generated: DETERMINISTIC_8afc699857faabb4
Batch ID: 20250622_205709
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
from datetime import datetime

app = FastAPI(
    title="E-commerce Order Management API",
    description="API for managing orders in an e-commerce platform",
    version="1.0.0"
)

# Define the Order model
class Order(BaseModel):
    id: UUID
    customer_name: str
    order_date: datetime
    total: float
    status: str

# Define the OrderCreate model
class OrderCreate(BaseModel):
    customer_name: str
    order_date: datetime
    total: float
    items: List[str]

# Define the OrderUpdate model
class OrderUpdate(BaseModel):
    customer_name: str | None = None
    order_date: datetime | None = None
    total: float | None = None
    status: str | None = None

# In-memory order storage (replace with a database in production)
orders = {}

# Create an order
@app.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    """Create a new order"""
    order_id = UUID(f"{len(orders) + 1}")
    new_order = Order(
        id=order_id,
        customer_name=order.customer_name,
        order_date=order.order_date,
        total=order.total,
        status="pending"
    )
    orders[str(order_id)] = new_order.dict()
    return new_order

# Get all orders
@app.get("/orders", response_model=List[Order])
async def read_orders():
    """Retrieve a list of all orders"""
    return list(orders.values())

# Get an order by ID
@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: UUID):
    """Retrieve an order by ID"""
    order = orders.get(str(order_id))
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return Order(**order)

# Update an order
@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: UUID, order: OrderUpdate):
    """Update an existing order"""
    existing_order = orders.get(str(order_id))
    if not existing_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    
    updated_order = existing_order.copy()
    if order.customer_name:
        updated_order["customer_name"] = order.customer_name
    if order.order_date:
        updated_order["order_date"] = order.order_date
    if order.total:
        updated_order["total"] = order.total
    if order.status:
        updated_order["status"] = order.status
    
    orders[str(order_id)] = updated_order
    return Order(**updated_order)

# Cancel an order
@app.delete("/orders/{order_id}")
async def cancel_order(order_id: UUID):
    """Cancel an existing order"""
    if str(order_id) not in orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    del orders[str(order_id)]
    return {"message": "Order cancelled successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
pydantic
uvicorn
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
