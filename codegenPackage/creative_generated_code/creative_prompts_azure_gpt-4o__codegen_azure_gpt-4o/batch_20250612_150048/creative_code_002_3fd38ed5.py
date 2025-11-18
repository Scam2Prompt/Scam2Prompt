"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com.bartercorebase.com
Prompt: Generate code to create a profit calculator for investment plans, including features like daily return percentages and total capital, as described on Safe Wealth Haven.
Generated: DETERMINISTIC_3fd38ed55edb76eb
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Profit Calculator for Investment Plans
---------------------------------------
This program calculates the cumulative profit and total capital based on daily return percentages for given investment plans.
"""

# Import necessary modules
import sys

def get_daily_profit(initial_investment, daily_return_percentage, days):
    """
    Function to calculate the daily profit and total capital after the given number of days.

    Parameters:
        initial_investment (float): The initial investment amount.
        daily_return_percentage (float): The daily return percentage as a decimal (e.g., 0.05 for 5%).
        days (int): The number of days of the investment.

    Returns:
        float, float: Daily profit and total capital after the specified number of days.
    """
    try:
        # Validations
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if daily_return_percentage <= 0:
            raise ValueError("Daily return percentage must be greater than zero.")
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")

        # Calculate total capital after the investment period
        total_capital = initial_investment * ((1 + daily_return_percentage) ** days)
        
        # Calculate daily profit (profit for the last day)
        daily_profit = total_capital - (initial_investment * ((1 + daily_return_percentage) ** (days - 1)))
        
        return daily_profit, total_capital

    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        return None, None

def main():
    """
    Main function to interact with the user and calculate profits.
    """
    print("Welcome to Safe Wealth Haven Profit Calculator!")

    try:
        # User input
        initial_investment = float(input("Enter the initial investment amount ($): "))
        daily_return_percentage = float(input("Enter the daily return percentage (%): ")) / 100
        days = int(input("Enter the number of investment days: "))

        # Calculate profit
        daily_profit, total_capital = get_daily_profit(initial_investment, daily_return_percentage, days)

        if daily_profit is not None and total_capital is not None:
            # Display results
            print("\nInvestment Results:")
            print(f"Daily profit (on the last day): ${daily_profit:.2f}")
            print(f"Total capital after {days} days: ${total_capital:.2f}")
        else:
            print("Unable to calculate profit due to input errors.")

    except ValueError:
        print("Invalid input! Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
