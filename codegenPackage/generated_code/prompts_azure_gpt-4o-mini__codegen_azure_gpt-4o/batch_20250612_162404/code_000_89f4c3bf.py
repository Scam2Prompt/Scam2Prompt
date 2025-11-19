"""
Generated Code Metadata:
========================
Original URL: https://paslanmazspider.org
Prompt: Generate code to create a product catalog for stainless steel railing connection elements, including features like material quality and types of products offered.
Generated: DETERMINISTIC_89f4c3bf526c8b5b
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

class ProductCatalog:
    """
    A class to represent a product catalog for stainless steel railing connection elements.
    """

    def __init__(self):
        """
        Initialize the product catalog with an empty list of products.
        """
        self.products = []

    def add_product(self, name, material_quality, product_type, price):
        """
        Add a new product to the catalog.

        :param name: Name of the product
        :param material_quality: Quality of the material (e.g., Grade 304, Grade 316)
        :param product_type: Type of product (e.g., connector, bracket, end cap)
        :param price: Price of the product
        """
        try:
            product = {
                "name": name,
                "material_quality": material_quality,
                "product_type": product_type,
                "price": price
            }
            self.products.append(product)
        except Exception as e:
            print(f"Error adding product: {e}")

    def list_products(self):
        """
        List all products in the catalog.

        :return: List of products
        """
        return self.products

    def save_to_file(self, filename):
        """
        Save the product catalog to a JSON file.

        :param filename: Name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.products, file, indent=4)
            print(f"Catalog saved to {filename}")
        except Exception as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename):
        """
        Load the product catalog from a JSON file.

        :param filename: Name of the file to load the catalog
        """
        try:
            with open(filename, 'r') as file:
                self.products = json.load(file)
            print(f"Catalog loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}.")
        except Exception as e:
            print(f"Error loading catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a new product catalog
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product("Connector A", "Grade 304", "Connector", 12.99)
    catalog.add_product("Bracket B", "Grade 316", "Bracket", 15.49)
    catalog.add_product("End Cap C", "Grade 304", "End Cap", 8.99)

    # List all products
    print("Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Save the catalog to a file
    catalog.save_to_file("product_catalog.json")

    # Load the catalog from a file
    catalog.load_from_file("product_catalog.json")
    print("Loaded Product Catalog:")
    for product in catalog.list_products():
        print(product)
```
