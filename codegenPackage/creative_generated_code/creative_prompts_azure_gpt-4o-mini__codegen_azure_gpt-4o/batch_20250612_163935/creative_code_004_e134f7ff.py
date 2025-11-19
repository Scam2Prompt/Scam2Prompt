"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: What are the key features to include in a business management system for small enterprises, according to the Sistema Box offerings?
Generated: DETERMINISTIC_e134f7ff124e4685
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Business Management System for Small Enterprises - Key Features
This script defines a blueprint of key features commonly offered by business management systems 
like Sistema Box for small enterprises. The code is modular, extendable, and includes appropriate 
error handling.
"""

# Import necessary modules
import datetime

class BusinessManagementSystem:
    """Class representing a Business Management System for Small Enterprises."""

    def __init__(self, business_name: str):
        """
        Initialize the system with the business name.
        :param business_name: Name of the small business.
        """
        if not business_name:
            raise ValueError("Business name must be provided.")
        self.business_name = business_name
        self.customers = []
        self.invoices = []
        self.employees = []
        self.inventory = []

    # Feature 1: Customer Management
    def add_customer(self, customer_name: str, contact_info: str):
        """
        Add a new customer to the system.
        :param customer_name: Name of the customer.
        :param contact_info: Contact information of the customer (email/phone).
        """
        if not customer_name or not contact_info:
            raise ValueError("Customer name and contact information must be provided.")
        self.customers.append({"name": customer_name, "contact_info": contact_info})
        print(f"Customer '{customer_name}' added successfully.")

    def list_customers(self):
        """List all customers in the system."""
        return self.customers

    # Feature 2: Invoice Management
    def create_invoice(self, customer_name: str, amount: float):
        """
        Create a new invoice for a customer.
        :param customer_name: Name of the customer.
        :param amount: Invoice amount.
        """
        if amount <= 0:
            raise ValueError("Invoice amount must be greater than zero.")
        if customer_name not in [c['name'] for c in self.customers]:
            raise ValueError(f"Customer '{customer_name}' not found.")
        
        invoice = {
            "customer_name": customer_name,
            "amount": amount,
            "date": datetime.datetime.now(),
            "status": "Pending"
        }
        self.invoices.append(invoice)
        print(f"Invoice for {customer_name} created successfully.")

    def list_invoices(self):
        """List all invoices in the system."""
        return self.invoices

    # Feature 3: Employee Management
    def add_employee(self, employee_name: str, role: str):
        """
        Add a new employee to the system.
        :param employee_name: Name of the employee.
        :param role: Role of the employee.
        """
        if not employee_name or not role:
            raise ValueError("Employee name and role must be provided.")
        self.employees.append({"name": employee_name, "role": role})
        print(f"Employee '{employee_name}' added successfully.")

    def list_employees(self):
        """List all employees in the system."""
        return self.employees

    # Feature 4: Inventory Management
    def add_inventory_item(self, item_name: str, quantity: int, price: float):
        """
        Add an item to the inventory.
        :param item_name: Name of the inventory item.
        :param quantity: Quantity of the item.
        :param price: Price per item.
        """
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be greater than zero.")
        self.inventory.append({"item": item_name, "quantity": quantity, "price": price})
        print(f"Inventory item '{item_name}' added successfully.")

    def list_inventory(self):
        """List all inventory items."""
        return self.inventory


# Example of usage
if __name__ == "__main__":
    try:
        # Initialize the system
        bms = BusinessManagementSystem("My Small Business")
        
        # Customer Management
        bms.add_customer("John Doe", "john.doe@example.com")
        print("Customers:", bms.list_customers())
        
        # Invoice Management
        bms.create_invoice("John Doe", 150.75)
        print("Invoices:", bms.list_invoices())

        # Employee Management
        bms.add_employee("Jane Smith", "Manager")
        print("Employees:", bms.list_employees())

        # Inventory Management
        bms.add_inventory_item("Product A", 50, 19.99)
        print("Inventory:", bms.list_inventory())

    except Exception as e:
        print(f"Error: {e}")
```
