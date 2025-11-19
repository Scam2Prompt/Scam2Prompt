"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Develop a code snippet that filters products by category and discount percentage, similar to the offerings on beckercalcados.
Generated: DETERMINISTIC_c40852a9d68dac31
Batch ID: 20250612_164132
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
    """Class representing a product with a category and discount percentage."""
    
    def __init__(self, name: str, category: str, discount_percentage: float):
        self.name = name
        self.category = category
        self.discount_percentage = discount_percentage

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category}, discount_percentage={self.discount_percentage})"

def filter_products(products: List[Product], category: str, min_discount: float) -> List[Product]:
    """
    Filters the list of products by category and minimum discount percentage.

    Args:
        products (List[Product]): The list of products to filter.
        category (str): The category to filter by.
        min_discount (float): The minimum discount percentage to filter by.

    Returns:
        List[Product]: A list of products that match the criteria.
    """
    if min_discount < 0:
        raise ValueError("Minimum discount percentage cannot be negative.")
    
    filtered_products = [
        product for product in products 
        if product.category == category and product.discount_percentage >= min_discount
    ]
    
    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Sneakers", "Footwear", 20.0),
        Product("Sandals", "Footwear", 15.0),
        Product("Boots", "Footwear", 30.0),
        Product("T-shirt", "Apparel", 10.0),
        Product("Jeans", "Apparel", 25.0),
    ]

    try:
        # Filter products in the 'Footwear' category with at least 20% discount
        filtered = filter_products(products, "Footwear", 20.0)
        print("Filtered Products:", filtered)
    except ValueError as e:
        print("Error:", e)
```
