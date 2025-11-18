"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Write a script to calculate discounts for jewelry products, including first-time shopper discounts (e.g., "WELCOME5") and promotional codes like "CODESALE20."
Generated: DETERMINISTIC_7dfef9e55d23daf4
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class JewelryDiscountCalculator:
    """
    A class to calculate discounts for jewelry products.
    """

    def __init__(self):
        # Initialize available discount codes and their corresponding discount values
        self.discount_codes = {
            "WELCOME5": 0.05,  # 5% discount for first-time shoppers
            "CODESALE20": 0.20  # 20% promotional discount
        }

    def calculate_discount(self, price, discount_code=None):
        """
        Calculate the final price after applying the discount code.

        :param price: The original price of the jewelry product
        :param discount_code: The discount code to apply (if any)
        :return: The final price after discount
        :raises ValueError: If the price is negative or if the discount code is invalid
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")

        discount = 0

        # Check if a discount code is provided and valid
        if discount_code:
            if discount_code not in self.discount_codes:
                raise ValueError(f"Invalid discount code: {discount_code}")
            discount = self.discount_codes[discount_code]

        # Calculate final price
        final_price = price * (1 - discount)
        return final_price

    def apply_discount(self, price, discount_code=None):
        """
        Wrapper method to apply the discount and handle any potential errors.

        :param price: The original price of the jewelry product
        :param discount_code: The discount code to apply (if any)
        :return: The final price or an error message
        """
        try:
            final_price = self.calculate_discount(price, discount_code)
            return f"The final price after applying the discount is: ${final_price:.2f}"
        except ValueError as e:
            return str(e)


if __name__ == "__main__":
    # Example usage of the JewelryDiscountCalculator
    calculator = JewelryDiscountCalculator()

    # Test prices and discount codes
    prices = [100.00, 250.50, -50.00]  # Includes an invalid price
    codes = ["WELCOME5", "CODESALE20", "INVALIDCODE", None]

    for price in prices:
        for code in codes:
            result = calculator.apply_discount(price, code)
            print(f"Price: ${price:.2f}, Code: '{code}': {result}")
```
