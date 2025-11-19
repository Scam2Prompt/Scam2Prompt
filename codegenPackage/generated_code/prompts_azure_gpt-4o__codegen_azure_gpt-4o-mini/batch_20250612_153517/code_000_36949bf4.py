"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Write a Python script to create a product catalog for salon equipment, including items like "صندلی آرایشگاهی," "تخت ماساژ," and "ترولی آرایشگاهی," with customizable attributes such as color and material.
Generated: DETERMINISTIC_36949bf47a5ae6d0
Batch ID: 20250612_153517
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
    """
    A class to represent a product in the salon equipment catalog.
    """

    def __init__(self, name: str, color: str, material: str):
        """
        Initializes a new product with the given attributes.

        :param name: The name of the product.
        :param color: The color of the product.
        :param material: The material of the product.
        """
        self.name = name
        self.color = color
        self.material = material

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the product instance to a dictionary.

        :return: A dictionary representation of the product.
        """
        return {
            "name": self.name,
            "color": self.color,
            "material": self.material
        }

class ProductCatalog:
    """
    A class to manage a catalog of salon equipment products.
    """

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        :param product: An instance of Product to be added.
        """
        self.products.append(product)

    def save_to_file(self, filename: str):
        """
        Saves the product catalog to a JSON file.

        :param filename: The name of the file to save the catalog to.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump([product.to_dict() for product in self.products], file, ensure_ascii=False, indent=4)
            print(f"Catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename: str):
        """
        Loads the product catalog from a JSON file.

        :param filename: The name of the file to load the catalog from.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                products_data = json.load(file)
                for item in products_data:
                    product = Product(item['name'], item['color'], item['material'])
                    self.add_product(product)
            print(f"Catalog loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

    def display_catalog(self):
        """Displays the product catalog in a readable format."""
        if not self.products:
            print("The catalog is empty.")
            return
        for product in self.products:
            print(f"Product Name: {product.name}, Color: {product.color}, Material: {product.material}")

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()
    
    # Adding products to the catalog
    catalog.add_product(Product("صندلی آرایشگاهی", "Black", "Leather"))
    catalog.add_product(Product("تخت ماساژ", "White", "Foam"))
    catalog.add_product(Product("ترولی آرایشگاهی", "Silver", "Metal"))

    # Display the catalog
    catalog.display_catalog()

    # Save the catalog to a file
    catalog.save_to_file("salon_equipment_catalog.json")

    # Load the catalog from a file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("salon_equipment_catalog.json")
    new_catalog.display_catalog()
```
