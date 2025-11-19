"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assets-maple.finance
Prompt: Create a function that calculates potential yields for BTC holders using Maple's BTC Yield Product, considering the target APY of 5%.
Generated: DETERMINISTIC_938bd03f8221faf9
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BTCYieldCalculator:
    """
    A class to calculate the potential yields for BTC holders using Maple's BTC Yield Product.
    """

    def __init__(self, amount_btc, target_apy=0.05):
        """
        Initializes the calculator with the amount of BTC and target APY.

        :param amount_btc: The amount of Bitcoin held (in BTC) by the user.
        :param target_apy: The target Annual Percentage Yield (APY), default is 5%.
        """
        if amount_btc < 0:
            raise ValueError("Amount of BTC cannot be negative.")
        if not (0 <= target_apy <= 1):
            raise ValueError("Target APY must be between 0 and 1.")

        self.amount_btc = amount_btc
        self.target_apy = target_apy

    def calculate_yield(self, years=1):
        """
        Calculates the potential yield over a specified number of years.

        :param years: The number of years for which to calculate the yield; default is 1 year.
        :return: The potential yield amount in BTC after the specified number of years.
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative.")

        # Compound interest formula: A = P * (1 + r/n)^(nt)
        # For simplicity, we assume interest is compounded annually (n=1)
        final_amount = self.amount_btc * (1 + self.target_apy) ** years
        potential_yield = final_amount - self.amount_btc
        
        return potential_yield

    def display_yield(self, years=1):
        """
        Displays the potential yield in a user-friendly format.

        :param years: The number of years for which to calculate the yield; default is 1 year.
        """
        yield_amount = self.calculate_yield(years)
        print(f"Potential yield for {self.amount_btc} BTC over {years} year(s) at {self.target_apy*100}% APY is: {yield_amount:.6f} BTC")


# Example usage:
if __name__ == "__main__":
    try:
        btc_amount = 1.5  # Amount of BTC held
        yield_calculator = BTCYieldCalculator(btc_amount)
        
        # Display potential yield for 1, 5, and 10 years
        yield_calculator.display_yield(years=1)
        yield_calculator.display_yield(years=5)
        yield_calculator.display_yield(years=10)

    except ValueError as e:
        print(f"Error: {e}")
```
