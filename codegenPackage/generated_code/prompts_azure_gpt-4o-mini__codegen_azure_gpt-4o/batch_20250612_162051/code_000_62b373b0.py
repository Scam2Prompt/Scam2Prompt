"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Generate a code snippet for a sewing machine inventory management system that includes features for tracking mechanical and electronic sewing machines, overlockers, and accessories available at Isabel Reina Chic.
Generated: DETERMINISTIC_62b373b07e4a7c28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sewing_machine_inventory.py

import json

class InventoryItem:
    """
    Base class for inventory items.
    """
    def __init__(self, item_id, name, category, quantity, price):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """
        Convert the inventory item to a dictionary for serialization.
        """
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price
        }

    def __str__(self):
        """
        String representation of the inventory item.
        """
        return f"{self.name} ({self.category}) - Quantity: {self.quantity}, Price: ${self.price:.2f}"


class SewingMachineInventory:
    """
    Inventory management system for sewing machines and accessories.
    """
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        """
        Add a new item to the inventory.
        """
        if item.item_id in self.inventory:
            raise ValueError(f"Item with ID {item.item_id} already exists.")
        self.inventory[item.item_id] = item

    def update_item(self, item_id, quantity=None, price=None):
        """
        Update the quantity and/or price of an existing item.
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} does not exist.")
        if quantity is not None:
            self.inventory[item_id].quantity = quantity
        if price is not None:
            self.inventory[item_id].price = price

    def remove_item(self, item_id):
        """
        Remove an item from the inventory.
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} does not exist.")
        del self.inventory[item_id]

    def list_items(self):
        """
        List all items in the inventory.
        """
        return [str(item) for item in self.inventory.values()]

    def save_to_file(self, filename):
        """
        Save the inventory to a JSON file.
        """
        with open(filename, 'w') as file:
            json.dump({item_id: item.to_dict() for item_id, item in self.inventory.items()}, file, indent=4)

    def load_from_file(self, filename):
        """
        Load the inventory from a JSON file.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.inventory = {item_id: InventoryItem(**item_data) for item_id, item_data in data.items()}
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {filename} contains invalid JSON.")

# Example usage
if __name__ == "__main__":
    inventory = SewingMachineInventory()

    # Add items to the inventory
    inventory.add_item(InventoryItem("001", "Mechanical Sewing Machine", "Mechanical", 10, 199.99))
    inventory.add_item(InventoryItem("002", "Electronic Sewing Machine", "Electronic", 5, 299.99))
    inventory.add_item(InventoryItem("003", "Overlocker", "Overlocker", 7, 249.99))
    inventory.add_item(InventoryItem("004", "Sewing Accessories Kit", "Accessories", 20, 49.99))

    # Update an item
    inventory.update_item("001", quantity=8)

    # List all items
    print("Current Inventory:")
    for item in inventory.list_items():
        print(item)

    # Save inventory to file
    inventory.save_to_file("inventory.json")

    # Load inventory from file
    new_inventory = SewingMachineInventory()
    new_inventory.load_from_file("inventory.json")
    print("\nLoaded Inventory:")
    for item in new_inventory.list_items():
        print(item)
```
