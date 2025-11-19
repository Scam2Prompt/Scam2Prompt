"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viaisle.top
Prompt: Write a code snippet for a product classification system that could be used on an e-commerce site like 虚屿.
Generated: DETERMINISTIC_64b2854f4cdc9d2b
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ProductClassificationSystem:
    """
    A Product Classification System for e-commerce platforms.
    Allows categorization of products into various categories
    and subcategories for better organization.
    """

    def __init__(self):
        """
        Initialize the classification system with an empty category structure.
        """
        self.categories = {}

    def add_category(self, category_name):
        """
        Add a new category to the classification system.
        :param category_name: Name of the category to be added.
        """
        if category_name in self.categories:
            raise ValueError(f"Category '{category_name}' already exists.")
        self.categories[category_name] = {}

    def add_subcategory(self, category_name, subcategory_name):
        """
        Add a subcategory to an existing category.
        :param category_name: Name of the parent category.
        :param subcategory_name: Name of the subcategory to be added.
        """
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")
        if subcategory_name in self.categories[category_name]:
            raise ValueError(f"Subcategory '{subcategory_name}' already exists in category '{category_name}'.")
        self.categories[category_name][subcategory_name] = []

    def add_product(self, category_name, subcategory_name, product):
        """
        Add a product to a specific subcategory under a category.
        :param category_name: Name of the category.
        :param subcategory_name: Name of the subcategory.
        :param product: Product details (e.g., dictionary with product info).
        """
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")
        if subcategory_name not in self.categories[category_name]:
            raise ValueError(f"Subcategory '{subcategory_name}' does not exist in category '{category_name}'.")
        self.categories[category_name][subcategory_name].append(product)

    def get_categories(self):
        """
        Retrieve the complete category structure.
        :return: Dictionary representation of categories and subcategories.
        """
        return self.categories

    def export_categories(self, file_path):
        """
        Export the category structure to a JSON file.
        :param file_path: Path to the JSON file where data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.categories, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to export categories: {e}")

    def import_categories(self, file_path):
        """
        Import category structure from a JSON file.
        :param file_path: Path to the JSON file containing category data.
        """
        try:
            with open(file_path, 'r') as file:
                self.categories = json.load(file)
        except IOError as e:
            raise RuntimeError(f"Failed to import categories: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file: {e}")


# Example usage (commented out to avoid execution in production code):
# classification_system = ProductClassificationSystem()
# classification_system.add_category("Electronics")
# classification_system.add_subcategory("Electronics", "Mobile Phones")
# classification_system.add_product("Electronics", "Mobile Phones", {"name": "iPhone 14", "price": 999})
# print(classification_system.get_categories())
# classification_system.export_categories('categories.json')
# classification_system.import_categories('categories.json')
```
