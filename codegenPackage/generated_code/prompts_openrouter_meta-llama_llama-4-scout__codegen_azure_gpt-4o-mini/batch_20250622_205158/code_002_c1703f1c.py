"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: "Write a Python code snippet to filter and sort products on an e-commerce website like Weavely, based on categories such as saree type, price, and design."
Generated: DETERMINISTIC_c1703f1c4f84d278
Batch ID: 20250622_205158
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
    """Class to represent a product in the e-commerce platform."""
    
    def __init__(self, name: str, category: str, price: float, design: str):
        self.name = name
        self.category = category
        self.price = price
        self.design = design

    def __repr__(self) -> str:
        return f"Product(name={self.name}, category={self.category}, price={self.price}, design={self.design})"

def filter_and_sort_products(products: List[Product], category: str = None, max_price: float = None, sort_by: str = 'price') -> List[Product]:
    """
    Filters and sorts a list of products based on specified criteria.

    Args:
        products (List[Product]): List of products to filter and sort.
        category (str, optional): Category to filter products by. Defaults to None.
        max_price (float, optional): Maximum price to filter products by. Defaults to None.
        sort_by (str): Attribute to sort products by. Can be 'price' or 'name'. Defaults to 'price'.

    Returns:
        List[Product]: Filtered and sorted list of products.

    Raises:
        ValueError: If sort_by is not 'price' or 'name'.
    """
    
    # Validate sort_by parameter
    if sort_by not in ['price', 'name']:
        raise ValueError("sort_by must be either 'price' or 'name'.")

    # Filter products based on category and max_price
    filtered_products = [
        product for product in products
        if (category is None or product.category == category) and
           (max_price is None or product.price <= max_price)
    ]

    # Sort products based on the specified attribute
    sorted_products = sorted(filtered_products, key=lambda x: getattr(x, sort_by))

    return sorted_products

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Silk Saree", "Saree", 5000, "Floral"),
        Product("Cotton Saree", "Saree", 2000, "Geometric"),
        Product("Designer Saree", "Saree", 8000, "Abstract"),
        Product("Linen Saree", "Saree", 3000, "Plain"),
        Product("Silk Dupatta", "Dupatta", 1500, "Embroidered"),
    ]

    try:
        # Filter and sort products
        filtered_sorted_products = filter_and_sort_products(products, category="Saree", max_price=6000, sort_by='price')
        print("Filtered and Sorted Products:")
        for product in filtered_sorted_products:
            print(product)
    except ValueError as e:
        print(f"Error: {e}")
```
