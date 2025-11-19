"""
Generated Code Metadata:
========================
Original URL: https://fotopoint.com.ar
Prompt: "Design a product catalog system using a programming language of your choice, inspired by Fotopoint's product categories and subcategories."
Generated: DETERMINISTIC_8dfdb27bfcd73d9e
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Product Catalog System
Language: Python
Description: A simple product catalog system inspired by Fotopoint's product categories and subcategories.
"""

# Import necessary modules
import json

class ProductCatalog:
    """
    A class to represent a product catalog system.
    """

    def __init__(self):
        """
        Initialize the product catalog with an empty dictionary.
        """
        self.catalog = {}

    def add_category(self, category_name):
        """
        Add a new category to the catalog.
        :param category_name: Name of the category to add.
        """
        if category_name in self.catalog:
            raise ValueError(f"Category '{category_name}' already exists.")
        self.catalog[category_name] = {}
        print(f"Category '{category_name}' added successfully.")

    def add_subcategory(self, category_name, subcategory_name):
        """
        Add a new subcategory to an existing category.
        :param category_name: Name of the category to add the subcategory to.
        :param subcategory_name: Name of the subcategory to add.
        """
        if category_name not in self.catalog:
            raise ValueError(f"Category '{category_name}' does not exist.")
        if subcategory_name in self.catalog[category_name]:
            raise ValueError(f"Subcategory '{subcategory_name}' already exists in category '{category_name}'.")
        self.catalog[category_name][subcategory_name] = []
        print(f"Subcategory '{subcategory_name}' added to category '{category_name}' successfully.")

    def add_product(self, category_name, subcategory_name, product_name):
        """
        Add a product to a specific subcategory within a category.
        :param category_name: Name of the category.
        :param subcategory_name: Name of the subcategory.
        :param product_name: Name of the product to add.
        """
        if category_name not in self.catalog:
            raise ValueError(f"Category '{category_name}' does not exist.")
        if subcategory_name not in self.catalog[category_name]:
            raise ValueError(f"Subcategory '{subcategory_name}' does not exist in category '{category_name}'.")
        self.catalog[category_name][subcategory_name].append(product_name)
        print(f"Product '{product_name}' added to subcategory '{subcategory_name}' in category '{category_name}' successfully.")

    def view_catalog(self):
        """
        View the entire product catalog.
        :return: A JSON representation of the catalog.
        """
        return json.dumps(self.catalog, indent=4)

    def search_product(self, product_name):
        """
        Search for a product in the catalog.
        :param product_name: Name of the product to search for.
        :return: A list of locations where the product is found.
        """
        results = []
        for category, subcategories in self.catalog.items():
            for subcategory, products in subcategories.items():
                if product_name in products:
                    results.append(f"Category: {category}, Subcategory: {subcategory}")
        if results:
            return results
        else:
            return f"Product '{product_name}' not found in the catalog."


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the catalog
        catalog = ProductCatalog()

        # Add categories
        catalog.add_category("Cameras")
        catalog.add_category("Accessories")

        # Add subcategories
        catalog.add_subcategory("Cameras", "DSLR")
        catalog.add_subcategory("Cameras", "Mirrorless")
        catalog.add_subcategory("Accessories", "Tripods")
        catalog.add_subcategory("Accessories", "Batteries")

        # Add products
        catalog.add_product("Cameras", "DSLR", "Canon EOS 90D")
        catalog.add_product("Cameras", "Mirrorless", "Sony Alpha A7 III")
        catalog.add_product("Accessories", "Tripods", "Manfrotto Compact Action")
        catalog.add_product("Accessories", "Batteries", "Duracell AA Batteries")

        # View the catalog
        print("Product Catalog:")
        print(catalog.view_catalog())

        # Search for a product
        print("\nSearch Results:")
        print(catalog.search_product("Sony Alpha A7 III"))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
