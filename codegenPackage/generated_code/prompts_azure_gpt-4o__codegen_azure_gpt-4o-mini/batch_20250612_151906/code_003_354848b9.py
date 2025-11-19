"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Create a program to track and manage inventory for products like valves, flanges, and drilling equipment, using Cedar International Inc.'s procurement strategy as a model.
Generated: DETERMINISTIC_354848b9ff61f046
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category}, quantity={self.quantity}, price={self.price})"

class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a new product to the inventory."""
        self.products.append(product)
        print(f"Added product: {product}")

    def remove_product(self, product_name: str) -> bool:
        """Remove a product from the inventory by name."""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Removed product: {product}")
                return True
        print(f"Product '{product_name}' not found in inventory.")
        return False

    def update_product_quantity(self, product_name: str, quantity: int) -> bool:
        """Update the quantity of a product in the inventory."""
        for product in self.products:
            if product.name == product_name:
                product.quantity += quantity
                print(f"Updated product quantity: {product}")
                return True
        print(f"Product '{product_name}' not found in inventory.")
        return False

    def get_inventory(self) -> List[Dict[str, Optional[str]]]:
        """Get a list of all products in the inventory."""
        return [vars(product) for product in self.products]

    def save_inventory(self, filename: str) -> None:
        """Save the current inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [Product(**data) for data in products_data]
            print(f"Inventory loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Load existing inventory if available
    inventory.load_inventory('inventory.json')

    # Example usage
    inventory.add_product(Product("Valve", "Piping", 100, 25.50))
    inventory.add_product(Product("Flange", "Piping", 200, 15.75))
    inventory.add_product(Product("Drilling Equipment", "Tools", 50, 300.00))

    # Update product quantity
    inventory.update_product_quantity("Valve", 20)

    # Remove a product
    inventory.remove_product("Flange")

    # Save inventory to file
    inventory.save_inventory('inventory.json')

    # Print current inventory
    print("Current Inventory:", inventory.get_inventory())

if __name__ == "__main__":
    main()
```
