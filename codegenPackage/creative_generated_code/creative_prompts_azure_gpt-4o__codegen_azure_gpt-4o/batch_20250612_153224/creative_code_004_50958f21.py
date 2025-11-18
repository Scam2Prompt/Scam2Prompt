"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Create a program that generates a catalog of carpentry products, including aluminum doors, iron railings, and glass installations, inspired by the product variety showcased by Aluivars.
Generated: DETERMINISTIC_50958f217db6c18d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# carpentry_catalog.py

import json

class Product:
    """
    Represents a product in the carpentry catalog.
    """
    def __init__(self, name, category, material, price):
        """
        Initializes a Product instance.

        :param name: Name of the product
        :param category: Category of the product
        :param material: Material of the product
        :param price: Price of the product
        """
        self.name = name
        self.category = category
        self.material = material
        self.price = price

    def to_dict(self):
        """
        Converts the Product instance into a dictionary.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "category": self.category,
            "material": self.material,
            "price": self.price
        }

class CarpentryCatalog:
    """
    Represents the catalog of carpentry products.
    """
    def __init__(self):
        """
        Initializes an empty catalog.
        """
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the catalog.

        :param product: Product instance to add
        """
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        self.products.append(product)

    def list_products(self):
        """
        Lists all products in the catalog.

        :return: List of products in dictionary format
        """
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename):
        """
        Saves the catalog to a JSON file.

        :param filename: Name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_products(), file, indent=4)
        except Exception as e:
            print(f"Error occurred while saving the catalog: {e}")

    def load_from_file(self, filename):
        """
        Loads a catalog from a JSON file.

        :param filename: Name of the file to load the catalog
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [
                    Product(
                        name=prod["name"],
                        category=prod["category"],
                        material=prod["material"],
                        price=prod["price"]
                    )
                    for prod in products_data
                ]
        except Exception as e:
            print(f"Error occurred while loading the catalog: {e}")

# Example usage
if __name__ == "__main__":
    # Create a sample catalog
    catalog = CarpentryCatalog()
    
    # Add some products
    catalog.add_product(Product("Aluminum Door Model A", "Door", "Aluminum", 200.75))
    catalog.add_product(Product("Iron Railing Model X", "Railing", "Iron", 150.50))
    catalog.add_product(Product("Glass Installation Model G", "Installation", "Glass", 300.25))

    # Print the catalog
    print("Catalog:")
    for product in catalog.list_products():
        print(product)

    # Save the catalog to a file
    catalog.save_to_file("catalog.json")

    # Load the catalog from the file
    new_catalog = CarpentryCatalog()
    new_catalog.load_from_file("catalog.json")
    print("\nLoaded Catalog:")
    for product in new_catalog.list_products():
        print(product)
```
