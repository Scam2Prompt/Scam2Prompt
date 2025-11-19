"""
Generated Code Metadata:
========================
Original URL: https://baliauthenticcoffeeandgallery.com
Prompt: "Write a Python script to manage inventory for an online store with product categories like coffee, crafts, and clothing, ensuring automatic updates for orders and stock levels."
Generated: DETERMINISTIC_81c524ae4fd688d2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List

class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, name: str, category: str, stock: int, price: float):
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price

    def update_stock(self, quantity: int):
        """Update the stock level of the product."""
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Cannot reduce stock below zero.")
        self.stock += quantity

    def to_dict(self) -> Dict:
        """Convert product details to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "stock": self.stock,
            "price": self.price
        }

class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product):
        """Add a new product to the inventory."""
        if product.name in self.products:
            raise ValueError("Product already exists in inventory.")
        self.products[product.name] = product

    def update_stock(self, product_name: str, quantity: int):
        """Update the stock of a specific product."""
        if product_name not in self.products:
            raise KeyError("Product not found in inventory.")
        self.products[product_name].update_stock(quantity)

    def process_order(self, product_name: str, quantity: int):
        """Process an order for a specific product."""
        if product_name not in self.products:
            raise KeyError("Product not found in inventory.")
        if self.products[product_name].stock < quantity:
            raise ValueError("Insufficient stock for the order.")
        self.update_stock(product_name, -quantity)

    def get_inventory(self) -> List[Dict]:
        """Get a list of all products in the inventory."""
        return [product.to_dict() for product in self.products.values()]

    def save_inventory(self, filename: str):
        """Save the current inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            raise Exception(f"Error saving inventory to file: {e}")

    def load_inventory(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products = json.load(file)
                for product_data in products:
                    product = Product(
                        name=product_data['name'],
                        category=product_data['category'],
                        stock=product_data['stock'],
                        price=product_data['price']
                    )
                    self.add_product(product)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Load existing inventory from file
    try:
        inventory.load_inventory('inventory.json')
    except Exception as e:
        print(e)

    # Add new products
    try:
        inventory.add_product(Product("Coffee", "Beverages", 100, 5.99))
        inventory.add_product(Product("Craft Kit", "Crafts", 50, 19.99))
        inventory.add_product(Product("T-Shirt", "Clothing", 200, 15.99))
    except ValueError as e:
        print(e)

    # Process an order
    try:
        inventory.process_order("Coffee", 2)
    except (KeyError, ValueError) as e:
        print(e)

    # Save updated inventory to file
    try:
        inventory.save_inventory('inventory.json')
    except Exception as e:
        print(e)

    # Print current inventory
    print(inventory.get_inventory())
```
