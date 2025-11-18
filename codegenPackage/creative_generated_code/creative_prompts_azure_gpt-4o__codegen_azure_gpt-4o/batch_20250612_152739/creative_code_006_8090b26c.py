"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillahgems.com
Prompt: Using the gemstone categories from "Bismillah Gems," write a program to generate a visual catalog that organizes gemstones by type, weight, and price.
Generated: DETERMINISTIC_8090b26c066a3243
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from prettytable import PrettyTable

# Define gemstone categories
gemstone_categories = [
    {"type": "Ruby", "weight": 1.5, "price": 3000},
    {"type": "Emerald", "weight": 2.0, "price": 5000},
    {"type": "Sapphire", "weight": 1.0, "price": 2500},
    {"type": "Diamond", "weight": 0.5, "price": 10000},
    {"type": "Amethyst", "weight": 3.0, "price": 1500},
]

# File for storing the visual catalog
catalog_file = "gemstone_catalog.json"


def save_catalog_to_file(catalog, file_path):
    """
    Save the gemstone catalog to a JSON file.

    :param catalog: List of gemstone details to save.
    :param file_path: Path to the output file.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(catalog, f, indent=4)
        print(f"Catalog successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving catalog to file: {e}")


def load_catalog_from_file(file_path):
    """
    Load the gemstone catalog from a JSON file.

    :param file_path: Path to the input JSON file.
    :return: Loaded catalog as a list or None if there was an error.
    """
    try:
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return None
        with open(file_path, 'r') as f:
            catalog = json.load(f)
        return catalog
    except Exception as e:
        print(f"Error loading catalog from file: {e}")
        return None


def display_catalog(catalog):
    """
    Display the gemstone catalog in a tabular format.

    :param catalog: List of gemstone details to display.
    """
    table = PrettyTable()
    table.field_names = ["Type", "Weight (ct)", "Price ($)"]

    for item in catalog:
        table.add_row([item["type"], item["weight"], item["price"]])

    print(table)


def main():
    """
    Main function to generate, save, and display the gemstone catalog.
    """
    print("Generating gemstone catalog...")

    # Save the catalog to a file
    save_catalog_to_file(gemstone_categories, catalog_file)

    # Load the catalog back from the file
    print("\nLoading gemstone catalog from file...")
    loaded_catalog = load_catalog_from_file(catalog_file)

    if loaded_catalog:
        print("\nDisplaying gemstone catalog...")
        display_catalog(loaded_catalog)


if __name__ == "__main__":
    main()
```
