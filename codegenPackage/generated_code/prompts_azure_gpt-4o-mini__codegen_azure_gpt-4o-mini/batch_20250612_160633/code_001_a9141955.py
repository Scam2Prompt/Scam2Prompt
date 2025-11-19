"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Write a function that filters a list of dining products based on categories such as "Mesa Posta" and "Acessórios para servir," inspired by the offerings on the Camicado website.
Generated: DETERMINISTIC_a9141955e0dca26e
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

def filter_dining_products(products: List[Dict[str, str]], categories: List[str]) -> List[Dict[str, str]]:
    """
    Filters a list of dining products based on specified categories.

    Args:
        products (List[Dict[str, str]]): A list of product dictionaries, where each dictionary contains product details.
        categories (List[str]): A list of categories to filter the products by.

    Returns:
        List[Dict[str, str]]: A list of products that belong to the specified categories.

    Raises:
        ValueError: If the input products list is empty or categories list is empty.
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

# Example usage
if __name__ == "__main__":
    # Sample product data
    dining_products = [
        {"name": "Mesa Posta Elegante", "category": "Mesa Posta"},
        {"name": "Conjunto de Talheres", "category": "Acessórios para servir"},
        {"name": "Prato de Cerâmica", "category": "Mesa Posta"},
        {"name": "Copo de Vidro", "category": "Acessórios para servir"},
        {"name": "Toalha de Mesa", "category": "Decoração"},
    ]

    # Categories to filter
    categories_to_filter = ["Mesa Posta", "Acessórios para servir"]

    # Get filtered products
    try:
        filtered = filter_dining_products(dining_products, categories_to_filter)
        print("Filtered Products:", filtered)
    except ValueError as e:
        print("Error:", e)
```
