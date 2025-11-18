"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peoner.com
Prompt: Suggest APIs or libraries for inventory management in textile manufacturing, specifically for tracking uniform production and embroidery services, as described by Peoner SAC.
Generated: DETERMINISTIC_7a5c2322e66e7080
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_management.py

"""
Inventory Management System for Textile Manufacturing
This module provides a basic structure for managing inventory,
specifically tailored for tracking uniform production and embroidery services.
"""

import json
from typing import List, Dict, Any

class InventoryItem:
    """
    Class representing an item in the inventory.
    """
    
    def __init__(self, item_id: str, description: str, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.item_id = item_id
        self.description = description
        self.quantity = quantity

    def update_quantity(self, amount: int) -> None:
        """
        Update the quantity of the inventory item.
        """
        if self.quantity + amount < 0:
            raise ValueError("Insufficient inventory to perform this operation")
        self.quantity += amount

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert item details to a dictionary.
        """
        return {
            "item_id": self.item_id,
            "description": self.description,
            "quantity": self.quantity
        }


class Inventory:
    """
    Class representing the inventory management system.
    """
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, item: InventoryItem) -> None:
        """
        Add a new item to the inventory.
        """
        if item.item_id in self.items:
            raise ValueError("Item already exists in inventory")
        self.items[item.item_id] = item

    def remove_item(self, item_id: str) -> None:
        """
        Remove an item from the inventory.
        """
        if item_id not in self.items:
            raise KeyError("Item not found in inventory")
        del self.items[item_id]

    def update_item_quantity(self, item_id: str, amount: int) -> None:
        """
        Update the quantity of a specific item.
        """
        if item_id not in self.items:
            raise KeyError("Item not found in inventory")
        self.items[item_id].update_quantity(amount)

    def get_inventory(self) -> List[Dict[str, Any]]:
        """
        Retrieve the current inventory as a list of dictionaries.
        """
        return [item.to_dict() for item in self.items.values()]

    def save_to_file(self, filename: str) -> None:
        """
        Save the inventory to a JSON file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load inventory from a JSON file.
        """
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(InventoryItem(item['item_id'], item['description'], item['quantity']))
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load inventory from file: {e}")

# Example usage
if __name__ == '__main__':
    inventory = Inventory()
    try:
        # Adding some items to the inventory
        inventory.add_item(InventoryItem("U001", "Uniform - Blue", 50))
        inventory.add_item(InventoryItem("E001", "Embroidery Service - Logo", 30))

        # Updating item quantity
        inventory.update_item_quantity("U001", -10)

        # Saving inventory to a file
        inventory.save_to_file("inventory.json")

        # Loading inventory from a file
        inventory.load_from_file("inventory.json")

        # Display current inventory
        print(inventory.get_inventory())
    except Exception as e:
        print(f"An error occurred: {e}")
```
