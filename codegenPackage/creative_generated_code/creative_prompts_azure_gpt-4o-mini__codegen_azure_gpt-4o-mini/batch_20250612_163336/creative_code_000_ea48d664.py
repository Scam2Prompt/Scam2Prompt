"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startec.com.my
Prompt: Generate a code snippet for a simple inventory management system that could help a computer hardware retailer like StarTec Computer System Sdn Bhd manage their products effectively.
Generated: DETERMINISTIC_ea48d6649a5d8b55
Batch ID: 20250612_163336
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

class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id      # Unique identifier for the product
        self.name = name                  # Name of the product
        self.quantity = quantity          # Quantity in stock
        self.price = price                # Price of the product

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.product_id}: {self.name}, Quantity: {self.quantity}, Price: {self.price}"

class Inventory:
    """Manages a collection of products."""
    
    def __init__(self, filename='inventory.json'):
        self.filename = filename
        self.products = {}                # Dictionary to hold products keyed by product_id
        self.load_inventory()             # Load existing inventory from file

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.products = {item['product_id']: Product(**item) for item in json.load(file)}
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error loading inventory: {e}")
    
    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([vars(product) for product in self.products.values()], file, indent=4)

    def add_product(self, product):
        """Add a new product to the inventory."""
        if product.product_id in self.products:
            print("Product ID already exists. Use update_product to modify.")
        else:
            self.products[product.product_id] = product
            self.save_inventory()
            print("Product added.")

    def update_product(self, product_id, quantity=None, price=None):
        """Update the quantity and/or price of a product in the inventory."""
        if product_id in self.products:
            product = self.products[product_id]
            if quantity is not None:
                product.quantity = quantity
            if price is not None:
                product.price = price
            self.save_inventory()
            print("Product updated.")
        else:
            print("Product not found.")

    def remove_product(self, product_id):
        """Remove a product from the inventory."""
        if product_id in self.products:
            del self.products[product_id]
            self.save_inventory()
            print("Product removed.")
        else:
            print("Product not found.")

    def list_products(self):
        """List all products in the inventory."""
        if not self.products:
            print("No products in inventory.")
        for product in self.products.values():
            print(product)

# Example usage:
if __name__ == "__main__":
    inventory = Inventory()

    # Adding products
    inventory.add_product(Product(product_id='P001', name='Gaming Laptop', quantity=10, price=1500.00))
    inventory.add_product(Product(product_id='P002', name='Mechanical Keyboard', quantity=25, price=100.00))

    # Listing products
    inventory.list_products()

    # Updating a product
    inventory.update_product('P001', quantity=8)

    # Removing a product
    inventory.remove_product('P002')

    # Final list of products
    inventory.list_products()
```
