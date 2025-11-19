"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Generate a Python script to create a catalog of Samba Plastic's furniture products, including categories like Rattan Chairs and Tables.
Generated: DETERMINISTIC_279055ca2758d78a
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FurnitureCatalog:
    """
    A class to manage a catalog of furniture products for Samba Plastic.
    """

    def __init__(self):
        """
        Initializes an empty catalog.
        """
        self.catalog = {}

    def add_category(self, category_name):
        """
        Adds a new category to the catalog.

        :param category_name: Name of the category to add.
        """
        if category_name in self.catalog:
            raise ValueError(f"Category '{category_name}' already exists.")
        self.catalog[category_name] = []

    def add_product(self, category_name, product_name, price, description):
        """
        Adds a new product to a specific category.

        :param category_name: Name of the category to add the product to.
        :param product_name: Name of the product.
        :param price: Price of the product.
        :param description: Description of the product.
        """
        if category_name not in self.catalog:
            raise ValueError(f"Category '{category_name}' does not exist.")
        product = {
            "name": product_name,
            "price": price,
            "description": description
        }
        self.catalog[category_name].append(product)

    def remove_product(self, category_name, product_name):
        """
        Removes a product from a specific category.

        :param category_name: Name of the category to remove the product from.
        :param product_name: Name of the product to remove.
        """
        if category_name not in self.catalog:
            raise ValueError(f"Category '{category_name}' does not exist.")
        products = self.catalog[category_name]
        self.catalog[category_name] = [
            product for product in products if product["name"] != product_name
        ]

    def get_catalog(self):
        """
        Returns the entire catalog.

        :return: The catalog as a dictionary.
        """
        return self.catalog

    def save_catalog_to_file(self, file_name):
        """
        Saves the catalog to a JSON file.

        :param file_name: Name of the file to save the catalog to.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.catalog, file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_catalog_from_file(self, file_name):
        """
        Loads the catalog from a JSON file.

        :param file_name: Name of the file to load the catalog from.
        """
        try:
            with open(file_name, 'r') as file:
                self.catalog = json.load(file)
        except IOError as e:
            print(f"Error loading catalog from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    catalog = FurnitureCatalog()

    # Adding categories
    catalog.add_category("Rattan Chairs")
    catalog.add_category("Tables")

    # Adding products
    catalog.add_product("Rattan Chairs", "Classic Rattan Chair", 49.99, "A comfortable and stylish rattan chair.")
    catalog.add_product("Tables", "Dining Table", 129.99, "A sturdy dining table made of high-quality materials.")

    # Displaying the catalog
    print("Current Catalog:")
    print(json.dumps(catalog.get_catalog(), indent=4))

    # Saving the catalog to a file
    catalog.save_catalog_to_file("furniture_catalog.json")

    # Loading the catalog from a file
    catalog.load_catalog_from_file("furniture_catalog.json")
    print("\nCatalog Loaded from File:")
    print(json.dumps(catalog.get_catalog(), indent=4))
```
