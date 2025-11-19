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

class InventoryManager:
    """
    A class to manage inventory for door knobs and levers, focusing 
    on finishes like satin nickel and bronze.
    """
    
    def __init__(self):
        # Initializes an empty inventory
        self.inventory = {}

    def add_item(self, item_type, finish, quantity):
        """
        Adds an item to the inventory.
        
        Args:
            item_type (str): The type of the item ('knob' or 'lever').
            finish (str): The finish of the item ('satin nickel' or 'bronze').
            quantity (int): The quantity of the item to add.
        """
        # Validate inputs
        if item_type not in ['knob', 'lever']:
            raise ValueError("Invalid item_type. Must be 'knob' or 'lever'.")
        if finish not in ['satin nickel', 'bronze']:
            raise ValueError("Invalid finish. Must be 'satin nickel' or 'bronze'.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Update inventory
        key = (item_type, finish)
        if key in self.inventory:
            self.inventory[key] += quantity
        else:
            self.inventory[key] = quantity

    def remove_item(self, item_type, finish, quantity):
        """
        Removes an item from the inventory.
        
        Args:
            item_type (str): The type of the item ('knob' or 'lever').
            finish (str): The finish of the item ('satin nickel' or 'bronze').
            quantity (int): The quantity of the item to remove.
        """
        # Validate inputs
        if item_type not in ['knob', 'lever']:
            raise ValueError("Invalid item_type. Must be 'knob' or 'lever'.")
        if finish not in ['satin nickel', 'bronze']:
            raise ValueError("Invalid finish. Must be 'satin nickel' or 'bronze'.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Update inventory
        key = (item_type, finish)
        if key not in self.inventory or self.inventory[key] < quantity:
            raise ValueError("Insufficient inventory to remove the requested quantity.")
        self.inventory[key] -= quantity

        # Remove the key if quantity becomes zero
        if self.inventory[key] == 0:
            self.inventory.pop(key)

    def get_inventory(self):
        """
        Returns a copy of the current inventory.
        
        Returns:
            dict: The current inventory.
        """
        return dict(self.inventory)

    def save_inventory(self, file_path):
        """
        Saves the inventory to a JSON file.
        
        Args:
            file_path (str): The path to the file where the inventory should be saved.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.inventory, f)
        except IOError as e:
            raise IOError(f"Failed to save inventory: {e}")

    def load_inventory(self, file_path):
        """
        Loads the inventory from a JSON file.
        
        Args:
            file_path (str): The path to the file from which the inventory should be loaded.
        """
        try:
            with open(file_path, 'r') as f:
                self.inventory = {tuple(key): value for key, value in json.load(f).items()}
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    try:
        # Adding items
        manager.add_item("knob", "satin nickel", 10)
        manager.add_item("lever", "bronze", 5)

        # Removing items
        manager.remove_item("knob", "satin nickel", 3)

        # Displaying inventory
        print("Current Inventory:", manager.get_inventory())

        # Saving inventory to a file
        manager.save_inventory("inventory.json")

        # Loading inventory from a file
        manager.load_inventory("inventory.json")
        print("Loaded Inventory:", manager.get_inventory())
    except Exception as e:
        print(f"An error occurred: {e}")
```
