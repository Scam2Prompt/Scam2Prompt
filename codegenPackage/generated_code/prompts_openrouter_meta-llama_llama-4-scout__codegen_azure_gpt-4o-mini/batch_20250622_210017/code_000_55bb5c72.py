"""
Generated Code Metadata:
========================
Original URL: https://blueseanice.com
Prompt: Write a Python script to manage a simple product catalog for a K-Beauty online store.
Generated: DETERMINISTIC_55bb5c72adcfee50
Batch ID: 20250622_210017
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
    """Class to represent a product in the catalog."""
    
    def __init__(self, product_id, name, price, quantity, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def to_dict(self):
        """Convert the product to a dictionary for JSON serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'description': self.description
        }

class ProductCatalog:
    """Class to manage a product catalog."""
    
    def __init__(self, filename='catalog.json'):
        self.filename = filename
        self.products = {}
        self.load_catalog()

    def load_catalog(self):
        """Load the product catalog from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.products = {p['product_id']: Product(**p) for p in json.load(file)}
                except json.JSONDecodeError as e:
                    print(f"Error loading catalog: {e}")
                    self.products = {}

    def save_catalog(self):
        """Save the product catalog to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([product.to_dict() for product in self.products.values()], file, indent=4)

    def add_product(self, product):
        """Add a new product to the catalog."""
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product
        self.save_catalog()

    def remove_product(self, product_id):
        """Remove a product from the catalog by its ID."""
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} does not exist.")
        del self.products[product_id]
        self.save_catalog()

    def update_product(self, product_id, **kwargs):
        """Update an existing product's details."""
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} does not exist.")
        product = self.products[product_id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        self.save_catalog()

    def get_product(self, product_id):
        """Retrieve a product by its ID."""
        return self.products.get(product_id)

    def list_products(self):
        """List all products in the catalog."""
        return [product.to_dict() for product in self.products.values()]

def main():
    """Main function to demonstrate the product catalog management."""
    catalog = ProductCatalog()

    # Example usage
    try:
        # Adding products
        catalog.add_product(Product('001', 'Hydrating Serum', 25.99, 100, 'A serum that hydrates and revitalizes skin.'))
        catalog.add_product(Product('002', 'Moisturizing Cream', 30.50, 50, 'A rich cream for deep hydration.'))

        # Listing products
        print("Product Catalog:")
        for product in catalog.list_products():
            print(product)

        # Updating a product
        catalog.update_product('001', price=24.99, quantity=90)

        # Removing a product
        catalog.remove_product('002')

        # Listing products after updates
        print("\nUpdated Product Catalog:")
        for product in catalog.list_products():
            print(product)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
