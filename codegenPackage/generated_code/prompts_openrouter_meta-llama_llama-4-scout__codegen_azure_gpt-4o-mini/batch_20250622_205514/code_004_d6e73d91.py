"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Write a Python script to manage an inventory of hair care products, including tracking stock levels and product prices, inspired by the product offerings on Zento Cosmetic.
Generated: DETERMINISTIC_d6e73d91147d11de
Batch ID: 20250622_205514
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

class Product:
    """Class to represent a hair care product."""
    
    def __init__(self, name, price, stock):
        """
        Initialize a new product.

        :param name: Name of the product
        :param price: Price of the product
        :param stock: Stock level of the product
        """
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """
        Update the stock level of the product.

        :param quantity: Quantity to add (positive) or remove (negative)
        :raises ValueError: If stock level goes below zero
        """
        if self.stock + quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.stock += quantity

    def to_dict(self):
        """Convert the product to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

class Inventory:
    """Class to manage the inventory of hair care products."""
    
    def __init__(self, filename='inventory.json'):
        """
        Initialize the inventory.

        :param filename: The filename to load/save inventory data
        """
        self.filename = filename
        self.products = {}
        self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    product = Product(item['name'], item['price'], item['stock'])
                    self.products[item['name']] = product

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([product.to_dict() for product in self.products.values()], file, indent=4)

    def add_product(self, name, price, stock):
        """
        Add a new product to the inventory.

        :param name: Name of the product
        :param price: Price of the product
        :param stock: Initial stock level of the product
        :raises ValueError: If the product already exists
        """
        if name in self.products:
            raise ValueError("Product already exists.")
        self.products[name] = Product(name, price, stock)
        self.save_inventory()

    def update_product_stock(self, name, quantity):
        """
        Update the stock level of a product.

        :param name: Name of the product
        :param quantity: Quantity to add (positive) or remove (negative)
        :raises KeyError: If the product does not exist
        """
        if name not in self.products:
            raise KeyError("Product not found.")
        self.products[name].update_stock(quantity)
        self.save_inventory()

    def get_product_info(self, name):
        """
        Get information about a product.

        :param name: Name of the product
        :return: Product information as a dictionary
        :raises KeyError: If the product does not exist
        """
        if name not in self.products:
            raise KeyError("Product not found.")
        product = self.products[name]
        return product.to_dict()

    def list_products(self):
        """List all products in the inventory."""
        return {name: product.to_dict() for name, product in self.products.items()}

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Example usage
    try:
        inventory.add_product("Shampoo", 12.99, 100)
        inventory.add_product("Conditioner", 14.99, 50)
        inventory.update_product_stock("Shampoo", -10)
        print(inventory.get_product_info("Shampoo"))
        print(inventory.list_products())
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
