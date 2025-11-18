"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Write Python code to generate a product catalog for sportswear and fitness wear, including categories like soccer uniforms, compression tops, and stringer hoodies, based on the structure of Rising Star International's product offerings.
Generated: DETERMINISTIC_bf7003d537bdb7de
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Product:
    """
    Represents a product in the catalog.
    
    Attributes:
        name (str): Name of the product.
        category (str): Category of the product.
        price (float): Price of the product.
        sku (str): Stock Keeping Unit identifier for the product.
    """

    def __init__(self, name: str, category: str, price: float, sku: str):
        self.name = name
        self.category = category
        self.price = price
        self.sku = sku

    def to_dict(self) -> Dict:
        """Converts the product to a dictionary format for JSON serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'sku': self.sku
        }


class ProductCatalog:
    """
    Represents a catalog of products.
    
    Attributes:
        products (List[Product]): List of products in the catalog.
    """

    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Adds a new product to the catalog."""
        self.products.append(product)

    def generate_catalog(self) -> List[Dict]:
        """Generates the catalog as a list of dictionaries."""
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename: str) -> None:
        """Saves the product catalog to a JSON file."""
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.generate_catalog(), json_file, indent=4)
            print(f"Catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")


def main():
    """Main function to create and save a sportswear product catalog."""
    catalog = ProductCatalog()

    # Define products for the catalog
    products = [
        Product("Soccer Uniform", "Soccer", 49.99, "SKU12345"),
        Product("Compression Top", "Fitness", 29.99, "SKU12346"),
        Product("Stringer Hoodie", "Fitness", 39.99, "SKU12347"),
        Product("Running Shorts", "Fitness", 24.99, "SKU12348"),
        Product("Soccer Cleats", "Soccer", 89.99, "SKU12349"),
        Product("Yoga Pants", "Fitness", 34.99, "SKU12350"),
    ]

    # Add products to the catalog
    for product in products:
        catalog.add_product(product)

    # Save the catalog to a JSON file
    catalog.save_to_file('sportwear_catalog.json')


if __name__ == "__main__":
    main()
```
