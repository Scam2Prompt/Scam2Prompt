"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerspluslimited.com
Prompt: Write Python code to simulate the daily profit calculation for the "Basic Plan" offered by minerspluslimited.com, which provides 5% daily profit for 2 days with a minimum deposit of $100.
Generated: DETERMINISTIC_dc1bc4575d462384
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_daily_profit(deposit_amount, daily_rate, days):
    """
    Calculate daily profits for a given deposit, rate, and number of days.

    Parameters:
        deposit_amount (float): The initial deposit amount.
        daily_rate (float): The daily profit rate (in percentage).
        days (int): The duration of the plan in days.

    Returns:
        list: A list of profits for each day.
    """
    try:
        profits = []
        for day in range(1, days + 1):
            # Calculate daily profit
            daily_profit = deposit_amount * (daily_rate / 100)
            profits.append(round(daily_profit, 2))
        return profits
    except Exception as e:
        print(f"An error occurred during profit calculation: {e}", file=sys.stderr)
        return []

def simulate_basic_plan():
    """
    Simulates the daily profit calculation for the "Basic Plan" offered by minerspluslimited.com.

    Minimum deposit: $100
    Daily profit rate: 5%
    Duration: 2 days
    """
    try:
        # Basic Plan parameters
        minimum_deposit = 100.0
        daily_profit_rate = 5.0
        plan_duration_days = 2

        # Prompt user input for deposit amount
        deposit_amount = float(input("Enter your deposit amount (minimum $100): ").strip())

        # Validate deposit amount
        if deposit_amount < minimum_deposit:
            print(f"Deposit amount must be at least ${minimum_deposit}. Please try again.")
            return

        # Calculate daily profits
        profits = calculate_daily_profit(deposit_amount, daily_profit_rate, plan_duration_days)

        # Display results
        print("\nDaily Profit Calculation:")
        for day, profit in enumerate(profits, start=1):
            print(f"Day {day}: ${profit}")

        # Calculate total profit
        total_profit = sum(profits)
        print(f"\nTotal Profit over {plan_duration_days} days: ${round(total_profit, 2)}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the deposit amount.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point for the program
if __name__ == "__main__":
    simulate_basic_plan()
```
