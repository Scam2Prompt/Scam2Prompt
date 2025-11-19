"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Write a Python code snippet to manage an e-commerce product catalog for a natural beauty products company, including product categories for "100% Natural, Energy, Food Supplement, Protein" products.
Generated: DETERMINISTIC_d1cf5fb0cf05c30b
Batch ID: 20250622_211652
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
    A class to manage the product catalog for an e-commerce platform.
    """

    def __init__(self):
        """
        Initializes the product catalog with predefined categories.
        """
        self.categories = {
            "100% Natural": [],
            "Energy": [],
            "Food Supplement": [],
            "Protein": []
        }

    def add_product(self, category, product_name, price, stock):
        """
        Adds a product to a specific category in the catalog.

        :param category: The category to which the product belongs.
        :param product_name: The name of the product.
        :param price: The price of the product.
        :param stock: The stock quantity of the product.
        :raises ValueError: If the category is invalid.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.categories.keys())}")
        
        product = {
            "name": product_name,
            "price": price,
            "stock": stock
        }
        self.categories[category].append(product)

    def remove_product(self, category, product_name):
        """
        Removes a product from a specific category in the catalog.

        :param category: The category from which the product should be removed.
        :param product_name: The name of the product to remove.
        :raises ValueError: If the category or product is invalid.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.categories.keys())}")
        
        for product in self.categories[category]:
            if product["name"] == product_name:
                self.categories[category].remove(product)
                return
        
        raise ValueError(f"Product '{product_name}' not found in category '{category}'.")

    def list_products(self, category=None):
        """
        Lists all products in the catalog or in a specific category.

        :param category: The category to list products from (optional).
        :return: A list of products.
        :raises ValueError: If the category is invalid.
        """
        if category:
            if category not in self.categories:
                raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.categories.keys())}")
            return self.categories[category]
        
        return self.categories

    def save_catalog(self, file_path):
        """
        Saves the product catalog to a JSON file.

        :param file_path: The path to the file where the catalog will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.categories, file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_catalog(self, file_path):
        """
        Loads the product catalog from a JSON file.

        :param file_path: The path to the file from which the catalog will be loaded.
        :raises IOError: If the file cannot be read.
        """
        try:
            with open(file_path, 'r') as file:
                self.categories = json.load(file)
        except IOError as e:
            print(f"Error loading catalog from file: {e}")


# Example usage:
if __name__ == "__main__":
    catalog = ProductCatalog()

    # Add products
    catalog.add_product("100% Natural", "Organic Face Cream", 25.99, 50)
    catalog.add_product("Energy", "Energy Bar", 2.99, 200)
    catalog.add_product("Food Supplement", "Vitamin C Tablets", 15.99, 100)
    catalog.add_product("Protein", "Whey Protein Powder", 45.99, 30)

    # List all products
    print("All Products:", catalog.list_products())

    # List products in a specific category
    print("Energy Products:", catalog.list_products("Energy"))

    # Remove a product
    catalog.remove_product("Energy", "Energy Bar")

    # Save catalog to file
    catalog.save_catalog("product_catalog.json")

    # Load catalog from file
    catalog.load_catalog("product_catalog.json")
    print("Loaded Catalog:", catalog.list_products())
```
