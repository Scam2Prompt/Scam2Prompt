"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Write a Python script to create a product catalog for salon equipment, including items like "صندلی آرایشگاهی," "تخت ماساژ," and "ترولی آرایشگاهی," with customizable attributes such as color and material.
Generated: DETERMINISTIC_36949bf47a5ae6d0
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Product:
    """
    Represents a product in the catalog with customizable attributes.

    Attributes:
        name (str): The name of the product.
        color (str): The color of the product.
        material (str): The material of the product.
        price (float): The price of the product.
    """

    def __init__(self, name: str, color: str, material: str, price: float):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            color (str): The color of the product.
            material (str): The material of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.color = color
        self.material = material
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Product instance to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the product.
        """
        return {
            "name": self.name,
            "color": self.color,
            "material": self.material,
            "price": self.price
        }

class ProductCatalog:
    """
    Represents a catalog of products.

    Attributes:
        products (List[Product]): A list of products in the catalog.
    """

    def __init__(self):
        """Initializes a ProductCatalog with an empty product list."""
        self.products = []

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): The product to be added.

        Raises:
            ValueError: If the product already exists in the catalog.
        """
        if product in self.products:
            raise ValueError("Product already exists in the catalog.")
        self.products.append(product)

    def save_to_file(self, file_path: str):
        """
        Saves the product catalog to a JSON file.

        Args:
            file_path (str): The path to the file where the catalog will be saved.

        Raises:
            IOError: If an error occurs while writing to the file.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump([product.to_dict() for product in self.products], file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def load_from_file(self, file_path: str):
        """
        Loads the product catalog from a JSON file.

        Args:
            file_path (str): The path to the file from which the catalog will be loaded.

        Raises:
            IOError: If an error occurs while reading from the file.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                products_data = json.load(file)
                for item in products_data:
                    product = Product(item['name'], item['color'], item['material'], item['price'])
                    self.add_product(product)
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while reading from the file: {e}")

if __name__ == "__main__":
    # Create a product catalog
    catalog = ProductCatalog()

    # Add some products to the catalog
    catalog.add_product(Product("صندلی آرایشگاهی", "black", "leather", 150.0))
    catalog.add_product(Product("تخت ماساژ", "white", "fabric", 300.0))
    catalog.add_product(Product("ترولی آرایشگاهی", "silver", "metal", 80.0))

    # Save the catalog to a JSON file
    catalog.save_to_file("product_catalog.json")

    # Load the catalog from the JSON file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("product_catalog.json")

    print("Catalog loaded successfully.")
    for product in new_catalog.products:
        print(product.to_dict())
```
