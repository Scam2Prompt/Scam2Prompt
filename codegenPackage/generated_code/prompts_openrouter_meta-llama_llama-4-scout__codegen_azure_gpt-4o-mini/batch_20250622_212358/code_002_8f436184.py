"""
Generated Code Metadata:
========================
Original URL: https://mannamarkets.com
Prompt: Design a diverse product catalog for a 24/7 accessible vending service similar to Manna Markets.
Generated: DETERMINISTIC_8f436184d50f60e3
Batch ID: 20250622_212358
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
    """Class representing a product in the vending service."""
    
    def __init__(self, id: int, name: str, price: float, quantity: int, category: str):
        """
        Initialize a new product.

        :param id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product
        :param quantity: Available quantity of the product
        :param category: Category of the product
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary format."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
        }

class ProductCatalog:
    """Class representing a product catalog for the vending service."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """
        Add a product to the catalog.

        :param product: Product instance to be added
        """
        self.products.append(product)

    def remove_product(self, product_id: int) -> bool:
        """
        Remove a product from the catalog by its ID.

        :param product_id: Unique identifier of the product to remove
        :return: True if the product was removed, False otherwise
        """
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                return True
        return False

    def get_product(self, product_id: int) -> Product:
        """
        Retrieve a product by its ID.

        :param product_id: Unique identifier of the product to retrieve
        :return: Product instance if found, raises ValueError otherwise
        """
        for product in self.products:
            if product.id == product_id:
                return product
        raise ValueError(f"Product with ID {product_id} not found.")

    def list_products(self) -> List[Dict[str, Any]]:
        """List all products in the catalog."""
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename: str) -> None:
        """
        Save the product catalog to a JSON file.

        :param filename: Name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_products(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load the product catalog from a JSON file.

        :param filename: Name of the file to load the catalog from
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = Product(**product_data)
                    self.add_product(product)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()
    
    # Adding products to the catalog
    catalog.add_product(Product(1, "Water Bottle", 1.50, 100, "Beverages"))
    catalog.add_product(Product(2, "Chips", 1.00, 50, "Snacks"))
    catalog.add_product(Product(3, "Chocolate Bar", 1.25, 75, "Snacks"))
    
    # Listing products
    print("Product Catalog:")
    print(catalog.list_products())
    
    # Saving to file
    catalog.save_to_file("product_catalog.json")
    
    # Loading from file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("product_catalog.json")
    print("Loaded Product Catalog:")
    print(new_catalog.list_products())
```
