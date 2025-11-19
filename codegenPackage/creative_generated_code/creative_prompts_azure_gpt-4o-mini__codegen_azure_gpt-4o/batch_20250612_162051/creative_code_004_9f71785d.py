"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplementeairsoft.com
Prompt: Illustrate how to implement a product filtering system for an online store, allowing users to browse items like sweatshirts and patches, similar to the product categories on Simplymente Airsoft.
Generated: DETERMINISTIC_9f71785d4b458a7f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Product:
    """
    Represents a product in the store.
    """
    def __init__(self, name, category, price, in_stock):
        """
        Initialize a Product object.
        :param name: Name of the product
        :param category: Category of the product (e.g., 'Sweatshirt', 'Patch')
        :param price: Price of the product
        :param in_stock: Boolean indicating if the product is in stock
        """
        self.name = name
        self.category = category
        self.price = price
        self.in_stock = in_stock

    def to_dict(self):
        """
        Convert the Product object to a dictionary.
        :return: Dictionary representation of the Product
        """
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "in_stock": self.in_stock,
        }


class ProductFilter:
    """
    A system for filtering products based on different criteria.
    """
    @staticmethod
    def filter_by_category(products, category):
        """
        Filter products by category.
        :param products: List of Product objects
        :param category: Category to filter by
        :return: List of Product objects that belong to the specified category
        """
        return [product for product in products if product.category.lower() == category.lower()]

    @staticmethod
    def filter_by_price_range(products, min_price, max_price):
        """
        Filter products within a specified price range.
        :param products: List of Product objects
        :param min_price: Minimum price
        :param max_price: Maximum price
        :return: List of Product objects within the price range
        """
        return [product for product in products if min_price <= product.price <= max_price]

    @staticmethod
    def filter_by_stock(products):
        """
        Filter products that are in stock.
        :param products: List of Product objects
        :return: List of Product objects that are currently in stock
        """
        return [product for product in products if product.in_stock]


def main():
    """
    Main function to demonstrate the product filtering system.
    """
    try:
        # Sample product data
        products = [
            Product("Tactical Sweatshirt", "Sweatshirt", 49.99, True),
            Product("Skull Patch", "Patch", 9.99, False),
            Product("Military Sweatshirt", "Sweatshirt", 59.99, True),
            Product("Flag Patch", "Patch", 8.99, True),
            Product("Hooded Sweatshirt", "Sweatshirt", 39.99, True),
        ]

        # User-selected filters (example scenarios)
        print("=== Product Filtering System ===")
        print("All Products:")
        print(json.dumps([product.to_dict() for product in products], indent=4))

        # Filter by category (e.g., Sweatshirt)
        sweatshirts = ProductFilter.filter_by_category(products, "Sweatshirt")
        print("\nFiltered by Category (Sweatshirt):")
        print(json.dumps([product.to_dict() for product in sweatshirts], indent=4))

        # Filter by price range (e.g., $40 - $60)
        price_filtered = ProductFilter.filter_by_price_range(products, 40, 60)
        print("\nFiltered by Price Range ($40 - $60):")
        print(json.dumps([product.to_dict() for product in price_filtered], indent=4))

        # Filter by stock availability
        in_stock_products = ProductFilter.filter_by_stock(products)
        print("\nFiltered by Stock Availability:")
        print(json.dumps([product.to_dict() for product in in_stock_products], indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
