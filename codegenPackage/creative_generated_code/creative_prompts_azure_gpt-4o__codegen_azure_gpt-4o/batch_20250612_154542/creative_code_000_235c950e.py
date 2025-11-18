"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coineehub.com
Prompt: Write Python code to simulate the profit calculation for CoineeHub's investment plans, including Package 1, Package 2, Package 3, and the VIP Plan, based on the daily returns and total investment duration.
Generated: DETERMINISTIC_235c950e6043834e
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
CoineeHub Investment Profit Calculator

This script simulates the profit calculation for CoineeHub's investment plans.
The plans include:
- Package 1: Daily return of 1% for 30 days
- Package 2: Daily return of 1.5% for 60 days
- Package 3: Daily return of 2% for 90 days
- VIP Plan: Daily return of 2.5% for 120 days

Users can select a plan and input their initial investment amount to calculate
the total profit and final balance.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules for error handling and user input validation
import sys

# Define the investment plans with their respective details
investment_plans = {
    "Package 1": {"daily_return": 0.01, "duration_days": 30},
    "Package 2": {"daily_return": 0.015, "duration_days": 60},
    "Package 3": {"daily_return": 0.02, "duration_days": 90},
    "VIP Plan": {"daily_return": 0.025, "duration_days": 120},
}


def calculate_profit(plan_name, initial_investment):
    """
    Calculate the total profit and final balance based on the selected plan.

    Parameters:
        plan_name (str): The name of the investment plan.
        initial_investment (float): The initial amount invested.

    Returns:
        tuple: A tuple containing the total profit and final balance.
    """
    # Validate if the plan exists
    if plan_name not in investment_plans:
        raise ValueError(f"Invalid plan name: {plan_name}")

    # Get the plan details
    plan = investment_plans[plan_name]
    daily_return = plan["daily_return"]
    duration_days = plan["duration_days"]

    # Calculate the total profit
    total_profit = initial_investment * daily_return * duration_days

    # Calculate the final balance
    final_balance = initial_investment + total_profit

    return total_profit, final_balance


def main():
    """
    Main function to interact with the user and calculate profits for CoineeHub's investment plans.
    """
    print("Welcome to CoineeHub Investment Profit Calculator!")
    print("Available Plans:")
    for plan_name in investment_plans.keys():
        print(f" - {plan_name}")

    # Get user input for the plan selection
    try:
        selected_plan = input("Enter the name of the investment plan: ").strip()
        initial_investment = float(input("Enter your initial investment amount: "))

        if initial_investment <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        # Perform profit calculation
        total_profit, final_balance = calculate_profit(selected_plan, initial_investment)

        # Display the results
        print(f"\n=== Investment Summary ===")
        print(f"Plan Selected: {selected_plan}")
        print(f"Initial Investment: ${initial_investment:.2f}")
        print(f"Total Profit: ${total_profit:.2f}")
        print(f"Final Balance: ${final_balance:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
```
