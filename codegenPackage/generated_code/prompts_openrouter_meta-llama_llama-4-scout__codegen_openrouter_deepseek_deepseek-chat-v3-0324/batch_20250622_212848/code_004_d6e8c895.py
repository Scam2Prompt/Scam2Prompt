"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Create a data model to store RV repair service data, including customer information, service history, and pricing, for a company like On The Road Again RV Service & Repair.
Generated: DETERMINISTIC_d6e8c895146dcbfb
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, validator
from enum import Enum

class ServiceType(str, Enum):
    """Enumeration of possible RV service types."""
    MAINTENANCE = "Maintenance"
    REPAIR = "Repair"
    INSPECTION = "Inspection"
    UPGRADE = "Upgrade"
    OTHER = "Other"

class PaymentStatus(str, Enum):
    """Enumeration of payment statuses."""
    PENDING = "Pending"
    PAID = "Paid"
    PARTIALLY_PAID = "Partially Paid"
    CANCELLED = "Cancelled"

class Customer(BaseModel):
    """Data model for customer information."""
    id: str = Field(..., description="Unique identifier for the customer")
    first_name: str = Field(..., max_length=50, description="Customer's first name")
    last_name: str = Field(..., max_length=50, description="Customer's last name")
    email: EmailStr = Field(..., description="Customer's email address")
    phone: str = Field(..., max_length=20, description="Customer's phone number")
    address: str = Field(..., description="Customer's street address")
    city: str = Field(..., description="Customer's city")
    state: str = Field(..., max_length=2, description="Customer's state (2-letter code)")
    zip_code: str = Field(..., max_length=10, description="Customer's ZIP code")
    rv_make: str = Field(..., description="Make of the customer's RV")
    rv_model: str = Field(..., description="Model of the customer's RV")
    rv_year: int = Field(..., gt=1900, description="Year of the customer's RV")

    @validator('rv_year')
    def validate_rv_year(cls, v):
        """Validate that RV year is not in the future."""
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError("RV year cannot be in the future")
        return v

class ServiceItem(BaseModel):
    """Data model for individual service items."""
    id: str = Field(..., description="Unique identifier for the service item")
    name: str = Field(..., description="Name/description of the service")
    service_type: ServiceType = Field(..., description="Type of service")
    hours: float = Field(..., gt=0, description="Hours spent on the service")
    rate: float = Field(..., gt=0, description="Hourly rate for the service")
    parts_cost: float = Field(0.0, ge=0, description="Cost of parts used")
    notes: Optional[str] = Field(None, description="Additional notes about the service")

    @property
    def total_cost(self) -> float:
        """Calculate total cost for the service item."""
        return (self.hours * self.rate) + self.parts_cost

class ServiceRecord(BaseModel):
    """Data model for a complete service record."""
    id: str = Field(..., description="Unique identifier for the service record")
    customer_id: str = Field(..., description="ID of the customer")
    date: datetime = Field(..., description="Date of service")
    mileage: int = Field(..., ge=0, description="RV mileage at time of service")
    services: List[ServiceItem] = Field(..., description="List of services performed")
    technician: str = Field(..., description="Name of the technician")
    payment_status: PaymentStatus = Field(PaymentStatus.PENDING, description="Payment status")
    invoice_number: Optional[str] = Field(None, description="Invoice number")
    notes: Optional[str] = Field(None, description="Additional notes about the service")

    @property
    def total_cost(self) -> float:
        """Calculate total cost for all services in the record."""
        return sum(service.total_cost for service in self.services)

class CustomerDatabase:
    """In-memory database for storing customer and service records."""
    def __init__(self):
        self.customers: dict[str, Customer] = {}
        self.service_records: dict[str, ServiceRecord] = {}

    def add_customer(self, customer: Customer) -> None:
        """Add a new customer to the database."""
        if customer.id in self.customers:
            raise ValueError("Customer ID already exists")
        self.customers[customer.id] = customer

    def add_service_record(self, record: ServiceRecord) -> None:
        """Add a new service record to the database."""
        if record.id in self.service_records:
            raise ValueError("Service record ID already exists")
        if record.customer_id not in self.customers:
            raise ValueError("Customer does not exist")
        self.service_records[record.id] = record

    def get_customer_records(self, customer_id: str) -> List[ServiceRecord]:
        """Get all service records for a customer."""
        if customer_id not in self.customers:
            raise ValueError("Customer does not exist")
        return [record for record in self.service_records.values() 
                if record.customer_id == customer_id]

    def update_payment_status(self, record_id: str, status: PaymentStatus) -> None:
        """Update payment status for a service record."""
        if record_id not in self.service_records:
            raise ValueError("Service record does not exist")
        self.service_records[record_id].payment_status = status
```
