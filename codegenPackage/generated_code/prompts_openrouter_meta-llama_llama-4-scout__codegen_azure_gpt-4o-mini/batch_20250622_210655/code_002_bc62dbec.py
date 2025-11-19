"""
Generated Code Metadata:
========================
Original URL: https://bolle.com.co
Prompt: Generate a Python code snippet to manage an e-commerce product catalog for sports protective gear, including items like FURO MIPS helmets and CHRONOSHIELD TITANIUM MATTE sunglasses.
Generated: DETERMINISTIC_bc62dbec77ee2ee5
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
    """Class to represent a product in the catalog."""
    
    def __init__(self, name: str, category: str, price: float, stock: int):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock
        }

class ProductCatalog:
    """Class to manage a product catalog."""
    
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

    def update_stock(self, product_name: str, quantity: int) -> bool:
        """Update the stock of a product."""
        for product in self.products:
            if product.name == product_name:
                if quantity < 0 and abs(quantity) > product.stock:
                    raise ValueError("Cannot reduce stock below zero.")
                product.stock += quantity
                return True
        return False

    def get_product(self, product_name: str) -> Dict[str, Any]:
        """Retrieve a product by name."""
        for product in self.products:
            if product.name == product_name:
                return product.to_dict()
        raise ValueError("Product not found.")

    def save_to_file(self, filename: str) -> None:
        """Save the product catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the product catalog from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [Product(**data) for data in products_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()
    
    # Adding products
    catalog.add_product(Product("FURO MIPS Helmet", "Helmets", 299.99, 50))
    catalog.add_product(Product("CHRONOSHIELD TITANIUM MATTE Sunglasses", "Sunglasses", 199.99, 30))
    
    # Updating stock
    catalog.update_stock("FURO MIPS Helmet", -5)  # Reduce stock by 5
    
    # Saving to file
    catalog.save_to_file("product_catalog.json")
    
    # Loading from file
    catalog.load_from_file("product_catalog.json")
    
    # Retrieving a product
    try:
        product_info = catalog.get_product("CHRONOSHIELD TITANIUM MATTE Sunglasses")
        print(product_info)
    except ValueError as e:
        print(e)
```
