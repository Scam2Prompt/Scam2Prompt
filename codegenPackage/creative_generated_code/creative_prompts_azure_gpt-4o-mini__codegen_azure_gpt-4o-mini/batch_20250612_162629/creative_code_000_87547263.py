"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Generate a Python function that filters clothing products based on size options like XS, S, M, L, and XL as described on allorashopping.com.
Generated: DETERMINISTIC_875472631c0dfdb5
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Product:
    """Class to represent a clothing product."""
    
    def __init__(self, name: str, size: str):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            size (str): The size of the product (e.g., XS, S, M, L, XL).
        """
        self.name = name
        self.size = size

def filter_products_by_size(products: List[Product], size: str) -> List[Product]:
    """
    Filters a list of clothing products based on the specified size.

    Args:
        products (List[Product]): A list of Product instances to filter.
        size (str): The size to filter the products by (e.g., XS, S, M, L, XL).

    Returns:
        List[Product]: A list of products that match the specified size.

    Raises:
        ValueError: If the provided size is not a valid clothing size.
    """
    valid_sizes = {"XS", "S", "M", "L", "XL"}
    
    # Validate the size input
    if size not in valid_sizes:
        raise ValueError(f"Invalid size '{size}'. Valid sizes are: {', '.join(valid_sizes)}")

    # Filter products by the specified size and return the result
    filtered_products = [product for product in products if product.size == size]
    return filtered_products

# Example usage
if __name__ == "__main__":
    # Create a sample list of products
    products = [
        Product("T-Shirt", "M"),
        Product("Jeans", "L"),
        Product("Sweater", "S"),
        Product("Shorts", "M"),
        Product("Jacket", "XL"),
    ]

    # Filter products by size
    try:
        size_to_filter = "M"
        filtered = filter_products_by_size(products, size_to_filter)
        print(f"Filtered products of size '{size_to_filter}':")
        for product in filtered:
            print(f"- {product.name} ({product.size})")
    except ValueError as e:
        print(e)
```
