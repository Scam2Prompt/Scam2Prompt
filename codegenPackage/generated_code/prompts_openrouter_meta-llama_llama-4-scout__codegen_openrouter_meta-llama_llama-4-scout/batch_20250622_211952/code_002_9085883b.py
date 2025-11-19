"""
Generated Code Metadata:
========================
Original URL: https://www.aquatic-green.ir
Prompt: "Generate a Python code snippet for an e-commerce website that lists Trust brand products, including their categories and prices."
Generated: DETERMINISTIC_9085883bee142ec5
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trust_products.py

class Product:
    """Represents a Trust brand product."""

    def __init__(self, name, category, price):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            category (str): Product category.
            price (float): Product price.
        """
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"{self.name} - {self.category}: ${self.price:.2f}"


class TrustProductList:
    """Manages a list of Trust brand products."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def get_products_by_category(self, category):
        """
        Retrieves products by category.

        Args:
            category (str): Category to filter by.

        Returns:
            list[Product]: Products in the specified category.
        """
        return [product for product in self.products if product.category == category]

    def list_all_products(self):
        """
        Lists all products.

        Returns:
            list[Product]: All products.
        """
        return self.products


def main():
    try:
        # Create a TrustProductList instance
        trust_products = TrustProductList()

        # Add some Trust brand products
        trust_products.add_product(Product("Trust GXT 252", "Gaming Mouse", 25.99))
        trust_products.add_product(Product("Trust Urban", "Headphones", 49.99))
        trust_products.add_product(Product("Trust Surya", "Gaming Keyboard", 69.99))
        trust_products.add_product(Product("Trust Primo", "Speakers", 29.99))

        # List all products
        print("All Trust Products:")
        for product in trust_products.list_all_products():
            print(product)

        # List products by category
        print("\nTrust Gaming Products:")
        for product in trust_products.get_products_by_category("Gaming Mouse"):
            print(product)
        for product in trust_products.get_products_by_category("Gaming Keyboard"):
            print(product)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
