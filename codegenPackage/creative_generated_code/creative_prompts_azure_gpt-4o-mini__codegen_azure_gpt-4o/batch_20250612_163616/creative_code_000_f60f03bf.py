"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Generate a code snippet for an inventory management system that tracks computer hardware and accessories like SSDs and projectors, similar to the offerings on mixpelinfobrazz.
Generated: DETERMINISTIC_f60f03bf7ef5e141
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Inventory Management System for Computer Hardware and Accessories

import json


class Item:
    """
    Represents a single item in the inventory.
    """
    def __init__(self, item_id, name, category, quantity, price):
        self.item_id = item_id         # Unique identifier for the item
        self.name = name               # Name of the item
        self.category = category       # Category, e.g., "SSD" or "Projector"
        self.quantity = quantity       # Quantity of the item in stock
        self.price = price             # Price per unit of the item

    def __str__(self):
        return f"{self.item_id}: {self.name} ({self.category}), Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Inventory:
    """
    Manages a collection of items in the inventory.
    """
    def __init__(self):
        self.items = {}  # Dictionary to store items, keyed by their item ID

    def add_item(self, item):
        """
        Add a new item to the inventory.
        :param item: The Item object to add.
        """
        if item.item_id in self.items:
            raise ValueError(f"Item with ID {item.item_id} already exists.")
        self.items[item.item_id] = item

    def update_item(self, item_id, quantity=None, price=None):
        """
        Update an item's quantity and/or price.
        :param item_id: The ID of the item to update.
        :param quantity: New quantity (optional).
        :param price: New price (optional).
        """
        if item_id not in self.items:
            raise ValueError(f"No item found with ID {item_id}.")
        if quantity is not None:
            self.items[item_id].quantity = quantity
        if price is not None:
            self.items[item_id].price = price

    def remove_item(self, item_id):
        """
        Remove an item from the inventory.
        :param item_id: The ID of the item to remove.
        """
        if item_id not in self.items:
            raise ValueError(f"No item found with ID {item_id}.")
        del self.items[item_id]

    def list_items(self):
        """
        List all items in the inventory.
        :return: List of all items.
        """
        return list(self.items.values())

    def save_to_file(self, filename):
        """
        Save the inventory data to a JSON file.
        :param filename: File name to save the inventory.
        """
        with open(filename, 'w') as f:
            json.dump({item_id: vars(item) for item_id, item in self.items.items()}, f, indent=4)

    def load_from_file(self, filename):
        """
        Load inventory data from a JSON file.
        :param filename: File name to load the inventory from.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.items = {item_id: Item(**item_data) for item_id, item_data in data.items()}
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        except json.JSONDecodeError:
            raise ValueError(f"Failed to decode JSON from file '{filename}'.")


# Example usage:
if __name__ == "__main__":
    # Initialize the inventory
    inventory = Inventory()

    # Add some items
    inventory.add_item(Item("SSD001", "Samsung 1TB SSD", "SSD", 50, 99.99))
    inventory.add_item(Item("PRJ001", "Epson Projector", "Projector", 20, 299.99))

    # Update an item's quantity and price
    inventory.update_item("SSD001", quantity=45, price=94.99)

    # List all items
    print("Current Inventory:")
    for item in inventory.list_items():
        print(item)

    # Save inventory to file
    inventory.save_to_file("inventory.json")

    # Load inventory from file (demonstration purpose)
    try:
        inventory.load_from_file("inventory.json")
        print("\nLoaded Inventory:")
        for item in inventory.list_items():
            print(item)
    except Exception as e:
        print(f"Error: {e}")
```
