"""
Generated Code Metadata:
========================
Original URL: https://binarygoldenoptions.com
Prompt: "Write a Python script to calculate the profit from investing $1000 in a plan that returns 10.95% every 24 hours, as described in the investment plans of Binary Golden Options."
Generated: DETERMINISTIC_d795802830cbf16a
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import List, Tuple

def calculate_profit(
    initial_investment: float,
    daily_return_rate: float,
    days: int
) -> List[Tuple[int, float]]:
    """
    Calculate the profit from an investment with a fixed daily return rate over a given period.

    Args:
        initial_investment: Initial amount invested (in dollars).
        daily_return_rate: Daily return rate (as a decimal, e.g., 0.1095 for 10.95%).
        days: Number of days to calculate the profit for.

    Returns:
        A list of tuples where each tuple contains:
        - Day number (starting from 1)
        - Total amount (initial investment + profit) at the end of that day

    Raises:
        ValueError: If any input is invalid (negative or zero investment, negative days).
    """
    if initial_investment <= 0:
        raise ValueError("Initial investment must be a positive number.")
    if daily_return_rate < 0:
        raise ValueError("Daily return rate cannot be negative.")
    if days < 0:
        raise ValueError("Number of days cannot be negative.")

    results = []
    current_amount = initial_investment

    for day in range(1, days + 1):
        current_amount *= (1 + daily_return_rate)
        results.append((day, round(current_amount, 2)))

    return results

def main():
    try:
        initial_investment = 1000.0
        daily_return_rate = 0.1095  # 10.95%
        investment_period_days = int(input("Enter the number of days to calculate profit for: "))

        if investment_period_days <= 0:
            print("Error: Number of days must be a positive integer.", file=sys.stderr)
            sys.exit(1)

        profit_data = calculate_profit(initial_investment, daily_return_rate, investment_period_days)

        print("\nDay\tTotal Amount ($)")
        print("----------------------")
        for day, amount in profit_data:
            print(f"{day}\t{amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
