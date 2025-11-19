"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for baby clothing and accessories, including product names, prices, and descriptions, similar to the ones listed on Somos Corujas.
Generated: DETERMINISTIC_6e390d6182ad20bb
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ProductCatalog:
    """
    A class to represent an e-commerce product catalog for baby clothing and accessories.
    """

    def __init__(self):
        """
        Initializes an empty product catalog.
        """
        self.products = []

    def add_product(self, name, price, description):
        """
        Adds a product to the catalog.

        :param name: str - Name of the product
        :param price: float - Price of the product
        :param description: str - Description of the product
        :raises ValueError: If price is negative or name/description is empty
        """
        if not name or not description:
            raise ValueError("Product name and description cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        
        product = {
            "name": name,
            "price": round(price, 2),  # Ensure price is rounded to 2 decimal places
            "description": description
        }
        self.products.append(product)

    def list_products(self):
        """
        Lists all products in the catalog.

        :return: list - List of products
        """
        return self.products

    def save_to_file(self, filename):
        """
        Saves the product catalog to a JSON file.

        :param filename: str - Name of the file to save the catalog
        :raises IOError: If there is an issue saving the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.products, file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename):
        """
        Loads the product catalog from a JSON file.

        :param filename: str - Name of the file to load the catalog from
        :raises IOError: If there is an issue reading the file
        :raises json.JSONDecodeError: If the file content is not valid JSON
        """
        try:
            with open(filename, 'r') as file:
                self.products = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    # Adding products to the catalog
    try:
        catalog.add_product("Baby Onesie", 19.99, "Soft cotton onesie for newborns.")
        catalog.add_product("Baby Blanket", 25.50, "Warm and cozy blanket for babies.")
        catalog.add_product("Baby Socks", 5.99, "Pack of 3 pairs of baby socks.")
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Listing products
    print("Product Catalog:")
    for product in catalog.list_products():
        print(f"Name: {product['name']}, Price: ${product['price']}, Description: {product['description']}")

    # Saving catalog to a file
    catalog.save_to_file("product_catalog.json")

    # Loading catalog from a file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("product_catalog.json")
    print("\nLoaded Product Catalog:")
    for product in new_catalog.list_products():
        print(f"Name: {product['name']}, Price: ${product['price']}, Description: {product['description']}")
```
