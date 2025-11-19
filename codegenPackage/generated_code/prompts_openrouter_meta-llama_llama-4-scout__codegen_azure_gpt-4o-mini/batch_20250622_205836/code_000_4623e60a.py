"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Write a Python code snippet to manage a logistics company's warehouse, including storage and inventory tracking, inspired by Bin Qutab Logistics L.L.C's warehousing services.
Generated: DETERMINISTIC_4623e60ab56a74cc
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Warehouse:
    def __init__(self):
        """Initialize the warehouse with an empty inventory."""
        self.inventory: Dict[str, int] = {}

    def add_item(self, item_name: str, quantity: int) -> None:
        """Add a specified quantity of an item to the inventory.

        Args:
            item_name (str): The name of the item to add.
            quantity (int): The quantity of the item to add.

        Raises:
            ValueError: If the quantity is less than or equal to zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name: str, quantity: int) -> None:
        """Remove a specified quantity of an item from the inventory.

        Args:
            item_name (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove.

        Raises:
            ValueError: If the quantity is less than or equal to zero or if the item does not exist or insufficient quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if item_name not in self.inventory:
            raise ValueError(f"Item '{item_name}' does not exist in inventory.")
        
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Insufficient quantity of '{item_name}' in inventory.")
        
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]

    def get_inventory(self) -> Dict[str, int]:
        """Get the current inventory.

        Returns:
            Dict[str, int]: A dictionary representing the current inventory.
        """
        return self.inventory

    def save_inventory(self, file_path: str) -> None:
        """Save the current inventory to a JSON file.

        Args:
            file_path (str): The path to the file where the inventory will be saved.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file)
        except IOError as e:
            raise IOError(f"Error saving inventory to {file_path}: {e}")

    def load_inventory(self, file_path: str) -> None:
        """Load inventory from a JSON file.

        Args:
            file_path (str): The path to the file from which the inventory will be loaded.

        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from {file_path}: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON from {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    warehouse = Warehouse()
    warehouse.add_item("Widget", 10)
    warehouse.add_item("Gadget", 5)
    print("Current Inventory:", warehouse.get_inventory())
    
    warehouse.remove_item("Widget", 3)
    print("Updated Inventory:", warehouse.get_inventory())
    
    warehouse.save_inventory("inventory.json")
    warehouse.load_inventory("inventory.json")
    print("Loaded Inventory:", warehouse.get_inventory())
```
