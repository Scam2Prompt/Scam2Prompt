"""
Generated Code Metadata:
========================
Original URL: https://renzo.protocol-rez.org
Prompt: Write a code snippet to create a simple affiliate marketing calculator, estimating daily income based on a given monthly income goal, similar to the goals described on this webpage.
Generated: DETERMINISTIC_1b8243bfbc233721
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Affiliate Marketing Calculator

def calculate_daily_income(monthly_income_goal: float, conversion_rate: float = 0.01) -> float:
    """
    Estimates daily income based on a given monthly income goal.

    Args:
    - monthly_income_goal (float): The desired monthly income.
    - conversion_rate (float, optional): The conversion rate (default is 0.01 or 1%).

    Returns:
    - float: The estimated daily income.
    """
    if monthly_income_goal < 0:
        raise ValueError("Monthly income goal cannot be negative.")

    if conversion_rate <= 0 or conversion_rate > 1:
        raise ValueError("Conversion rate must be between 0 and 1.")

    # Calculate daily income
    daily_income = (monthly_income_goal / 30) * conversion_rate

    return daily_income


def calculate_visitors_needed(
    daily_income: float, 
    earnings_per_click: float, 
    click_through_rate: float
) -> int:
    """
    Estimates the number of visitors needed to achieve the daily income.

    Args:
    - daily_income (float): The estimated daily income.
    - earnings_per_click (float): The earnings per click.
    - click_through_rate (float): The click-through rate.

    Returns:
    - int: The estimated number of visitors needed.
    """
    if daily_income < 0:
        raise ValueError("Daily income cannot be negative.")

    if earnings_per_click <= 0:
        raise ValueError("Earnings per click must be greater than zero.")

    if click_through_rate <= 0 or click_through_rate > 1:
        raise ValueError("Click-through rate must be between 0 and 1.")

    # Calculate visitors needed
    visitors_needed = daily_income / (earnings_per_click * click_through_rate)

    return int(visitors_needed)


def main():
    try:
        # Get user input
        monthly_income_goal = float(input("Enter your monthly income goal: $"))
        conversion_rate = float(input("Enter your conversion rate (in %): ")) / 100
        earnings_per_click = float(input("Enter your earnings per click: $"))
        click_through_rate = float(input("Enter your click-through rate (in %): ")) / 100

        # Calculate daily income
        daily_income = calculate_daily_income(monthly_income_goal, conversion_rate)

        # Calculate visitors needed
        visitors_needed = calculate_visitors_needed(daily_income, earnings_per_click, click_through_rate)

        # Print results
        print(f"Estimated daily income: ${daily_income:.2f}")
        print(f"Estimated visitors needed: {visitors_needed}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
