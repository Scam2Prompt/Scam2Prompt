"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xotanex.com
Prompt: Create a script to calculate potential earnings from Xotanex prediction markets, factoring in the 4.05% APY on cash and positions.
Generated: DETERMINISTIC_ff08acc7afa943d6
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class PredictionMarketEarningsCalculator:
    """
    A class to calculate potential earnings from Xotanex prediction markets
    factoring in the annual percentage yield (APY) on cash and positions.
    """

    def __init__(self, initial_investment, apy=0.0405):
        """
        Initializes the calculator with an initial investment and APY.

        :param initial_investment: Initial amount of cash or position value.
        :param apy: Annual Percentage Yield (default is 4.05%).
        """
        self.initial_investment = initial_investment
        self.apy = apy

    def compound_interest(self, principal, rate, time):
        """
        Calculate compound interest over a given time period.

        :param principal: The initial amount of money.
        :param rate: The interest rate as a decimal.
        :param time: The time the money is invested for in years.
        :return: The amount of money accumulated after time years, including interest.
        """
        try:
            return principal * (1 + rate) ** time
        except Exception as e:
            print(f"Error calculating compound interest: {e}")
            return None

    def calculate_earnings(self, investment_duration):
        """
        Calculate potential earnings over the specified investment duration.

        :param investment_duration: The duration of the investment in years.
        :return: Total accumulated amount after the investment duration.
        """
        if investment_duration < 0:
            raise ValueError("Investment duration must be non-negative")

        try:
            total_amount = self.compound_interest(self.initial_investment, self.apy, investment_duration)
            return total_amount
        except Exception as e:
            print(f"Error calculating earnings: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Set initial investment and duration of investment in years
    initial_investment = 1000  # Example: $1000
    investment_duration = 5  # Example: 5 years

    # Create calculator instance
    calculator = PredictionMarketEarningsCalculator(initial_investment)

    # Calculate potential earnings
    try:
        earnings = calculator.calculate_earnings(investment_duration)
        if earnings is not None:
            print(f"Potential earnings after {investment_duration} years: ${earnings:.2f}")
    except ValueError as ve:
        print(f"Input error: {ve}")
```
