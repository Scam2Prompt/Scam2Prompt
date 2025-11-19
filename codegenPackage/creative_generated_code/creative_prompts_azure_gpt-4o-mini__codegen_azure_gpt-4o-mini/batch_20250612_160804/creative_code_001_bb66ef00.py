"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo-8g2.pages.dev
Prompt: Write a function to filter products by size (Large, Medium, Small) in a shopping cart application, inspired by the filtering options available on the T-Shirt Store.
Generated: DETERMINISTIC_bb66ef00f1bc0632
Batch ID: 20250612_160804
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
    """Class to represent a product in the shopping cart."""
    
    def __init__(self, name: str, size: str):
        """
        Initialize a product with a name and size.
        
        Args:
            name (str): The name of the product.
            size (str): The size of the product (e.g., 'Small', 'Medium', 'Large').
        """
        self.name = name
        self.size = size

def filter_products_by_size(products: List[Product], size: str) -> List[Product]:
    """
    Filters a list of products by the specified size.
    
    Args:
        products (List[Product]): The list of products to filter.
        size (str): The size to filter products by (e.g., 'Small', 'Medium', 'Large').
    
    Returns:
        List[Product]: A list of products that match the specified size.
    
    Raises:
        ValueError: If the size is not one of the allowed options.
    """
    # Define allowed sizes for validation
    allowed_sizes = {'Small', 'Medium', 'Large'}
    
    # Validate the input size
    if size not in allowed_sizes:
        raise ValueError(f"Invalid size '{size}'. Allowed sizes are: {allowed_sizes}")

    # Filter products by size
    filtered_products = [product for product in products if product.size == size]
    
    return filtered_products

# Example usage
if __name__ == "__main__":
    # Create a list of products
    products = [
        Product("T-Shirt A", "Small"),
        Product("T-Shirt B", "Medium"),
        Product("T-Shirt C", "Large"),
        Product("T-Shirt D", "Small"),
        Product("T-Shirt E", "Large"),
    ]

    try:
        # Filter products by size 'Small'
        small_products = filter_products_by_size(products, 'Small')
        print(f"Filtered Products (Small): {[product.name for product in small_products]}")

        # Filter products by size 'Large'
        large_products = filter_products_by_size(products, 'Large')
        print(f"Filtered Products (Large): {[product.name for product in large_products]}")
        
        # Attempt to filter with an invalid size
        invalid_products = filter_products_by_size(products, 'Extra Large')
    
    except ValueError as e:
        print(f"Error: {e}")
```
