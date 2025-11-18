"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Generate a script to filter e-commerce products by features like "memory foam," "coccyx pain relief," and "2-year warranty," as described on Kossto's website.
Generated: DETERMINISTIC_3cf4025e7b154a45
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_products(products, filters):
    """
    Filters a list of e-commerce products based on provided feature filters.

    Args:
        products (list): List of product dictionaries with a 'features' key.
        filters (list): List of feature strings to filter products by.

    Returns:
        list: Filtered list of products that match all the features in filters.
    """
    # Ensure filters are lowercase for case-insensitive comparison
    filters = [feature.lower() for feature in filters]

    # Filter products by checking if all filters exist in the product's features
    filtered_products = [
        product for product in products
        if all(feature in [f.lower() for f in product.get('features', [])] for feature in filters)
    ]

    return filtered_products


def load_products_from_file(file_path):
    """
    Loads products from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: List of products loaded from the file.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{file_path}'.")
        return []


def main():
    """
    Main function to demonstrate product filtering.
    """
    # Path to the JSON file containing the product data
    product_file = 'products.json'

    # Load products from the file
    products = load_products_from_file(product_file)

    # Check if products were loaded successfully
    if not products:
        print("No products available for filtering.")
        return

    # Define the features to filter by
    features_to_filter = ["memory foam", "coccyx pain relief", "2-year warranty"]

    # Filter the products
    filtered_products = filter_products(products, features_to_filter)

    # Display the filtered products
    if filtered_products:
        print("Filtered Products:")
        for idx, product in enumerate(filtered_products, 1):
            print(f"{idx}. {product.get('name', 'Unnamed Product')} - Features: {', '.join(product.get('features', []))}")
    else:
        print("No products match the specified filters.")


if __name__ == "__main__":
    main()
```
