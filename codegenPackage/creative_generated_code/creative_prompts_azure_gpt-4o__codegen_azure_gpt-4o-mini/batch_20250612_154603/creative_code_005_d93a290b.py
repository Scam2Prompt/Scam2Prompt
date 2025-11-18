"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Write a script to calculate investment growth based on the daily interest rates provided by Access Link Limited's investment plans (e.g., Beginner Plan: 2%, Standard Plan: 3%).
Generated: DETERMINISTIC_d93a290b5203667a
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_growth.py

class InvestmentPlan:
    """
    Class to represent an investment plan with a specific daily interest rate.
    """
    
    def __init__(self, name, daily_interest_rate):
        """
        Initialize the investment plan with name and daily interest rate.
        
        :param name: Name of the investment plan
        :param daily_interest_rate: Daily interest rate as a percentage (e.g., 2 for 2%)
        """
        self.name = name
        self.daily_interest_rate = daily_interest_rate / 100  # Convert percentage to decimal
        
    def calculate_growth(self, principal, days):
        """
        Calculate the total amount after a certain number of days with daily compounding interest.

        :param principal: Initial investment amount
        :param days: Number of days the investment is held
        :return: Total amount after interest
        """
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        if days < 0:
            raise ValueError("Number of days cannot be negative.")
        
        total_amount = principal * (1 + self.daily_interest_rate) ** days
        return total_amount


def main():
    """
    Main function to demonstrate investment growth calculation.
    """
    # Define investment plans
    beginner_plan = InvestmentPlan("Beginner Plan", 2)
    standard_plan = InvestmentPlan("Standard Plan", 3)

    # Input: Principal amount and duration in days
    try:
        principal = float(input("Enter the principal investment amount: "))
        days = int(input("Enter the number of days for investment: "))

        # Calculate growth for each plan
        beginner_growth = beginner_plan.calculate_growth(principal, days)
        standard_growth = standard_plan.calculate_growth(principal, days)

        # Output the results
        print(f"Total amount after {days} days in the {beginner_plan.name}: ${beginner_growth:.2f}")
        print(f"Total amount after {days} days in the {standard_plan.name}: ${standard_growth:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
