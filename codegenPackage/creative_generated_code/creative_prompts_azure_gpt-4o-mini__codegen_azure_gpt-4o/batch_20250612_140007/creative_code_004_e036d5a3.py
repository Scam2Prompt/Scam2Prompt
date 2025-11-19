"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradezeenetwork.com
Prompt: How do the profit accruals work for different investment plans on Tradezeenetwork, and can you illustrate this with an example calculation?
Generated: DETERMINISTIC_e036d5a397e27139
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Investment profit accrual calculation for Tradezeenetwork
# This program calculates the profit for different investment plans based on user input.
# It supports multiple investment plans with fixed interest rates and durations.

class InvestmentPlan:
    """
    Class representing an investment plan.
    Attributes:
        name (str): Name of the investment plan.
        interest_rate (float): Interest rate (as a percentage) for the plan.
        duration (int): Duration of the plan in days.
    """
    def __init__(self, name, interest_rate, duration):
        self.name = name
        self.interest_rate = interest_rate
        self.duration = duration


class TradezeenetworkProfitCalculator:
    """
    Calculator for profit accruals based on Tradezeenetwork investment plans.
    """
    def __init__(self):
        # Define available investment plans
        self.investment_plans = [
            InvestmentPlan("Basic Plan", interest_rate=5, duration=30),
            InvestmentPlan("Silver Plan", interest_rate=7, duration=60),
            InvestmentPlan("Gold Plan", interest_rate=10, duration=90),
        ]

    def calculate_profit(self, plan_name: str, principal: float) -> float:
        """
        Calculate profit based on the investment plan and principal amount.

        Args:
            plan_name (str): Name of the investment plan.
            principal (float): Amount of money invested.

        Returns:
            float: Total profit accrued for the investment duration.

        Raises:
            ValueError: If the investment plan is invalid or not found.
        """
        # Find the investment plan by name
        plan = next((p for p in self.investment_plans if p.name == plan_name), None)
        if not plan:
            raise ValueError(f"Invalid investment plan: {plan_name}")

        # Calculate profit: (Principal * Interest Rate * Duration) / 100
        profit = (principal * plan.interest_rate * plan.duration) / (365 * 100)

        return profit

    def display_available_plans(self):
        """
        Display all available investment plans.
        """
        print("Available Investment Plans:")
        for plan in self.investment_plans:
            print(f"- {plan.name}: {plan.interest_rate}% interest rate, {plan.duration} days duration")


# Example usage
if __name__ == "__main__":
    # Create calculator instance
    calculator = TradezeenetworkProfitCalculator()

    # Display available plans
    calculator.display_available_plans()

    try:
        # User input: Plan name and principal amount
        selected_plan = input("Enter the name of the investment plan: ").strip()
        principal_amount = float(input("Enter the principal amount (e.g., 1000): "))

        # Calculate profit
        profit = calculator.calculate_profit(selected_plan, principal_amount)

        # Display result
        print(f"Total profit for the '{selected_plan}' plan: ${profit:.2f}")
    except ValueError as e:
        # Handle invalid input or errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
