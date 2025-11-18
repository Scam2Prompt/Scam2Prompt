"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbullminingpro.com
Prompt: Write Python code to calculate investment returns based on the guaranteed profit percentages and durations provided in BitBullMiningPro's investment plans (e.g., Silver, Bronze, Gold, Ultimate).
Generated: DETERMINISTIC_4edd68a0cc6c9c00
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Investment Returns Calculator for BitBullMiningPro Plans

# Import required modules
from typing import Dict, Tuple

class InvestmentPlanCalculator:
    """
    A class to calculate investment returns for BitBullMiningPro's investment plans.
    """

    def __init__(self):
        # Define investment plans with their profit percentages and durations in days
        self.investment_plans = {
            "Silver": {"profit_percentage": 3, "duration_days": 30},
            "Bronze": {"profit_percentage": 5, "duration_days": 60},
            "Gold": {"profit_percentage": 7, "duration_days": 90},
            "Ultimate": {"profit_percentage": 10, "duration_days": 180},
        }

    def calculate_return(self, plan_name: str, initial_investment: float) -> Dict[str, float]:
        """
        Calculates the total returns based on the selected investment plan and initial investment.

        Args:
            plan_name (str): Name of the investment plan (e.g., 'Silver', 'Bronze', 'Gold', 'Ultimate').
            initial_investment (float): The amount of money invested.

        Returns:
            Dict[str, float]: A dictionary containing:
                - 'initial_investment': The original investment amount.
                - 'profit_percentage': The profit percentage of the plan.
                - 'duration_days': The duration of the investment plan in days.
                - 'total_profit': The total profit earned.
                - 'total_return': The total amount after the investment period.
        """
        try:
            # Validate input plan name
            if plan_name not in self.investment_plans:
                raise ValueError(f"Invalid plan name: '{plan_name}'. Available plans are: {', '.join(self.investment_plans.keys())}")

            # Validate input investment amount
            if initial_investment <= 0:
                raise ValueError("Initial investment must be greater than zero.")

            # Get the plan details
            plan_details = self.investment_plans[plan_name]

            # Calculate total profit and total return
            profit_percentage = plan_details["profit_percentage"]
            total_profit = (profit_percentage / 100) * initial_investment
            total_return = initial_investment + total_profit

            # Return the results as a dictionary
            return {
                "initial_investment": initial_investment,
                "profit_percentage": profit_percentage,
                "duration_days": plan_details["duration_days"],
                "total_profit": round(total_profit, 2),
                "total_return": round(total_return, 2),
            }

        except ValueError as ve:
            # Handle invalid input errors
            print(f"Error: {ve}")
        except Exception as e:
            # Handle unexpected errors
            print(f"An unexpected error occurred: {e}")

# Example usage of the InvestmentPlanCalculator
if __name__ == "__main__":
    calculator = InvestmentPlanCalculator()

    # Define test parameters
    plan_name = "Gold"
    initial_investment = 1000.0

    # Calculate and print investment returns
    result = calculator.calculate_return(plan_name, initial_investment)
    if result:
        print("Investment Details:")
        for key, value in result.items():
            print(f"{key}: {value}")
```
