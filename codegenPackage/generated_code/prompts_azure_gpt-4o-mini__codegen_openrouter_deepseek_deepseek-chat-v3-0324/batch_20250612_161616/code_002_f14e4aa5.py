"""
Generated Code Metadata:
========================
Original URL: https://snackpointemmen.nl
Prompt: Create an API endpoint for a snack bar that allows customers to place orders for items like fries, burgers, and milkshakes, referencing the unique snack wall feature at Snackpoint Emmen.
Generated: DETERMINISTIC_f14e4aa54ad9ca1d
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID
from enum import Enum

app = FastAPI(
    title="Snackpoint Emmen API",
    description="API for placing orders at Snackpoint Emmen's unique snack wall",
    version="1.0.0"
)

class ItemType(str, Enum):
    FRIES = "fries"
    BURGER = "burger"
    MILKSHAKE = "milkshake"

class OrderItem(BaseModel):
    item_type: ItemType = Field(..., description="Type of snack item")
    quantity: int = Field(1, gt=0, description="Quantity of the item")
    special_requests: Optional[str] = Field(None, description="Any special requests for the item")

class Order(BaseModel):
    customer_name: str = Field(..., min_length=1, description="Name of the customer")
    items: List[OrderItem] = Field(..., min_items=1, description="List of items in the order")
    snack_wall_location: str = Field(..., description="Unique identifier for the snack wall location")

class OrderResponse(BaseModel):
    order_id: UUID
    customer_name: str
    items: List[OrderItem]
    snack_wall_location: str
    status: str = "received"

# In-memory database for demo purposes
orders_db = {}

@app.post("/orders/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def place_order(order: Order):
    """
    Place a new order at Snackpoint Emmen's snack wall.
    
    Args:
        order: Order details including customer name, items, and snack wall location.
    
    Returns:
        OrderResponse: Confirmation of the placed order with a unique order ID.
    """
    order_id = uuid4()
    order_response = OrderResponse(
        order_id=order_id,
        customer_name=order.customer_name,
        items=order.items,
        snack_wall_location=order.snack_wall_location
    )
    orders_db[order_id] = order_response
    return order_response

@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: UUID):
    """
    Retrieve details of a specific order by its ID.
    
    Args:
        order_id: UUID of the order to retrieve.
    
    Returns:
        OrderResponse: Details of the requested order.
    
    Raises:
        HTTPException: If the order is not found.
    """
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return orders_db[order_id]

@app.get("/orders/", response_model=List[OrderResponse])
async def list_orders():
    """
    List all orders placed at Snackpoint Emmen.
    
    Returns:
        List[OrderResponse]: All orders in the system.
    """
    return list(orders_db.values())

@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_order(order_id: UUID):
    """
    Cancel an existing order by its ID.
    
    Args:
        order_id: UUID of the order to cancel.
    
    Raises:
        HTTPException: If the order is not found.
    """
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    del orders_db[order_id]
```
