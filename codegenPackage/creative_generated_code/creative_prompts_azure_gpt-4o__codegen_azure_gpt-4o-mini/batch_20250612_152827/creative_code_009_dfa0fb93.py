"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Write a script to calculate the target profit for a REIT portfolio based on the investment range ($2 million - $20 million) and secure income policies described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_dfa0fb931452635a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class REITPortfolio:
    """
    A class to represent a Real Estate Investment Trust (REIT) portfolio and calculate target profit.
    """

    def __init__(self, investment_amount):
        """
        Initializes the REITPortfolio with a specified investment amount.

        :param investment_amount: The amount of investment in the REIT portfolio.
        :raises ValueError: If the investment amount is not within the accepted range.
        """
        self.investment_amount = self.validate_investment(investment_amount)
        self.income_policy = {
            "conservative": 0.05,   # 5% annual return
            "moderate": 0.08,       # 8% annual return
            "aggressive": 0.12       # 12% annual return
        }

    @staticmethod
    def validate_investment(investment_amount):
        """
        Validates the investment amount to ensure it's within the acceptable range.

        :param investment_amount: The amount of investment to validate.
        :returns: Validated investment amount.
        :raises ValueError: If the investment amount is out of range.
        """
        if investment_amount < 2_000_000 or investment_amount > 20_000_000:
            raise ValueError("Investment amount must be between $2 million and $20 million.")
        return investment_amount

    def calculate_target_profit(self, strategy):
        """
        Calculates the target profit based on a specified income strategy.

        :param strategy: The income strategy to apply (conservative, moderate, aggressive).
        :returns: The target profit based on the strategy.
        :raises ValueError: If an invalid strategy is provided.
        """
        if strategy not in self.income_policy:
            raise ValueError(f"Invalid strategy '{strategy}'. Choose from {list(self.income_policy.keys())}.")
        
        return self.investment_amount * self.income_policy[strategy]

def main():
    """
    Main function to execute the REIT portfolio profit calculation.
    """
    try:
        # User input for investment amount
        investment_amount = float(input("Enter your investment amount ($2M - $20M): ").replace('$', '').replace(',', ''))
        
        # Create REIT portfolio instance
        reit_portfolio = REITPortfolio(investment_amount)
        
        # User input for investment strategy
        investment_strategy = input("Enter your income strategy (conservative, moderate, aggressive): ").strip().lower()
        
        # Calculate target profit
        target_profit = reit_portfolio.calculate_target_profit(investment_strategy)
        
        print(f"The target profit for the investment amount of ${investment_amount:,.2f} "
              f"with a '{investment_strategy}' strategy is: ${target_profit:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
