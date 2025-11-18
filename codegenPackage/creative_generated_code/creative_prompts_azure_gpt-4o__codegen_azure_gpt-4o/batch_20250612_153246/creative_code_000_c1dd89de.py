"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Write Python code to create a catalog system for surgical instruments, including categories like "Dental Instruments," "Manicure Products," and "Surgical Products," as described on the Curative Surgical Industry website.
Generated: DETERMINISTIC_c1dd89de75e57df3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# surgical_instruments_catalog.py

import json


class CatalogError(Exception):
    """Custom exception for catalog errors."""
    pass


class SurgicalInstrumentsCatalog:
    """
    A class to manage a catalog of surgical instruments, including categories like:
    - Dental Instruments
    - Manicure Products
    - Surgical Products
    """

    def __init__(self):
        # Initialize the catalog as a dictionary with predefined categories
        self.catalog = {
            "Dental Instruments": [],
            "Manicure Products": [],
            "Surgical Products": []
        }

    def add_item(self, category, item_name, details):
        """
        Add an item to a specific category in the catalog.

        Args:
            category (str): The category of the item (e.g., "Dental Instruments").
            item_name (str): The name of the item.
            details (dict): Additional details about the item (e.g., description, price).

        Raises:
            CatalogError: If the category does not exist.
        """
        if category not in self.catalog:
            raise CatalogError(f"Category '{category}' does not exist in the catalog.")
        
        self.catalog[category].append({
            "name": item_name,
            "details": details
        })

    def remove_item(self, category, item_name):
        """
        Remove an item from a specific category in the catalog.

        Args:
            category (str): The category of the item.
            item_name (str): The name of the item to remove.

        Raises:
            CatalogError: If the category or item does not exist.
        """
        if category not in self.catalog:
            raise CatalogError(f"Category '{category}' does not exist in the catalog.")

        items = self.catalog[category]
        for item in items:
            if item["name"] == item_name:
                items.remove(item)
                return
        
        raise CatalogError(f"Item '{item_name}' not found in category '{category}'.")

    def list_items(self, category):
        """
        List all items in a specific category.

        Args:
            category (str): The category to list items from.

        Returns:
            list: A list of items in the specified category.

        Raises:
            CatalogError: If the category does not exist.
        """
        if category not in self.catalog:
            raise CatalogError(f"Category '{category}' does not exist in the catalog.")
        
        return self.catalog[category]

    def save_catalog(self, file_path):
        """
        Save the catalog to a JSON file.

        Args:
            file_path (str): The path to the file where the catalog will be saved.
        """
        with open(file_path, 'w') as file:
            json.dump(self.catalog, file, indent=4)

    def load_catalog(self, file_path):
        """
        Load the catalog from a JSON file.

        Args:
            file_path (str): The path to the file from which the catalog will be loaded.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(file_path, 'r') as file:
                self.catalog = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found.")


if __name__ == "__main__":
    # Example usage of the SurgicalInstrumentsCatalog class
    catalog = SurgicalInstrumentsCatalog()

    try:
        # Add items to the catalog
        catalog.add_item("Dental Instruments", "Dental Forceps", {"description": "Used for tooth extraction", "price": 120.00})
        catalog.add_item("Manicure Products", "Nail Clipper", {"description": "Stainless steel nail clipper", "price": 15.99})
        catalog.add_item("Surgical Products", "Scalpel", {"description": "Surgical knife with sharp blade", "price": 45.50})

        # List items in a category
        print("Dental Instruments:", catalog.list_items("Dental Instruments"))
        print("Manicure Products:", catalog.list_items("Manicure Products"))
        print("Surgical Products:", catalog.list_items("Surgical Products"))

        # Remove an item
        catalog.remove_item("Dental Instruments", "Dental Forceps")
        print("Dental Instruments after removal:", catalog.list_items("Dental Instruments"))

        # Save catalog to a file
        catalog.save_catalog("surgical_instruments_catalog.json")

        # Load catalog from a file
        catalog.load_catalog("surgical_instruments_catalog.json")
        print("Catalog loaded from file:", catalog.catalog)

    except CatalogError as e:
        print(f"Catalog error: {e}")
    except FileNotFoundError as e:
        print(f"File error: {e}")
```
