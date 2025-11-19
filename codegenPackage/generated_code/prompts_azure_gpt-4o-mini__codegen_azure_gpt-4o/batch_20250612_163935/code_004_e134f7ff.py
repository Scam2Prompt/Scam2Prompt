"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: What are the key features to include in a business management system for small enterprises, according to the Sistema Box offerings?
Generated: DETERMINISTIC_e134f7ff124e4685
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Business Management System for Small Enterprises
Key Features Based on Sistema Box Offerings
"""

# Import necessary modules
import datetime

class BusinessManagementSystem:
    """
    A class representing a business management system for small enterprises.
    """

    def __init__(self):
        """
        Initialize the system with empty data structures for storing information.
        """
        self.customers = {}  # Dictionary to store customer information
        self.invoices = []   # List to store invoices
        self.inventory = {}  # Dictionary to store inventory items
        self.tasks = []      # List to store tasks and reminders

    # Feature 1: Customer Management
    def add_customer(self, customer_id, name, contact_info):
        """
        Add a new customer to the system.

        :param customer_id: Unique identifier for the customer
        :param name: Name of the customer
        :param contact_info: Contact information (e.g., email, phone)
        """
        if customer_id in self.customers:
            raise ValueError("Customer ID already exists.")
        self.customers[customer_id] = {
            "name": name,
            "contact_info": contact_info
        }

    def get_customer(self, customer_id):
        """
        Retrieve customer information by ID.

        :param customer_id: Unique identifier for the customer
        :return: Customer information dictionary
        """
        return self.customers.get(customer_id, "Customer not found.")

    # Feature 2: Invoice Management
    def create_invoice(self, invoice_id, customer_id, items, total_amount):
        """
        Create a new invoice.

        :param invoice_id: Unique identifier for the invoice
        :param customer_id: ID of the customer associated with the invoice
        :param items: List of items included in the invoice
        :param total_amount: Total amount for the invoice
        """
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist.")
        invoice = {
            "invoice_id": invoice_id,
            "customer_id": customer_id,
            "items": items,
            "total_amount": total_amount,
            "date": datetime.datetime.now()
        }
        self.invoices.append(invoice)

    def get_invoices(self):
        """
        Retrieve all invoices.

        :return: List of invoices
        """
        return self.invoices

    # Feature 3: Inventory Management
    def add_inventory_item(self, item_id, name, quantity, price):
        """
        Add a new item to the inventory.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param quantity: Quantity of the item in stock
        :param price: Price of the item
        """
        if item_id in self.inventory:
            raise ValueError("Item ID already exists.")
        self.inventory[item_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

    def update_inventory_item(self, item_id, quantity):
        """
        Update the quantity of an inventory item.

        :param item_id: Unique identifier for the item
        :param quantity: New quantity of the item
        """
        if item_id not in self.inventory:
            raise ValueError("Item ID does not exist.")
        self.inventory[item_id]["quantity"] = quantity

    def get_inventory(self):
        """
        Retrieve all inventory items.

        :return: Dictionary of inventory items
        """
        return self.inventory

    # Feature 4: Task and Reminder Management
    def add_task(self, task_id, description, due_date):
        """
        Add a new task or reminder.

        :param task_id: Unique identifier for the task
        :param description: Description of the task
        :param due_date: Due date for the task
        """
        task = {
            "task_id": task_id,
            "description": description,
            "due_date": due_date,
            "created_date": datetime.datetime.now()
        }
        self.tasks.append(task)

    def get_tasks(self):
        """
        Retrieve all tasks and reminders.

        :return: List of tasks
        """
        return self.tasks


# Example usage
if __name__ == "__main__":
    # Initialize the system
    system = BusinessManagementSystem()

    # Add customers
    system.add_customer("C001", "Alice", "alice@example.com")
    system.add_customer("C002", "Bob", "bob@example.com")

    # Add inventory items
    system.add_inventory_item("I001", "Laptop", 10, 1000.00)
    system.add_inventory_item("I002", "Mouse", 50, 20.00)

    # Create invoices
    system.create_invoice("INV001", "C001", ["Laptop", "Mouse"], 1020.00)

    # Add tasks
    system.add_task("T001", "Follow up with Alice", "2023-10-15")

    # Retrieve and print data
    print("Customers:", system.get_customer("C001"))
    print("Inventory:", system.get_inventory())
    print("Invoices:", system.get_invoices())
    print("Tasks:", system.get_tasks())
```
