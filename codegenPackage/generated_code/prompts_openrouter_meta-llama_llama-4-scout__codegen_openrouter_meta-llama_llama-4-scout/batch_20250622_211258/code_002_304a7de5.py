"""
Generated Code Metadata:
========================
Original URL: https://patwacompany.com
Prompt: "Write a Python code snippet for an e-commerce website to display men's kurta pyjama products, including style codes Patwa-1, Patwa-2, Patwa-3, and Patwa-4, with their respective prices and discounts."
Generated: DETERMINISTIC_304a7de5f1386e84
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kurta_pyjama_products.py

class KurtaPyjamaProduct:
    """Represents a men's kurta pyjama product."""

    def __init__(self, style_code, name, price, discount=0):
        """
        Initializes a KurtaPyjamaProduct.

        Args:
            style_code (str): Unique style code for the product.
            name (str): Name of the product.
            price (float): Price of the product.
            discount (float, optional): Discount percentage. Defaults to 0.
        """
        self.style_code = style_code
        self.name = name
        self.price = price
        self.discount = discount

    def get_discounted_price(self):
        """Calculates the discounted price of the product."""
        return self.price - (self.price * self.discount / 100)

    def __str__(self):
        """Returns a string representation of the product."""
        return f"Style Code: {self.style_code}\nName: {self.name}\nPrice: ${self.price:.2f}\nDiscount: {self.discount}%\nDiscounted Price: ${self.get_discounted_price():.2f}"


class ECommerceWebsite:
    """Represents an e-commerce website."""

    def __init__(self):
        """Initializes an ECommerceWebsite."""
        self.products = []

    def add_product(self, product):
        """Adds a product to the website."""
        self.products.append(product)

    def display_products(self):
        """Displays all products on the website."""
        for product in self.products:
            print(product)
            print("------------------------")


def main():
    try:
        # Create e-commerce website
        website = ECommerceWebsite()

        # Create kurta pyjama products
        products = [
            KurtaPyjamaProduct("Patwa-1", "Men's Kurta Pyjama - Style 1", 49.99, 10),
            KurtaPyjamaProduct("Patwa-2", "Men's Kurta Pyjama - Style 2", 59.99, 15),
            KurtaPyjamaProduct("Patwa-3", "Men's Kurta Pyjama - Style 3", 69.99, 20),
            KurtaPyjamaProduct("Patwa-4", "Men's Kurta Pyjama - Style 4", 79.99, 25),
        ]

        # Add products to website
        for product in products:
            website.add_product(product)

        # Display products
        website.display_products()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
