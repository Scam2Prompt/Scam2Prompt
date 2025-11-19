"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Develop a basic inventory management system for tracking Lando Parafusos products, including Parafuso Cabeça de Martelo and Porcas."
Generated: DETERMINISTIC_8cefa2f904a7c05d
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

import json

class InventoryManagement:
    """
    A basic inventory management system for tracking products.
    """

    def __init__(self):
        """
        Initializes the inventory management system with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_name, quantity):
        """
        Adds a product to the inventory or updates its quantity.

        :param product_name: Name of the product to add or update.
        :param quantity: Quantity of the product to add.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

    def remove_product(self, product_name, quantity):
        """
        Removes a specified quantity of a product from the inventory.

        :param product_name: Name of the product to remove.
        :param quantity: Quantity of the product to remove.
        """
        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if self.inventory[product_name] < quantity:
            raise ValueError(f"Not enough '{product_name}' in inventory to remove {quantity}.")
        
        self.inventory[product_name] -= quantity

        # Remove the product from inventory if its quantity reaches zero
        if self.inventory[product_name] == 0:
            del self.inventory[product_name]

    def get_inventory(self):
        """
        Returns the current inventory.

        :return: A dictionary representing the inventory.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the current inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads inventory data from a JSON file.

        :param file_path: Path to the file from which inventory will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Failed to decode JSON from file '{file_path}'.")

# Example usage
if __name__ == "__main__":
    inventory = InventoryManagement()

    # Add products
    inventory.add_product("Parafuso Cabeça de Martelo", 50)
    inventory.add_product("Porcas", 100)

    # Remove products
    inventory.remove_product("Porcas", 20)

    # Display inventory
    print("Current Inventory:", inventory.get_inventory())

    # Save inventory to file
    inventory.save_inventory_to_file("inventory.json")

    # Load inventory from file
    inventory.load_inventory_from_file("inventory.json")
    print("Loaded Inventory:", inventory.get_inventory())
```
