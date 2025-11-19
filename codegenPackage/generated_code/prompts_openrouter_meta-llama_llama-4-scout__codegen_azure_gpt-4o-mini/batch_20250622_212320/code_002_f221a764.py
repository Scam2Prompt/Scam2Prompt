"""
Generated Code Metadata:
========================
Original URL: https://tudulcepecado.cl
Prompt: Write a Python script to manage an e-commerce inventory system for a sex toy store like Tu Dulce Pecado, including product categorization and pricing.
Generated: DETERMINISTIC_f221a764ac983357
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, name: str, category: str, price: float, stock: int):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'stock': self.stock
        }

class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a new product to the inventory."""
        self.products.append(product)

    def remove_product(self, product_name: str) -> None:
        """Remove a product from the inventory by name."""
        self.products = [p for p in self.products if p.name != product_name]

    def update_stock(self, product_name: str, quantity: int) -> None:
        """Update the stock of a product."""
        for product in self.products:
            if product.name == product_name:
                product.stock += quantity
                return
        raise ValueError(f"Product '{product_name}' not found in inventory.")

    def get_product(self, product_name: str) -> Product:
        """Retrieve a product by name."""
        for product in self.products:
            if product.name == product_name:
                return product
        raise ValueError(f"Product '{product_name}' not found in inventory.")

    def list_products(self) -> List[Dict[str, Any]]:
        """List all products in the inventory."""
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_products(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [Product(**data) for data in products_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to demonstrate the inventory management system."""
    inventory = Inventory()

    # Example products
    inventory.add_product(Product("Vibrating Toy", "Vibrators", 29.99, 100))
    inventory.add_product(Product("Silicone Dildo", "Dildos", 19.99, 50))
    inventory.add_product(Product("Lube", "Accessories", 9.99, 200))

    # List all products
    print("Current Inventory:")
    for product in inventory.list_products():
        print(product)

    # Update stock
    try:
        inventory.update_stock("Vibrating Toy", 20)
    except ValueError as e:
        print(e)

    # Save inventory to file
    inventory.save_to_file("inventory.json")

    # Load inventory from file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print("\nLoaded Inventory from File:")
    for product in new_inventory.list_products():
        print(product)

if __name__ == "__main__":
    main()
```
