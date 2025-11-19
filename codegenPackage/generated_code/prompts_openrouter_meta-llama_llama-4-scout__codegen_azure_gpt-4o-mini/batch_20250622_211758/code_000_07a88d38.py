"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Write a Python code to manage inventory of eucalyptus and pine wood products for a company like Trattar Madeiras that uses vacuum/pressure treatment with hydro-soluble CCA agents."
Generated: DETERMINISTIC_07a88d38691ec107
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class WoodProduct:
    """Class representing a wood product in the inventory."""
    
    def __init__(self, name: str, species: str, quantity: int, treatment: str):
        self.name = name
        self.species = species
        self.quantity = quantity
        self.treatment = treatment

    def __repr__(self):
        return f"{self.name} ({self.species}): {self.quantity} units, Treatment: {self.treatment}"

class Inventory:
    """Class to manage the inventory of wood products."""
    
    def __init__(self):
        self.products: Dict[str, WoodProduct] = {}

    def add_product(self, product: WoodProduct) -> None:
        """Add a new product to the inventory."""
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists in the inventory.")
        self.products[product.name] = product

    def update_quantity(self, product_name: str, quantity: int) -> None:
        """Update the quantity of an existing product."""
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in the inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_name].quantity = quantity

    def remove_product(self, product_name: str) -> None:
        """Remove a product from the inventory."""
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in the inventory.")
        del self.products[product_name]

    def get_product(self, product_name: str) -> Optional[WoodProduct]:
        """Retrieve a product from the inventory."""
        return self.products.get(product_name)

    def list_products(self) -> List[WoodProduct]:
        """List all products in the inventory."""
        return list(self.products.values())

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.products, file, default=lambda p: p.__dict__, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = {name: WoodProduct(**data) for name, data in products_data.items()}
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products
    try:
        inventory.add_product(WoodProduct("Eucalyptus Plank", "Eucalyptus", 100, "CCA Treatment"))
        inventory.add_product(WoodProduct("Pine Beam", "Pine", 50, "CCA Treatment"))
    except ValueError as e:
        print(e)

    # Listing products
    print("Current Inventory:")
    for product in inventory.list_products():
        print(product)

    # Updating quantity
    try:
        inventory.update_quantity("Eucalyptus Plank", 120)
    except (KeyError, ValueError) as e:
        print(e)

    # Saving inventory to file
    inventory.save_to_file("inventory.json")

    # Loading inventory from file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print("Loaded Inventory:")
    for product in new_inventory.list_products():
        print(product)
```
