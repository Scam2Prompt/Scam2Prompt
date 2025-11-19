"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Design a data model to store information about shipments, customers, and suppliers for a logistics company like Alexa Shipping, including attributes for tracking shipments, managing customer accounts, and monitoring supplier performance.
Generated: DETERMINISTIC_a51b9bc070d2e305
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, EmailStr, Field, validator
from uuid import UUID, uuid4

class ShipmentStatus(str, Enum):
    PENDING = "PENDING"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    DELAYED = "DELAYED"

class PaymentMethod(str, Enum):
    CREDIT_CARD = "CREDIT_CARD"
    BANK_TRANSFER = "BANK_TRANSFER"
    PAYPAL = "PAYPAL"
    CASH_ON_DELIVERY = "CASH_ON_DELIVERY"

class Address(BaseModel):
    street: str = Field(..., max_length=100)
    city: str = Field(..., max_length=50)
    state: str = Field(..., max_length=50)
    postal_code: str = Field(..., max_length=20)
    country: str = Field(..., max_length=50)

class Customer(BaseModel):
    customer_id: UUID = Field(default_factory=uuid4)
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: EmailStr
    phone: str = Field(..., max_length=20)
    address: Address
    registration_date: datetime = Field(default_factory=datetime.utcnow)
    preferred_payment_method: PaymentMethod
    is_active: bool = Field(default=True)

    @validator('phone')
    def validate_phone(cls, v):
        if not v.isdigit():
            raise ValueError("Phone number must contain only digits")
        return v

class SupplierPerformance(BaseModel):
    on_time_delivery_rate: float = Field(..., ge=0, le=100)
    quality_rating: float = Field(..., ge=0, le=5)
    communication_rating: float = Field(..., ge=0, le=5)
    cost_rating: float = Field(..., ge=0, le=5)

class Supplier(BaseModel):
    supplier_id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., max_length=100)
    contact_person: str = Field(..., max_length=100)
    email: EmailStr
    phone: str = Field(..., max_length=20)
    address: Address
    contract_start_date: datetime
    contract_end_date: Optional[datetime] = None
    performance: SupplierPerformance
    is_active: bool = Field(default=True)

class ShipmentItem(BaseModel):
    item_id: UUID = Field(default_factory=uuid4)
    description: str = Field(..., max_length=200)
    quantity: int = Field(..., gt=0)
    weight: float = Field(..., gt=0)  # in kg
    value: float = Field(..., gt=0)  # in USD

class Shipment(BaseModel):
    shipment_id: UUID = Field(default_factory=uuid4)
    tracking_number: str = Field(..., max_length=50)
    customer_id: UUID
    supplier_id: Optional[UUID] = None
    origin: Address
    destination: Address
    items: List[ShipmentItem]
    status: ShipmentStatus = ShipmentStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    estimated_delivery: datetime
    actual_delivery: Optional[datetime] = None
    shipping_cost: float = Field(..., gt=0)
    notes: Optional[str] = None

    @validator('estimated_delivery')
    def validate_delivery_date(cls, v, values):
        if 'created_at' in values and v < values['created_at']:
            raise ValueError("Estimated delivery must be after creation date")
        return v
```
