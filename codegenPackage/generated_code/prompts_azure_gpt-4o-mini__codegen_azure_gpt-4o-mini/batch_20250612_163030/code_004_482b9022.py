"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Develop a code example that filters a list of Milly Mally products to show only those categorized as "zabawki edukacyjne" and "akcesoria niemowlęce."
Generated: DETERMINISTIC_482b9022e0075232
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

def filter_products(products: List[Dict[str, str]], categories: List[str]) -> List[Dict[str, str]]:
    """
    Filters a list of products to include only those that belong to specified categories.

    Args:
        products (List[Dict[str, str]]): A list of product dictionaries, where each dictionary contains product details.
        categories (List[str]): A list of categories to filter the products by.

    Returns:
        List[Dict[str, str]]: A list of products that belong to the specified categories.
    """
    if not isinstance(products, list) or not isinstance(categories, list):
        raise ValueError("Both products and categories must be lists.")

    filtered_products = []
    
    for product in products:
        # Check if the product has a 'category' key
        if 'category' not in product:
            raise KeyError("Each product must have a 'category' key.")
        
        # Check if the product's category is in the specified categories
        if product['category'] in categories:
            filtered_products.append(product)

    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample list of Milly Mally products
    milly_mally_products = [
        {"name": "Klocki edukacyjne", "category": "zabawki edukacyjne"},
        {"name": "Smycz dla niemowlaka", "category": "akcesoria niemowlęce"},
        {"name": "Zabawka interaktywna", "category": "zabawki"},
        {"name": "Poduszka do karmienia", "category": "akcesoria niemowlęce"},
        {"name": "Puzzle", "category": "zabawki edukacyjne"},
    ]

    # Categories to filter by
    categories_to_filter = ["zabawki edukacyjne", "akcesoria niemowlęce"]

    try:
        # Filter products
        filtered = filter_products(milly_mally_products, categories_to_filter)
        print("Filtered Products:", filtered)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
