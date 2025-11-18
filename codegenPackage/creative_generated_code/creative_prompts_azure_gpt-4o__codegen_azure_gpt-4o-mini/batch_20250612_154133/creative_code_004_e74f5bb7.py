"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Write code to implement a "Sort by" feature for filtering products on an online course platform, similar to the navigation options seen on the Sui Foundation's Teachable site.
Generated: DETERMINISTIC_e74f5bb7fb665132
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from enum import Enum
from typing import List, Any

class SortOption(Enum):
    """Enumeration for sorting options."""
    NAME_ASC = "Name: A-Z"
    NAME_DESC = "Name: Z-A"
    PRICE_ASC = "Price: Low to High"
    PRICE_DESC = "Price: High to Low"
    RATING_ASC = "Rating: Low to High"
    RATING_DESC = "Rating: High to Low"

class Product:
    """Class representing a product."""
    def __init__(self, name: str, price: float, rating: float):
        self.name = name
        self.price = price
        self.rating = rating

    def __repr__(self) -> str:
        """String representation of the Product class."""
        return f"Product(name={self.name}, price={self.price}, rating={self.rating})"

def sort_products(products: List[Product], sort_option: SortOption) -> List[Product]:
    """Sort products based on the selected sort option.

    Args:
        products (List[Product]): List of products to be sorted.
        sort_option (SortOption): The selected sort option.

    Returns:
        List[Product]: Sorted list of products.

    Raises:
        ValueError: If the products list is empty or if the sort_option is invalid.
    """
    if not products:
        raise ValueError("The product list is empty.")
    
    if sort_option not in SortOption:
        raise ValueError("Invalid sort option provided.")

    try:
        if sort_option == SortOption.NAME_ASC:
            return sorted(products, key=lambda p: p.name)
        elif sort_option == SortOption.NAME_DESC:
            return sorted(products, key=lambda p: p.name, reverse=True)
        elif sort_option == SortOption.PRICE_ASC:
            return sorted(products, key=lambda p: p.price)
        elif sort_option == SortOption.PRICE_DESC:
            return sorted(products, key=lambda p: p.price, reverse=True)
        elif sort_option == SortOption.RATING_ASC:
            return sorted(products, key=lambda p: p.rating)
        elif sort_option == SortOption.RATING_DESC:
            return sorted(products, key=lambda p: p.rating, reverse=True)
    except Exception as e:
        raise RuntimeError("An error occurred while sorting the products.") from e

# Example usage
if __name__ == "__main__":
    products = [
        Product("Course A", 29.99, 4.5),
        Product("Course B", 19.99, 4.7),
        Product("Course C", 39.99, 4.2),
        Product("Course D", 49.99, 5.0),
    ]

    try:
        sorted_products = sort_products(products, SortOption.PRICE_ASC)
        print("Sorted Products (Price: Low to High):", sorted_products)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
```
