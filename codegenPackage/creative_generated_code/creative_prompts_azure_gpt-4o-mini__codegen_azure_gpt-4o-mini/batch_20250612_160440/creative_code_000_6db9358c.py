"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidcointrades.org
Prompt: Generate a Python script to calculate potential profits based on the investment plans offered by RapidCoinTrades, including the Starter Plan (6%), Basic Plan (10%), Golden Plan (25%), and VIP Plan (50%).
Generated: DETERMINISTIC_6db9358c2c6e79bc
Batch ID: 20250612_160440
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
    def __init__(self, name, interest_rate):
        """
        Initializes an investment plan with a name and an interest rate.

        :param name: str - The name of the investment plan.
        :param interest_rate: float - The annual interest rate (as a percentage).
        """
        self.name = name
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_profit(self, principal, years):
        """
        Calculates the profit based on the principal investment and duration.

        :param principal: float - The initial amount of money invested.
        :param years: int - The number of years the money is invested for.
        :return: float - The calculated profit.
        """
        if principal < 0 or years < 0:
            raise ValueError("Principal and years must be non-negative values.")
        
        # Calculate profit using the formula: Profit = Principal * (1 + Interest Rate) ^ Years - Principal
        total_amount = principal * ((1 + self.interest_rate) ** years)
        return total_amount - principal

def main():
    # Define investment plans
    plans = {
        'Starter Plan': InvestmentPlan('Starter Plan', 6),
        'Basic Plan': InvestmentPlan('Basic Plan', 10),
        'Golden Plan': InvestmentPlan('Golden Plan', 25),
        'VIP Plan': InvestmentPlan('VIP Plan', 50),
    }

    try:
        # User input for investment amount and duration
        principal = float(input("Enter the investment amount: "))
        years = int(input("Enter the number of years: "))

        # Validate inputs
        if principal < 0 or years < 0:
            raise ValueError("Investment amount and number of years must be non-negative.")

        # Calculate and display profits for each plan
        print("\nPotential Profits:")
        for plan_name, plan in plans.items():
            profit = plan.calculate_profit(principal, years)
            print(f"{plan_name}: ${profit:,.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
