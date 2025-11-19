"""
Generated Code Metadata:
========================
Original URL: https://syncexperttrade.com
Prompt: "Generate a Python script to calculate potential profits from forex trading based on SyncExpertTrade's investment plans, including Bronze, Silver, Gold, and Premium accounts."
Generated: DETERMINISTIC_3258d357b89ec1f4
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Forex Trading Profit Calculator

This script calculates potential profits from forex trading based on SyncExpertTrade's investment plans.
The investment plans include Bronze, Silver, Gold, and Premium accounts, each with different profit rates.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_profit(investment_amount, plan):
    """
    Calculate potential profit based on the investment plan.

    Parameters:
        investment_amount (float): The amount of money invested.
        plan (str): The investment plan (Bronze, Silver, Gold, Premium).

    Returns:
        float: The calculated profit.
    """
    # Define profit rates for each plan
    profit_rates = {
        "Bronze": 0.05,  # 5% profit
        "Silver": 0.10,  # 10% profit
        "Gold": 0.15,    # 15% profit
        "Premium": 0.20  # 20% profit
    }

    # Validate the investment plan
    if plan not in profit_rates:
        raise ValueError(f"Invalid plan '{plan}'. Valid plans are: {', '.join(profit_rates.keys())}")

    # Calculate profit
    profit = investment_amount * profit_rates[plan]
    return profit

def main():
    """
    Main function to handle user input and calculate profits.
    """
    try:
        # Prompt user for investment amount
        investment_amount = float(input("Enter your investment amount (e.g., 1000): "))
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        # Prompt user for investment plan
        plan = input("Enter your investment plan (Bronze, Silver, Gold, Premium): ").capitalize()

        # Calculate profit
        profit = calculate_profit(investment_amount, plan)

        # Display the result
        print(f"\nInvestment Plan: {plan}")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Potential Profit: ${profit:.2f}")

    except ValueError as ve:
        # Handle invalid input
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
