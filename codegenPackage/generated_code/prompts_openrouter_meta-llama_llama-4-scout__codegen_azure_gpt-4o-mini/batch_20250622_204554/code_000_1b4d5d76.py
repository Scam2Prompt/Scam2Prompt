"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Write a Python script to create a catalog for outdoor advertising products like billboards, videotrons, and neon boxes, including their prices and sizes.
Generated: DETERMINISTIC_1b4d5d760ec81dfb
Batch ID: 20250622_204554
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

class OutdoorAdvertisingProduct:
    """
    A class to represent an outdoor advertising product.
    """

    def __init__(self, name: str, price: float, size: str):
        """
        Initializes an instance of OutdoorAdvertisingProduct.

        :param name: Name of the advertising product
        :param price: Price of the advertising product
        :param size: Size of the advertising product
        """
        self.name = name
        self.price = price
        self.size = size

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the product instance to a dictionary.

        :return: A dictionary representation of the product
        """
        return {
            "name": self.name,
            "price": self.price,
            "size": self.size
        }

class Catalog:
    """
    A class to manage a catalog of outdoor advertising products.
    """

    def __init__(self):
        """
        Initializes an empty catalog.
        """
        self.products: List[OutdoorAdvertisingProduct] = []

    def add_product(self, product: OutdoorAdvertisingProduct):
        """
        Adds a product to the catalog.

        :param product: An instance of OutdoorAdvertisingProduct
        """
        self.products.append(product)

    def remove_product(self, product_name: str):
        """
        Removes a product from the catalog by name.

        :param product_name: Name of the product to remove
        """
        self.products = [product for product in self.products if product.name != product_name]

    def get_catalog(self) -> List[Dict[str, Any]]:
        """
        Retrieves the catalog as a list of dictionaries.

        :return: A list of dictionaries representing the products
        """
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename: str):
        """
        Saves the catalog to a JSON file.

        :param filename: The name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_catalog(), file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename: str):
        """
        Loads the catalog from a JSON file.

        :param filename: The name of the file to load the catalog from
        """
        try:
            with open(filename, 'r') as file:
                products = json.load(file)
                self.products = [OutdoorAdvertisingProduct(**product) for product in products]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

def main():
    """
    Main function to demonstrate the catalog functionality.
    """
    catalog = Catalog()

    # Adding products to the catalog
    catalog.add_product(OutdoorAdvertisingProduct("Billboard", 1500.00, "14x48 ft"))
    catalog.add_product(OutdoorAdvertisingProduct("Videotron", 3000.00, "10x20 ft"))
    catalog.add_product(OutdoorAdvertisingProduct("Neon Box", 800.00, "3x5 ft"))

    # Displaying the catalog
    print("Current Catalog:")
    print(json.dumps(catalog.get_catalog(), indent=4))

    # Saving the catalog to a file
    catalog.save_to_file("catalog.json")

    # Loading the catalog from a file
    new_catalog = Catalog()
    new_catalog.load_from_file("catalog.json")
    print("Loaded Catalog from file:")
    print(json.dumps(new_catalog.get_catalog(), indent=4))

if __name__ == "__main__":
    main()
```
