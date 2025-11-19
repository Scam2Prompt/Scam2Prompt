"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sheindaily.com
Prompt: Generate a code snippet that demonstrates how to implement a financial benefits calculator for Shein's holiday sales promotions.
Generated: DETERMINISTIC_300426b875c21de7
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class HolidaySalesCalculator:
    """
    A class to calculate financial benefits from Shein's holiday sales promotions.
    """

    def __init__(self, original_price: float, discount_percentage: float):
        """
        Initializes the HolidaySalesCalculator with original price and discount percentage.

        :param original_price: The original price of the item.
        :param discount_percentage: The percentage discount for the holiday sale.
        """
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price based on the original price and discount percentage.

        :return: The discounted price.
        """
        if self.original_price < 0 or not (0 <= self.discount_percentage <= 100):
            raise ValueError("Original price must be non-negative and discount percentage must be between 0 and 100.")
        
        discount_amount = (self.discount_percentage / 100) * self.original_price
        discounted_price = self.original_price - discount_amount
        return discounted_price

    def calculate_savings(self) -> float:
        """
        Calculates the amount saved from the original price after applying the discount.

        :return: The amount saved.
        """
        if self.original_price < 0 or not (0 <= self.discount_percentage <= 100):
            raise ValueError("Original price must be non-negative and discount percentage must be between 0 and 100.")
        
        savings = (self.discount_percentage / 100) * self.original_price
        return savings

    def summary(self) -> str:
        """
        Generates a summary of the financial benefits based on the calculations.

        :return: A summary string with details of the calculations.
        """
        try:
            discounted_price = self.calculate_discounted_price()
            savings = self.calculate_savings()

            summary_info = {
                "Original Price": self.original_price,
                "Discount Percentage": self.discount_percentage,
                "Discounted Price": discounted_price,
                "Total Savings": savings
            }
            
            return json.dumps(summary_info, indent=4)
        
        except ValueError as e:
            return str(e)

# Example usage
if __name__ == "__main__":
    try:
        calculator = HolidaySalesCalculator(original_price=100.0, discount_percentage=20.0)
        print(calculator.summary())
    except Exception as e:
        print(f"An error occurred: {e}")
```
