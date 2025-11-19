"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write a Python script to manage inventory for a factory producing customized flip-flops and shoe soles, including tracking product types like Sueco Tiburón Infantil and Ojota Hombre Estampada Rider.
Generated: DETERMINISTIC_c2843d633dff6b73
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class InventoryManager:
    """
    A class to manage inventory for a factory producing customized flip-flops and shoe soles.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the inventory manager with a file to store inventory data.
        :param inventory_file: Path to the inventory file (default: inventory.json)
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self._load_inventory()

    def _load_inventory(self):
        """
        Load inventory data from the file. If the file doesn't exist, initialize an empty inventory.
        """
        if os.path.exists(self.inventory_file):
            try:
                with open(self.inventory_file, 'r') as file:
                    self.inventory = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading inventory file. Initializing empty inventory.")
                self.inventory = {}
        else:
            self.inventory = {}

    def _save_inventory(self):
        """
        Save the current inventory data to the file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory file: {e}")

    def add_product(self, product_name, quantity):
        """
        Add a product to the inventory or update its quantity.
        :param product_name: Name of the product
        :param quantity: Quantity to add (must be positive)
        """
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

        self._save_inventory()
        print(f"Added {quantity} units of '{product_name}' to inventory.")

    def remove_product(self, product_name, quantity):
        """
        Remove a product from the inventory or decrease its quantity.
        :param product_name: Name of the product
        :param quantity: Quantity to remove (must be positive)
        """
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        if product_name in self.inventory:
            if self.inventory[product_name] >= quantity:
                self.inventory[product_name] -= quantity
                if self.inventory[product_name] == 0:
                    del self.inventory[product_name]
                self._save_inventory()
                print(f"Removed {quantity} units of '{product_name}' from inventory.")
            else:
                print(f"Not enough '{product_name}' in inventory to remove {quantity} units.")
        else:
            print(f"Product '{product_name}' not found in inventory.")

    def view_inventory(self):
        """
        Display the current inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product, quantity in self.inventory.items():
                print(f" - {product}: {quantity} units")

    def search_product(self, product_name):
        """
        Search for a product in the inventory.
        :param product_name: Name of the product to search for
        """
        if product_name in self.inventory:
            print(f"'{product_name}' is in inventory with {self.inventory[product_name]} units.")
        else:
            print(f"'{product_name}' is not in inventory.")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("Sueco Tiburón Infantil", 50)
    manager.add_product("Ojota Hombre Estampada Rider", 30)

    # View inventory
    manager.view_inventory()

    # Remove products
    manager.remove_product("Sueco Tiburón Infantil", 10)

    # Search for a product
    manager.search_product("Ojota Hombre Estampada Rider")

    # View inventory again
    manager.view_inventory()
```
