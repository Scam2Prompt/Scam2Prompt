"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a script to simulate filtering products by brand names like "Porcelana Schmidt" or "Bon Gourmet," as listed on the "asacanelbrazzz" website.
Generated: DETERMINISTIC_f0b80265e5d505bd
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample data representing products from the fictional "asacanelbrazzz" website
PRODUCTS = [
    {"id": 1, "name": "Porcelain Plate", "brand": "Porcelana Schmidt", "price": 20.99},
    {"id": 2, "name": "Glassware Set", "brand": "Bon Gourmet", "price": 35.50},
    {"id": 3, "name": "Stainless Steel Fork", "brand": "Cutlery Pro", "price": 5.99},
    {"id": 4, "name": "Ceramic Mug", "brand": "Porcelana Schmidt", "price": 12.99},
    {"id": 5, "name": "Chef Knife", "brand": "Bon Gourmet", "price": 45.00},
]

def filter_products_by_brand(products, brand_names):
    """
    Filters products by the specified brand names.

    Args:
        products (list): List of product dictionaries.
        brand_names (list): List of brand names to filter by.

    Returns:
        list: Filtered list of products matching the specified brands.
    """
    # Validate input types
    if not isinstance(products, list) or not isinstance(brand_names, list):
        raise ValueError("Both 'products' and 'brand_names' must be lists.")

    # Filter products by checking if the product's brand is in the given brand names list
    return [product for product in products if product["brand"] in brand_names]

def main():
    """
    Main function to demonstrate filtering products by brand names.
    """
    try:
        # Brands to filter by
        brands_to_filter = ["Porcelana Schmidt", "Bon Gourmet"]

        # Filter products
        filtered_products = filter_products_by_brand(PRODUCTS, brands_to_filter)

        # Pretty-print the filtered products as JSON
        print("Filtered Products:")
        print(json.dumps(filtered_products, indent=4))

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
