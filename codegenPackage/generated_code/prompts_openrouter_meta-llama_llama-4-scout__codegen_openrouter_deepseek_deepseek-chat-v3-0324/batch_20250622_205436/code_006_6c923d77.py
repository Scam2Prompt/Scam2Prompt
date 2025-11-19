"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: "Design a system for tracking orders, shipments, and customer inquiries for an auto parts distribution company, including a simple data model and potential software tools or libraries for implementation."
Generated: DETERMINISTIC_6c923d77b094e52c
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# order_tracking_system.py
import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, validator
from uuid import uuid4

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class ShipmentStatus(str, Enum):
    PREPARING = "preparing"
    IN_TRANSIT = "in_transit"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    RETURNED = "returned"

class InquiryStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class Customer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    email: str
    phone: str
    address: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v

class AutoPart(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    description: str
    price: float
    stock_quantity: int
    category: str

class OrderItem(BaseModel):
    part_id: str
    quantity: int
    unit_price: float

    @validator('quantity')
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be positive')
        return v

class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    customer_id: str
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.PENDING
    total_amount: float
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    def calculate_total(self):
        return sum(item.quantity * item.unit_price for item in self.items)

class Shipment(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    order_id: str
    tracking_number: str
    carrier: str
    status: ShipmentStatus = ShipmentStatus.PREPARING
    estimated_delivery: datetime.datetime
    actual_delivery: Optional[datetime.datetime] = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

class CustomerInquiry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    customer_id: str
    order_id: Optional[str] = None
    subject: str
    message: str
    status: InquiryStatus = InquiryStatus.OPEN
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

class OrderTrackingSystem:
    def __init__(self):
        self.customers = {}
        self.orders = {}
        self.shipments = {}
        self.inquiries = {}
        self.parts = {}

    def add_customer(self, customer: Customer) -> Customer:
        self.customers[customer.id] = customer
        return customer

    def add_part(self, part: AutoPart) -> AutoPart:
        self.parts[part.id] = part
        return part

    def create_order(self, customer_id: str, items: List[OrderItem]) -> Order:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        for item in items:
            if item.part_id not in self.parts:
                raise ValueError(f"Part {item.part_id} not found")
            
            part = self.parts[item.part_id]
            if part.stock_quantity < item.quantity:
                raise ValueError(f"Insufficient stock for part {part.name}")
            
            part.stock_quantity -= item.quantity

        order = Order(
            customer_id=customer_id,
            items=items,
            total_amount=sum(item.quantity * item.unit_price for item in items)
        )
        self.orders[order.id] = order
        return order

    def update_order_status(self, order_id: str, status: OrderStatus) -> Order:
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        order = self.orders[order_id]
        order.status = status
        order.updated_at = datetime.datetime.now()
        return order

    def create_shipment(self, order_id: str, carrier: str, tracking_number: str, estimated_delivery: datetime.datetime) -> Shipment:
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        shipment = Shipment(
            order_id=order_id,
            carrier=carrier,
            tracking_number=tracking_number,
            estimated_delivery=estimated_delivery
        )
        self.shipments[shipment.id] = shipment
        return shipment

    def update_shipment_status(self, shipment_id: str, status: ShipmentStatus) -> Shipment:
        if shipment_id not in self.shipments:
            raise ValueError("Shipment not found")
        
        shipment = self.shipments[shipment_id]
        shipment.status = status
        shipment.updated_at = datetime.datetime.now()
        
        if status == ShipmentStatus.DELIVERED:
            shipment.actual_delivery = datetime.datetime.now()
            self.update_order_status(shipment.order_id, OrderStatus.DELIVERED)
        
        return shipment

    def create_inquiry(self, customer_id: str, subject: str, message: str, order_id: Optional[str] = None) -> CustomerInquiry:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        if order_id and order_id not in self.orders:
            raise ValueError("Order not found")
        
        inquiry = CustomerInquiry(
            customer_id=customer_id,
            order_id=order_id,
            subject=subject,
            message=message
        )
        self.inquiries[inquiry.id] = inquiry
        return inquiry

    def update_inquiry_status(self, inquiry_id: str, status: InquiryStatus) -> CustomerInquiry:
        if inquiry_id not in self.inquiries:
            raise ValueError("Inquiry not found")
        
        inquiry = self.inquiries[inquiry_id]
        inquiry.status = status
        inquiry.updated_at = datetime.datetime.now()
        return inquiry

# Potential tools/libs to use:
# - FastAPI for REST API
# - SQLAlchemy for database ORM
# - Alembic for migrations
# - Pydantic for data validation
# - Redis for caching
# - Celery for background tasks
# - pytest for testing
```
