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
from enum import Enum
from typing import List, Dict

class SortByOptions(Enum):
    """Enum for sort by options"""
    PRICE_LOW_TO_HIGH = 1
    PRICE_HIGH_TO_LOW = 2
    ALPHABETICAL = 3
    NEWEST = 4
    POPULAR = 5

class Product:
    """Class representing a product"""
    def __init__(self, id: int, name: str, price: float, created_at: str, popularity: int):
        self.id = id
        self.name = name
        self.price = price
        self.created_at = created_at
        self.popularity = popularity

class ProductSorter:
    """Class for sorting products"""
    def __init__(self, products: List[Product]):
        self.products = products

    def sort_by(self, option: SortByOptions) -> List[Product]:
        """Sort products by given option"""
        if option == SortByOptions.PRICE_LOW_TO_HIGH:
            return sorted(self.products, key=lambda x: x.price)
        elif option == SortByOptions.PRICE_HIGH_TO_LOW:
            return sorted(self.products, key=lambda x: x.price, reverse=True)
        elif option == SortByOptions.ALPHABETICAL:
            return sorted(self.products, key=lambda x: x.name)
        elif option == SortByOptions.NEWEST:
            return sorted(self.products, key=lambda x: x.created_at, reverse=True)
        elif option == SortByOptions.POPULAR:
            return sorted(self.products, key=lambda x: x.popularity, reverse=True)
        else:
            raise ValueError("Invalid sort by option")

def main():
    try:
        # Example products
        products = [
            Product(1, "Product A", 10.99, "2022-01-01", 100),
            Product(2, "Product B", 5.99, "2022-01-15", 50),
            Product(3, "Product C", 7.99, "2022-01-10", 200),
        ]

        # Create product sorter
        product_sorter = ProductSorter(products)

        # Sort by price low to high
        sorted_products = product_sorter.sort_by(SortByOptions.PRICE_LOW_TO_HIGH)
        print("Sorted by price low to high:")
        for product in sorted_products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")

        # Sort by alphabetical
        sorted_products = product_sorter.sort_by(SortByOptions.ALPHABETICAL)
        print("\nSorted by alphabetical:")
        for product in sorted_products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
