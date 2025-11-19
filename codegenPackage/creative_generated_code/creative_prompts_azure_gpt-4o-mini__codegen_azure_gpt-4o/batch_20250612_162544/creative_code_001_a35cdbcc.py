"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a Python function that filters products based on price and category, similar to the features on asacanelbrazzz.
Generated: DETERMINISTIC_a35cdbcc087210ee
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict


def filter_products(products: List[Dict], min_price: float = None, max_price: float = None, category: str = None) -> List[Dict]:
    """
    Filters a list of products based on price range and category.

    Args:
        products (List[Dict]): A list of products where each product is a dictionary containing keys like 'price' and 'category'.
        min_price (float, optional): The minimum price for filtering products. Defaults to None.
        max_price (float, optional): The maximum price for filtering products. Defaults to None.
        category (str, optional): The category to filter products by. Defaults to None.

    Returns:
        List[Dict]: A list of products that match the filtering criteria.
    """
    # Validate input arguments
    if min_price is not None and min_price < 0:
        raise ValueError("min_price cannot be negative")
    if max_price is not None and max_price < 0:
        raise ValueError("max_price cannot be negative")
    if min_price is not None and max_price is not None and min_price > max_price:
        raise ValueError("min_price cannot be greater than max_price")

    # Apply filters
    filtered_products = []
    for product in products:
        try:
            # Extract product details
            price = product.get('price')
            product_category = product.get('category')

            # Skip products with missing required fields
            if price is None or product_category is None:
                continue

            # Check price and category filters
            if min_price is not None and price < min_price:
                continue
            if max_price is not None and price > max_price:
                continue
            if category is not None and product_category.lower() != category.lower():
                continue

            # Product matches all filters; add to result
            filtered_products.append(product)

        except Exception as e:
            # Log or handle unexpected errors (placeholder for real logging)
            print(f"Error processing product {product}: {e}")
            continue

    return filtered_products


# Example usage
if __name__ == "__main__":
    # Product list example
    products = [
        {"name": "Laptop", "price": 1500, "category": "electronics"},
        {"name": "Smartphone", "price": 800, "category": "electronics"},
        {"name": "Sofa", "price": 1200, "category": "furniture"},
        {"name": "Desk", "price": 300, "category": "furniture"},
        {"name": "Headphones", "price": 200, "category": "electronics"},
    ]

    # Filtering products
    filtered = filter_products(products, min_price=500, max_price=1000, category="electronics")
    print(filtered)
```
