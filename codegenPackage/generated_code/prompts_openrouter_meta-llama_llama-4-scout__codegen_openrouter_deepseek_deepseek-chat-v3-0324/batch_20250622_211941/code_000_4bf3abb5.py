"""
Generated Code Metadata:
========================
Original URL: https://zadepositslot.com
Prompt: "Write a Python script to calculate the total returns on investment for a plan that offers 50% daily returns for 7 days, assuming an initial investment of R1,000 ZAR."
Generated: DETERMINISTIC_4bf3abb5a125080e
Batch ID: 20250622_211941
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_investment_returns(initial_investment: float, daily_return_rate: float, days: int) -> float:
    """
    Calculate the total returns on an investment with a fixed daily return rate over a given period.

    Args:
        initial_investment (float): The initial amount invested.
        daily_return_rate (float): The daily return rate (e.g., 0.5 for 50%).
        days (int): The number of days the investment will grow.

    Returns:
        float: The total returns after the investment period.
    """
    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than 0.")
    if daily_return_rate <= 0:
        raise ValueError("Daily return rate must be greater than 0.")
    if days <= 0:
        raise ValueError("Number of days must be greater than 0.")

    total = initial_investment
    for _ in range(days):
        total += total * daily_return_rate

    return total


def main():
    try:
        initial_investment = 1000.0  # ZAR
        daily_return_rate = 0.5      # 50%
        days = 7

        total_returns = calculate_investment_returns(initial_investment, daily_return_rate, days)
        print(f"Initial Investment: R{initial_investment:.2f} ZAR")
        print(f"Daily Return Rate: {daily_return_rate * 100:.0f}%")
        print(f"Investment Period: {days} days")
        print(f"Total Returns: R{total_returns:.2f} ZAR")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
