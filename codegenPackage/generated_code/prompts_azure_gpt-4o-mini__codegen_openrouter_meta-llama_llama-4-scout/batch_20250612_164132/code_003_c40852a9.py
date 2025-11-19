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
# product_filter.py

class Product:
    """Represents a product with category, price, and discount percentage."""

    def __init__(self, name, category, price, discount_percentage):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            category (str): Product category.
            price (float): Product price.
            discount_percentage (float): Discount percentage.
        """
        self.name = name
        self.category = category
        self.price = price
        self.discount_percentage = discount_percentage

    def get_discounted_price(self):
        """Calculates the discounted price."""
        return self.price * (1 - self.discount_percentage / 100)


class ProductFilter:
    """Filters products by category and discount percentage."""

    def __init__(self, products):
        """
        Initializes a ProductFilter instance.

        Args:
            products (list[Product]): List of products.
        """
        self.products = products

    def filter_by_category(self, category):
        """
        Filters products by category.

        Args:
            category (str): Category to filter by.

        Returns:
            list[Product]: Filtered products.
        """
        return [product for product in self.products if product.category == category]

    def filter_by_discount_percentage(self, min_discount_percentage):
        """
        Filters products by discount percentage.

        Args:
            min_discount_percentage (float): Minimum discount percentage.

        Returns:
            list[Product]: Filtered products.
        """
        return [product for product in self.products if product.discount_percentage >= min_discount_percentage]

    def filter_products(self, category=None, min_discount_percentage=None):
        """
        Filters products by category and discount percentage.

        Args:
            category (str, optional): Category to filter by. Defaults to None.
            min_discount_percentage (float, optional): Minimum discount percentage. Defaults to None.

        Returns:
            list[Product]: Filtered products.
        """
        filtered_products = self.products

        if category:
            filtered_products = self.filter_by_category(category)

        if min_discount_percentage:
            filtered_products = self.filter_by_discount_percentage(min_discount_percentage)

        return filtered_products


def main():
    # Example usage:
    products = [
        Product("Product 1", "Shoes", 100.0, 10.0),
        Product("Product 2", "Shoes", 200.0, 20.0),
        Product("Product 3", "Clothes", 50.0, 5.0),
        Product("Product 4", "Shoes", 150.0, 15.0),
    ]

    product_filter = ProductFilter(products)

    try:
        filtered_products = product_filter.filter_products(category="Shoes", min_discount_percentage=10.0)

        print("Filtered Products:")
        for product in filtered_products:
            print(f"Name: {product.name}, Category: {product.category}, Price: {product.price}, Discount Percentage: {product.discount_percentage}%")
            print(f"Discounted Price: {product.get_discounted_price()}")
            print("-" * 50)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
