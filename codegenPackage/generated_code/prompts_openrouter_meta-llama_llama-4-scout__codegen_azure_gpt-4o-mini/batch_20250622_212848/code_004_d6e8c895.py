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
import json

class Customer:
    """Class to represent a customer."""
    
    def __init__(self, customer_id: int, name: str, phone: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        """Convert customer data to dictionary format for storage."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

class ServiceRecord:
    """Class to represent a service record."""
    
    def __init__(self, service_id: int, customer_id: int, service_date: datetime, description: str, cost: float):
        self.service_id = service_id
        self.customer_id = customer_id
        self.service_date = service_date
        self.description = description
        self.cost = cost

    def to_dict(self):
        """Convert service record data to dictionary format for storage."""
        return {
            "service_id": self.service_id,
            "customer_id": self.customer_id,
            "service_date": self.service_date.isoformat(),
            "description": self.description,
            "cost": self.cost
        }

class RVRepairService:
    """Class to manage RV repair service data."""
    
    def __init__(self):
        self.customers: List[Customer] = []
        self.service_records: List[ServiceRecord] = []

    def add_customer(self, customer: Customer):
        """Add a new customer to the service."""
        self.customers.append(customer)

    def add_service_record(self, service_record: ServiceRecord):
        """Add a new service record for a customer."""
        self.service_records.append(service_record)

    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Retrieve a customer by their ID."""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def get_service_history(self, customer_id: int) -> List[ServiceRecord]:
        """Retrieve service history for a specific customer."""
        return [record for record in self.service_records if record.customer_id == customer_id]

    def save_to_file(self, filename: str):
        """Save customers and service records to a JSON file."""
        try:
            data = {
                "customers": [customer.to_dict() for customer in self.customers],
                "service_records": [record.to_dict() for record in self.service_records]
            }
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load customers and service records from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.customers = [Customer(**customer) for customer in data.get("customers", [])]
                self.service_records = [ServiceRecord(**record) for record in data.get("service_records", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    service = RVRepairService()
    
    # Adding a customer
    customer1 = Customer(customer_id=1, name="John Doe", phone="555-1234", email="john@example.com")
    service.add_customer(customer1)
    
    # Adding a service record
    service_record1 = ServiceRecord(service_id=1, customer_id=1, service_date=datetime.now(), description="Oil Change", cost=99.99)
    service.add_service_record(service_record1)
    
    # Save data to file
    service.save_to_file("rv_service_data.json")
    
    # Load data from file
    service.load_from_file("rv_service_data.json")
```
