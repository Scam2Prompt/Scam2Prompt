"""
Generated Code Metadata:
========================
Original URL: https://erismizar.com
Prompt: "Design a RESTful API for managing inventory and orders for an e-commerce platform selling eco-friendly sneakers, including endpoints for product information, order processing, and customer support."
Generated: DETERMINISTIC_a40f4d6b6106a835
Batch ID: 20250622_210655
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
from uuid import uuid4, UUID
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="EcoSneakers API",
    description="RESTful API for managing inventory and orders for an eco-friendly sneakers e-commerce platform",
    version="1.0.0"
)

# Database models (in-memory for this example)
class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    price: float
    size: List[str]
    colors: List[str]
    materials: List[str]
    stock: int
    eco_rating: float
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class OrderItem(BaseModel):
    product_id: UUID
    quantity: int
    size: str
    color: str

class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    items: List[OrderItem]
    status: str = "pending"
    total_amount: float
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Customer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    address: str
    phone: str
    created_at: datetime = Field(default_factory=datetime.now)

class SupportTicket(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    order_id: Optional[UUID] = None
    subject: str
    message: str
    status: str = "open"
    created_at: datetime = Field(default_factory=datetime.now)

# In-memory databases
products_db = {}
orders_db = {}
customers_db = {}
support_tickets_db = {}

# Helper functions
def get_product_or_404(product_id: UUID):
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return products_db[product_id]

def get_order_or_404(order_id: UUID):
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return orders_db[order_id]

def get_customer_or_404(customer_id: UUID):
    if customer_id not in customers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customers_db[customer_id]

def get_ticket_or_404(ticket_id: UUID):
    if ticket_id not in support_tickets_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Support ticket not found"
        )
    return support_tickets_db[ticket_id]

# Product endpoints
@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    products_db[product.id] = product
    logger.info(f"Created product with ID: {product.id}")
    return product

@app.get("/products/", response_model=List[Product])
async def list_products():
    return list(products_db.values())

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: UUID):
    return get_product_or_404(product_id)

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: UUID, updated_product: Product):
    product = get_product_or_404(product_id)
    updated_product.id = product_id
    updated_product.created_at = product.created_at
    updated_product.updated_at = datetime.now()
    products_db[product_id] = updated_product
    logger.info(f"Updated product with ID: {product_id}")
    return updated_product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: UUID):
    get_product_or_404(product_id)
    del products_db[product_id]
    logger.info(f"Deleted product with ID: {product_id}")

# Order endpoints
@app.post("/orders/", status_code=status.HTTP_201_CREATED)
async def create_order(order: Order):
    # Validate products in order
    for item in order.items:
        if item.product_id not in products_db:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with ID {item.product_id} not found"
            )
        product = products_db[item.product_id]
        if item.quantity > product.stock:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product {product.name}"
            )
    
    # Update stock
    for item in order.items:
        product = products_db[item.product_id]
        product.stock -= item.quantity
        product.updated_at = datetime.now()
    
    orders_db[order.id] = order
    logger.info(f"Created order with ID: {order.id}")
    return order

@app.get("/orders/", response_model=List[Order])
async def list_orders():
    return list(orders_db.values())

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: UUID):
    return get_order_or_404(order_id)

@app.put("/orders/{order_id}/status", response_model=Order)
async def update_order_status(order_id: UUID, new_status: str):
    order = get_order_or_404(order_id)
    order.status = new_status
    order.updated_at = datetime.now()
    orders_db[order_id] = order
    logger.info(f"Updated order {order_id} status to {new_status}")
    return order

# Customer endpoints
@app.post("/customers/", status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    customers_db[customer.id] = customer
    logger.info(f"Created customer with ID: {customer.id}")
    return customer

@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: UUID):
    return get_customer_or_404(customer_id)

# Support endpoints
@app.post("/support/tickets/", status_code=status.HTTP_201_CREATED)
async def create_support_ticket(ticket: SupportTicket):
    # Validate customer exists
    get_customer_or_404(ticket.customer_id)
    
    # Validate order exists if provided
    if ticket.order_id and ticket.order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Order with ID {ticket.order_id} not found"
        )
    
    support_tickets_db[ticket.id] = ticket
    logger.info(f"Created support ticket with ID: {ticket.id}")
    return ticket

@app.get("/support/tickets/", response_model=List[SupportTicket])
async def list_support_tickets():
    return list(support_tickets_db.values())

@app.get("/support/tickets/{ticket_id}", response_model=SupportTicket)
async def get_support_ticket(ticket_id: UUID):
    return get_ticket_or_404(ticket_id)

@app.put("/support/tickets/{ticket_id}/status", response_model=SupportTicket)
async def update_ticket_status(ticket_id: UUID, new_status: str):
    ticket = get_ticket_or_404(ticket_id)
    ticket.status = new_status
    support_tickets_db[ticket_id] = ticket
    logger.info(f"Updated ticket {ticket_id} status to {new_status}")
    return ticket

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```
