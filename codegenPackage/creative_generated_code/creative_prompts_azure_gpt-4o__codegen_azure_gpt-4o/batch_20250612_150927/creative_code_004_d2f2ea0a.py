"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Suggest a library or tool to implement a discount system for an online store, including features like "гарантированная скидка от 3%," as mentioned on acula.com.ua.
Generated: DETERMINISTIC_d2f2ea0ab6bb5083
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script implements a discount system for an online store using
the `decimal` library for accurate financial calculations. It includes features
such as a guaranteed discount of 3% and additional configurable discounts.

The script is production-ready and handles errors gracefully.
"""

from decimal import Decimal, ROUND_DOWN

class DiscountSystem:
    """
    A class to manage and apply discounts for an online store.
    """

    def __init__(self, guaranteed_discount: Decimal = Decimal("0.03")):
        """
        Initializes the DiscountSystem with a guaranteed discount rate.

        Args:
            guaranteed_discount (Decimal): Guaranteed minimum discount rate (default is 3%).
        """
        self.guaranteed_discount = guaranteed_discount

    def apply_discount(self, original_price: Decimal, additional_discount: Decimal = Decimal("0")) -> Decimal:
        """
        Applies the guaranteed discount and an additional configurable discount.

        Args:
            original_price (Decimal): The original price of the item.
            additional_discount (Decimal): An additional discount rate (default is 0%).

        Returns:
            Decimal: The final price after applying all discounts.

        Raises:
            ValueError: If original_price or discount rates are negative.
        """
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if additional_discount < 0:
            raise ValueError("Additional discount rate cannot be negative.")

        # Calculate guaranteed discount
        guaranteed_discount_amount = original_price * self.guaranteed_discount

        # Calculate additional discount
        additional_discount_amount = original_price * additional_discount

        # Total discount
        total_discount = guaranteed_discount_amount + additional_discount_amount

        # Ensure the final price is not negative
        final_price = max(original_price - total_discount, Decimal("0"))

        # Round down to two decimal places for currency representation
        return final_price.quantize(Decimal("0.01"), rounding=ROUND_DOWN)


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the discount system with a guaranteed discount of 3%
        discount_system = DiscountSystem()

        # Original price
        original_price = Decimal("100.00")  # Example price in currency

        # Additional discount rate (e.g., promotional offer of 5%)
        additional_discount = Decimal("0.05")

        # Calculate final price
        final_price = discount_system.apply_discount(original_price, additional_discount)

        print(f"Original Price: {original_price}")
        print(f"Final Price after Discounts: {final_price}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```

**Dependencies**: This script uses only Python's built-in libraries and does not require any external dependencies. It is ready for production use.
