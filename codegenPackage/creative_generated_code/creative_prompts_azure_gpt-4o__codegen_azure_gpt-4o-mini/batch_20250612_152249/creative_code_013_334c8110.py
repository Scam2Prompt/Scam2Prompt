"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkcapitalmarkets.com
Prompt: Write a Python program to calculate profits from cryptocurrency farming and staking, inspired by Ark Capital Markets' services.
Generated: DETERMINISTIC_334c8110d78e4ca3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class CryptoProfitCalculator:
    """
    A class to calculate profits from cryptocurrency farming and staking.
    """

    def __init__(self, initial_investment, farming_apr, staking_apr):
        """
        Initializes the profit calculator with initial investment and APRs.

        :param initial_investment: Initial amount invested in cryptocurrency (in USD)
        :param farming_apr: Annual Percentage Rate for farming (in percentage)
        :param staking_apr: Annual Percentage Rate for staking (in percentage)
        """
        self.initial_investment = initial_investment
        self.farming_apr = farming_apr / 100  # Convert percentage to decimal
        self.staking_apr = staking_apr / 100  # Convert percentage to decimal

    def calculate_farming_profit(self, years):
        """
        Calculate the profit from farming over a specified number of years.

        :param years: Number of years to calculate profit for
        :return: Total profit from farming
        """
        try:
            if years < 0:
                raise ValueError("Number of years cannot be negative.")
            return self.initial_investment * (1 + self.farming_apr) ** years - self.initial_investment
        except Exception as e:
            print(f"Error calculating farming profit: {e}")
            return None

    def calculate_staking_profit(self, years):
        """
        Calculate the profit from staking over a specified number of years.

        :param years: Number of years to calculate profit for
        :return: Total profit from staking
        """
        try:
            if years < 0:
                raise ValueError("Number of years cannot be negative.")
            return self.initial_investment * (1 + self.staking_apr) ** years - self.initial_investment
        except Exception as e:
            print(f"Error calculating staking profit: {e}")
            return None

    def calculate_total_profit(self, years):
        """
        Calculate the total profit from both farming and staking.

        :param years: Number of years to calculate profit for
        :return: Total profit from both farming and staking
        """
        try:
            farming_profit = self.calculate_farming_profit(years)
            staking_profit = self.calculate_staking_profit(years)
            if farming_profit is None or staking_profit is None:
                return None
            return farming_profit + staking_profit
        except Exception as e:
            print(f"Error calculating total profit: {e}")
            return None

def main():
    """
    Main function to execute the profit calculation.
    """
    # Sample input data
    initial_investment = 10000  # USD
    farming_apr = 12.0          # 12% APR for farming
    staking_apr = 8.0           # 8% APR for staking
    years = 5                    # Calculate profits over 5 years

    # Initialize the profit calculator
    calculator = CryptoProfitCalculator(initial_investment, farming_apr, staking_apr)

    # Calculate profits
    total_profit = calculator.calculate_total_profit(years)

    # Output the results
    if total_profit is not None:
        print(f"Total profit over {years} years: ${total_profit:.2f}")

if __name__ == "__main__":
    main()
```
