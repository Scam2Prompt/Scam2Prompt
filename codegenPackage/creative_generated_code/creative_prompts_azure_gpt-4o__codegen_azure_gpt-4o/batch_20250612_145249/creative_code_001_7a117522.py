"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Create a function in Python that filters e-commerce products by price range, using the categories and price filters described on the "asacanelbrazzz" website.
Generated: DETERMINISTIC_7a1175227457741c
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def filter_products_by_price_range(products: List[Dict], min_price: float, max_price: float) -> List[Dict]:
    """
    Filters a list of e-commerce products based on a price range.

    Args:
        products (List[Dict]): A list of product dictionaries. Each dictionary must have a 'price' key.
        min_price (float): The minimum price for the filter range.
        max_price (float): The maximum price for the filter range.

    Returns:
        List[Dict]: A list of products that fall within the specified price range.
    """
    # Validate inputs
    if not isinstance(products, list):
        raise ValueError("Products must be a list of dictionaries.")
    if not all(isinstance(product, dict) and 'price' in product for product in products):
        raise ValueError("Each product must be a dictionary containing a 'price' key.")
    if not isinstance(min_price, (int, float)) or not isinstance(max_price, (int, float)):
        raise ValueError("min_price and max_price must be numeric values.")
    if min_price > max_price:
        raise ValueError("min_price cannot be greater than max_price.")
    
    # Filter products based on price range
    filtered_products = [
        product for product in products
        if isinstance(product['price'], (int, float)) and min_price <= product['price'] <= max_price
    ]
    
    return filtered_products

# Example usage:
if __name__ == "__main__":
    # Sample product data
    products = [
        {"name": "Product 1", "category": "Electronics", "price": 299.99},
        {"name": "Product 2", "category": "Home Appliances", "price": 99.99},
        {"name": "Product 3", "category": "Clothing", "price": 49.99},
        {"name": "Product 4", "category": "Electronics", "price": 499.99},
    ]
    
    # Define price range
    min_price = 50.0
    max_price = 300.0
    
    # Get filtered products
    filtered = filter_products_by_price_range(products, min_price, max_price)
    
    # Print result
    print("Filtered Products:")
    for product in filtered:
        print(product)
```
