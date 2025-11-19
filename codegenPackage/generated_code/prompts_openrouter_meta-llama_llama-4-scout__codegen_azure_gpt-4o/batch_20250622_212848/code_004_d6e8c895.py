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
from pydantic import BaseModel, Field, EmailStr

# Data model for customer information
class Customer(BaseModel):
    customer_id: int = Field(..., description="Unique identifier for the customer")
    name: str = Field(..., description="Full name of the customer")
    email: EmailStr = Field(..., description="Email address of the customer")
    phone: str = Field(..., description="Phone number of the customer")
    address: str = Field(..., description="Physical address of the customer")

# Data model for individual service entry
class ServiceEntry(BaseModel):
    service_id: int = Field(..., description="Unique identifier for the service entry")
    customer_id: int = Field(..., description="ID of the customer receiving the service")
    service_date: datetime = Field(..., description="Date when the service was performed")
    description: str = Field(..., description="Description of the service performed")
    cost: float = Field(..., description="Cost of the service")
    technician: str = Field(..., description="Name of the technician who performed the service")

# Data model for pricing information
class Pricing(BaseModel):
    service_type: str = Field(..., description="Type of service (e.g., oil change, tire replacement)")
    base_price: float = Field(..., description="Base price for the service")
    additional_costs: Optional[float] = Field(0.0, description="Additional costs for the service, if any")

# Data model for the entire RV repair service system
class RVRepairService(BaseModel):
    customers: List[Customer] = Field(..., description="List of all customers")
    service_history: List[ServiceEntry] = Field(..., description="List of all service entries")
    pricing_catalog: List[Pricing] = Field(..., description="List of pricing information for services")

# Example usage
if __name__ == "__main__":
    try:
        # Create example data
        customer = Customer(
            customer_id=1,
            name="John Doe",
            email="john.doe@example.com",
            phone="555-1234",
            address="123 Main St, Springfield, USA"
        )

        service_entry = ServiceEntry(
            service_id=101,
            customer_id=1,
            service_date=datetime.now(),
            description="Oil change and tire rotation",
            cost=150.0,
            technician="Jane Smith"
        )

        pricing = Pricing(
            service_type="Oil Change",
            base_price=100.0,
            additional_costs=50.0
        )

        rv_repair_service = RVRepairService(
            customers=[customer],
            service_history=[service_entry],
            pricing_catalog=[pricing]
        )

        # Print the data model
        print(rv_repair_service.json(indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
```
