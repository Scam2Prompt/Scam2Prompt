"""
Generated Code Metadata:
========================
Original URL: https://alsafwaq8.com
Prompt: "Write a code snippet for filtering and sorting products by size and price on an e-commerce website, similar to the layout and functionality seen on الصفوة للملابس الجاهزة for their men's winter dishdashas."
Generated: DETERMINISTIC_ff2ba3f22619dd97
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Product:
    """Class representing a product in the e-commerce store."""
    
    def __init__(self, name: str, size: str, price: float):
        self.name = name
        self.size = size
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, size={self.size}, price={self.price})"

def filter_and_sort_products(products: List[Product], size_filter: str, sort_by: str = 'price', ascending: bool = True) -> List[Product]:
    """
    Filters and sorts a list of products by size and price.

    Args:
        products (List[Product]): List of products to filter and sort.
        size_filter (str): The size to filter products by.
        sort_by (str): The attribute to sort by ('price' or 'name').
        ascending (bool): Sort order; True for ascending, False for descending.

    Returns:
        List[Product]: Filtered and sorted list of products.

    Raises:
        ValueError: If sort_by is not 'price' or 'name'.
    """
    
    # Validate sort_by parameter
    if sort_by not in ['price', 'name']:
        raise ValueError("sort_by must be either 'price' or 'name'.")

    # Filter products by size
    filtered_products = [product for product in products if product.size == size_filter]

    # Sort products based on the specified attribute
    sorted_products = sorted(filtered_products, key=lambda x: getattr(x, sort_by), reverse=not ascending)

    return sorted_products

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Winter Dishdasha A", "L", 150.0),
        Product("Winter Dishdasha B", "M", 120.0),
        Product("Winter Dishdasha C", "L", 130.0),
        Product("Winter Dishdasha D", "S", 110.0),
    ]

    try:
        # Filter and sort products by size 'L' and price in ascending order
        filtered_sorted_products = filter_and_sort_products(products, size_filter='L', sort_by='price', ascending=True)
        print("Filtered and Sorted Products:", filtered_sorted_products)
    except ValueError as e:
        print("Error:", e)
```
