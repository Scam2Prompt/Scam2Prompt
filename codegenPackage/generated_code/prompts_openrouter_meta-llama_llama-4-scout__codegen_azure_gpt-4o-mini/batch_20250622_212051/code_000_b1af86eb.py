"""
Generated Code Metadata:
========================
Original URL: https://coindexe.fx-inc.us
Prompt: "Generate a Python script to calculate profit based on Coindexe FX investment plans, considering the Starter Plan with a $100-$900 investment and a 15% weekly return."
Generated: DETERMINISTIC_b1af86eb93ce572f
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class InvestmentPlan:
    """
    A class to represent an investment plan for Coindexe FX.
    """

    def __init__(self, investment_amount):
        """
        Initializes the investment plan with the given investment amount.

        :param investment_amount: The amount of money invested.
        """
        self.investment_amount = investment_amount
        self.weekly_return_rate = 0.15  # 15% weekly return

    def calculate_profit(self, weeks):
        """
        Calculates the profit based on the investment amount and the number of weeks.

        :param weeks: The number of weeks the investment is held.
        :return: The total profit after the specified number of weeks.
        """
        if weeks < 0:
            raise ValueError("Number of weeks cannot be negative.")
        
        profit = self.investment_amount * (1 + self.weekly_return_rate) ** weeks - self.investment_amount
        return profit

def main():
    """
    Main function to execute the investment profit calculation.
    """
    try:
        # User input for investment amount
        investment_amount = float(input("Enter your investment amount ($100 - $900): "))
        
        # Validate investment amount
        if investment_amount < 100 or investment_amount > 900:
            raise ValueError("Investment amount must be between $100 and $900.")

        # User input for number of weeks
        weeks = int(input("Enter the number of weeks for the investment: "))
        
        # Create an investment plan instance
        plan = InvestmentPlan(investment_amount)
        
        # Calculate profit
        profit = plan.calculate_profit(weeks)
        
        # Display the result
        print(f"Total profit after {weeks} week(s): ${profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
