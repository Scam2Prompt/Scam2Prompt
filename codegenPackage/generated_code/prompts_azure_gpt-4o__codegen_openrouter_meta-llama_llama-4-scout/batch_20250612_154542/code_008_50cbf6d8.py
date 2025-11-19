"""
Generated Code Metadata:
========================
Original URL: https://crypto4rex360.com
Prompt: Write a Python script to simulate the lifetime earnings for the "Diamond Plan" investment, which offers an 11.67% daily return for a lifetime.
Generated: DETERMINISTIC_50cbf6d844d3a4dd
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulates the lifetime earnings for the 'Diamond Plan' investment.

The Diamond Plan offers an 11.67% daily return for a lifetime.

This script calculates and displays the lifetime earnings based on an initial investment.
"""

def calculate_lifetime_earnings(initial_investment, days):
    """
    Calculates the lifetime earnings for the Diamond Plan investment.

    Args:
        initial_investment (float): The initial amount invested.
        days (int): The number of days the investment is held.

    Returns:
        float: The total earnings after the specified number of days.

    Raises:
        ValueError: If the initial investment or days are negative.
    """
    if initial_investment < 0 or days < 0:
        raise ValueError("Initial investment and days must be non-negative.")

    daily_return_rate = 0.1167  # 11.67% daily return rate
    total_earnings = initial_investment * (1 + daily_return_rate) ** days
    return total_earnings


def main():
    try:
        initial_investment = float(input("Enter the initial investment: $"))
        days = int(input("Enter the number of days: "))

        lifetime_earnings = calculate_lifetime_earnings(initial_investment, days)
        print(f"After {days} days, your investment of ${initial_investment:.2f} will be worth: ${lifetime_earnings:.2f}")
        print(f"Your total earnings will be: ${lifetime_earnings - initial_investment:.2f}")
        print(f"Return on Investment (ROI): {(lifetime_earnings / initial_investment - 1) * 100:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
