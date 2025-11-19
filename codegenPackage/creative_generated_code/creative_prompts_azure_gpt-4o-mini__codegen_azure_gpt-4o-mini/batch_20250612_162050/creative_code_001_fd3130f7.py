"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://southernbrass.com
Prompt: Write a Python script that manages inventory for door knobs and levers, focusing on finishes like satin nickel and bronze.
Generated: DETERMINISTIC_fd3130f7306b6e8a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class InventoryManager:
    """
    A class to manage inventory for door knobs and levers with specific finishes.
    """
    
    def __init__(self, inventory_file='inventory.json'):
        """
        Initializes the InventoryManager with a specified inventory file.
        
        Args:
            inventory_file (str): The path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Loads the inventory from a JSON file. If the file does not exist, initializes an empty inventory.
        
        Returns:
            dict: The loaded inventory data.
        """
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """
        Saves the current inventory to the JSON file.
        """
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, item_name, finish, quantity):
        """
        Adds a new item to the inventory or updates the quantity if it already exists.
        
        Args:
            item_name (str): The name of the item (e.g., "Door Knob").
            finish (str): The finish of the item (e.g., "satin nickel", "bronze").
            quantity (int): The quantity of the item to add.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        key = f"{item_name}_{finish}"
        if key in self.inventory:
            self.inventory[key] += quantity
        else:
            self.inventory[key] = quantity
        
        self.save_inventory()

    def remove_item(self, item_name, finish, quantity):
        """
        Removes a quantity of an item from the inventory.
        
        Args:
            item_name (str): The name of the item to remove.
            finish (str): The finish of the item to remove.
            quantity (int): The quantity of the item to remove.
        
        Raises:
            ValueError: If the quantity is negative or exceeds the available stock.
        """
        key = f"{item_name}_{finish}"
        if key not in self.inventory:
            raise KeyError(f"{key} not found in inventory.")
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if self.inventory[key] < quantity:
            raise ValueError("Cannot remove more than available stock.")

        self.inventory[key] -= quantity
        if self.inventory[key] == 0:
            del self.inventory[key]

        self.save_inventory()

    def get_inventory(self):
        """
        Returns the current inventory.
        
        Returns:
            dict: The current inventory data.
        """
        return self.inventory


def main():
    """
    Main function to demonstrate the InventoryManager functionality.
    """
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_item("Door Knob", "satin nickel", 10)
        manager.add_item("Lever", "bronze", 5)
        print("Inventory after additions:", manager.get_inventory())

        manager.remove_item("Door Knob", "satin nickel", 3)
        print("Inventory after removal:", manager.get_inventory())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
