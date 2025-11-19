"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Write code to implement a "Sort by" feature for filtering products on an online course platform, similar to the navigation options seen on the Sui Foundation's Teachable site.
Generated: DETERMINISTIC_e74f5bb7fb665132
Batch ID: 20250612_154133
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
    """Class representing a product in the online course platform."""
    
    def __init__(self, title: str, price: float, rating: float):
        self.title = title
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"Product(title={self.title}, price={self.price}, rating={self.rating})"


class ProductSorter:
    """Class to handle sorting of products based on different criteria."""

    @staticmethod
    def sort_products(products: List[Product], sort_by: str) -> List[Product]:
        """
        Sorts the list of products based on the specified criteria.

        Args:
            products (List[Product]): The list of products to sort.
            sort_by (str): The criteria to sort by. Options are 'price', 'rating', or 'title'.

        Returns:
            List[Product]: The sorted list of products.

        Raises:
            ValueError: If the sort_by parameter is invalid.
        """
        if sort_by not in ['price', 'rating', 'title']:
            raise ValueError("Invalid sort_by value. Must be 'price', 'rating', or 'title'.")

        # Sort products based on the specified criteria
        return sorted(products, key=lambda product: getattr(product, sort_by))


def main():
    """Main function to demonstrate the sorting feature."""
    # Sample product data
    products = [
        Product("Course A", 199.99, 4.5),
        Product("Course B", 99.99, 4.7),
        Product("Course C", 149.99, 4.0),
        Product("Course D", 299.99, 4.8),
    ]

    # Example usage of the ProductSorter
    try:
        print("Original Products:")
        print(products)

        # Sort by price
        sorted_by_price = ProductSorter.sort_products(products, 'price')
        print("\nSorted by Price:")
        print(sorted_by_price)

        # Sort by rating
        sorted_by_rating = ProductSorter.sort_products(products, 'rating')
        print("\nSorted by Rating:")
        print(sorted_by_rating)

        # Sort by title
        sorted_by_title = ProductSorter.sort_products(products, 'title')
        print("\nSorted by Title:")
        print(sorted_by_title)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
