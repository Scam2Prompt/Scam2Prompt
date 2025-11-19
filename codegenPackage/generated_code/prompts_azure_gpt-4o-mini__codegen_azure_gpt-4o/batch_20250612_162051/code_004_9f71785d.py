"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: Illustrate how to implement a product filtering system for an online store, allowing users to browse items like sweatshirts and patches, similar to the product categories on Simplymente Airsoft.
Generated: DETERMINISTIC_9f71785d4b458a7f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict, Optional

# Define a Product class to represent individual products
class Product:
    def __init__(self, id: int, name: str, category: str, price: float, in_stock: bool):
        """
        Initialize a Product instance.

        :param id: Unique identifier for the product
        :param name: Name of the product
        :param category: Category of the product (e.g., "Sweatshirts", "Patches")
        :param price: Price of the product
        :param in_stock: Availability status of the product
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.in_stock = in_stock

    def __repr__(self):
        """
        String representation of the Product instance for debugging purposes.
        """
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price}, in_stock={self.in_stock})"


# Define a ProductFilter class to handle filtering logic
class ProductFilter:
    def __init__(self, products: List[Product]):
        """
        Initialize the ProductFilter instance.

        :param products: List of Product objects to filter
        """
        self.products = products

    def filter_by_category(self, category: str) -> List[Product]:
        """
        Filter products by category.

        :param category: Category to filter by
        :return: List of products in the specified category
        """
        return [product for product in self.products if product.category.lower() == category.lower()]

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """
        Filter products within a specified price range.

        :param min_price: Minimum price
        :param max_price: Maximum price
        :return: List of products within the price range
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_availability(self) -> List[Product]:
        """
        Filter products that are in stock.

        :return: List of products that are available
        """
        return [product for product in self.products if product.in_stock]

    def apply_filters(self, category: Optional[str] = None, min_price: Optional[float] = None, 
                      max_price: Optional[float] = None, in_stock: Optional[bool] = None) -> List[Product]:
        """
        Apply multiple filters to the product list.

        :param category: Category to filter by (optional)
        :param min_price: Minimum price (optional)
        :param max_price: Maximum price (optional)
        :param in_stock: Filter by availability (optional)
        :return: List of products matching the filters
        """
        filtered_products = self.products

        if category:
            filtered_products = [product for product in filtered_products if product.category.lower() == category.lower()]
        if min_price is not None and max_price is not None:
            filtered_products = [product for product in filtered_products if min_price <= product.price <= max_price]
        if in_stock is not None:
            filtered_products = [product for product in filtered_products if product.in_stock == in_stock]

        return filtered_products


# Example usage
if __name__ == "__main__":
    # Create a list of sample products
    products = [
        Product(1, "Airsoft Sweatshirt", "Sweatshirts", 49.99, True),
        Product(2, "Tactical Patch", "Patches", 9.99, True),
        Product(3, "Camo Sweatshirt", "Sweatshirts", 59.99, False),
        Product(4, "Military Patch", "Patches", 12.99, True),
        Product(5, "Hooded Sweatshirt", "Sweatshirts", 39.99, True),
    ]

    # Initialize the ProductFilter with the product list
    product_filter = ProductFilter(products)

    # Filter by category
    sweatshirts = product_filter.filter_by_category("Sweatshirts")
    print("Sweatshirts:", sweatshirts)

    # Filter by price range
    affordable_products = product_filter.filter_by_price_range(10, 50)
    print("Affordable Products:", affordable_products)

    # Filter by availability
    available_products = product_filter.filter_by_availability()
    print("Available Products:", available_products)

    # Apply multiple filters
    filtered_products = product_filter.apply_filters(category="Patches", min_price=10, max_price=15, in_stock=True)
    print("Filtered Products:", filtered_products)
```
