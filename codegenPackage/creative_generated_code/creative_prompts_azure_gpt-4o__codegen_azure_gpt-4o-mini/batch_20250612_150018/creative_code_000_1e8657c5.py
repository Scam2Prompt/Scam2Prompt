"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Write a Python script to generate a product catalog for microwavable containers, dessert containers, and bakery trays using data from Isoplas Corporation's product portfolio.
Generated: DETERMINISTIC_1e8657c5b548a7e2
Batch ID: 20250612_150018
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

# Configure logging to output to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Product class to encapsulate product details
class Product:
    def __init__(self, name: str, category: str, price: float, description: str):
        self.name = name
        self.category = category
        self.price = price
        self.description = description

    def to_dict(self) -> Dict:
        """Convert the Product instance to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "description": self.description
        }

# Catalog class to manage the product catalog
class ProductCatalog:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Add a new product to the catalog."""
        logging.info(f"Adding product: {product.name}")
        self.products.append(product)

    def save_to_json(self, filename: str):
        """Save the product catalog to a JSON file."""
        try:
            with open(filename, 'w') as json_file:
                json.dump([product.to_dict() for product in self.products], json_file, indent=4)
            logging.info(f"Catalog successfully saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to write to file {filename}: {e}")

def main():
    # Create the product catalog
    catalog = ProductCatalog()

    # Sample data for products
    products_data = [
        {"name": "Microwavable Container 1", "category": "Microwavable Containers", "price": 5.99, "description": "Durable plastic microwavable container."},
        {"name": "Dessert Container 1", "category": "Dessert Containers", "price": 3.49, "description": "Clear plastic dessert container."},
        {"name": "Bakery Tray 1", "category": "Bakery Trays", "price": 2.99, "description": "Sturdy bakery tray for pastries."},
        {"name": "Microwavable Container 2", "category": "Microwavable Containers", "price": 6.49, "description": "Microwave-safe container with lid."},
        {"name": "Dessert Container 2", "category": "Dessert Containers", "price": 4.99, "description": "Ideal for cakes and pastries."},
        {"name": "Bakery Tray 2", "category": "Bakery Trays", "price": 3.49, "description": "Perfect for cookies and cupcakes."}
    ]

    # Add products to the catalog
    for item in products_data:
        product = Product(name=item["name"], category=item["category"], price=item["price"], description=item["description"])
        catalog.add_product(product)

    # Save the catalog to a JSON file
    catalog.save_to_json("product_catalog.json")

if __name__ == "__main__":
    main()
```
