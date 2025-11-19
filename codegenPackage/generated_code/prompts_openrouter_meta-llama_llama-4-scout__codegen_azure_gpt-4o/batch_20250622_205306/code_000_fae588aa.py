"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Write a Python script to manage inventory of packaging materials for exporting blueberries and grapes, considering variables such as product type and destination country."
Generated: DETERMINISTIC_fae588aa94cd6dbc
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManager:
    """
    A class to manage inventory of packaging materials for exporting blueberries and grapes.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_material(self, product_type, destination_country, material, quantity):
        """
        Adds packaging material to the inventory.

        Args:
            product_type (str): Type of product (e.g., 'blueberries', 'grapes').
            destination_country (str): Destination country for export.
            material (str): Packaging material name.
            quantity (int): Quantity of the material to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        key = (product_type.lower(), destination_country.lower())
        if key not in self.inventory:
            self.inventory[key] = {}
        
        if material in self.inventory[key]:
            self.inventory[key][material] += quantity
        else:
            self.inventory[key][material] = quantity

    def remove_material(self, product_type, destination_country, material, quantity):
        """
        Removes packaging material from the inventory.

        Args:
            product_type (str): Type of product (e.g., 'blueberries', 'grapes').
            destination_country (str): Destination country for export.
            material (str): Packaging material name.
            quantity (int): Quantity of the material to remove.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        key = (product_type.lower(), destination_country.lower())
        if key not in self.inventory or material not in self.inventory[key]:
            raise KeyError("Material not found in inventory.")
        
        if self.inventory[key][material] < quantity:
            raise ValueError("Insufficient quantity in inventory.")
        
        self.inventory[key][material] -= quantity
        if self.inventory[key][material] == 0:
            del self.inventory[key][material]
        if not self.inventory[key]:
            del self.inventory[key]

    def get_inventory(self):
        """
        Returns the current inventory.

        Returns:
            dict: The inventory data.
        """
        return self.inventory

    def save_inventory(self, file_path):
        """
        Saves the inventory to a JSON file.

        Args:
            file_path (str): Path to the file where inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads the inventory from a JSON file.

        Args:
            file_path (str): Path to the file from which inventory will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Adding materials
    manager.add_material("blueberries", "USA", "plastic box", 100)
    manager.add_material("grapes", "Canada", "cardboard box", 50)

    # Removing materials
    try:
        manager.remove_material("blueberries", "USA", "plastic box", 20)
    except Exception as e:
        print(f"Error: {e}")

    # Displaying inventory
    print("Current Inventory:")
    print(manager.get_inventory())

    # Saving inventory to file
    try:
        manager.save_inventory("inventory.json")
        print("Inventory saved to 'inventory.json'.")
    except Exception as e:
        print(f"Error: {e}")

    # Loading inventory from file
    try:
        manager.load_inventory("inventory.json")
        print("Inventory loaded from 'inventory.json'.")
        print(manager.get_inventory())
    except Exception as e:
        print(f"Error: {e}")
```
