"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Suggest an API for managing customer orders and agreements for customized golf grips, similar to the four-step process outlined on the Longhui Golf website.
Generated: DETERMINISTIC_4503957b2efebabf
Batch ID: 20250612_153648
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

app = FastAPI(
    title="Custom Golf Grips Order API",
    description="API for managing customer orders and agreements for customized golf grips",
    version="1.0.0"
)

# Database mock (in production, use a real database)
orders_db = {}
agreements_db = {}

# Models
class CustomerInfo(BaseModel):
    name: str
    email: str
    phone: str
    shipping_address: str

class GripSpecification(BaseModel):
    model: str
    color: str
    size: str
    texture: str
    logo: Optional[str] = None
    custom_text: Optional[str] = None

class OrderItem(BaseModel):
    grip_spec: GripSpecification
    quantity: int

class OrderCreate(BaseModel):
    customer_info: CustomerInfo
    items: List[OrderItem]
    notes: Optional[str] = None

class Order(OrderCreate):
    order_id: UUID
    status: str = "pending"
    created_at: datetime
    updated_at: datetime

class Agreement(BaseModel):
    agreement_id: UUID
    order_id: UUID
    terms_accepted: bool
    accepted_at: datetime
    ip_address: str

# Helper functions
def get_current_time():
    return datetime.utcnow()

# API Endpoints
@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(order_data: OrderCreate):
    """Create a new custom golf grip order"""
    order_id = uuid4()
    now = get_current_time()
    
    order = Order(
        order_id=order_id,
        created_at=now,
        updated_at=now,
        **order_data.dict()
    )
    
    orders_db[str(order_id)] = order
    return order

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: UUID):
    """Retrieve order details"""
    order = orders_db.get(str(order_id))
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order

@app.post("/agreements/", response_model=Agreement, status_code=status.HTTP_201_CREATED)
def create_agreement(order_id: UUID, ip_address: str):
    """Create an agreement for an order"""
    if str(order_id) not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    agreement_id = uuid4()
    now = get_current_time()
    
    agreement = Agreement(
        agreement_id=agreement_id,
        order_id=order_id,
        terms_accepted=True,
        accepted_at=now,
        ip_address=ip_address
    )
    
    agreements_db[str(agreement_id)] = agreement
    
    # Update order status
    order = orders_db[str(order_id)]
    order.status = "agreement_accepted"
    order.updated_at = now
    
    return agreement

@app.get("/agreements/{agreement_id}", response_model=Agreement)
def get_agreement(agreement_id: UUID):
    """Retrieve agreement details"""
    agreement = agreements_db.get(str(agreement_id))
    if not agreement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agreement not found"
        )
    return agreement

@app.put("/orders/{order_id}/confirm", response_model=Order)
def confirm_order(order_id: UUID):
    """Confirm an order (final step)"""
    order = orders_db.get(str(order_id))
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    # Check if agreement exists
    agreement_exists = any(
        str(agreement.order_id) == str(order_id)
        for agreement in agreements_db.values()
    )
    
    if not agreement_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Agreement must be accepted before confirming order"
        )
    
    order.status = "confirmed"
    order.updated_at = get_current_time()
    
    return order

@app.get("/orders/", response_model=List[Order])
def list_orders(status: Optional[str] = None):
    """List all orders with optional status filter"""
    orders = list(orders_db.values())
    if status:
        orders = [order for order in orders if order.status == status]
    return orders
```
