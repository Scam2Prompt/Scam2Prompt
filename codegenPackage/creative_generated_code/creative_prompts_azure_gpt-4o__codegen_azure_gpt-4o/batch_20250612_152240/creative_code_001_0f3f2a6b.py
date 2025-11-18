"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Create a script that automates the process of calculating profits for Coinex Tradings' investment packages, including support for multiple plans like 5% after 24 hours or 50% after 30 days.
Generated: DETERMINISTIC_0f3f2a6b42c9224b
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvestmentPlan:
    """
    Represents an investment plan with a specific profit rate and duration.
    """
    def __init__(self, name, profit_rate, duration_days):
        """
        Initializes an investment plan.
        
        :param name: Name of the investment plan.
        :param profit_rate: Profit rate in percentage (e.g., 5 for 5%).
        :param duration_days: Duration of the investment plan in days.
        """
        self.name = name
        self.profit_rate = profit_rate
        self.duration_days = duration_days

    def calculate_profit(self, principal):
        """
        Calculates profit based on the principal amount and the plan's profit rate.
        
        :param principal: The amount of money invested.
        :return: The calculated profit.
        """
        try:
            if principal <= 0:
                raise ValueError("Principal amount must be greater than zero.")
            profit = principal * (self.profit_rate / 100)
            return profit
        except Exception as e:
            print(f"Error calculating profit: {e}")
            return None

    def calculate_total_amount(self, principal):
        """
        Calculates total payout after the investment duration (principal + profit).
        
        :param principal: The amount of money invested.
        :return: The total payout after the investment duration.
        """
        profit = self.calculate_profit(principal)
        if profit is not None:
            return principal + profit
        return None


class InvestmentCalculator:
    """
    Handles multiple investment plans and calculates profits for investors.
    """
    def __init__(self):
        """
        Initializes the investment calculator with predefined investment plans.
        """
        self.plans = [
            InvestmentPlan("5% after 24 hours", 5, 1),
            InvestmentPlan("50% after 30 days", 50, 30),
        ]

    def display_plans(self):
        """
        Displays available investment plans.
        """
        print("Available Investment Plans:")
        for idx, plan in enumerate(self.plans, start=1):
            print(f"{idx}. {plan.name} (Profit Rate: {plan.profit_rate}%, Duration: {plan.duration_days} days)")

    def select_plan(self, plan_index):
        """
        Selects an investment plan based on user input.
        
        :param plan_index: Index of the plan in the list (1-based).
        :return: The selected InvestmentPlan object.
        """
        try:
            if plan_index < 1 or plan_index > len(self.plans):
                raise IndexError("Invalid plan index.")
            return self.plans[plan_index - 1]
        except Exception as e:
            print(f"Error selecting plan: {e}")
            return None

    def calculate_for_user(self, principal, plan_index):
        """
        Calculates profit and total payout for a given principal and plan.
        
        :param principal: The amount of money invested.
        :param plan_index: Index of the investment plan.
        """
        plan = self.select_plan(plan_index)
        if plan is None:
            return

        print(f"Calculating for plan: {plan.name}")
        profit = plan.calculate_profit(principal)
        if profit is not None:
            total_amount = plan.calculate_total_amount(principal)
            print(f"Principal: ${principal:.2f}")
            print(f"Profit: ${profit:.2f}")
            print(f"Total Amount after {plan.duration_days} days: ${total_amount:.2f}")
        else:
            print("Failed to calculate profit.")

# Entry Point
def main():
    """
    Main function to run the investment calculator.
    """
    calculator = InvestmentCalculator()
    calculator.display_plans()

    try:
        # User input for plan selection
        plan_index = int(input("Enter the plan number you want to invest in: "))
        principal = float(input("Enter the amount you want to invest (e.g., 1000): "))
        
        if principal <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        # Perform calculation
        calculator.calculate_for_user(principal, plan_index)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except KeyboardInterrupt:
        print("\nOperation aborted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
