"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://padmavatienterprise.org
Prompt: Write a Python script to generate a product catalog for a B2B industrial goods provider, including categories like "IT Materials," "Office Stationery," "Signage Materials," and "Packing Materials," with options for adding descriptions and prices.
Generated: DETERMINISTIC_ca7ccce560c3b42b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Product:
    """Represents a product in the catalog."""
    
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self) -> dict:
        """Convert the Product object to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

class Category:
    """Represents a category of products in the catalog."""
    
    def __init__(self, name: str):
        self.name = name
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Adds a product to the category."""
        self.products.append(product)

    def to_dict(self) -> dict:
        """Convert the Category object to a dictionary."""
        return {
            "name": self.name,
            "products": [product.to_dict() for product in self.products]
        }

class Catalog:
    """Represents the product catalog containing multiple categories."""
    
    def __init__(self):
        self.categories: Dict[str, Category] = {}

    def add_category(self, category: Category):
        """Adds a category to the catalog."""
        self.categories[category.name] = category

    def to_dict(self) -> dict:
        """Convert the Catalog object to a dictionary."""
        return {
            "categories": [category.to_dict() for category in self.categories.values()]
        }

    def save_to_file(self, file_path: str):
        """Saves the catalog to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            logging.info(f"Catalog saved to {file_path}")
        except Exception as e:
            logging.error(f"Failed to save catalog to {file_path}: {e}")

def main():
    # Initialize the catalog
    catalog = Catalog()

    # Create categories
    it_materials = Category("IT Materials")
    office_stationery = Category("Office Stationery")
    signage_materials = Category("Signage Materials")
    packing_materials = Category("Packing Materials")

    # Add products to IT Materials
    it_materials.add_product(Product("Laptop", "High-performance laptop.", 1200.00))
    it_materials.add_product(Product("Server", "Rack-mounted server.", 2500.00))

    # Add products to Office Stationery
    office_stationery.add_product(Product("Printer", "All-in-one color printer.", 300.00))
    office_stationery.add_product(Product("Notebook", "Spiral notebook, 200 pages.", 2.50))

    # Add products to Signage Materials
    signage_materials.add_product(Product("Banner", "Vinyl banner, custom design.", 150.00))
    signage_materials.add_product(Product("Yard Sign", "Durable yard sign for outdoor use.", 25.00))

    # Add products to Packing Materials
    packing_materials.add_product(Product("Bubble Wrap", "Large roll of bubble wrap.", 50.00))
    packing_materials.add_product(Product("Packing Tape", "Heavy-duty packing tape.", 5.00))

    # Add categories to the catalog
    catalog.add_category(it_materials)
    catalog.add_category(office_stationery)
    catalog.add_category(signage_materials)
    catalog.add_category(packing_materials)

    # Save the catalog to a JSON file
    catalog.save_to_file("product_catalog.json")

if __name__ == "__main__":
    main()
```
