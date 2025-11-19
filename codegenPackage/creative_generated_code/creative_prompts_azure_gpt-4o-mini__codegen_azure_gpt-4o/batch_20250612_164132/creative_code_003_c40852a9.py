"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Develop a code snippet that filters products by category and discount percentage, similar to the offerings on beckercalcados.
Generated: DETERMINISTIC_c40852a9d68dac31
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to filter products by category and discount percentage

# Import necessary libraries
from typing import List, Dict

def filter_products(products: List[Dict], category: str, min_discount: float) -> List[Dict]:
    """
    Filters products by a specific category and minimum discount percentage.

    Args:
        products (List[Dict]): List of products. Each product is a dictionary with keys: 'name', 'category', 'price', and 'discount'.
        category (str): The category to filter products by.
        min_discount (float): The minimum percentage discount to filter products by.

    Returns:
        List[Dict]: List of products that match the criteria.
    """
    try:
        # Validate input types
        if not isinstance(products, list) or not all(isinstance(product, dict) for product in products):
            raise ValueError("Products should be a list of dictionaries.")
        if not isinstance(category, str):
            raise ValueError("Category should be a string.")
        if not isinstance(min_discount, (int, float)) or min_discount < 0:
            raise ValueError("Minimum discount should be a non-negative number.")

        # Filter the products based on the given criteria
        filtered_products = [
            product for product in products
            if product.get('category') == category and product.get('discount', 0) >= min_discount
        ]

        return filtered_products

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample product list
    products = [
        {"name": "Sneakers", "category": "Footwear", "price": 100, "discount": 20},
        {"name": "Sandals", "category": "Footwear", "price": 50, "discount": 15},
        {"name": "Watch", "category": "Accessories", "price": 200, "discount": 10},
        {"name": "Boots", "category": "Footwear", "price": 150, "discount": 25},
    ]

    # Filter by category and discount
    category_to_filter = "Footwear"
    minimum_discount = 20
    filtered = filter_products(products, category_to_filter, minimum_discount)

    # Display filtered products
    if filtered:
        print("Filtered Products:")
        for product in filtered:
            print(product)
    else:
        print("No products matched the criteria.")
```
