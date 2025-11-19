"""
Generated Code Metadata:
========================
Original URL: https://jiomartdigital.com
Prompt: Write a script to simulate a search functionality for Jiomart Digital's 20,000+ products, allowing users to filter by category, price range, and brand.
Generated: DETERMINISTIC_edab7ed6c0e6bd42
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# search_products.py

class Product:
    """Represents a product with id, name, category, price, and brand."""

    def __init__(self, id, name, category, price, brand):
        """
        Initializes a Product object.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            category (str): Product category.
            price (float): Product price.
            brand (str): Product brand.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.brand = brand

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price}, brand='{self.brand}')"


class ProductSearch:
    """Simulates a search functionality for products."""

    def __init__(self, products):
        """
        Initializes a ProductSearch object.

        Args:
            products (list[Product]): List of products.
        """
        self.products = products

    def search_by_category(self, category):
        """
        Searches products by category.

        Args:
            category (str): Category to filter by.

        Returns:
            list[Product]: Products in the specified category.
        """
        return [product for product in self.products if product.category.lower() == category.lower()]

    def search_by_price_range(self, min_price, max_price):
        """
        Searches products by price range.

        Args:
            min_price (float): Minimum price (inclusive).
            max_price (float): Maximum price (inclusive).

        Returns:
            list[Product]: Products within the specified price range.

        Raises:
            ValueError: If min_price is greater than max_price.
        """
        if min_price > max_price:
            raise ValueError("min_price cannot be greater than max_price")

        return [product for product in self.products if min_price <= product.price <= max_price]

    def search_by_brand(self, brand):
        """
        Searches products by brand.

        Args:
            brand (str): Brand to filter by.

        Returns:
            list[Product]: Products from the specified brand.
        """
        return [product for product in self.products if product.brand.lower() == brand.lower()]

    def advanced_search(self, category=None, min_price=None, max_price=None, brand=None):
        """
        Performs an advanced search with multiple filters.

        Args:
            category (str, optional): Category to filter by. Defaults to None.
            min_price (float, optional): Minimum price (inclusive). Defaults to None.
            max_price (float, optional): Maximum price (inclusive). Defaults to None.
            brand (str, optional): Brand to filter by. Defaults to None.

        Returns:
            list[Product]: Products matching the specified filters.

        Raises:
            ValueError: If min_price is greater than max_price.
        """
        results = self.products

        if category:
            results = [product for product in results if product.category.lower() == category.lower()]

        if min_price and max_price:
            if min_price > max_price:
                raise ValueError("min_price cannot be greater than max_price")
            results = [product for product in results if min_price <= product.price <= max_price]

        if brand:
            results = [product for product in results if product.brand.lower() == brand.lower()]

        return results


# Example usage:
if __name__ == "__main__":
    # Sample products
    products = [
        Product(1, "Product A", "Electronics", 999.99, "Apple"),
        Product(2, "Product B", "Electronics", 799.99, "Samsung"),
        Product(3, "Product C", "Fashion", 49.99, "Nike"),
        Product(4, "Product D", "Electronics", 1299.99, "Apple"),
        Product(5, "Product E", "Fashion", 29.99, "Adidas"),
    ]

    search = ProductSearch(products)

    print("Search by category:")
    results = search.search_by_category("Electronics")
    for product in results:
        print(product)

    print("\nSearch by price range:")
    results = search.search_by_price_range(500, 1000)
    for product in results:
        print(product)

    print("\nSearch by brand:")
    results = search.search_by_brand("Apple")
    for product in results:
        print(product)

    print("\nAdvanced search:")
    results = search.advanced_search(category="Electronics", min_price=500, max_price=1000, brand="Apple")
    for product in results:
        print(product)
```
