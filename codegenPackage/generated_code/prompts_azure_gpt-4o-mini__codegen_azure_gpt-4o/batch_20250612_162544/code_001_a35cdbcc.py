"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a Python function that filters products based on price and category, similar to the features on asacanelbrazzz.
Generated: DETERMINISTIC_a35cdbcc087210ee
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

def filter_products(products: List[Dict], min_price: float = 0.0, max_price: float = float('inf'), category: str = None) -> List[Dict]:
    """
    Filters a list of products based on price range and category.

    Args:
        products (List[Dict]): A list of product dictionaries. Each dictionary should contain 'price' and 'category' keys.
        min_price (float): Minimum price for filtering. Default is 0.0.
        max_price (float): Maximum price for filtering. Default is infinity.
        category (str): Category to filter by. If None, category filtering is ignored. Default is None.

    Returns:
        List[Dict]: A list of filtered product dictionaries.
    """
    # Validate input types
    if not isinstance(products, list):
        raise ValueError("The 'products' parameter must be a list of dictionaries.")
    if not all(isinstance(product, dict) for product in products):
        raise ValueError("Each item in the 'products' list must be a dictionary.")
    if not isinstance(min_price, (int, float)) or not isinstance(max_price, (int, float)):
        raise ValueError("The 'min_price' and 'max_price' parameters must be numeric.")
    if category is not None and not isinstance(category, str):
        raise ValueError("The 'category' parameter must be a string or None.")

    # Filter products based on price and category
    filtered_products = [
        product for product in products
        if min_price <= product.get('price', 0) <= max_price and
           (category is None or product.get('category') == category)
    ]

    return filtered_products

# Example usage:
if __name__ == "__main__":
    # Sample product list
    sample_products = [
        {"name": "Product A", "price": 25.0, "category": "Electronics"},
        {"name": "Product B", "price": 15.0, "category": "Books"},
        {"name": "Product C", "price": 50.0, "category": "Electronics"},
        {"name": "Product D", "price": 10.0, "category": "Books"},
    ]

    # Filter products with price between 10 and 30 in the "Books" category
    filtered = filter_products(sample_products, min_price=10, max_price=30, category="Books")
    print(filtered)
```
