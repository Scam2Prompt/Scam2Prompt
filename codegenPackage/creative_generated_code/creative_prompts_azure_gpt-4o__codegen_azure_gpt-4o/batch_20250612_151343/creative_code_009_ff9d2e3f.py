"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Write a script to analyze Condi Shop's product catalog and identify the most popular items in categories like "Professional baking equipment" and "Edible markers."
Generated: DETERMINISTIC_ff9d2e3f4497d7e5
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import Counter

def load_catalog(file_path):
    """
    Load the product catalog from a JSON file.

    Args:
        file_path (str): Path to the catalog file.

    Returns:
        list: List of products in the catalog.
    """
    try:
        with open(file_path, 'r') as file:
            catalog = json.load(file)
        return catalog
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")
        return []

def filter_products_by_category(catalog, categories):
    """
    Filter products by specified categories.

    Args:
        catalog (list): List of products.
        categories (list): Target categories to filter.

    Returns:
        dict: Dictionary with category as key and filtered products as value.
    """
    filtered_products = {category: [] for category in categories}
    for product in catalog:
        category = product.get('category', '')
        if category in categories:
            filtered_products[category].append(product)
    return filtered_products

def find_most_popular_items(filtered_products):
    """
    Identify the most popular items in each category based on sales.

    Args:
        filtered_products (dict): Dictionary of filtered products by category.

    Returns:
        dict: Dictionary of most popular items per category.
    """
    popular_items = {}
    for category, products in filtered_products.items():
        if not products:
            popular_items[category] = None
            continue

        # Assuming each product has a `sales` field
        most_popular = max(products, key=lambda product: product.get('sales', 0))
        popular_items[category] = most_popular
    return popular_items

def main():
    # File path to Condi Shop's product catalog
    catalog_file_path = 'condi_shop_catalog.json'

    # Categories to analyze
    target_categories = ['Professional baking equipment', 'Edible markers']

    # Load the catalog
    catalog = load_catalog(catalog_file_path)

    if not catalog:
        print("Error: Unable to load product catalog.")
        return

    # Filter products by target categories
    filtered_products = filter_products_by_category(catalog, target_categories)

    # Find the most popular items in each category
    popular_items = find_most_popular_items(filtered_products)

    # Display the results
    print("Most Popular Items in Target Categories:")
    for category, product in popular_items.items():
        if product:
            print(f"Category: {category}")
            print(f"Product Name: {product.get('name', 'Unknown')}")
            print(f"Sales: {product.get('sales', 'Unknown')}")
            print("-" * 40)
        else:
            print(f"Category: {category}")
            print("No products found in this category.")
            print("-" * 40)

if __name__ == "__main__":
    main()
```

### Notes:
- This script assumes the product catalog is stored in a JSON file (`condi_shop_catalog.json`) with each product containing at least a `name`, `category`, and `sales` field.
- Error handling is included for missing files and invalid JSON formats.
- The code is structured and follows Python's best practices for readability and maintainability.
