"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Write a Python script to simulate daily ROI calculations for the investment plans offered by Access Link Limited, including the Beginner, Standard, Royal, and Diamond plans.
Generated: DETERMINISTIC_2c731f79ccea9328
Batch ID: 20250612_154603
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
    """
    Represents an investment plan with daily ROI calculations.
    """
    def __init__(self, name, daily_roi_percentage, minimum_investment, maximum_investment):
        """
        Initialize the investment plan.

        :param name: Name of the investment plan.
        :param daily_roi_percentage: Daily ROI percentage for the plan.
        :param minimum_investment: Minimum investment amount for the plan.
        :param maximum_investment: Maximum investment amount for the plan.
        """
        self.name = name
        self.daily_roi_percentage = daily_roi_percentage
        self.minimum_investment = minimum_investment
        self.maximum_investment = maximum_investment

    def calculate_daily_roi(self, investment_amount):
        """
        Calculate the daily ROI for a given investment amount.

        :param investment_amount: The amount invested.
        :return: Daily ROI value.
        """
        if investment_amount < self.minimum_investment:
            raise ValueError(f"Investment amount is below the minimum required for {self.name} plan.")
        if investment_amount > self.maximum_investment:
            raise ValueError(f"Investment amount exceeds the maximum allowed for {self.name} plan.")
        
        # Calculate ROI
        daily_roi = (investment_amount * self.daily_roi_percentage) / 100
        return daily_roi


def main():
    """
    Main function to simulate daily ROI calculations for investment plans.
    """

    try:
        # Define the investment plans
        plans = [
            InvestmentPlan("Beginner", daily_roi_percentage=1.5, minimum_investment=100, maximum_investment=1000),
            InvestmentPlan("Standard", daily_roi_percentage=2.0, minimum_investment=1001, maximum_investment=5000),
            InvestmentPlan("Royal", daily_roi_percentage=2.5, minimum_investment=5001, maximum_investment=20000),
            InvestmentPlan("Diamond", daily_roi_percentage=3.0, minimum_investment=20001, maximum_investment=100000)
        ]

        # Simulate ROI calculations
        print("Welcome to Access Link Limited ROI Calculator!")
        investment_amount = float(input("Enter the investment amount: "))

        print("\nAvailable Investment Plans:")
        for plan in plans:
            print(f"{plan.name}: {plan.daily_roi_percentage}% daily ROI ({plan.minimum_investment}-{plan.maximum_investment})")

        plan_name = input("\nChoose your investment plan (Beginner, Standard, Royal, Diamond): ").strip().capitalize()

        # Find the selected plan
        selected_plan = next((plan for plan in plans if plan.name == plan_name), None)
        if not selected_plan:
            print("Invalid plan selection. Please try again.")
            sys.exit(1)

        # Calculate and display the daily ROI
        daily_roi = selected_plan.calculate_daily_roi(investment_amount)
        print(f"\nInvestment Plan: {selected_plan.name}")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Daily ROI: ${daily_roi:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using Access Link Limited ROI Calculator!")

if __name__ == "__main__":
    main()
```
