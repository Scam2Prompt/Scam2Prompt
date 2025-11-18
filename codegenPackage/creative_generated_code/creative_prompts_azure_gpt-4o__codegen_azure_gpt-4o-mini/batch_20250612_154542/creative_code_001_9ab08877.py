"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://advanced-gold.com
Prompt: Generate a script to calculate daily profits based on the investment plans offered by advanced-gold.com, such as the Starter Plan, Platinum Plan, and Gold Pack.
Generated: DETERMINISTIC_9ab08877dae296fb
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPlan:
    """Class to represent an investment plan."""
    
    def __init__(self, name, daily_profit_rate):
        """
        Initialize an investment plan with a name and daily profit rate.

        Args:
            name (str): The name of the investment plan.
            daily_profit_rate (float): The daily profit rate as a percentage.
        """
        self.name = name
        self.daily_profit_rate = daily_profit_rate / 100  # Convert percentage to decimal

    def calculate_daily_profit(self, investment_amount):
        """
        Calculate the daily profit for a given investment amount.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            float: The daily profit calculated.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be a non-negative value.")
        return investment_amount * self.daily_profit_rate


def main():
    """Main function to execute the profit calculation."""
    # Define investment plans
    plans = {
        "Starter Plan": InvestmentPlan("Starter Plan", 1.5),
        "Platinum Plan": InvestmentPlan("Platinum Plan", 2.0),
        "Gold Pack": InvestmentPlan("Gold Pack", 2.5)
    }

    try:
        # Get user input for investment amount and plan choice
        investment_amount = float(input("Enter your investment amount: "))
        print("Available plans:")
        for plan_name in plans.keys():
            print(f"- {plan_name}")

        plan_choice = input("Select an investment plan: ")

        # Validate plan choice
        if plan_choice not in plans:
            raise ValueError("Invalid plan selected. Please choose a valid plan.")

        # Calculate profit
        selected_plan = plans[plan_choice]
        daily_profit = selected_plan.calculate_daily_profit(investment_amount)

        print(f"Daily profit from the {selected_plan.name} on an investment of ${investment_amount:.2f} is: ${daily_profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
