"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aphatradespro.com
Prompt: Create a Python script to manage investment plans with varying durations (e.g., 7 days, 14 days, 1 month, 6 months) and calculate projected profits, as described in Aphatradespro's investment offerings.
Generated: DETERMINISTIC_17b855e4cf460814
Batch ID: 20250612_154632
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
    A class to represent an investment plan.

    Attributes:
        name (str): Name of the investment plan.
        duration (datetime.timedelta): Duration of the investment plan.
        annual_interest_rate (float): Annual interest rate as a percentage.
    """
    def __init__(self, name, duration_days, annual_interest_rate):
        """
        Initializes the InvestmentPlan instance.

        Args:
            name (str): Name of the investment plan.
            duration_days (int): Duration of the plan in days.
            annual_interest_rate (float): Annual interest rate as a percentage (e.g., 12.5 for 12.5%).
        """
        self.name = name
        self.duration = datetime.timedelta(days=duration_days)
        self.annual_interest_rate = annual_interest_rate

    def calculate_profit(self, principal):
        """
        Calculates the projected profit for the investment plan.

        Args:
            principal (float): The initial investment amount.

        Returns:
            float: Projected profit for the investment plan.
        """
        try:
            # Calculate daily interest rate from the annual interest rate
            daily_interest_rate = self.annual_interest_rate / 100 / 365
            
            # Total days of the investment plan
            total_days = self.duration.days
            
            # Projected profit
            profit = principal * daily_interest_rate * total_days
            return round(profit, 2)
        except Exception as e:
            print(f"Error calculating profit: {e}")
            return 0.0

    def __str__(self):
        """
        Returns a string representation of the investment plan.

        Returns:
            str: String representation of the investment plan.
        """
        return f"Plan: {self.name}, Duration: {self.duration.days} days, Annual Interest Rate: {self.annual_interest_rate}%"


def main():
    """
    Main function to manage investment plans and calculate profits.
    """
    try:
        # Define the available investment plans
        investment_plans = [
            InvestmentPlan("7-Day Plan", 7, 5.0),
            InvestmentPlan("14-Day Plan", 14, 6.0),
            InvestmentPlan("1-Month Plan", 30, 8.0),
            InvestmentPlan("6-Month Plan", 180, 12.5),
        ]

        # Prompt the user for their principal amount
        principal = float(input("Enter your investment amount: $"))

        if principal <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        print("\nAvailable Investment Plans:")
        for idx, plan in enumerate(investment_plans, start=1):
            print(f"{idx}. {plan}")

        # Ask the user to choose a plan
        choice = int(input("\nSelect an investment plan (1-4): "))
        if choice < 1 or choice > len(investment_plans):
            raise ValueError("Invalid choice. Please choose a valid plan.")

        # Get the selected plan
        selected_plan = investment_plans[choice - 1]

        # Calculate and display the projected profit
        profit = selected_plan.calculate_profit(principal)
        print(f"\nYou selected: {selected_plan}")
        print(f"Projected Profit: ${profit:.2f}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
