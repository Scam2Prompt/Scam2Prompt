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
from typing import List
from datetime import datetime
from enum import Enum

# Define an Enum for shipment status
class ShipmentStatus(str, Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    LOST = "lost"
    DAMAGED = "damaged"

# Define a class for Address
class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str, country: str):
        """
        Initialize an Address object.

        Args:
        street (str): Street address.
        city (str): City.
        state (str): State or province.
        zip_code (str): ZIP code.
        country (str): Country.
        """
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

# Define a class for Customer
class Customer:
    def __init__(self, customer_id: int, name: str, email: str, phone: str, address: Address):
        """
        Initialize a Customer object.

        Args:
        customer_id (int): Unique customer ID.
        name (str): Customer name.
        email (str): Customer email.
        phone (str): Customer phone number.
        address (Address): Customer address.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

# Define a class for Supplier
class Supplier:
    def __init__(self, supplier_id: int, name: str, email: str, phone: str, address: Address):
        """
        Initialize a Supplier object.

        Args:
        supplier_id (int): Unique supplier ID.
        name (str): Supplier name.
        email (str): Supplier email.
        phone (str): Supplier phone number.
        address (Address): Supplier address.
        """
        self.supplier_id = supplier_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

# Define a class for Shipment
class Shipment:
    def __init__(self, shipment_id: int, customer: Customer, supplier: Supplier, tracking_number: str, status: ShipmentStatus, shipment_date: datetime):
        """
        Initialize a Shipment object.

        Args:
        shipment_id (int): Unique shipment ID.
        customer (Customer): Customer associated with the shipment.
        supplier (Supplier): Supplier associated with the shipment.
        tracking_number (str): Tracking number for the shipment.
        status (ShipmentStatus): Status of the shipment.
        shipment_date (datetime): Date the shipment was created.
        """
        self.shipment_id = shipment_id
        self.customer = customer
        self.supplier = supplier
        self.tracking_number = tracking_number
        self.status = status
        self.shipment_date = shipment_date

# Define a class for LogisticsCompany
class LogisticsCompany:
    def __init__(self):
        """
        Initialize a LogisticsCompany object.
        """
        self.customers: List[Customer] = []
        self.suppliers: List[Supplier] = []
        self.shipments: List[Shipment] = []

    def add_customer(self, customer: Customer):
        """
        Add a customer to the logistics company.

        Args:
        customer (Customer): Customer to add.
        """
        self.customers.append(customer)

    def add_supplier(self, supplier: Supplier):
        """
        Add a supplier to the logistics company.

        Args:
        supplier (Supplier): Supplier to add.
        """
        self.suppliers.append(supplier)

    def add_shipment(self, shipment: Shipment):
        """
        Add a shipment to the logistics company.

        Args:
        shipment (Shipment): Shipment to add.
        """
        self.shipments.append(shipment)

    def update_shipment_status(self, shipment_id: int, status: ShipmentStatus):
        """
        Update the status of a shipment.

        Args:
        shipment_id (int): ID of the shipment to update.
        status (ShipmentStatus): New status of the shipment.

        Raises:
        ValueError: If the shipment ID is not found.
        """
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                shipment.status = status
                return
        raise ValueError("Shipment ID not found")

# Example usage
if __name__ == "__main__":
    company = LogisticsCompany()

    # Create customers
    customer1_address = Address("123 Main St", "Anytown", "CA", "12345", "USA")
    customer1 = Customer(1, "John Doe", "john.doe@example.com", "123-456-7890", customer1_address)
    company.add_customer(customer1)

    # Create suppliers
    supplier1_address = Address("456 Elm St", "Othertown", "NY", "67890", "USA")
    supplier1 = Supplier(1, "Jane Smith", "jane.smith@example.com", "987-654-3210", supplier1_address)
    company.add_supplier(supplier1)

    # Create shipments
    shipment1 = Shipment(1, customer1, supplier1, "ABC123", ShipmentStatus.PENDING, datetime.now())
    company.add_shipment(shipment1)

    # Update shipment status
    company.update_shipment_status(1, ShipmentStatus.IN_TRANSIT)

    # Print shipment information
    for shipment in company.shipments:
        print(f"Shipment ID: {shipment.shipment_id}")
        print(f"Customer Name: {shipment.customer.name}")
        print(f"Supplier Name: {shipment.supplier.name}")
        print(f"Tracking Number: {shipment.tracking_number}")
        print(f"Status: {shipment.status.value}")
        print(f"Shipment Date: {shipment.shipment_date}")
        print("------------------------")
```
