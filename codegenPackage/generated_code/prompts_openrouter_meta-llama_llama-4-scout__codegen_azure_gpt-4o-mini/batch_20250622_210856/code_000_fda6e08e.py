"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write a Python script to manage inventory for a cosmetic product manufacturing company like Fabricare Cosmeticos, including tracking raw materials and finished products.
Generated: DETERMINISTIC_fda6e08e7db634f7
Batch ID: 20250622_210856
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
    """A class to manage inventory for a cosmetic product manufacturing company."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {'raw_materials': {}, 'finished_products': {}}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_raw_material(self, material_name, quantity):
        """Add raw material to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory['raw_materials'].setdefault(material_name, 0)
        self.inventory['raw_materials'][material_name] += quantity
        self.save_inventory()

    def remove_raw_material(self, material_name, quantity):
        """Remove raw material from the inventory."""
        if material_name not in self.inventory['raw_materials']:
            raise KeyError(f"{material_name} not found in raw materials.")
        if self.inventory['raw_materials'][material_name] < quantity:
            raise ValueError("Insufficient quantity to remove.")
        self.inventory['raw_materials'][material_name] -= quantity
        if self.inventory['raw_materials'][material_name] == 0:
            del self.inventory['raw_materials'][material_name]
        self.save_inventory()

    def add_finished_product(self, product_name, quantity):
        """Add finished product to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory['finished_products'].setdefault(product_name, 0)
        self.inventory['finished_products'][product_name] += quantity
        self.save_inventory()

    def remove_finished_product(self, product_name, quantity):
        """Remove finished product from the inventory."""
        if product_name not in self.inventory['finished_products']:
            raise KeyError(f"{product_name} not found in finished products.")
        if self.inventory['finished_products'][product_name] < quantity:
            raise ValueError("Insufficient quantity to remove.")
        self.inventory['finished_products'][product_name] -= quantity
        if self.inventory['finished_products'][product_name] == 0:
            del self.inventory['finished_products'][product_name]
        self.save_inventory()

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

if __name__ == "__main__":
    # Example usage of the InventoryManager
    manager = InventoryManager()

    # Adding raw materials
    try:
        manager.add_raw_material('Shea Butter', 50)
        manager.add_raw_material('Coconut Oil', 30)
    except Exception as e:
        print(f"Error adding raw materials: {e}")

    # Adding finished products
    try:
        manager.add_finished_product('Moisturizing Cream', 20)
    except Exception as e:
        print(f"Error adding finished products: {e}")

    # Display current inventory
    print("Current Inventory:")
    print(json.dumps(manager.get_inventory(), indent=4))
```
