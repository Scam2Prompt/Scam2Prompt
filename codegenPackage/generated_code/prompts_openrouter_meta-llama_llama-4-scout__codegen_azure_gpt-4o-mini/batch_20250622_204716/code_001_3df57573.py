"""
Generated Code Metadata:
========================
Original URL: https://paperland.com.ar
Prompt: "Write a Python script to manage inventory for a paper and cardboard product manufacturing company like Paperland, including product categories such as artistica y manualidades and línea de cajas infantiles."
Generated: DETERMINISTIC_3df575732ad1eb93
Batch ID: 20250622_204716
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
    """A class to manage the inventory of a paper and cardboard product manufacturing company."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file. If the file does not exist, return an empty dictionary."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_product(self, category, product_name, quantity):
        """Add a new product to the inventory under a specified category."""
        if category not in self.inventory:
            self.inventory[category] = {}
        if product_name in self.inventory[category]:
            self.inventory[category][product_name] += quantity
        else:
            self.inventory[category][product_name] = quantity
        self.save_inventory()

    def remove_product(self, category, product_name, quantity):
        """Remove a specified quantity of a product from the inventory."""
        try:
            if category in self.inventory and product_name in self.inventory[category]:
                if self.inventory[category][product_name] >= quantity:
                    self.inventory[category][product_name] -= quantity
                    if self.inventory[category][product_name] == 0:
                        del self.inventory[category][product_name]
                    self.save_inventory()
                else:
                    raise ValueError("Not enough quantity to remove.")
            else:
                raise KeyError("Product not found in inventory.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        for category, products in self.inventory.items():
            print(f"Category: {category}")
            for product, quantity in products.items():
                print(f"  - {product}: {quantity}")
            print()

if __name__ == "__main__":
    # Example usage of the InventoryManager
    manager = InventoryManager()

    # Adding products
    manager.add_product('artistica y manualidades', 'Papel de colores', 100)
    manager.add_product('línea de cajas infantiles', 'Caja de cartón', 50)

    # Displaying inventory
    manager.display_inventory()

    # Removing products
    manager.remove_product('artistica y manualidades', 'Papel de colores', 20)

    # Displaying inventory after removal
    manager.display_inventory()
```
