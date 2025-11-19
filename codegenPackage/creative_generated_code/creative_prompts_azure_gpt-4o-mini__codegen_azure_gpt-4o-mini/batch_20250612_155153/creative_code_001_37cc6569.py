"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Write a function that filters a product list based on categories such as kerti gépek and lámpák, returning only the relevant items.
Generated: DETERMINISTIC_37cc656990b3fe93
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def filter_products_by_category(products: List[Dict[str, str]], categories: List[str]) -> List[Dict[str, str]]:
    """
    Filters a list of products based on specified categories.

    Args:
        products (List[Dict[str, str]]): A list of product dictionaries, where each dictionary contains product details.
        categories (List[str]): A list of categories to filter products by.

    Returns:
        List[Dict[str, str]]: A list of products that belong to the specified categories.

    Raises:
        ValueError: If the products list is empty or categories list is empty.
    """
    
    # Validate input
    if not products:
        raise ValueError("The products list cannot be empty.")
    if not categories:
        raise ValueError("The categories list cannot be empty.")

    # Filter products based on the specified categories
    filtered_products = [
        product for product in products
        if product.get('category') in categories
    ]
    
    return filtered_products

# Example usage:
if __name__ == "__main__":
    # Sample product list
    products_list = [
        {'name': 'Trimmer', 'category': 'kerti gépek'},
        {'name': 'LED Lamp', 'category': 'lámpák'},
        {'name': 'Lawn Mower', 'category': 'kerti gépek'},
        {'name': 'Desk Lamp', 'category': 'lámpák'},
        {'name': 'Hammer', 'category': 'tools'}
    ]
    
    # Categories to filter by
    categories_to_filter = ['kerti gépek', 'lámpák']

    try:
        filtered = filter_products_by_category(products_list, categories_to_filter)
        print("Filtered Products:", filtered)
    except ValueError as e:
        print("Error:", e)
```
