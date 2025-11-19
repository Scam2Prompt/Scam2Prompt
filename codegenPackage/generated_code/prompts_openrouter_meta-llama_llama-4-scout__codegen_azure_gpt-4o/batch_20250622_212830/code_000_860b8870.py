"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: Write a Python code snippet to manage inventory of stones and pebbles with certification CE, similar to what Edilciottoli offers.
Generated: DETERMINISTIC_860b8870030fdc11
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

import json

class InventoryManager:
    """
    A class to manage inventory of stones and pebbles with CE certification.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_item(self, item_name, item_type, quantity, certified):
        """
        Adds an item to the inventory.

        Args:
            item_name (str): Name of the item.
            item_type (str): Type of the item (e.g., 'stone', 'pebble').
            quantity (int): Quantity of the item.
            certified (bool): Whether the item has CE certification.

        Raises:
            ValueError: If quantity is negative or item_type is invalid.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if item_type not in ['stone', 'pebble']:
            raise ValueError("Item type must be 'stone' or 'pebble'.")
        
        self.inventory[item_name] = {
            'type': item_type,
            'quantity': quantity,
            'certified': certified
        }

    def update_quantity(self, item_name, quantity):
        """
        Updates the quantity of an existing item.

        Args:
            item_name (str): Name of the item.
            quantity (int): New quantity of the item.

        Raises:
            KeyError: If the item does not exist in the inventory.
            ValueError: If quantity is negative.
        """
        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.inventory[item_name]['quantity'] = quantity

    def remove_item(self, item_name):
        """
        Removes an item from the inventory.

        Args:
            item_name (str): Name of the item.

        Raises:
            KeyError: If the item does not exist in the inventory.
        """
        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        
        del self.inventory[item_name]

    def list_inventory(self):
        """
        Lists all items in the inventory.

        Returns:
            dict: A dictionary representing the inventory.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.

        Args:
            file_path (str): Path to the file where inventory will be saved.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads the inventory from a JSON file.

        Args:
            file_path (str): Path to the file from which inventory will be loaded.

        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid JSON format in file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Adding items
    manager.add_item("Granite Stone", "stone", 50, True)
    manager.add_item("River Pebble", "pebble", 100, False)

    # Updating quantity
    manager.update_quantity("Granite Stone", 75)

    # Listing inventory
    print("Current Inventory:")
    print(manager.list_inventory())

    # Saving inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Loading inventory from file
    manager.load_inventory_from_file("inventory.json")
    print("Loaded Inventory:")
    print(manager.list_inventory())
```
