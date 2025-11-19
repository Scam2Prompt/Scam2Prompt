"""
Generated Code Metadata:
========================
Original URL: https://marant.com.mx
Prompt: "Write a Python script to manage a skincare product inventory for a professional spa, including product names, descriptions, and quantities."
Generated: DETERMINISTIC_57b66b61efdf0542
Batch ID: 20250622_204920
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

class SkincareProduct:
    """Class to represent a skincare product."""
    
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    def to_dict(self):
        """Convert the product to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity
        }

class InventoryManager:
    """Class to manage the skincare product inventory."""
    
    def __init__(self, inventory_file='inventory.json'):
        self.inventory_file = inventory_file
        self.products = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                try:
                    products_data = json.load(file)
                    return [SkincareProduct(**data) for data in products_data]
                except json.JSONDecodeError as e:
                    print(f"Error loading inventory: {e}")
                    return []
        return []

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump([product.to_dict() for product in self.products], file, indent=4)

    def add_product(self, name, description, quantity):
        """Add a new product to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        new_product = SkincareProduct(name, description, quantity)
        self.products.append(new_product)
        self.save_inventory()

    def update_product(self, name, quantity):
        """Update the quantity of an existing product."""
        for product in self.products:
            if product.name == name:
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                product.quantity = quantity
                self.save_inventory()
                return
        raise ValueError("Product not found.")

    def remove_product(self, name):
        """Remove a product from the inventory."""
        self.products = [product for product in self.products if product.name != name]
        self.save_inventory()

    def list_products(self):
        """List all products in the inventory."""
        return [product.to_dict() for product in self.products]

def main():
    """Main function to demonstrate inventory management."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_product("Hydrating Serum", "A serum that hydrates the skin.", 10)
        manager.add_product("Exfoliating Scrub", "A scrub that removes dead skin cells.", 5)
        print("Current Inventory:")
        print(manager.list_products())

        manager.update_product("Hydrating Serum", 8)
        print("Updated Inventory:")
        print(manager.list_products())

        manager.remove_product("Exfoliating Scrub")
        print("Final Inventory:")
        print(manager.list_products())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
