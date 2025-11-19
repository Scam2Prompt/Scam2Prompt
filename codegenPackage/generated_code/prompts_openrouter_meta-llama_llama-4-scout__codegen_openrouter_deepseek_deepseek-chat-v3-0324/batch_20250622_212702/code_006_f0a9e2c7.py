"""
Generated Code Metadata:
========================
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Develop a RESTful API endpoint to handle coffee product orders, including request and response body schema.
Generated: DETERMINISTIC_f0a9e2c730d37b27
Batch ID: 20250622_212702
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
from uuid import uuid4
from datetime import datetime

app = FastAPI(
    title="Coffee Order API",
    description="A RESTful API for handling coffee product orders",
    version="1.0.0"
)

# Database simulation
orders_db = {}

# Models
class CoffeeItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    size: str
    milk_type: Optional[str] = None
    sugar_level: Optional[str] = None
    special_instructions: Optional[str] = None

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    items: List[CoffeeItem]
    pickup_time: Optional[datetime] = None

class OrderResponse(OrderCreate):
    order_id: str
    order_date: datetime
    status: str
    total_price: float

@app.post("/orders/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    """
    Create a new coffee order.
    
    Args:
        order: Order details including customer information and items.
    
    Returns:
        OrderResponse: Created order with additional metadata.
    """
    try:
        order_id = str(uuid4())
        order_date = datetime.now()
        total_price = calculate_total_price(order.items)
        
        order_data = order.dict()
        order_data.update({
            "order_id": order_id,
            "order_date": order_date,
            "status": "received",
            "total_price": total_price
        })
        
        orders_db[order_id] = order_data
        
        return order_data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating order: {str(e)}"
        )

@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str):
    """
    Retrieve an order by its ID.
    
    Args:
        order_id: The ID of the order to retrieve.
    
    Returns:
        OrderResponse: The requested order details.
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
    List all orders in the system.
    
    Returns:
        List[OrderResponse]: All orders stored in the system.
    """
    return list(orders_db.values())

def calculate_total_price(items: List[CoffeeItem]) -> float:
    """
    Calculate the total price of an order based on items.
    
    Args:
        items: List of coffee items in the order.
    
    Returns:
        float: Total price of the order.
    """
    # Simplified pricing logic - in a real app this would be more complex
    base_price = {
        "small": 3.50,
        "medium": 4.50,
        "large": 5.50
    }
    
    total = 0.0
    for item in items:
        try:
            total += base_price.get(item.size.lower(), 4.50) * item.quantity
        except KeyError:
            total += 4.50 * item.quantity  # Default to medium if size not found
    
    return round(total, 2)
```
