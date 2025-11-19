"""
Generated Code Metadata:
========================
Original URL: https://tslaspacetrade.com
Prompt: Create a Python function that calculates the total earnings after 60 days for an investment plan offering 420% returns, as outlined in Tslaspacetrade's investment plans.
Generated: DETERMINISTIC_a2ac71a6f48f6cf5
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_earnings(principal_amount: float, daily_return_rate: float, days: int) -> float:
    """
    Calculates the total earnings after a specified number of days for an investment plan.

    Args:
    - principal_amount (float): The initial investment amount.
    - daily_return_rate (float): The daily return rate as a decimal.
    - days (int): The number of days the investment is held.

    Returns:
    - float: The total earnings after the specified number of days.

    Raises:
    - ValueError: If the principal amount, daily return rate, or days are invalid.
    """

    # Validate input parameters
    if principal_amount <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if daily_return_rate <= 0:
        raise ValueError("Daily return rate must be greater than zero.")
    if days <= 0:
        raise ValueError("Number of days must be greater than zero.")

    # Calculate total earnings using compound interest formula
    total_earnings = principal_amount * (1 + daily_return_rate) ** days - principal_amount

    return total_earnings


def main():
    try:
        # Tslaspacetrade's investment plan offering 420% returns per 60 days
        # Assuming the 420% return is the total return for 60 days, not annualized
        total_return_rate = 4.20  # 420% as a decimal

        # Convert total return rate to daily return rate
        daily_return_rate = (total_return_rate + 1) ** (1 / 60) - 1

        principal_amount = float(input("Enter the principal amount: "))
        days = 60

        total_earnings = calculate_total_earnings(principal_amount, daily_return_rate, days)
        print(f"Total earnings after {days} days: ${total_earnings:.2f}")
        print(f"Total amount after {days} days: ${principal_amount + total_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
