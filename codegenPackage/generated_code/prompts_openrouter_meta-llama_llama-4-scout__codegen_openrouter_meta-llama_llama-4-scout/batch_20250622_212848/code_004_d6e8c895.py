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
# models.py

from datetime import datetime
from typing import List
from pydantic import BaseModel, validator

class Address(BaseModel):
    """Address data model"""
    street: str
    city: str
    state: str
    zip_code: str

class Customer(BaseModel):
    """Customer data model"""
    id: int
    name: str
    email: str
    phone_number: str
    address: Address

class Service(BaseModel):
    """Service data model"""
    id: int
    name: str
    description: str
    price: float

class Repair(BaseModel):
    """Repair data model"""
    id: int
    service_id: int
    customer_id: int
    date: datetime
    description: str
    labor_hours: float
    labor_rate: float
    parts_cost: float

    @property
    def total_cost(self) -> float:
        """Calculate total cost of repair"""
        labor_cost = self.labor_hours * self.labor_rate
        return labor_cost + self.parts_cost

class ServiceHistory(BaseModel):
    """Service history data model"""
    customer_id: int
    repairs: List[Repair]

class Pricing(BaseModel):
    """Pricing data model"""
    services: List[Service]
    labor_rate: float

class RVRepairService(BaseModel):
    """RV repair service data model"""
    customers: List[Customer]
    services: List[Service]
    repairs: List[Repair]
    pricing: Pricing

    @validator('customers')
    def validate_customers(cls, v):
        """Validate customers list"""
        if not isinstance(v, list):
            raise ValueError('Customers must be a list')
        return v

    @validator('services')
    def validate_services(cls, v):
        """Validate services list"""
        if not isinstance(v, list):
            raise ValueError('Services must be a list')
        return v

    @validator('repairs')
    def validate_repairs(cls, v):
        """Validate repairs list"""
        if not isinstance(v, list):
            raise ValueError('Repairs must be a list')
        return v

# Example usage
if __name__ == "__main__":
    try:
        customer1 = Customer(
            id=1,
            name="John Doe",
            email="john.doe@example.com",
            phone_number="123-456-7890",
            address=Address(
                street="123 Main St",
                city="Anytown",
                state="CA",
                zip_code="12345"
            )
        )

        service1 = Service(
            id=1,
            name="Oil Change",
            description="Oil change service",
            price=50.0
        )

        repair1 = Repair(
            id=1,
            service_id=1,
            customer_id=1,
            date=datetime(2022, 1, 1),
            description="Oil change and filter replacement",
            labor_hours=1.0,
            labor_rate=100.0,
            parts_cost=50.0
        )

        pricing1 = Pricing(
            services=[service1],
            labor_rate=100.0
        )

        rv_repair_service = RVRepairService(
            customers=[customer1],
            services=[service1],
            repairs=[repair1],
            pricing=pricing1
        )

        print(rv_repair_service)
        print(f"Total cost of repair: ${repair1.total_cost:.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
