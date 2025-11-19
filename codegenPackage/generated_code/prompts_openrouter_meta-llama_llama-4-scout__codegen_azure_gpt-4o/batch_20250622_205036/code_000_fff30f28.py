"""
Generated Code Metadata:
========================
Original URL: https://metlifeinvests.com
Prompt: "Generate a Python code snippet to calculate daily profit and total profit for an investment plan with a principal amount of $1000 and a 65-day plan period, similar to MET LIFE INVESTS investment plans."
Generated: DETERMINISTIC_fff30f28eb787013
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Tuple

def calculate_daily_and_total_profit(principal: float, days: int, daily_rate: float) -> Tuple[List[float], float]:
    """
    Calculate daily profit and total profit for an investment plan.

    Args:
        principal (float): The initial investment amount.
        days (int): The duration of the investment plan in days.
        daily_rate (float): The daily profit rate as a percentage (e.g., 1.5 for 1.5%).

    Returns:
        Tuple[List[float], float]: A tuple containing a list of daily profits and the total profit.
    """
    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if days <= 0:
        raise ValueError("Number of days must be greater than zero.")
    if daily_rate <= 0:
        raise ValueError("Daily rate must be greater than zero.")

    # Calculate daily profits
    daily_profits = []
    for day in range(1, days + 1):
        daily_profit = principal * (daily_rate / 100)
        daily_profits.append(daily_profit)

    # Calculate total profit
    total_profit = sum(daily_profits)

    return daily_profits, total_profit


# Main function to demonstrate the calculation
def main():
    # Investment parameters
    principal_amount = 1000.0  # Principal amount in dollars
    plan_period = 65          # Investment plan duration in days
    daily_profit_rate = 1.5   # Daily profit rate in percentage

    try:
        # Calculate daily and total profit
        daily_profits, total_profit = calculate_daily_and_total_profit(
            principal=principal_amount,
            days=plan_period,
            daily_rate=daily_profit_rate
        )

        # Display results
        print("Daily Profits:")
        for day, profit in enumerate(daily_profits, start=1):
            print(f"Day {day}: ${profit:.2f}")

        print(f"\nTotal Profit after {plan_period} days: ${total_profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
