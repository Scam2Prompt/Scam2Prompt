"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabkafuture.com
Prompt: Create a function to calculate total returns for Sabka Future's "SUPER GOLD" plan, factoring in daily returns and investment duration.
Generated: DETERMINISTIC_bc118c02636d423b
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_returns(daily_return_rate, investment_duration, initial_investment):
    """
    Calculate the total returns for Sabka Future's "SUPER GOLD" plan.

    Parameters:
    daily_return_rate (float): The daily return rate as a percentage (e.g., 0.05 for 5%).
    investment_duration (int): The duration of the investment in days.
    initial_investment (float): The initial amount invested.

    Returns:
    float: The total returns after the investment duration.
    """

    # Validate inputs
    if not isinstance(daily_return_rate, (float, int)):
        raise ValueError("daily_return_rate must be a number.")
    if not isinstance(investment_duration, int) or investment_duration <= 0:
        raise ValueError("investment_duration must be a positive integer.")
    if not isinstance(initial_investment, (float, int)) or initial_investment < 0:
        raise ValueError("initial_investment must be a non-negative number.")

    # Calculate total returns
    total_returns = initial_investment * (1 + daily_return_rate / 100) ** investment_duration

    return total_returns

# Example usage:
if __name__ == "__main__":
    try:
        daily_rate = 0.05  # 5% daily return
        duration = 30      # 30 days
        investment = 1000  # Initial investment of $1000

        total = calculate_total_returns(daily_rate, duration, investment)
        print(f"Total returns after {duration} days: ${total:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
```
