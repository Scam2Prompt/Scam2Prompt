"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Create a Python function to calculate the profit and withdrawal amounts for Astragoldbitx.org's investment plans, based on the initial deposit, daily return rate, and duration.
Generated: DETERMINISTIC_62febae02f5462c0
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_investment_returns(initial_deposit, daily_return_rate, duration):
    """
    Calculate the total profit and withdrawal amounts for an investment plan.

    Parameters:
    initial_deposit (float): The initial amount of money invested.
    daily_return_rate (float): The daily return rate as a percentage (e.g., 5 for 5%).
    duration (int): The number of days the investment is held.

    Returns:
    tuple: A tuple containing total_profit (float) and total_withdrawal (float).
    """

    # Input validation
    if not isinstance(initial_deposit, (int, float)) or initial_deposit <= 0:
        raise ValueError("Initial deposit must be a positive number.")
    if not isinstance(daily_return_rate, (int, float)) or daily_return_rate < 0:
        raise ValueError("Daily return rate must be a non-negative number.")
    if not isinstance(duration, int) or duration <= 0:
        raise ValueError("Duration must be a positive integer.")

    # Calculate daily return as a decimal
    daily_return = daily_return_rate / 100

    # Calculate total profit over the duration
    total_profit = initial_deposit * daily_return * duration

    # Calculate total withdrawal amount including the initial deposit
    total_withdrawal = initial_deposit + total_profit

    return total_profit, total_withdrawal


# Example usage:
if __name__ == "__main__":
    try:
        initial_investment = 1000.00  # Example initial deposit
        daily_rate = 5.0               # Example daily return rate (5%)
        investment_duration = 30        # Example duration in days

        profit, withdrawal = calculate_investment_returns(initial_investment, daily_rate, investment_duration)

        print(f"Total Profit: ${profit:.2f}")
        print(f"Total Withdrawal Amount: ${withdrawal:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
