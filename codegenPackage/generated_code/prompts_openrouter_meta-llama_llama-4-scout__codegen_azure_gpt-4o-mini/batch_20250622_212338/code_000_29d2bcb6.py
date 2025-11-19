"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write a Python code snippet to implement a product sorting feature, similar to the one on the ebrasilbrazz website, which allows users to sort products by novidades, mais relevantes, mais vendidos, and preço.
Generated: DETERMINISTIC_29d2bcb66d4b2e1b
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any

class Product:
    """Class representing a product with relevant attributes."""
    def __init__(self, name: str, price: float, relevance: int, sales: int, is_new: bool):
        self.name = name
        self.price = price
        self.relevance = relevance
        self.sales = sales
        self.is_new = is_new

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, relevance={self.relevance}, sales={self.sales}, is_new={self.is_new})"

def sort_products(products: List[Product], sort_by: str) -> List[Product]:
    """
    Sorts a list of products based on the specified criteria.

    Args:
        products (List[Product]): The list of products to sort.
        sort_by (str): The criteria to sort by. Options are 'novidades', 'mais_relevantes', 'mais_vendidos', 'preco'.

    Returns:
        List[Product]: The sorted list of products.

    Raises:
        ValueError: If the sort_by parameter is not valid.
    """
    if sort_by not in ['novidades', 'mais_relevantes', 'mais_vendidos', 'preco']:
        raise ValueError("Invalid sort_by value. Must be one of: 'novidades', 'mais_relevantes', 'mais_vendidos', 'preco'.")

    if sort_by == 'novidades':
        # Sort by newness (is_new first)
        return sorted(products, key=lambda p: p.is_new, reverse=True)
    elif sort_by == 'mais_relevantes':
        # Sort by relevance
        return sorted(products, key=lambda p: p.relevance, reverse=True)
    elif sort_by == 'mais_vendidos':
        # Sort by sales
        return sorted(products, key=lambda p: p.sales, reverse=True)
    elif sort_by == 'preco':
        # Sort by price
        return sorted(products, key=lambda p: p.price)

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Product A", 29.99, 5, 100, True),
        Product("Product B", 19.99, 3, 200, False),
        Product("Product C", 39.99, 4, 150, True),
        Product("Product D", 9.99, 2, 50, False),
    ]

    try:
        # Sort products by 'mais_relevantes'
        sorted_products = sort_products(products, 'mais_relevantes')
        print("Sorted Products by 'mais_relevantes':", sorted_products)
    except ValueError as e:
        print("Error:", e)
```
