"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Write a script to calculate the target profit for a REIT portfolio based on the investment range ($2 million - $20 million) and secure income policies described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_dfa0fb931452635a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class REITPortfolio:
    """
    A class to represent a Real Estate Investment Trust (REIT) portfolio.
    """

    def __init__(self, investment_amount):
        """
        Initializes the REITPortfolio with a specified investment amount.

        :param investment_amount: The amount invested in the REIT portfolio.
        :raises ValueError: If the investment amount is not within the allowed range.
        """
        self.investment_amount = investment_amount
        self.validate_investment()

    def validate_investment(self):
        """
        Validates the investment amount to ensure it is within the allowed range.
        """
        if not (2_000_000 <= self.investment_amount <= 20_000_000):
            raise ValueError("Investment amount must be between $2 million and $20 million.")

    def calculate_target_profit(self, target_yield):
        """
        Calculates the target profit based on the investment amount and target yield.

        :param target_yield: The target yield as a percentage (e.g., 0.08 for 8%).
        :return: The calculated target profit.
        :raises ValueError: If the target yield is not a positive number.
        """
        if target_yield <= 0:
            raise ValueError("Target yield must be a positive number.")

        target_profit = self.investment_amount * target_yield
        return target_profit

def main():
    """
    Main function to execute the REIT portfolio target profit calculation.
    """
    try:
        # Example investment amount and target yield
        investment_amount = 5_000_000  # Example: $5 million
        target_yield = 0.08  # Example: 8%

        # Create a REIT portfolio instance
        portfolio = REITPortfolio(investment_amount)

        # Calculate the target profit
        target_profit = portfolio.calculate_target_profit(target_yield)

        # Output the result
        print(f"Target Profit for an investment of ${investment_amount:,.2f} "
              f"at a target yield of {target_yield * 100:.2f}% is: "
              f"${target_profit:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
