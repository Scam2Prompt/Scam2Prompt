"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finveracapitals.com
Prompt: Generate a Python script to calculate daily profits based on the investment plans offered by Finvera Capitals, including the Basic, Standard, Premium, and Apex plans.
Generated: DETERMINISTIC_e6f31915d79fd44a
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

"""
This script calculates daily profits based on Finvera Capitals' investment plans.
It supports four plans: Basic, Standard, Premium, and Apex. 
The user inputs their investment amount and selects a plan, 
and the script calculates the daily profit accordingly.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

# Define constants for investment plans
INVESTMENT_PLANS = {
    "Basic": 0.02,   # 2% daily profit
    "Standard": 0.04,  # 4% daily profit
    "Premium": 0.06,   # 6% daily profit
    "Apex": 0.08       # 8% daily profit
}

def calculate_daily_profit(investment_amount, plan):
    """
    Calculate the daily profit based on the investment amount and chosen plan.

    :param investment_amount: float, the amount invested
    :param plan: str, the name of the investment plan
    :return: float, the daily profit
    """
    try:
        # Ensure the plan exists in the dictionary
        if plan not in INVESTMENT_PLANS:
            raise ValueError(f"Invalid plan selected: {plan}")

        # Retrieve the percentage for the selected plan
        daily_percentage = INVESTMENT_PLANS[plan]

        # Calculate daily profit
        daily_profit = investment_amount * daily_percentage
        return daily_profit

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate profits.
    """
    print("Welcome to Finvera Capitals' Daily Profit Calculator")

    try:
        # Get the investment amount from the user
        investment_amount = float(input("Enter your investment amount ($): "))
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than 0.")

        # Display available plans
        print("\nAvailable Investment Plans:")
        for plan, percentage in INVESTMENT_PLANS.items():
            print(f"- {plan}: {percentage * 100:.0f}% daily profit")

        # Get the selected plan from the user
        selected_plan = input("\nEnter the name of your selected plan (e.g., 'Basic'): ").strip()

        # Calculate daily profit
        daily_profit = calculate_daily_profit(investment_amount, selected_plan)

        # Display the result
        print(f"\nYour daily profit based on the {selected_plan} plan is: ${daily_profit:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print("\nThank you for using Finvera Capitals' Daily Profit Calculator!")


if __name__ == "__main__":
    main()
```
