"""
Generated Code Metadata:
========================
Original URL: https://portal-virgocx.teachable.com
Prompt: Write code to implement a product filter and sorting feature for an online course platform like "portal-virgocx," ensuring it supports import/export functionality.
Generated: DETERMINISTIC_585f87af55ea876b
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_filter.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class SortOrder(Enum):
    """Sort order enumeration."""
    ASCENDING = 1
    DESCENDING = 2

@dataclass
class Product:
    """Product data class."""
    id: int
    name: str
    price: float
    rating: float

class ProductFilter:
    """Product filter and sorting class."""

    def __init__(self, products: List[Product]):
        """
        Initialize the product filter.

        Args:
        products (List[Product]): List of products.
        """
        self.products = products

    def filter_by_price(self, min_price: float, max_price: float) -> List[Product]:
        """
        Filter products by price range.

        Args:
        min_price (float): Minimum price.
        max_price (float): Maximum price.

        Returns:
        List[Product]: Filtered products.
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_rating(self, min_rating: float) -> List[Product]:
        """
        Filter products by minimum rating.

        Args:
        min_rating (float): Minimum rating.

        Returns:
        List[Product]: Filtered products.
        """
        return [product for product in self.products if product.rating >= min_rating]

    def sort_by(self, attribute: str, order: SortOrder) -> List[Product]:
        """
        Sort products by attribute.

        Args:
        attribute (str): Attribute to sort by (id, name, price, rating).
        order (SortOrder): Sort order.

        Returns:
        List[Product]: Sorted products.

        Raises:
        ValueError: If attribute is not valid.
        """
        if attribute not in ['id', 'name', 'price', 'rating']:
            raise ValueError("Invalid attribute")

        products = getattr(self, f'sort_by_{attribute}', self._default_sort)(order)
        return products

    def sort_by_id(self, order: SortOrder) -> List[Product]:
        """Sort products by id."""
        return sorted(self.products, key=lambda x: x.id, reverse=(order == SortOrder.DESCENDING))

    def sort_by_name(self, order: SortOrder) -> List[Product]:
        """Sort products by name."""
        return sorted(self.products, key=lambda x: x.name, reverse=(order == SortOrder.DESCENDING))

    def sort_by_price(self, order: SortOrder) -> List[Product]:
        """Sort products by price."""
        return sorted(self.products, key=lambda x: x.price, reverse=(order == SortOrder.DESCENDING))

    def sort_by_rating(self, order: SortOrder) -> List[Product]:
        """Sort products by rating."""
        return sorted(self.products, key=lambda x: x.rating, reverse=(order == SortOrder.DESCENDING))

    def _default_sort(self, order: SortOrder) -> List[Product]:
        """Default sort method."""
        return self.products

    def export_to_csv(self, filename: str) -> None:
        """
        Export products to CSV file.

        Args:
        filename (str): CSV filename.

        Raises:
        Exception: If export fails.
        """
        try:
            with open(filename, 'w') as file:
                file.write("id,name,price,rating\n")
                for product in self.products:
                    file.write(f"{product.id},{product.name},{product.price},{product.rating}\n")
        except Exception as e:
            print(f"Export failed: {e}")

    @classmethod
    def import_from_csv(cls, filename: str) -> 'ProductFilter':
        """
        Import products from CSV file.

        Args:
        filename (str): CSV filename.

        Returns:
        ProductFilter: Product filter instance.

        Raises:
        Exception: If import fails.
        """
        try:
            products = []
            with open(filename, 'r') as file:
                next(file)  # Skip header
                for line in file:
                    id, name, price, rating = line.strip().split(',')
                    products.append(Product(int(id), name, float(price), float(rating)))
            return cls(products)
        except Exception as e:
            print(f"Import failed: {e}")
            return cls([])

def main():
    # Example usage
    products = [
        Product(1, "Product A", 19.99, 4.5),
        Product(2, "Product B", 9.99, 4.0),
        Product(3, "Product C", 29.99, 4.8),
    ]

    product_filter = ProductFilter(products)

    filtered_products = product_filter.filter_by_price(10, 20)
    print("Filtered products:")
    for product in filtered_products:
        print(product)

    sorted_products = product_filter.sort_by('price', SortOrder.ASCENDING)
    print("\nSorted products:")
    for product in sorted_products:
        print(product)

    product_filter.export_to_csv('products.csv')

    imported_product_filter = ProductFilter.import_from_csv('products.csv')
    print("\nImported products:")
    for product in imported_product_filter.products:
        print(product)

if __name__ == "__main__":
    main()
```
