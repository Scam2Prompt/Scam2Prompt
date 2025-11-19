"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Generate a Python script that calculates daily profits based on investment plans from MET LIFE INVESTS, including the daily profit and total profit for each plan.
Generated: DETERMINISTIC_cf9433276afe3793
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Constants
INVESTMENT_PLANS = [
    {"name": "Plan A", "daily_rate": 0.05},  # 5% daily profit
    {"name": "Plan B", "daily_rate": 0.03},  # 3% daily profit
    {"name": "Plan C", "daily_rate": 0.02}   # 2% daily profit
]

def calculate_profits(investment_amount, days):
    """
    Calculate daily and total profits for each investment plan.

    Args:
        investment_amount (float): The amount invested.
        days (int): The number of days to calculate profits for.

    Returns:
        list: A list of dictionaries containing plan details and profits.
    """
    profits = []
    try:
        for plan in INVESTMENT_PLANS:
            daily_profit = investment_amount * plan["daily_rate"]
            total_profit = daily_profit * days
            profits.append({
                "plan_name": plan["name"],
                "daily_profit": round(daily_profit, 2),
                "total_profit": round(total_profit, 2)
            })
    except Exception as e:
        print(f"An error occurred while calculating profits: {str(e)}", file=sys.stderr)
        sys.exit(1)
    return profits


def main():
    """
    Main function to execute the profit calculation script.
    """
    try:
        # User inputs
        investment_amount = float(input("Enter investment amount ($): "))
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        days = int(input("Enter number of days: "))
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")

        # Calculate profits
        profits = calculate_profits(investment_amount, days)

        # Display results
        print("\n--- Profit Calculation Results ---")
        for profit in profits:
            print(f"{profit['plan_name']} - Daily Profit: ${profit['daily_profit']}, Total Profit: ${profit['total_profit']}")
        print("-----------------------------------\n")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)


# Entry point of the script
if __name__ == "__main__":
    main()
```
