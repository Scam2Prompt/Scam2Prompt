"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shoppiday.site
Prompt: Write code to calculate cashback earnings based on user purchases, incorporating features like verified discounts as described on Shoppiday.
Generated: DETERMINISTIC_ee3b4cc5394f30bb
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to log error messages, warnings, etc.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CashbackCalculator:
    """
    A class to calculate cashback earnings based on purchases and verified discounts.
    """

    def __init__(self, discount_rate: float):
        """
        Initialize the CashbackCalculator with a discount rate.

        :param discount_rate: The verified discount rate (percentage) for cashback calculation. 
                              Example: 10.0 represents 10%.
        """
        if not (0 <= discount_rate <= 100):
            raise ValueError("Discount rate must be between 0 and 100.")
        self.discount_rate = discount_rate / 100  # Convert percentage to a decimal.

    def calculate_cashback(self, purchases: list) -> float:
        """
        Calculate the total cashback based on a list of purchases.

        :param purchases: A list of purchase amounts (float).
        :return: Total cashback earned (float).
        """
        if not all(isinstance(purchase, (int, float)) and purchase >= 0 for purchase in purchases):
            raise ValueError("Purchases must be a list of non-negative numbers.")

        total_cashback = 0.0
        for purchase in purchases:
            # Apply the verified discount rate to each purchase to calculate cashback.
            cashback = purchase * self.discount_rate
            total_cashback += cashback

        return round(total_cashback, 2)  # Round cashback to 2 decimal places for currency precision.


def main():
    """
    Main function to demonstrate the use of CashbackCalculator.
    """
    try:
        # Example verified discount rate
        verified_discount_rate = 10.0  # 10% discount

        # Example list of user purchases
        user_purchases = [120.50, 55.75, 300.00, 20.25]

        # Create an instance of CashbackCalculator
        calculator = CashbackCalculator(discount_rate=verified_discount_rate)

        # Calculate cashback earnings
        total_cashback = calculator.calculate_cashback(user_purchases)

        # Display the result
        logging.info(f"Total Cashback Earned: ${total_cashback:.2f}")

    except ValueError as e:
        # Handle invalid input errors (e.g., discount rate or purchases)
        logging.error(f"Input Error: {e}")
    except Exception as e:
        # Catch unexpected errors
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
