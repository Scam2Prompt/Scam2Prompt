"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: Write a Python script to generate a product catalog for a B2B industrial goods provider, including categories like "IT Materials," "Office Stationery," "Signage Materials," and "Packing Materials," with options for adding descriptions and prices.
Generated: DETERMINISTIC_ca7ccce560c3b42b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Product:
    """Class representing a product in the catalog."""
    
    def __init__(self, name: str, category: str, description: str, price: float):
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "price": self.price
        }

class ProductCatalog:
    """Class representing a product catalog."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        self.products.append(product)

    def save_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
            print(f"Catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the catalog from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = Product(
                        name=product_data['name'],
                        category=product_data['category'],
                        description=product_data['description'],
                        price=product_data['price']
                    )
                    self.add_product(product)
            print(f"Catalog loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

def main():
    """Main function to demonstrate the product catalog functionality."""
    catalog = ProductCatalog()

    # Example products
    catalog.add_product(Product("Laptop", "IT Materials", "High-performance laptop", 1200.00))
    catalog.add_product(Product("Printer", "Office Stationery", "Laser printer for office use", 300.00))
    catalog.add_product(Product("Banner", "Signage Materials", "Vinyl banner for outdoor use", 150.00))
    catalog.add_product(Product("Packing Tape", "Packing Materials", "Strong packing tape", 10.00))

    # Save the catalog to a file
    catalog.save_to_file("product_catalog.json")

    # Load the catalog from a file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("product_catalog.json")

if __name__ == "__main__":
    main()
```
