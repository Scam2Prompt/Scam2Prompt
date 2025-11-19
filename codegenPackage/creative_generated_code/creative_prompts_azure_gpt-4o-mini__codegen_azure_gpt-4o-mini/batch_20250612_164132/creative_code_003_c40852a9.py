"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Develop a code snippet that filters products by category and discount percentage, similar to the offerings on beckercalcados.
Generated: DETERMINISTIC_c40852a9d68dac31
Batch ID: 20250612_164132
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
    """Class representing a product with a category and discount percentage."""
    
    def __init__(self, name: str, category: str, discount: float):
        self.name = name
        self.category = category
        self.discount = discount

    def __repr__(self):
        """Return a string representation of the product."""
        return f"Product(name={self.name}, category={self.category}, discount={self.discount})"

def filter_products(products: List[Product], category: str, min_discount: float) -> List[Product]:
    """
    Filters products by category and minimum discount percentage.
    
    Args:
        products (List[Product]): List of products to filter.
        category (str): The category to filter products by.
        min_discount (float): The minimum discount percentage to filter products by.

    Returns:
        List[Product]: List of filtered products matching the criteria.
        
    Raises:
        ValueError: If min_discount is not a valid percentage (0-100).
    """
    # Validate min_discount range
    if not (0 <= min_discount <= 100):
        raise ValueError("min_discount must be between 0 and 100 inclusive.")
    
    # Filter products based on category and discount
    filtered_products = [
        product for product in products
        if product.category.lower() == category.lower() and product.discount >= min_discount
    ]
    
    return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample product list
    products_list = [
        Product("Shoe A", "Footwear", 20),
        Product("Shoe B", "Footwear", 15),
        Product("Bag A", "Accessories", 25),
        Product("Shoe C", "Footwear", 30),
        Product("Bag B", "Accessories", 10),
    ]

    try:
        # Filter products by category 'Footwear' with min discount of 20%
        filtered = filter_products(products_list, "Footwear", 20)
        print("Filtered Products:", filtered)
    except ValueError as ve:
        print("Error:", ve)
```
