"""
Generated Code Metadata:
========================
Original URL: https://help-virgocx.teachable.com
Prompt: Provide code examples for filtering and sorting products in a web application, similar to the "Product filters: Sort by: import_export" functionality mentioned on the Metamask Help page.
Generated: DETERMINISTIC_1a3af9530c8d649e
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Product Filter and Sorter**
==========================

### Product Model

```python
# models/product.py

class Product:
    def __init__(self, id, name, price, category):
        """
        Initialize a Product object.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            category (str): Product category.
        """
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"
```

### Product Filter and Sorter Class

```python
# services/product_filter_sorter.py

from typing import List
from models.product import Product

class ProductFilterSorter:
    def __init__(self, products: List[Product]):
        """
        Initialize a ProductFilterSorter object.

        Args:
            products (List[Product]): List of Product objects.
        """
        self.products = products

    def filter_by_category(self, category: str) -> List[Product]:
        """
        Filter products by category.

        Args:
            category (str): Category to filter by.

        Returns:
            List[Product]: Filtered list of Product objects.
        """
        return [product for product in self.products if product.category == category]

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """
        Filter products by price range.

        Args:
            min_price (float): Minimum price.
            max_price (float): Maximum price.

        Returns:
            List[Product]: Filtered list of Product objects.
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

    def sort_by_price(self, ascending: bool = True) -> List[Product]:
        """
        Sort products by price.

        Args:
            ascending (bool): Sort in ascending order (default) or descending order.

        Returns:
            List[Product]: Sorted list of Product objects.
        """
        return sorted(self.products, key=lambda product: product.price, reverse=not ascending)

    def sort_by_name(self, ascending: bool = True) -> List[Product]:
        """
        Sort products by name.

        Args:
            ascending (bool): Sort in ascending order (default) or descending order.

        Returns:
            List[Product]: Sorted list of Product objects.
        """
        return sorted(self.products, key=lambda product: product.name, reverse=not ascending)
```

### Example Usage

```python
# main.py

from models.product import Product
from services.product_filter_sorter import ProductFilterSorter

def main():
    # Create sample products
    products = [
        Product(1, "Product A", 19.99, "Electronics"),
        Product(2, "Product B", 9.99, "Electronics"),
        Product(3, "Product C", 29.99, "Fashion"),
        Product(4, "Product D", 39.99, "Fashion"),
        Product(5, "Product E", 49.99, "Home Goods"),
    ]

    # Create a ProductFilterSorter object
    product_filter_sorter = ProductFilterSorter(products)

    # Filter products by category
    electronics_products = product_filter_sorter.filter_by_category("Electronics")
    print("Electronics Products:")
    for product in electronics_products:
        print(product)

    # Filter products by price range
    affordable_products = product_filter_sorter.filter_by_price_range(0, 20)
    print("\nAffordable Products:")
    for product in affordable_products:
        print(product)

    # Sort products by price
    sorted_products_by_price = product_filter_sorter.sort_by_price()
    print("\nSorted Products by Price (Ascending):")
    for product in sorted_products_by_price:
        print(product)

    # Sort products by name
    sorted_products_by_name = product_filter_sorter.sort_by_name()
    print("\nSorted Products by Name (Ascending):")
    for product in sorted_products_by_name:
        print(product)

if __name__ == "__main__":
    main()
```
