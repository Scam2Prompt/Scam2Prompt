"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Develop a basic CRM system for a wood products supplier like Maderas Elaboradas, incorporating features for tracking customer inquiries, orders, and product deliveries.
Generated: DETERMINISTIC_e5033854ce332841
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm_system.py

class Customer:
    """Class to represent a customer in the CRM system."""
    
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.inquiries = []
        self.orders = []

    def add_inquiry(self, inquiry):
        """Add an inquiry to the customer's record."""
        self.inquiries.append(inquiry)

    def add_order(self, order):
        """Add an order to the customer's record."""
        self.orders.append(order)


class Inquiry:
    """Class to represent a customer inquiry."""
    
    def __init__(self, inquiry_id, customer_id, message):
        self.inquiry_id = inquiry_id
        self.customer_id = customer_id
        self.message = message


class Order:
    """Class to represent a customer order."""
    
    def __init__(self, order_id, customer_id, product, quantity):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product = product
        self.quantity = quantity
        self.status = 'Pending'  # Default status


class CRMSystem:
    """Class to manage the CRM system."""
    
    def __init__(self):
        self.customers = {}
        self.inquiries = {}
        self.orders = {}

    def add_customer(self, customer_id, name, email):
        """Add a new customer to the CRM system."""
        if customer_id in self.customers:
            raise ValueError("Customer ID already exists.")
        self.customers[customer_id] = Customer(customer_id, name, email)

    def add_inquiry(self, inquiry_id, customer_id, message):
        """Add a new inquiry for a customer."""
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist.")
        inquiry = Inquiry(inquiry_id, customer_id, message)
        self.customers[customer_id].add_inquiry(inquiry)
        self.inquiries[inquiry_id] = inquiry

    def add_order(self, order_id, customer_id, product, quantity):
        """Add a new order for a customer."""
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist.")
        order = Order(order_id, customer_id, product, quantity)
        self.customers[customer_id].add_order(order)
        self.orders[order_id] = order

    def get_customer_info(self, customer_id):
        """Retrieve customer information including inquiries and orders."""
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist.")
        customer = self.customers[customer_id]
        return {
            "name": customer.name,
            "email": customer.email,
            "inquiries": [inquiry.message for inquiry in customer.inquiries],
            "orders": [(order.product, order.quantity, order.status) for order in customer.orders]
        }


# Example usage
if __name__ == "__main__":
    crm = CRMSystem()
    
    # Adding customers
    try:
        crm.add_customer(1, "John Doe", "john@example.com")
        crm.add_customer(2, "Jane Smith", "jane@example.com")
        
        # Adding inquiries
        crm.add_inquiry(101, 1, "What types of wood do you supply?")
        crm.add_inquiry(102, 2, "Do you offer bulk discounts?")
        
        # Adding orders
        crm.add_order(201, 1, "Oak Wood", 10)
        crm.add_order(202, 2, "Pine Wood", 5)
        
        # Retrieving customer info
        customer_info = crm.get_customer_info(1)
        print(customer_info)
        
    except ValueError as e:
        print(f"Error: {e}")
```
