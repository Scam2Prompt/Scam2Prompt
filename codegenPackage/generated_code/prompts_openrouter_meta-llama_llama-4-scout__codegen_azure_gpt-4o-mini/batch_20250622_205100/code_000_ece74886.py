"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for pet supplies, including items like "Caixa de Transporte" and "Antipulgas e Carrapatos Frontline Plus".
Generated: DETERMINISTIC_ece74886d9abd955
Batch ID: 20250622_205100
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
    """Class to represent a product in the e-commerce catalog."""
    
    def __init__(self, name: str, category: str, price: float, description: str):
        """
        Initialize a new product.

        :param name: Name of the product
        :param category: Category of the product
        :param price: Price of the product
        :param description: Description of the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.description = description

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary format for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "description": self.description
        }

class ProductCatalog:
    """Class to manage a catalog of products."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Add a product to the catalog.

        :param product: Product instance to be added
        """
        self.products.append(product)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

def main():
    """Main function to create and display the product catalog."""
    try:
        # Create a product catalog
        catalog = ProductCatalog()

        # Add products to the catalog
        catalog.add_product(Product("Caixa de Transporte", "Transport", 150.00, "Caixa de transporte para pets, ideal para viagens."))
        catalog.add_product(Product("Antipulgas e Carrapatos Frontline Plus", "Health", 75.00, "Tratamento eficaz contra pulgas e carrapatos."))

        # Convert catalog to JSON and print
        catalog_json = catalog.to_json()
        print(catalog_json)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
