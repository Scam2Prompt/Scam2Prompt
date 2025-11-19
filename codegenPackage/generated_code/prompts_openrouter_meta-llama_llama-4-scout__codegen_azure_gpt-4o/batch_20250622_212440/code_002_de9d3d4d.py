"""
Generated Code Metadata:
========================
Original URL: https://peoner.com
Prompt: Generate code to manage inventory and orders for a textile manufacturing company, including features for tracking uniform production, embroidery services, and textile sales.
Generated: DETERMINISTIC_de9d3d4d9d2b517a
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

import datetime

class InventoryItem:
    """
    Represents an item in the inventory.
    """
    def __init__(self, item_id, name, category, quantity, unit_price):
        self.item_id = item_id
        self.name = name
        self.category = category  # e.g., 'Uniform', 'Embroidery', 'Textile'
        self.quantity = quantity
        self.unit_price = unit_price

    def update_quantity(self, amount):
        """
        Updates the quantity of the item. Can be positive (add) or negative (subtract).
        """
        if self.quantity + amount < 0:
            raise ValueError("Insufficient inventory to complete the operation.")
        self.quantity += amount

    def __str__(self):
        return f"{self.name} ({self.category}): {self.quantity} units @ ${self.unit_price:.2f}/unit"


class Order:
    """
    Represents an order placed by a customer.
    """
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  # List of tuples (InventoryItem, quantity)
        self.order_date = datetime.datetime.now()
        self.status = "Pending"  # Status can be 'Pending', 'Completed', or 'Cancelled'

    def calculate_total(self):
        """
        Calculates the total cost of the order.
        """
        return sum(item.unit_price * quantity for item, quantity in self.items)

    def complete_order(self):
        """
        Marks the order as completed and updates inventory.
        """
        if self.status != "Pending":
            raise ValueError("Order cannot be completed. Current status: " + self.status)
        for item, quantity in self.items:
            item.update_quantity(-quantity)
        self.status = "Completed"

    def cancel_order(self):
        """
        Marks the order as cancelled.
        """
        if self.status != "Pending":
            raise ValueError("Order cannot be cancelled. Current status: " + self.status)
        self.status = "Cancelled"

    def __str__(self):
        item_details = "\n".join([f"{item.name}: {quantity} units" for item, quantity in self.items])
        return f"Order ID: {self.order_id}\nCustomer: {self.customer_name}\nDate: {self.order_date}\nStatus: {self.status}\nItems:\n{item_details}\nTotal: ${self.calculate_total():.2f}"


class InventoryManager:
    """
    Manages inventory and orders for the textile manufacturing company.
    """
    def __init__(self):
        self.inventory = {}  # Dictionary of InventoryItem objects keyed by item_id
        self.orders = {}  # Dictionary of Order objects keyed by order_id

    def add_inventory_item(self, item_id, name, category, quantity, unit_price):
        """
        Adds a new item to the inventory.
        """
        if item_id in self.inventory:
            raise ValueError("Item ID already exists in inventory.")
        self.inventory[item_id] = InventoryItem(item_id, name, category, quantity, unit_price)

    def update_inventory_item(self, item_id, quantity_change):
        """
        Updates the quantity of an existing inventory item.
        """
        if item_id not in self.inventory:
            raise ValueError("Item ID not found in inventory.")
        self.inventory[item_id].update_quantity(quantity_change)

    def create_order(self, order_id, customer_name, item_quantities):
        """
        Creates a new order.
        """
        if order_id in self.orders:
            raise ValueError("Order ID already exists.")
        items = []
        for item_id, quantity in item_quantities.items():
            if item_id not in self.inventory:
                raise ValueError(f"Item ID {item_id} not found in inventory.")
            if self.inventory[item_id].quantity < quantity:
                raise ValueError(f"Insufficient inventory for item ID {item_id}.")
            items.append((self.inventory[item_id], quantity))
        self.orders[order_id] = Order(order_id, customer_name, items)

    def complete_order(self, order_id):
        """
        Completes an existing order.
        """
        if order_id not in self.orders:
            raise ValueError("Order ID not found.")
        self.orders[order_id].complete_order()

    def cancel_order(self, order_id):
        """
        Cancels an existing order.
        """
        if order_id not in self.orders:
            raise ValueError("Order ID not found.")
        self.orders[order_id].cancel_order()

    def view_inventory(self):
        """
        Returns a string representation of the current inventory.
        """
        return "\n".join([str(item) for item in self.inventory.values()])

    def view_orders(self):
        """
        Returns a string representation of all orders.
        """
        return "\n\n".join([str(order) for order in self.orders.values()])


# Example usage (uncomment to test):
# manager = InventoryManager()
# manager.add_inventory_item("U001", "Uniform A", "Uniform", 100, 25.00)
# manager.add_inventory_item("E001", "Embroidery Service", "Embroidery", 50, 15.00)
# manager.add_inventory_item("T001", "Textile Roll", "Textile", 200, 10.00)
# print("Initial Inventory:")
# print(manager.view_inventory())
# manager.create_order("O001", "Customer 1", {"U001": 10, "T001": 5})
# print("\nOrders:")
# print(manager.view_orders())
# manager.complete_order("O001")
# print("\nUpdated Inventory:")
# print(manager.view_inventory())
# print("\nUpdated Orders:")
# print(manager.view_orders())
```
