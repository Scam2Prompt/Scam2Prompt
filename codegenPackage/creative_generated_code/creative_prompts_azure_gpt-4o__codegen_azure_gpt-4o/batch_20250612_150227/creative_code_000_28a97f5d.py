"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binarygoldenoptions.com
Prompt: Write a Python script to calculate investment returns based on the daily percentage rates provided by Binary Golden Options' investment plans (e.g., Basic Return: 3.99%, Gold Return: 10.95%, etc.) for a given principal amount and duration.
Generated: DETERMINISTIC_28a97f5d11e18a04
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_returns.py

# Import necessary modules
from typing import Dict, Union


def calculate_investment_return(principal: Union[int, float], daily_rate: float, days: int) -> float:
    """
    Calculate the total return on an investment based on daily percentage rate.

    :param principal: The initial amount of money invested (must be positive).
    :param daily_rate: The daily return rate in percentage (e.g., 3.99 for 3.99%).
    :param days: The number of days the investment is held (must be positive).
    :return: The total return (including the original principal).
    """

    # Input validation
    if principal <= 0:
        raise ValueError("Principal must be a positive number.")
    if daily_rate <= 0:
        raise ValueError("Daily rate must be a positive number.")
    if days <= 0:
        raise ValueError("Number of days must be a positive integer.")

    # Convert percentage rate to decimal
    rate_decimal = daily_rate / 100

    # Compound the investment daily based on the provided rate and duration
    total_return = principal * ((1 + rate_decimal) ** days)

    return round(total_return, 2)


def main():
    """
    Main function to interact with the user and calculate investment returns.
    """

    # Predefined investment plans by Binary Golden Options
    investment_plans: Dict[str, float] = {
        "Basic Return": 3.99,  # 3.99% daily
        "Gold Return": 10.95,  # 10.95% daily
        "Platinum Return": 15.5,  # 15.5% daily
    }

    print("Welcome to Binary Golden Options Investment Calculator!")
    print("Available plans and their daily percentage rates:")
    for plan_name, daily_rate in investment_plans.items():
        print(f"- {plan_name}: {daily_rate}% daily")

    try:
        # User input for principal amount
        principal = float(input("\nEnter the principal amount (e.g., 1000): "))

        # User input for investment plan
        plan_name = input("Enter the investment plan name (e.g., Basic Return, Gold Return): ")
        if plan_name not in investment_plans:
            raise ValueError("Invalid investment plan selected.")

        # Fetch the daily rate for the selected plan
        daily_rate = investment_plans[plan_name]

        # User input for duration
        days = int(input("Enter the duration of investment in days (e.g., 30): "))

        # Calculate the total investment return
        total_return = calculate_investment_return(principal, daily_rate, days)

        # Display the result
        print(f"\nInvestment Plan: {plan_name}")
        print(f"Principal Amount: ${principal}")
        print(f"Daily Rate: {daily_rate}%")
        print(f"Duration: {days} days")
        print(f"Total Return: ${total_return}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
