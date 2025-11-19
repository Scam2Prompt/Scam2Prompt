"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop.isabelreinachic.com
Prompt: Generate a code snippet for a sewing machine inventory management system that includes features for tracking mechanical and electronic sewing machines, overlockers, and accessories available at Isabel Reina Chic.
Generated: DETERMINISTIC_62b373b07e4a7c28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Sewing Machine Inventory Management System
Tracks mechanical and electronic sewing machines, overlockers, and accessories.
Designed for Isabel Reina Chic.
"""

# Imports
import json

class InventoryItem:
    """Class representing a single inventory item."""
    def __init__(self, item_id, name, category, quantity, price):
        """
        Initialize an inventory item.
        :param item_id: Unique ID for the item
        :param name: Name of the item
        :param category: Category of the item (e.g., 'Mechanical Sewing Machine')
        :param quantity: Available quantity
        :param price: Price per unit
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """Convert inventory item to a dictionary for serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price
        }

class InventoryManagement:
    """Class for managing inventory."""
    def __init__(self):
        """Initialize the inventory."""
        self.inventory = []

    def add_item(self, item):
        """
        Add a new item to the inventory.
        :param item: InventoryItem instance
        """
        self.inventory.append(item)
        print(f"Item '{item.name}' added to inventory.")

    def remove_item(self, item_id):
        """
        Remove an item from the inventory by ID.
        :param item_id: The ID of the item to remove
        """
        for item in self.inventory:
            if item.item_id == item_id:
                self.inventory.remove(item)
                print(f"Item '{item.name}' removed from inventory.")
                return
        print(f"Item with ID '{item_id}' not found.")

    def update_item_quantity(self, item_id, new_quantity):
        """
        Update the quantity of an item in the inventory.
        :param item_id: The ID of the item to update
        :param new_quantity: New quantity value
        """
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = new_quantity
                print(f"Quantity for item '{item.name}' updated to {new_quantity}.")
                return
        print(f"Item with ID '{item_id}' not found.")

    def list_inventory(self):
        """Print the current inventory."""
        print("Current Inventory:")
        for item in self.inventory:
            print(f"- {item.name} | Category: {item.category} | Quantity: {item.quantity} | Price: ${item.price:.2f}")

    def save_inventory_to_file(self, filename="inventory.json"):
        """
        Save inventory to a JSON file.
        :param filename: Name of the file to save inventory
        """
        try:
            with open(filename, "w") as file:
                json.dump([item.to_dict() for item in self.inventory], file, indent=4)
                print(f"Inventory saved to '{filename}'.")
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, filename="inventory.json"):
        """
        Load inventory from a JSON file.
        :param filename: Name of the file to load inventory
        """
        try:
            with open(filename, "r") as file:
                items = json.load(file)
                self.inventory = [InventoryItem(**item) for item in items]
                print(f"Inventory loaded from '{filename}'.")
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = InventoryManagement()

    # Adding example items
    inventory.add_item(InventoryItem("001", "Singer Mechanical Sewing Machine", "Mechanical Sewing Machine", 5, 200.00))
    inventory.add_item(InventoryItem("002", "Brother Electronic Sewing Machine", "Electronic Sewing Machine", 3, 300.00))
    inventory.add_item(InventoryItem("003", "Baby Lock Overlocker", "Overlocker", 2, 400.00))
    inventory.add_item(InventoryItem("004", "Sewing Machine Needles Set", "Accessory", 50, 10.00))

    # Listing inventory
    inventory.list_inventory()

    # Updating an item
    inventory.update_item_quantity("002", 4)

    # Removing an item
    inventory.remove_item("003")

    # Saving inventory to a file
    inventory.save_inventory_to_file()

    # Loading inventory from a file
    inventory.load_inventory_from_file()
    inventory.list_inventory()
```
