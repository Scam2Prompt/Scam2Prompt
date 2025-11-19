"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Write a function to manage product categories and items for a site catalog, similar to the offerings on ra-don.com.
Generated: DETERMINISTIC_c4021d172a1f0ff8
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Catalog Manager Module

This module provides functionality to manage product categories and items for a site catalog.
It allows adding, updating, deleting, and listing categories and products, ensuring a clean and efficient design.
"""

# Importing necessary libraries
from typing import Dict, List, Union

class CatalogManager:
    """
    A class to manage product categories and items in a catalog.
    """

    def __init__(self):
        """
        Initializes an empty catalog.
        The catalog is represented as a dictionary:
        {
            "category_name": ["item1", "item2", ...]
        }
        """
        self.catalog: Dict[str, List[str]] = {}

    def add_category(self, category_name: str) -> None:
        """
        Adds a new category to the catalog.
        :param category_name: Name of the category to add.
        """
        if category_name in self.catalog:
            raise ValueError(f"Category '{category_name}' already exists.")
        self.catalog[category_name] = []

    def delete_category(self, category_name: str) -> None:
        """
        Deletes an existing category from the catalog.
        :param category_name: Name of the category to delete.
        """
        if category_name not in self.catalog:
            raise ValueError(f"Category '{category_name}' does not exist.")
        del self.catalog[category_name]

    def add_item(self, category_name: str, item_name: str) -> None:
        """
        Adds an item to a specific category.
        :param category_name: Name of the category to add the item to.
        :param item_name: Name of the item to add.
        """
        if category_name not in self.catalog:
            raise ValueError(f"Category '{category_name}' does not exist.")
        if item_name in self.catalog[category_name]:
            raise ValueError(f"Item '{item_name}' already exists in category '{category_name}'.")
        self.catalog[category_name].append(item_name)

    def delete_item(self, category_name: str, item_name: str) -> None:
        """
        Deletes an item from a specific category.
        :param category_name: Name of the category to delete the item from.
        :param item_name: Name of the item to delete.
        """
        if category_name not in self.catalog:
            raise ValueError(f"Category '{category_name}' does not exist.")
        if item_name not in self.catalog[category_name]:
            raise ValueError(f"Item '{item_name}' does not exist in category '{category_name}'.")
        self.catalog[category_name].remove(item_name)

    def list_categories(self) -> List[str]:
        """
        Lists all categories in the catalog.
        :return: A list of category names.
        """
        return list(self.catalog.keys())

    def list_items(self, category_name: str) -> Union[List[str], None]:
        """
        Lists all items in a specific category.
        :param category_name: Name of the category to list items from.
        :return: A list of items in the category, or None if the category does not exist.
        """
        if category_name not in self.catalog:
            return None
        return self.catalog[category_name]

    def display_catalog(self) -> None:
        """
        Displays the entire catalog.
        """
        if not self.catalog:
            print("The catalog is empty.")
            return
        for category, items in self.catalog.items():
            print(f"Category: {category}")
            print(f"Items: {', '.join(items) if items else 'No items available.'}")
            print("-" * 40)


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the catalog manager
        manager = CatalogManager()

        # Add categories
        manager.add_category("Electronics")
        manager.add_category("Books")

        # Add items to categories
        manager.add_item("Electronics", "Smartphone")
        manager.add_item("Electronics", "Laptop")
        manager.add_item("Books", "Fiction Novel")

        # Display the catalog
        manager.display_catalog()

        # List categories
        print("Categories:", manager.list_categories())

        # List items in a category
        print("Items in Electronics:", manager.list_items("Electronics"))

        # Delete an item
        manager.delete_item("Electronics", "Laptop")

        # Delete a category
        manager.delete_category("Books")

        # Display the catalog after modifications
        manager.display_catalog()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
