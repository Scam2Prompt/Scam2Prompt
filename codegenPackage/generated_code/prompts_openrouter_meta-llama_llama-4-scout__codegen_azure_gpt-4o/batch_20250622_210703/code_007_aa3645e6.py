"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Design a library for managing essential oil inventory, including functions for tracking stock levels, orders, and shipping information for an online store like Use Essential Oils Australia.
Generated: DETERMINISTIC_aa3645e6e47c9fdc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# essential_oil_inventory.py

"""
Essential Oil Inventory Management Library

This library provides functionality for managing essential oil inventory, 
including tracking stock levels, processing orders, and managing shipping information.

Author: [Your Name]
Date: [Today's Date]
"""

import json


class EssentialOilInventory:
    def __init__(self):
        """
        Initializes the inventory with an empty stock dictionary.
        """
        self.stock = {}  # Dictionary to store stock levels {oil_name: quantity}
        self.orders = []  # List to store orders
        self.shipping_info = {}  # Dictionary to store shipping information {order_id: shipping_details}

    def add_oil(self, oil_name, quantity):
        """
        Adds a new essential oil to the inventory or updates the quantity of an existing oil.

        :param oil_name: Name of the essential oil
        :param quantity: Quantity to add to the inventory
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.stock[oil_name] = self.stock.get(oil_name, 0) + quantity

    def remove_oil(self, oil_name, quantity):
        """
        Removes a specified quantity of an essential oil from the inventory.

        :param oil_name: Name of the essential oil
        :param quantity: Quantity to remove from the inventory
        """
        if oil_name not in self.stock:
            raise KeyError(f"{oil_name} not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if self.stock[oil_name] < quantity:
            raise ValueError(f"Not enough stock of {oil_name} to remove {quantity}.")
        self.stock[oil_name] -= quantity
        if self.stock[oil_name] == 0:
            del self.stock[oil_name]

    def get_stock(self, oil_name):
        """
        Retrieves the current stock level of a specific essential oil.

        :param oil_name: Name of the essential oil
        :return: Current stock level
        """
        return self.stock.get(oil_name, 0)

    def place_order(self, order_id, oil_name, quantity):
        """
        Places an order for a specific essential oil.

        :param order_id: Unique identifier for the order
        :param oil_name: Name of the essential oil
        :param quantity: Quantity to order
        """
        if oil_name not in self.stock:
            raise KeyError(f"{oil_name} not found in inventory.")
        if self.stock[oil_name] < quantity:
            raise ValueError(f"Not enough stock of {oil_name} to fulfill the order.")
        self.remove_oil(oil_name, quantity)
        self.orders.append({"order_id": order_id, "oil_name": oil_name, "quantity": quantity})

    def add_shipping_info(self, order_id, shipping_details):
        """
        Adds shipping information for a specific order.

        :param order_id: Unique identifier for the order
        :param shipping_details: Dictionary containing shipping details (e.g., address, tracking number)
        """
        if not any(order["order_id"] == order_id for order in self.orders):
            raise KeyError(f"Order ID {order_id} not found.")
        self.shipping_info[order_id] = shipping_details

    def get_shipping_info(self, order_id):
        """
        Retrieves shipping information for a specific order.

        :param order_id: Unique identifier for the order
        :return: Shipping details dictionary
        """
        return self.shipping_info.get(order_id, None)

    def save_inventory_to_file(self, file_path):
        """
        Saves the current inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.stock, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads inventory data from a JSON file.

        :param file_path: Path to the file containing inventory data
        """
        try:
            with open(file_path, 'r') as file:
                self.stock = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON data: {e}")


# Example usage (uncomment to test):
# inventory = EssentialOilInventory()
# inventory.add_oil("Lavender", 50)
# inventory.add_oil("Peppermint", 30)
# inventory.place_order("ORDER123", "Lavender", 10)
# inventory.add_shipping_info("ORDER123", {"address": "123 Main St", "tracking_number": "TRACK123"})
# print(inventory.get_stock("Lavender"))
# print(inventory.get_shipping_info("ORDER123"))
# inventory.save_inventory_to_file("inventory.json")
# inventory.load_inventory_from_file("inventory.json")
```
