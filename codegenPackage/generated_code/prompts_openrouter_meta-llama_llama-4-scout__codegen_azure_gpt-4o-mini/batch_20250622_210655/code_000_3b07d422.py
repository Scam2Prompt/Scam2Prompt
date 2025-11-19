"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Write a Python code to manage a catalog of customized textile products, including t-shirts, hoodies, and kids' items, with options for serigraphy, vinyl textile, and DTF printing.
Generated: DETERMINISTIC_3b07d42246668d74
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Product:
    """Class representing a textile product."""
    
    def __init__(self, name: str, category: str, printing_method: str, price: float):
        self.name = name
        self.category = category
        self.printing_method = printing_method
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "printing_method": self.printing_method,
            "price": self.price
        }

class Catalog:
    """Class to manage a catalog of textile products."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a new product to the catalog."""
        self.products.append(product)

    def remove_product(self, product_name: str) -> bool:
        """Remove a product from the catalog by name."""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return True
        return False

    def find_product(self, product_name: str) -> Product:
        """Find a product by name."""
        for product in self.products:
            if product.name == product_name:
                return product
        raise ValueError(f"Product '{product_name}' not found in the catalog.")

    def list_products(self) -> List[Dict[str, Any]]:
        """List all products in the catalog."""
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_products(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the catalog from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [Product(**data) for data in products_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    catalog = Catalog()
    
    # Adding products
    catalog.add_product(Product("Cool T-Shirt", "T-Shirt", "Serigraphy", 19.99))
    catalog.add_product(Product("Warm Hoodie", "Hoodie", "Vinyl Textile", 39.99))
    catalog.add_product(Product("Kids Fun Tee", "Kids", "DTF Printing", 14.99))

    # Listing products
    print("Catalog Products:")
    for product in catalog.list_products():
        print(product)

    # Saving to file
    catalog.save_to_file("catalog.json")

    # Loading from file
    new_catalog = Catalog()
    new_catalog.load_from_file("catalog.json")
    print("Loaded Products:")
    for product in new_catalog.list_products():
        print(product)
```
