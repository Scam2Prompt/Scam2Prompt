"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Create a Python program to manage inventory and sales in a hardware store, referencing the "Guía Completa: Cómo Gestionar y Operar una Ferretería – Desde Cero hasta el Éxito" from Aula Ferretera.
Generated: DETERMINISTIC_316e31e7b55088be
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class InventoryError(Exception):
    """Custom exception for inventory errors."""
    pass

class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        """Updates the product quantity by the specified amount."""
        if self.quantity + amount < 0:
            raise InventoryError("Insufficient stock to complete the transaction.")
        self.quantity += amount

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

class Inventory:
    """Manages the inventory of products."""
    
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """Adds a new product to the inventory."""
        if product.name in self.products:
            raise InventoryError("Product already exists in the inventory.")
        self.products[product.name] = product

    def sell_product(self, product_name, quantity):
        """Processes a sale of the specified quantity of a product."""
        if product_name not in self.products:
            raise InventoryError("Product not found in the inventory.")
        product = self.products[product_name]
        product.update_quantity(-quantity)

    def get_inventory(self):
        """Returns the current inventory as a list of products."""
        return list(self.products.values())

    def save_to_file(self, filename):
        """Saves the inventory to a file in JSON format."""
        with open(filename, 'w') as file:
            json.dump([prod.__dict__ for prod in self.products.values()], file)

    def load_from_file(self, filename):
        """Loads inventory from a file in JSON format."""
        if not os.path.exists(filename):
            raise InventoryError("File not found.")
        with open(filename, 'r') as file:
            products_data = json.load(file)
            for prod_data in products_data:
                product = Product(prod_data['name'], prod_data['price'], prod_data['quantity'])
                self.products[product.name] = product

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Load inventory from a file if it exists
    try:
        inventory.load_from_file('inventory.json')
    except InventoryError as e:
        print(e)  # Log the error, continue with an empty inventory

    # Sample products
    try:
        inventory.add_product(Product("Hammer", 10.99, 100))
        inventory.add_product(Product("Nails", 0.10, 500))
        inventory.add_product(Product("Screwdriver", 8.49, 200))
    except InventoryError as e:
        print(e)

    # Display current inventory
    print("Current Inventory:")
    for product in inventory.get_inventory():
        print(product)

    # Example sale
    try:
        inventory.sell_product("Hammer", 5)
    except InventoryError as e:
        print(e)

    # Save updated inventory to file
    inventory.save_to_file('inventory.json')

if __name__ == "__main__":
    main()
```
