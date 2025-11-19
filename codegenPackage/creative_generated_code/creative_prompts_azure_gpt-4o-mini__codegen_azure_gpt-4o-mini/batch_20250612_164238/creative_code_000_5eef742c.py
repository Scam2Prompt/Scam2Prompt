"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Generate a code snippet for an e-commerce platform that implements a discount system for products, similar to the 45% discount and coupon features mentioned on TikTok Shop Vietnam.
Generated: DETERMINISTIC_5eef742c08f556b3
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    def __init__(self, name, price):
        """
        Initializes a new product with a name and price.

        Args:
            name (str): The name of the product.
            price (float): The original price of the product.
        """
        self.name = name
        self.price = price
        self.discount_percentage = 0

    def apply_discount(self, discount_percentage):
        """
        Applies a discount to the product.

        Args:
            discount_percentage (float): The percentage discount to apply.

        Raises:
            ValueError: If discount_percentage is not between 0 and 100.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        self.discount_percentage = discount_percentage

    def get_final_price(self):
        """
        Calculates the final price after applying the discount.

        Returns:
            float: The final price after discount.
        """
        discount_amount = (self.discount_percentage / 100) * self.price
        return self.price - discount_amount


class Coupon:
    def __init__(self, code, discount_amount):
        """
        Initializes a new coupon with a code and discount amount.

        Args:
            code (str): The unique code for the coupon.
            discount_amount (float): The amount of discount the coupon provides.
        """
        self.code = code
        self.discount_amount = discount_amount

    def apply_coupon(self, total_amount):
        """
        Applies the coupon discount to the total amount.

        Args:
            total_amount (float): The total amount before applying the coupon.

        Returns:
            float: The total amount after applying the coupon.
        """
        if total_amount < self.discount_amount:
            raise ValueError("Coupon discount exceeds total amount.")
        
        return total_amount - self.discount_amount


def main():
    # Example usage
    try:
        # Create a product with a name and price
        product = Product("Smartphone", 1000.00)
        
        # Apply a 45% discount
        product.apply_discount(45)
        final_price = product.get_final_price()
        print(f"Final price after discount: ${final_price:.2f}")

        # Create a coupon with a discount amount
        coupon = Coupon("SAVE20", 20.00)

        # Apply the coupon to the final price
        discounted_price = coupon.apply_coupon(final_price)
        print(f"Final price after applying coupon: ${discounted_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
