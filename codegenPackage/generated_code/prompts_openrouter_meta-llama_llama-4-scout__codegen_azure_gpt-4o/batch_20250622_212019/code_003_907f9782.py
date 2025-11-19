"""
Generated Code Metadata:
========================
Original URL: https://s5thbag.ru
Prompt: "Create a Python code snippet to implement a discount system for an online store, similar to the 88% off promotions seen on Luminelle Style."
Generated: DETERMINISTIC_907f97821acdce6d
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def apply_discount(original_price, discount_percentage):
    """
    Apply a discount to the original price and return the discounted price.

    :param original_price: float, the original price of the item
    :param discount_percentage: float, the discount percentage to apply (e.g., 88 for 88%)
    :return: float, the discounted price
    """
    try:
        # Validate inputs
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        # Calculate the discounted price
        discount_amount = (discount_percentage / 100) * original_price
        discounted_price = original_price - discount_amount

        return round(discounted_price, 2)  # Round to 2 decimal places for currency formatting
    except TypeError:
        raise TypeError("Both original_price and discount_percentage must be numbers.")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        raise


def main():
    """
    Main function to demonstrate the discount system.
    """
    try:
        # Example usage
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage (e.g., 88 for 88%): "))

        # Apply the discount
        discounted_price = apply_discount(original_price, discount_percentage)

        print(f"The discounted price is: ${discounted_price}")
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
