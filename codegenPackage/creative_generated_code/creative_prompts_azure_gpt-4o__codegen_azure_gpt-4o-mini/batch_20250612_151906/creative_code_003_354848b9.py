"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Create a program to track and manage inventory for products like valves, flanges, and drilling equipment, using Cedar International Inc.'s procurement strategy as a model.
Generated: DETERMINISTIC_354848b9ff61f046
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Union

class Product:
    """Class representing a product in the inventory."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount: int):
        """Update the quantity of the product. Can be positive or negative."""
        if self.quantity + amount < 0:
            raise ValueError("Cannot reduce quantity below zero.")
        self.quantity += amount

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category}, quantity={self.quantity}, price={self.price})"

class Inventory:
    """Class for managing an inventory of products."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, name: str, category: str, quantity: int, price: float):
        """Add a new product to the inventory."""
        if name in self.products:
            raise ValueError("Product already exists in the inventory.")
        self.products[name] = Product(name, category, quantity, price)

    def update_product_quantity(self, name: str, amount: int):
        """Update the quantity of an existing product."""
        if name not in self.products:
            raise KeyError("Product not found in the inventory.")
        self.products[name].update_quantity(amount)

    def get_inventory(self) -> List[Dict[str, Union[str, int, float]]]:
        """Return a list of all products in the inventory."""
        return [vars(product) for product in self.products.values()]

    def save_inventory(self, filename: str):
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str):
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products = json.load(file)
                for product in products:
                    self.add_product(product['name'], product['category'], product['quantity'], product['price'])
        except (IOError, ValueError) as e:
            print(f"Error loading inventory: {e}")

def main():
    """Main function to run the inventory management system."""
    inventory = Inventory()
    
    # Load existing inventory from a file
    inventory.load_inventory("inventory.json")

    # Add new products
    inventory.add_product("Valve", "Piping", 50, 20.0)
    inventory.add_product("Flange", "Piping", 100, 5.0)
    inventory.add_product("Drill Bit", "Drilling Equipment", 200, 15.0)

    # Update product quantities
    inventory.update_product_quantity("Valve", -10)
    inventory.update_product_quantity("Flange", 20)

    # Display current inventory
    print("Current Inventory:")
    for product in inventory.get_inventory():
        print(product)

    # Save updated inventory to the file
    inventory.save_inventory("inventory.json")

if __name__ == "__main__":
    main()
```
