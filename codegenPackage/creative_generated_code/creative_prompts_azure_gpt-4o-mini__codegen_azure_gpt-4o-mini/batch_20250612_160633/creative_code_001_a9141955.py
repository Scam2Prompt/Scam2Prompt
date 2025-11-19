"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Write a function that filters a list of dining products based on categories such as "Mesa Posta" and "Acessórios para servir," inspired by the offerings on the Camicado website.
Generated: DETERMINISTIC_a9141955e0dca26e
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def filter_dining_products(products: List[Dict[str, str]], categories: List[str]) -> List[Dict[str, str]]:
    """
    Filters a list of dining products based on specified categories.

    Args:
        products (List[Dict[str, str]]): A list of products where each product is a dictionary
                                           containing product details including a 'category' key.
        categories (List[str]): A list of categories to filter the products by.

    Returns:
        List[Dict[str, str]]: A list of products that belong to the specified categories.

    Raises:
        ValueError: If the input products or categories are not in the expected format.
    """
    
    # Validate input types
    if not isinstance(products, list) or not isinstance(categories, list):
        raise ValueError("Both products and categories must be lists.")
    
    if not all(isinstance(product, dict) for product in products):
        raise ValueError("Each product must be a dictionary.")
    
    # Filter products based on categories
    filtered_products = []
    
    for product in products:
        # Check if category exists in product and is valid
        if 'category' in product and product['category'] in categories:
            filtered_products.append(product)

    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample list of dining products
    dining_products = [
        {'name': 'Dinner Plate', 'category': 'Mesa Posta'},
        {'name': 'Serving Spoon', 'category': 'Acessórios para servir'},
        {'name': 'Salad Bowl', 'category': 'Mesa Posta'},
        {'name': 'Table Cloth', 'category': 'Decoração'},
    ]
    
    # Categories to filter
    desired_categories = ['Mesa Posta', 'Acessórios para servir']
    
    try:
        # Filter the dining products
        filtered = filter_dining_products(dining_products, desired_categories)
        print("Filtered Products:", filtered)
    except ValueError as e:
        print("Error:", e)
```
