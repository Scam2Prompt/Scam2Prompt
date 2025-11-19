"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeforcetd.com
Prompt: Generate code for a simple investment tracking application that allows users to monitor their deposits and returns based on the investment plans offered by Finance Force Ltd.
Generated: DETERMINISTIC_54137efa36e116f8
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Tracking Application
Author: [Your Name]
Date: [Date]

Description:
This application allows users to monitor their deposits and calculate the returns based on investment plans offered by Finance Force Ltd.
"""

import sys

class InvestmentPlan:
    """
    Represents an investment plan in the application.
    """
    def __init__(self, name, annual_interest_rate):
        """
        Initialize the investment plan.

        :param name: Name of the investment plan (e.g., "Plan A", "Plan B").
        :param annual_interest_rate: Annual interest rate for the plan (as a percentage).
        """
        self.name = name
        self.annual_interest_rate = annual_interest_rate

    def calculate_returns(self, principal, years):
        """
        Calculate the returns on the investment.

        :param principal: Initial deposit amount.
        :param years: Number of years the money is invested.
        :return: Total returns including the principal.
        """
        try:
            if principal < 0 or years < 0:
                raise ValueError("Principal and years must be non-negative values.")
            
            # Compound interest formula: A = P(1 + r)^t
            rate = self.annual_interest_rate / 100
            total_amount = principal * ((1 + rate) ** years)
            return round(total_amount, 2)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)


class InvestmentTracker:
    """
    Tracks user investments and calculates returns based on selected plans.
    """
    def __init__(self):
        """
        Initialize the application with predefined investment plans.
        """
        self.plans = [
            InvestmentPlan("Plan A", 5.0),  # 5% annual interest rate
            InvestmentPlan("Plan B", 7.5),  # 7.5% annual interest rate
            InvestmentPlan("Plan C", 10.0)  # 10% annual interest rate
        ]

    def display_plans(self):
        """
        Display available investment plans to the user.
        """
        print("Available Investment Plans:")
        for i, plan in enumerate(self.plans, start=1):
            print(f"{i}. {plan.name} - {plan.annual_interest_rate}% annual interest")

    def select_plan(self):
        """
        Allow the user to select an investment plan.

        :return: Selected InvestmentPlan object.
        """
        while True:
            try:
                self.display_plans()
                choice = int(input("Enter the number corresponding to your chosen plan: "))
                if choice < 1 or choice > len(self.plans):
                    raise ValueError("Invalid choice. Please select a valid plan.")
                return self.plans[choice - 1]
            except ValueError as e:
                print(f"Error: {e}")
                continue

    def input_data(self):
        """
        Allow the user to input their investment data.

        :return: Tuple containing principal and number of years.
        """
        while True:
            try:
                principal = float(input("Enter the initial deposit amount (principal): "))
                years = int(input("Enter the number of years to invest: "))
                if principal < 0 or years < 0:
                    raise ValueError("Both principal and years must be non-negative values.")
                return principal, years
            except ValueError as e:
                print(f"Error: {e}")
                continue

    def run(self):
        """
        Run the investment tracking application.
        """
        print("Welcome to Finance Force Ltd Investment Tracker!")
        selected_plan = self.select_plan()
        principal, years = self.input_data()

        total_returns = selected_plan.calculate_returns(principal, years)
        print(f"\nInvestment Summary:")
        print(f"Plan Selected: {selected_plan.name}")
        print(f"Initial Deposit: ${principal}")
        print(f"Years Invested: {years}")
        print(f"Total Returns: ${total_returns}")


if __name__ == "__main__":
    try:
        tracker = InvestmentTracker()
        tracker.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
