"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: "Create a Python API for managing orders of custom illuminated signs, including samostojeća svjetleća slova and totemi."
Generated: DETERMINISTIC_ab33fa9d3efcc365
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid
from enum import Enum

app = FastAPI(
    title="Illuminated Signs Order API",
    description="API for managing orders of custom illuminated signs",
    version="1.0.0"
)

# Database simulation
orders_db = []

class SignType(str, Enum):
    SAMOSTOJECA_SVJETLECA_SLOVA = "samostojeća svjetleća slova"
    TOTEMI = "totemi"

class OrderStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class OrderItem(BaseModel):
    sign_type: SignType
    text: str = Field(..., min_length=1, max_length=100)
    color: str = Field(..., min_length=3, max_length=20)
    size: str = Field(..., min_length=1, max_length=20)
    quantity: int = Field(..., gt=0)
    notes: Optional[str] = Field(None, max_length=500)

class OrderCreate(BaseModel):
    customer_name: str = Field(..., min_length=1, max_length=100)
    customer_email: str = Field(..., min_length=3, max_length=100)
    customer_phone: str = Field(..., min_length=6, max_length=20)
    items: List[OrderItem]
    delivery_address: str = Field(..., min_length=5, max_length=200)
    installation_required: bool = False
    special_instructions: Optional[str] = Field(None, max_length=500)

class Order(OrderCreate):
    id: str
    order_date: datetime
    status: OrderStatus
    total_price: Optional[float] = None

@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    """
    Create a new illuminated sign order.
    """
    order_id = str(uuid.uuid4())
    new_order = Order(
        id=order_id,
        order_date=datetime.now(),
        status=OrderStatus.PENDING,
        **order.dict()
    )
    orders_db.append(new_order)
    return new_order

@app.get("/orders/", response_model=List[Order])
async def list_orders(status: Optional[OrderStatus] = None):
    """
    List all orders, optionally filtered by status.
    """
    if status:
        return [order for order in orders_db if order.status == status]
    return orders_db

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: str):
    """
    Get details of a specific order by ID.
    """
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.patch("/orders/{order_id}/status", response_model=Order)
async def update_order_status(order_id: str, new_status: OrderStatus):
    """
    Update the status of an order.
    """
    for order in orders_db:
        if order.id == order_id:
            order.status = new_status
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{order_id}/price", response_model=Order)
async def update_order_price(order_id: str, total_price: float):
    """
    Update the total price of an order.
    """
    if total_price <= 0:
        raise HTTPException(status_code=400, detail="Price must be positive")
    
    for order in orders_db:
        if order.id == order_id:
            order.total_price = total_price
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: str):
    """
    Delete an order by ID.
    """
    for i, order in enumerate(orders_db):
        if order.id == order_id:
            orders_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/customer/{email}", response_model=List[Order])
async def get_orders_by_customer(email: str):
    """
    Get all orders for a specific customer by email.
    """
    customer_orders = [order for order in orders_db if order.customer_email.lower() == email.lower()]
    if not customer_orders:
        raise HTTPException(status_code=404, detail="No orders found for this customer")
    return customer_orders
```
