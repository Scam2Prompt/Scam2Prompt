"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Write a script to filter and display products from 심바공구's catalog based on keywords like "혼다 엔진톱" or "그린웍스 충전예초기" and sort them by price.
Generated: DETERMINISTIC_bd19e8f7425617eb
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_catalog(file_path):
    """
    Load the product catalog from a JSON file.

    :param file_path: Path to the JSON file containing the catalog.
    :return: List of products.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return []


def filter_products_by_keywords(products, keywords):
    """
    Filter the products based on the given keywords.

    :param products: List of products (dictionaries).
    :param keywords: List of keywords to filter the products.
    :return: Filtered list of products.
    """
    filtered = [
        product for product in products
        if any(keyword in product.get('name', '') for keyword in keywords)
    ]
    return filtered


def sort_products_by_price(products, ascending=True):
    """
    Sort the products by price.

    :param products: List of products (dictionaries).
    :param ascending: Whether to sort in ascending order (default: True).
    :return: Sorted list of products.
    """
    try:
        return sorted(products, key=lambda x: x.get('price', 0), reverse=not ascending)
    except TypeError:
        print("Error: Price values must be numeric to sort.")
        return products


def display_products(products):
    """
    Display the filtered and sorted products.

    :param products: List of products (dictionaries).
    """
    if not products:
        print("No products to display.")
        return

    for product in products:
        name = product.get('name', 'No name')
        price = product.get('price', 'Unknown price')
        print(f"Name: {name}, Price: {price}")


def main():
    """
    Main function to load, filter, sort, and display products.
    """
    # Path to the catalog file
    catalog_file = 'simba_catalog.json'

    # Keywords to filter products
    keywords = ["혼다 엔진톱", "그린웍스 충전예초기"]

    # Load the catalog
    products = load_catalog(catalog_file)

    if not products:
        return

    # Filter products based on keywords
    filtered_products = filter_products_by_keywords(products, keywords)

    # Sort products by price (ascending order)
    sorted_products = sort_products_by_price(filtered_products, ascending=True)

    # Display the filtered and sorted products
    display_products(sorted_products)


if __name__ == '__main__':
    main()
```
