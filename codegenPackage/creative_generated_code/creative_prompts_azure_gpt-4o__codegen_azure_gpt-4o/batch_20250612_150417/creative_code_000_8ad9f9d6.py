"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passiveinvestincome.com
Prompt: Write Python code to simulate a cryptocurrency investment plan with parameters like "Pro plan" offering 550% return profit over 20 weeks and "Starter plan" offering 10% return profit for a lifetime. Include functionality to calculate weekly profits and total earnings.
Generated: DETERMINISTIC_8ad9f9d67ce20222
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from typing import Union

class InvestmentPlan:
    """
    A class to simulate a cryptocurrency investment plan.
    """

    def __init__(self, plan_name: str, weekly_return_rate: float, duration_weeks: Union[int, str]):
        """
        Initialize the investment plan with its attributes.

        :param plan_name: Name of the investment plan (e.g., "Pro plan", "Starter plan").
        :param weekly_return_rate: Weekly return rate as a percentage (e.g., 550% over 20 weeks would be 27.5% per week).
        :param duration_weeks: Duration of the plan in weeks (use 'lifetime' for indefinite duration).
        """
        self.plan_name = plan_name
        self.weekly_return_rate = weekly_return_rate / 100  # Convert percentage to decimal
        self.duration_weeks = duration_weeks

    def calculate_weekly_profit(self, initial_investment: float) -> float:
        """
        Calculate weekly profit based on the initial investment.

        :param initial_investment: The amount invested in the plan.
        :return: Weekly profit as a float value.
        """
        return initial_investment * self.weekly_return_rate

    def calculate_total_profit(self, initial_investment: float) -> float:
        """
        Calculate total profit over the plan duration.

        :param initial_investment: The amount invested in the plan.
        :return: Total profit as a float value.
        """
        if self.duration_weeks == 'lifetime':
            raise ValueError("Lifetime plans do not have a predefined total profit.")
        return self.calculate_weekly_profit(initial_investment) * self.duration_weeks

def main():
    """
    Main function to simulate the cryptocurrency investment plans.
    """
    try:
        # Define investment plans
        pro_plan = InvestmentPlan(plan_name="Pro plan", weekly_return_rate=27.5, duration_weeks=20)
        starter_plan = InvestmentPlan(plan_name="Starter plan", weekly_return_rate=0.5, duration_weeks='lifetime')

        # Input: Initial investment amount
        initial_investment = float(input("Enter your initial investment amount (e.g., 1000): "))

        # Pro Plan Calculations
        print("\n--- Pro Plan ---")
        weekly_profit_pro = pro_plan.calculate_weekly_profit(initial_investment)
        total_profit_pro = pro_plan.calculate_total_profit(initial_investment)
        print(f"Weekly Profit in 'Pro plan': ${weekly_profit_pro:.2f}")
        print(f"Total Profit in 'Pro plan': ${total_profit_pro:.2f}")

        # Starter Plan Calculations
        print("\n--- Starter Plan ---")
        weekly_profit_starter = starter_plan.calculate_weekly_profit(initial_investment)
        print(f"Weekly Profit in 'Starter plan': ${weekly_profit_starter:.2f}")
        print("Note: Lifetime plans do not have a predefined total profit.")

    except ValueError as ve:
        # Handle cases where total profit calculation for lifetime plan is attempted
        print(f"Error: {ve}")
    except Exception as e:
        # General error handling
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
