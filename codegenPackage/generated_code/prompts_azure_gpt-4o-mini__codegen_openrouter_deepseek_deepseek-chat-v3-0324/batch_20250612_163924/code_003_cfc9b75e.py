"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Create a REST API endpoint for managing orders on an e-commerce site similar to Bio Green Asia, focusing on natural products like floor cleaners and hand washes.
Generated: DETERMINISTIC_cfc9b75e5d44e1bb
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Bio Green Asia Orders API",
    description="REST API for managing orders of natural products",
    version="1.0.0"
)

# Database mock (in production, use a real database)
orders_db = []

# Models
class ProductItem(BaseModel):
    product_id: UUID
    name: str
    quantity: int
    price: float
    category: Optional[str] = None  # e.g., "floor_cleaner", "hand_wash"

class OrderCreate(BaseModel):
    customer_id: UUID
    items: List[ProductItem]
    shipping_address: str
    notes: Optional[str] = None

class Order(OrderCreate):
    order_id: UUID
    created_at: datetime
    status: str  # e.g., "pending", "processing", "shipped", "delivered", "cancelled"

# Helper functions
def find_order(order_id: UUID) -> Optional[Order]:
    """Find an order in the database by ID."""
    for order in orders_db:
        if order["order_id"] == order_id:
            return order
    return None

# Endpoints
@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order_data: OrderCreate):
    """
    Create a new order for natural products.
    
    Args:
        order_data: Order details including customer ID, items, and shipping address.
    
    Returns:
        The created order with generated order ID and timestamps.
    """
    try:
        order = Order(
            order_id=uuid4(),
            created_at=datetime.utcnow(),
            status="pending",
            **order_data.dict()
        )
        orders_db.append(order.dict())
        return order
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating order: {str(e)}"
        )

@app.get("/orders/", response_model=List[Order])
async def list_orders(limit: int = 10, offset: int = 0):
    """
    List all orders with pagination support.
    
    Args:
        limit: Maximum number of orders to return.
        offset: Number of orders to skip.
    
    Returns:
        List of orders.
    """
    try:
        return orders_db[offset:offset + limit]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving orders: {str(e)}"
        )

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: UUID):
    """
    Get details of a specific order.
    
    Args:
        order_id: UUID of the order to retrieve.
    
    Returns:
        The requested order details.
    """
    order = find_order(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order

@app.put("/orders/{order_id}", response_model=Order)
async def update_order_status(order_id: UUID, status: str):
    """
    Update the status of an order.
    
    Args:
        order_id: UUID of the order to update.
        status: New status for the order.
    
    Returns:
        The updated order details.
    """
    order = find_order(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    valid_statuses = ["pending", "processing", "shipped", "delivered", "cancelled"]
    if status not in valid_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status. Must be one of: {valid_statuses}"
        )
    
    try:
        order["status"] = status
        return order
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating order: {str(e)}"
        )

@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: UUID):
    """
    Delete an order (admin only).
    
    Args:
        order_id: UUID of the order to delete.
    """
    global orders_db
    order = find_order(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    try:
        orders_db = [o for o in orders_db if o["order_id"] != order_id]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting order: {str(e)}"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Endpoint for health checks."""
    return {"status": "healthy"}
```
