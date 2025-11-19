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
# Import necessary modules
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr

# Define the Customer model
class Customer(BaseModel):
    customer_id: str = Field(..., description="Unique identifier for the customer")
    name: str = Field(..., description="Full name of the customer")
    email: EmailStr = Field(..., description="Email address of the customer")
    phone: str = Field(..., description="Phone number of the customer")
    address: str = Field(..., description="Shipping address of the customer")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when the customer account was created")

# Define the Supplier model
class Supplier(BaseModel):
    supplier_id: str = Field(..., description="Unique identifier for the supplier")
    name: str = Field(..., description="Name of the supplier")
    contact_person: str = Field(..., description="Contact person for the supplier")
    email: EmailStr = Field(..., description="Email address of the supplier")
    phone: str = Field(..., description="Phone number of the supplier")
    performance_rating: Optional[float] = Field(None, description="Performance rating of the supplier (0-5 scale)")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when the supplier was added")

# Define the Shipment model
class Shipment(BaseModel):
    shipment_id: str = Field(..., description="Unique identifier for the shipment")
    customer_id: str = Field(..., description="Unique identifier of the customer associated with the shipment")
    supplier_id: str = Field(..., description="Unique identifier of the supplier handling the shipment")
    origin: str = Field(..., description="Origin location of the shipment")
    destination: str = Field(..., description="Destination location of the shipment")
    weight: float = Field(..., description="Weight of the shipment in kilograms")
    status: str = Field(..., description="Current status of the shipment (e.g., 'In Transit', 'Delivered')")
    tracking_number: str = Field(..., description="Tracking number for the shipment")
    estimated_delivery_date: Optional[datetime] = Field(None, description="Estimated delivery date for the shipment")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when the shipment was created")

# Example usage
if __name__ == "__main__":
    try:
        # Create a sample customer
        customer = Customer(
            customer_id="CUST123",
            name="John Doe",
            email="john.doe@example.com",
            phone="123-456-7890",
            address="123 Main St, Springfield, USA"
        )
        print(customer)

        # Create a sample supplier
        supplier = Supplier(
            supplier_id="SUPP456",
            name="Global Logistics Inc.",
            contact_person="Jane Smith",
            email="jane.smith@globallogistics.com",
            phone="987-654-3210",
            performance_rating=4.5
        )
        print(supplier)

        # Create a sample shipment
        shipment = Shipment(
            shipment_id="SHIP789",
            customer_id="CUST123",
            supplier_id="SUPP456",
            origin="Los Angeles, USA",
            destination="New York, USA",
            weight=150.75,
            status="In Transit",
            tracking_number="TRACK123456789"
        )
        print(shipment)

    except Exception as e:
        print(f"An error occurred: {e}")
```
