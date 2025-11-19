"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Develop a RESTful API endpoint that allows users to place orders for industrial cleaning brushes, incorporating the quick delivery service mentioned by VIRCOMEM.
Generated: DETERMINISTIC_6ad9a1efdee21e94
Batch ID: 20250612_155327
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
from typing import Optional
from datetime import datetime, timedelta
import uvicorn

app = FastAPI(
    title="Industrial Cleaning Brushes Order API",
    description="API for placing orders of industrial cleaning brushes with quick delivery service",
    version="1.0.0"
)

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    unit_price: float

class Order(BaseModel):
    customer_id: str
    items: list[OrderItem]
    shipping_address: str
    special_instructions: Optional[str] = None
    quick_delivery: bool = False

class OrderResponse(BaseModel):
    order_id: str
    customer_id: str
    items: list[OrderItem]
    total_amount: float
    shipping_address: str
    estimated_delivery: str
    order_status: str
    quick_delivery: bool

# Mock database
orders_db = {}

@app.post("/orders/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def place_order(order: Order):
    """
    Place a new order for industrial cleaning brushes.
    
    Parameters:
    - order: Order details including items, shipping address, and delivery preference
    
    Returns:
    - Order confirmation with estimated delivery date
    """
    try:
        # Generate order ID
        order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Calculate total amount
        total_amount = sum(item.quantity * item.unit_price for item in order.items)
        
        # Calculate estimated delivery
        base_delivery_days = 3 if order.quick_delivery else 7
        delivery_date = datetime.now() + timedelta(days=base_delivery_days)
        
        # Create order response
        order_response = OrderResponse(
            order_id=order_id,
            customer_id=order.customer_id,
            items=order.items,
            total_amount=total_amount,
            shipping_address=order.shipping_address,
            estimated_delivery=delivery_date.strftime("%Y-%m-%d"),
            order_status="Received",
            quick_delivery=order.quick_delivery
        )
        
        # Store order in mock database
        orders_db[order_id] = order_response.dict()
        
        return order_response
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing order: {str(e)}"
        )

@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str):
    """
    Retrieve order details by order ID.
    
    Parameters:
    - order_id: The ID of the order to retrieve
    
    Returns:
    - Order details if found
    """
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return orders_db[order_id]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
