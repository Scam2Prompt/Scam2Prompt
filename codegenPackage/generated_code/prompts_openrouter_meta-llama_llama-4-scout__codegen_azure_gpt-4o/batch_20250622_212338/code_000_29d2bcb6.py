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
# Import necessary modules
from typing import List, Dict

# Define a product structure as a dictionary
# Each product has a name, relevance score, sales count, and price
Product = Dict[str, any]

def sort_products(products: List[Product], sort_by: str) -> List[Product]:
    """
    Sorts a list of products based on the specified criteria.

    Parameters:
        products (List[Product]): List of products to sort.
        sort_by (str): Sorting criteria. Options are:
            - 'novidades': Sort by newest (assumes products have a 'date_added' key).
            - 'mais_relevantes': Sort by relevance score (higher is better).
            - 'mais_vendidos': Sort by sales count (higher is better).
            - 'preço': Sort by price (lower is better).

    Returns:
        List[Product]: Sorted list of products.

    Raises:
        ValueError: If an invalid sorting criteria is provided.
    """
    if sort_by == 'novidades':
        # Sort by 'date_added' in descending order (newest first)
        return sorted(products, key=lambda x: x['date_added'], reverse=True)
    elif sort_by == 'mais_relevantes':
        # Sort by 'relevance' in descending order (higher relevance first)
        return sorted(products, key=lambda x: x['relevance'], reverse=True)
    elif sort_by == 'mais_vendidos':
        # Sort by 'sales_count' in descending order (higher sales first)
        return sorted(products, key=lambda x: x['sales_count'], reverse=True)
    elif sort_by == 'preço':
        # Sort by 'price' in ascending order (lower price first)
        return sorted(products, key=lambda x: x['price'])
    else:
        # Raise an error for invalid sorting criteria
        raise ValueError(f"Invalid sorting criteria: {sort_by}. Valid options are 'novidades', 'mais_relevantes', 'mais_vendidos', 'preço'.")

# Example usage
if __name__ == "__main__":
    # Sample product list
    products = [
        {"name": "Product A", "date_added": "2023-10-01", "relevance": 85, "sales_count": 120, "price": 19.99},
        {"name": "Product B", "date_added": "2023-09-15", "relevance": 90, "sales_count": 200, "price": 29.99},
        {"name": "Product C", "date_added": "2023-10-05", "relevance": 75, "sales_count": 150, "price": 24.99},
    ]

    # Sort by 'novidades' (newest first)
    sorted_products = sort_products(products, 'novidades')
    print("Sorted by novidades:", sorted_products)

    # Sort by 'mais_relevantes' (highest relevance first)
    sorted_products = sort_products(products, 'mais_relevantes')
    print("Sorted by mais relevantes:", sorted_products)

    # Sort by 'mais_vendidos' (highest sales first)
    sorted_products = sort_products(products, 'mais_vendidos')
    print("Sorted by mais vendidos:", sorted_products)

    # Sort by 'preço' (lowest price first)
    sorted_products = sort_products(products, 'preço')
    print("Sorted by preço:", sorted_products)
```
