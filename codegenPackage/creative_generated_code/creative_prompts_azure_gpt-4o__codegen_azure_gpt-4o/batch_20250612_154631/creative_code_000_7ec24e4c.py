"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidcointrades.org
Prompt: Write a Python script to calculate investment profits using the specific profit percentages and plans (Starter, Basic, Golden, VIP) described on the RapidCoinTrades website. Include functionality for user input of deposit amount and plan selection.
Generated: DETERMINISTIC_7ec24e4c39dd8408
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_calculator.py

# Import necessary modules
import sys

def calculate_profit(deposit, plan):
    """
    Calculate investment profit based on the selected plan and deposit amount.

    Args:
        deposit (float): The amount of money invested.
        plan (str): The investment plan selected.

    Returns:
        float: The profit earned based on the selected plan.
    """
    # Profit percentages based on RapidCoinTrades plans
    plans = {
        "Starter": 5,  # 5% profit
        "Basic": 10,   # 10% profit
        "Golden": 20,  # 20% profit
        "VIP": 30      # 30% profit
    }

    if plan not in plans:
        raise ValueError(f"Invalid plan selected: {plan}. Please choose from {', '.join(plans.keys())}.")

    # Calculate profit based on the percentage
    profit_percentage = plans[plan]
    profit = (deposit * profit_percentage) / 100
    return profit


def main():
    """
    Main function to handle user input and calculate investment profits.
    """
    print("Welcome to the RapidCoinTrades Investment Profit Calculator!")
    print("Available plans: Starter (5%), Basic (10%), Golden (20%), VIP (30%)\n")

    try:
        # Get deposit amount from the user
        deposit = float(input("Enter the deposit amount (in dollars): "))
        if deposit <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        # Get investment plan from the user
        plan = input("Enter the investment plan (Starter, Basic, Golden, VIP): ").strip()

        # Calculate profit
        profit = calculate_profit(deposit, plan)
        print(f"\nWith a deposit of ${deposit:.2f} under the '{plan}' plan, your profit will be ${profit:.2f}.")
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
    except Exception as e:
        # Catch all other exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the RapidCoinTrades Investment Profit Calculator!")


if __name__ == "__main__":
    # Entry point for the program
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(1)
```
