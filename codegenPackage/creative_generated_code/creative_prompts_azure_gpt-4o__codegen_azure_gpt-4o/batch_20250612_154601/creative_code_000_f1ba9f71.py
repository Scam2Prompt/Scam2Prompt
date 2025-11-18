"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Write Python code to calculate daily profits for the investment plans offered by Finance Impact Pro, including Basic, Silver, Gold, and Ultimate plans, based on their guaranteed profit percentages and durations.
Generated: DETERMINISTIC_f1ba9f71017b351a
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate daily profits for investment plans offered by Finance Impact Pro

# Importing required modules
import sys

def calculate_daily_profit(investment_amount, profit_percentage, duration_days):
    """
    Function to calculate daily profits for an investment plan.

    Parameters:
    - investment_amount (float): The amount invested in the plan.
    - profit_percentage (float): The guaranteed profit percentage of the plan (per day).
    - duration_days (int): Duration of the plan in days.

    Returns:
    - daily_profit (float): The profit earned per day.
    - total_profit (float): The total profit earned at the end of the plan's duration.
    """
    try:
        # Validate input types
        if not isinstance(investment_amount, (int, float)) or investment_amount <= 0:
            raise ValueError("Investment amount must be a positive number.")
        if not isinstance(profit_percentage, (int, float)) or profit_percentage <= 0:
            raise ValueError("Profit percentage must be a positive number.")
        if not isinstance(duration_days, int) or duration_days <= 0:
            raise ValueError("Duration days must be a positive integer.")

        # Calculate daily profit
        daily_profit = (investment_amount * (profit_percentage / 100))
        # Calculate total profit
        total_profit = daily_profit * duration_days

        return daily_profit, total_profit

    except Exception as e:
        # Handle exceptions gracefully
        print(f"Error: {e}", file=sys.stderr)
        return None, None

def main():
    """
    Main function to demonstrate the calculation of daily profits for different investment plans.
    """
    # Define investment plans
    investment_plans = {
        "Basic": {"profit_percentage": 1.5, "duration_days": 30},
        "Silver": {"profit_percentage": 2.0, "duration_days": 45},
        "Gold": {"profit_percentage": 2.5, "duration_days": 60},
        "Ultimate": {"profit_percentage": 3.0, "duration_days": 90}
    }

    # Input investment amount
    try:
        investment_amount = float(input("Enter the investment amount: "))
        if investment_amount <= 0:
            raise ValueError("Investment amount must be a positive number.")
    except ValueError as ve:
        print(f"Invalid input: {ve}", file=sys.stderr)
        return

    print("\nProfit calculations for different investment plans:\n")

    # Iterate through the plans and calculate profits
    for plan_name, plan_details in investment_plans.items():
        daily_profit, total_profit = calculate_daily_profit(
            investment_amount,
            plan_details["profit_percentage"],
            plan_details["duration_days"]
        )

        if daily_profit is not None and total_profit is not None:
            print(f"Plan: {plan_name}")
            print(f"  Daily Profit: ${daily_profit:.2f}")
            print(f"  Total Profit after {plan_details['duration_days']} days: ${total_profit:.2f}")
            print("-" * 40)

if __name__ == "__main__":
    main()
```
