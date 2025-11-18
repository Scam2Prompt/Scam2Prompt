"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1iiinch.teachable.com
Prompt: Provide a script to filter and sort products on an online course platform like Teachable, even when no products are currently listed.
Generated: DETERMINISTIC_674ea6e9b1ccb392
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to filter and sort products on an online course platform.
Even if no products are listed, the script handles the scenario gracefully.

Requirements:
1. Filter products by category and price range.
2. Sort products by price or title, in ascending or descending order.
3. Return an empty list if no products are available.

Author: Expert Programmer
"""

from typing import List, Dict, Optional


def filter_and_sort_products(
    products: List[Dict],
    category: Optional[str] = None,
    price_range: Optional[tuple] = None,
    sort_by: str = "price",
    sort_order: str = "asc"
) -> List[Dict]:
    """
    Filters and sorts a list of products based on the given criteria.

    Args:
        products (List[Dict]): List of product dictionaries.
        category (Optional[str]): Filter products by category. Default is None (no filter).
        price_range (Optional[tuple]): Tuple (min_price, max_price) to filter by price range. Default is None (no filter).
        sort_by (str): Attribute to sort by ('price' or 'title'). Default is 'price'.
        sort_order (str): Order to sort ('asc' for ascending, 'desc' for descending). Default is 'asc'.

    Returns:
        List[Dict]: A filtered and sorted list of products.
    """
    
    # Sanity checks for inputs
    if sort_by not in {"price", "title"}:
        raise ValueError("Invalid sort_by value. Must be 'price' or 'title'.")
    if sort_order not in {"asc", "desc"}:
        raise ValueError("Invalid sort_order value. Must be 'asc' or 'desc'.")
    
    # Handle edge case: Empty products list
    if not products:
        return []

    # Filter products by category if provided
    if category:
        products = [product for product in products if product.get("category") == category]

    # Filter products by price range if provided
    if price_range:
        min_price, max_price = price_range
        products = [
            product for product in products
            if min_price <= product.get("price", 0) <= max_price
        ]

    # Sort products by the specified attribute
    reverse = True if sort_order == "desc" else False
    products = sorted(products, key=lambda x: x.get(sort_by, ""), reverse=reverse)

    return products


# Example usage
if __name__ == "__main__":
    # Example list of products
    example_products = [
        {"title": "Python Basics", "price": 50, "category": "Programming"},
        {"title": "Advanced Python", "price": 75, "category": "Programming"},
        {"title": "UI/UX Design", "price": 30, "category": "Design"},
    ]

    # Filtering and sorting products
    filtered_sorted_products = filter_and_sort_products(
        example_products,
        category="Programming",
        price_range=(40, 80),
        sort_by="price",
        sort_order="asc"
    )

    print("Filtered and Sorted Products:")
    print(filtered_sorted_products)
```
