"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Generate a code snippet for an e-commerce platform that implements a discount system for products, similar to the 45% discount and coupon features mentioned on TikTok Shop Vietnam.
Generated: DETERMINISTIC_5eef742c08f556b3
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    A class to represent a product in the e-commerce platform.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a new product with a name and price.

        :param name: The name of the product.
        :param price: The original price of the product.
        """
        self.name = name
        self.price = price
        self.discount_percentage = 0.0
        self.coupon_discount = 0.0

    def apply_discount(self, percentage: float):
        """
        Applies a percentage discount to the product.

        :param percentage: The discount percentage to apply.
        :raises ValueError: If the percentage is not between 0 and 100.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.discount_percentage = percentage

    def apply_coupon(self, discount: float):
        """
        Applies a coupon discount to the product.

        :param discount: The fixed amount discount to apply.
        :raises ValueError: If the discount is negative.
        """
        if discount < 0:
            raise ValueError("Coupon discount cannot be negative.")
        self.coupon_discount = discount

    def final_price(self) -> float:
        """
        Calculates the final price after applying discounts.

        :return: The final price after applying the discount and coupon.
        """
        # Calculate the price after percentage discount
        price_after_discount = self.price * (1 - self.discount_percentage / 100)
        # Apply coupon discount
        final_price = price_after_discount - self.coupon_discount
        # Ensure final price is not negative
        return max(final_price, 0)

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return f"Product(name={self.name}, price={self.price:.2f}, " \
               f"discount_percentage={self.discount_percentage:.2f}, " \
               f"coupon_discount={self.coupon_discount:.2f}, " \
               f"final_price={self.final_price():.2f})"


# Example usage
if __name__ == "__main__":
    try:
        # Create a product instance
        product = Product("Sample Product", 100.00)

        # Apply a 45% discount
        product.apply_discount(45)

        # Apply a coupon discount of 5
        product.apply_coupon(5)

        # Print the product details
        print(product)

    except ValueError as e:
        print(f"Error: {e}")
```
