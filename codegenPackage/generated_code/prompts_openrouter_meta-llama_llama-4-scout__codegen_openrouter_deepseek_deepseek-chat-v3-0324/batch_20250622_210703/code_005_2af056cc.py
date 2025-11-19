"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Create a RESTful API in Python to manage orders for Rehau windows, including endpoints for creating, updating, and deleting orders, and provide a sample use case."
Generated: DETERMINISTIC_2af056ccba0b93e8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from datetime import datetime

app = FastAPI(title="Rehau Windows Order API", description="API for managing orders of Rehau windows")

class WindowSpecs(BaseModel):
    width: float
    height: float
    frame_color: str
    glass_type: str
    has_mullions: bool = False

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    address: str
    window_specs: WindowSpecs
    quantity: int = 1
    notes: Optional[str] = None

class Order(OrderCreate):
    order_id: UUID
    order_date: datetime
    status: str = "pending"

# In-memory database for demonstration purposes
orders_db = {}

@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    """Create a new order for Rehau windows."""
    order_id = uuid4()
    order_date = datetime.now()
    new_order = Order(
        order_id=order_id,
        order_date=order_date,
        **order.dict()
    )
    orders_db[str(order_id)] = new_order
    return new_order

@app.get("/orders/", response_model=List[Order])
async def list_orders():
    """List all orders."""
    return list(orders_db.values())

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: str):
    """Get details of a specific order."""
    try:
        return orders_db[order_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: str, updated_order: OrderCreate):
    """Update an existing order."""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    order = Order(
        order_id=UUID(order_id),
        order_date=orders_db[order_id].order_date,
        **updated_order.dict()
    )
    orders_db[order_id] = order
    return order

@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: str):
    """Delete an order."""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    del orders_db[order_id]
    return None

@app.patch("/orders/{order_id}/status", response_model=Order)
async def update_order_status(order_id: str, status: str):
    """Update the status of an order."""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    order = orders_db[order_id]
    order.status = status
    orders_db[order_id] = order
    return order

# Sample use case
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
