"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Generate a Python code snippet to manage an inventory of visual communication materials, including chapas de ACM, lonas unibanner, and vinil auto adesivo.
Generated: DETERMINISTIC_842b207f75e72f69
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class InventoryManager:
    """A class to manage an inventory of visual communication materials."""

    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with a specified inventory file.

        Args:
            inventory_file (str): The path to the JSON file that stores the inventory.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, int]:
        """Loads the inventory from a JSON file.

        Returns:
            Dict[str, int]: A dictionary representing the inventory items and their quantities.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file does not exist, initialize an empty inventory
            return {}
        except json.JSONDecodeError:
            # Handle JSON decoding errors
            print("Error: The inventory file is not a valid JSON.")
            return {}

    def save_inventory(self) -> None:
        """Saves the current inventory to the JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, item: str, quantity: int) -> None:
        """Adds a specified quantity of an item to the inventory.

        Args:
            item (str): The name of the item to add.
            quantity (int): The quantity of the item to add.
        """
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return

        self.inventory[item] = self.inventory.get(item, 0) + quantity
        self.save_inventory()

    def remove_item(self, item: str, quantity: int) -> None:
        """Removes a specified quantity of an item from the inventory.

        Args:
            item (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove.
        """
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return

        if item in self.inventory:
            if self.inventory[item] < quantity:
                print(f"Error: Not enough {item} in inventory to remove.")
                return
            self.inventory[item] -= quantity
            if self.inventory[item] == 0:
                del self.inventory[item]  # Remove item if quantity is zero
            self.save_inventory()
        else:
            print(f"Error: {item} not found in inventory.")

    def get_inventory(self) -> Dict[str, int]:
        """Returns the current inventory.

        Returns:
            Dict[str, int]: The current inventory items and their quantities.
        """
        return self.inventory

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager("inventory.json")
    inventory_manager.add_item("chapas de ACM", 10)
    inventory_manager.add_item("lonas unibanner", 5)
    inventory_manager.add_item("vinil auto adesivo", 20)
    print(inventory_manager.get_inventory())
    inventory_manager.remove_item("chapas de ACM", 3)
    print(inventory_manager.get_inventory())
```
