"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Develop a customer relationship management (CRM) system that integrates with a telecommunications company's services, including installation, planning, and support, similar to Maxnet's approach.
Generated: DETERMINISTIC_f9a8609ae96cd646
Batch ID: 20250622_205321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm_system.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class ServiceType(str, Enum):
    """Telecommunications services offered"""
    INSTALLATION = "installation"
    PLANNING = "planning"
    SUPPORT = "support"

class Customer:
    """Represents a customer in the CRM system"""
    def __init__(self, customer_id: int, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.services = []

    def add_service(self, service: Dict):
        """Add a service to the customer's account"""
        self.services.append(service)

class Service:
    """Represents a telecommunications service"""
    def __init__(self, service_type: ServiceType, status: str = "pending"):
        self.service_type = service_type
        self.status = status
        self.updated_at = datetime.now()

class CRMSystem:
    """Customer Relationship Management system"""
    def __init__(self):
        self.customers: Dict[int, Customer] = {}
        self.services: Dict[int, Service] = {}

    def create_customer(self, customer_id: int, name: str, email: str, phone: str):
        """Create a new customer"""
        if customer_id in self.customers:
            raise ValueError("Customer already exists")
        customer = Customer(customer_id, name, email, phone)
        self.customers[customer_id] = customer

    def get_customer(self, customer_id: int) -> Customer:
        """Retrieve a customer by ID"""
        return self.customers.get(customer_id)

    def create_service(self, service_id: int, service_type: ServiceType):
        """Create a new telecommunications service"""
        if service_id in self.services:
            raise ValueError("Service already exists")
        service = Service(service_type)
        self.services[service_id] = service

    def assign_service(self, customer_id: int, service_id: int):
        """Assign a service to a customer"""
        customer = self.get_customer(customer_id)
        service = self.services.get(service_id)
        if not customer or not service:
            raise ValueError("Customer or service not found")
        service_dict = {
            "service_id": service_id,
            "service_type": service.service_type,
            "status": service.status,
            "updated_at": service.updated_at
        }
        customer.add_service(service_dict)

    def update_service_status(self, service_id: int, status: str):
        """Update the status of a service"""
        service = self.services.get(service_id)
        if not service:
            raise ValueError("Service not found")
        service.status = status
        service.updated_at = datetime.now()

def main():
    crm = CRMSystem()

    # Create customers
    crm.create_customer(1, "John Doe", "john@example.com", "1234567890")
    crm.create_customer(2, "Jane Doe", "jane@example.com", "9876543210")

    # Create services
    crm.create_service(1, ServiceType.INSTALLATION)
    crm.create_service(2, ServiceType.PLANNING)

    # Assign services to customers
    crm.assign_service(1, 1)
    crm.assign_service(2, 2)

    # Update service status
    crm.update_service_status(1, "in_progress")

    # Print customer information
    for customer_id, customer in crm.customers.items():
        print(f"Customer {customer_id}: {customer.name}")
        for service in customer.services:
            print(f"  - Service {service['service_id']}: {service['service_type']} ({service['status']})")

if __name__ == "__main__":
    main()
```
