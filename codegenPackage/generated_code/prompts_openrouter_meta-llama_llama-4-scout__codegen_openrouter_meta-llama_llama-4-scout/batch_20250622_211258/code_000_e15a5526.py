"""
Generated Code Metadata:
========================
Original URL: https://patwacompany.com
Prompt: "Generate a product description for a men's white half-sleeve kurta with style code Patwa-1, priced at Rs. 600.00 after a 9% discount."
Generated: DETERMINISTIC_e15a5526adf632e1
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    def __init__(self, style_code, original_price, discount_percentage):
        """
        Initialize a Product object.

        Args:
            style_code (str): Unique style code for the product.
            original_price (float): Original price of the product.
            discount_percentage (float): Discount percentage for the product.
        """
        self.style_code = style_code
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self):
        """
        Calculate the discounted price of the product.

        Returns:
            float: Discounted price of the product.
        """
        return self.original_price - (self.original_price * self.discount_percentage / 100)

    def generate_product_description(self):
        """
        Generate a product description.

        Returns:
            str: Product description.
        """
        discounted_price = self.calculate_discounted_price()
        return f"Men's White Half-Sleeve Kurta, Style Code: {self.style_code}\nPrice: Rs.{self.original_price:.2f}\nDiscount: {self.discount_percentage}%\nDiscounted Price: Rs.{discounted_price:.2f}"


def main():
    try:
        style_code = "Patwa-1"
        original_price = 600.00
        discount_percentage = 9.00

        product = Product(style_code, original_price, discount_percentage)
        product_description = product.generate_product_description()
        print(product_description)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
