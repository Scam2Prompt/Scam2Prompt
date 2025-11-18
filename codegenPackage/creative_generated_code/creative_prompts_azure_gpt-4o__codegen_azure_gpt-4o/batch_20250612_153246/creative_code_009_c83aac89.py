"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Write code to generate a customer management system for tracking orders from private companies, NGOs, government offices, and learning institutions, as described on Sanuri Supplies' site.
Generated: DETERMINISTIC_c83aac89292a086a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# customer_management_system.py
# A Customer Management System for tracking orders from private companies, NGOs, government offices, and learning institutions.

import uuid
from datetime import datetime


class Customer:
    """
    Represents a customer in the system.
    """
    def __init__(self, name, customer_type, email, phone_number):
        self.customer_id = str(uuid.uuid4())  # Generate a unique ID for the customer
        self.name = name
        self.customer_type = customer_type  # Private Company, NGO, Government Office, Learning Institution
        self.email = email
        self.phone_number = phone_number
        self.orders = []  # List to store orders for the customer

    def add_order(self, order):
        """
        Add an order to the customer's list of orders.
        """
        self.orders.append(order)

    def __str__(self):
        return f"Customer: {self.name} | Type: {self.customer_type} | Orders: {len(self.orders)}"


class Order:
    """
    Represents an order in the system.
    """
    def __init__(self, description, amount, order_date=None):
        self.order_id = str(uuid.uuid4())  # Generate a unique ID for the order
        self.description = description
        self.amount = amount
        self.order_date = order_date if order_date else datetime.now()  # Default to current date/time

    def __str__(self):
        return f"Order ID: {self.order_id} | Description: {self.description} | Amount: {self.amount} | Date: {self.order_date}"


class CustomerManagementSystem:
    """
    The main system for managing customers and their orders.
    """
    def __init__(self):
        self.customers = {}  # Dictionary to store customers by their ID

    def add_customer(self, name, customer_type, email, phone_number):
        """
        Add a new customer to the system.
        """
        if customer_type not in ['Private Company', 'NGO', 'Government Office', 'Learning Institution']:
            raise ValueError(f"Invalid customer type: {customer_type}. Must be one of: Private Company, NGO, Government Office, Learning Institution.")
        
        customer = Customer(name, customer_type, email, phone_number)
        self.customers[customer.customer_id] = customer
        return customer.customer_id

    def get_customer(self, customer_id):
        """
        Retrieve a customer by their ID.
        """
        if customer_id not in self.customers:
            raise ValueError(f"Customer with ID {customer_id} not found.")
        return self.customers[customer_id]

    def add_order_to_customer(self, customer_id, description, amount):
        """
        Add an order to a specific customer.
        """
        customer = self.get_customer(customer_id)
        order = Order(description, amount)
        customer.add_order(order)
        return order.order_id

    def get_all_customers(self):
        """
        Retrieve all customers in the system.
        """
        return list(self.customers.values())

    def get_customer_orders(self, customer_id):
        """
        Retrieve all orders for a specific customer.
        """
        customer = self.get_customer(customer_id)
        return customer.orders


# Example usage (can be commented out for production environments)
if __name__ == "__main__":
    cms = CustomerManagementSystem()

    # Add customers
    customer_id_1 = cms.add_customer("ABC Corp", "Private Company", "contact@abccorp.com", "123-456-7890")
    customer_id_2 = cms.add_customer("Helping Hands NGO", "NGO", "info@helpinghands.org", "987-654-3210")
    
    # Add orders to customers
    cms.add_order_to_customer(customer_id_1, "Office Supplies", 500.75)
    cms.add_order_to_customer(customer_id_2, "Educational Materials", 1200.00)
    
    # Retrieve and display customers
    for customer in cms.get_all_customers():
        print(customer)
        for order in customer.orders:
            print("  ", order)
```
