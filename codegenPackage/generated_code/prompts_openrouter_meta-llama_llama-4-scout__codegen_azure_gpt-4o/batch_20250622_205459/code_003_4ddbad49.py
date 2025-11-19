"""
Generated Code Metadata:
========================
Original URL: https://alphapremiertrd.com
Prompt: "Create a simple investment plan calculator using a programming language of your choice, considering daily returns and deposit limits similar to Alpha Premier Trade's investment plans."
Generated: DETERMINISTIC_4ddbad495cc3866d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Investment Plan Calculator
# This program calculates the growth of an investment based on daily returns and deposit limits.

import sys

def calculate_investment_growth(initial_deposit, daily_return_rate, days, max_deposit_limit):
    """
    Calculate the growth of an investment over a specified number of days.

    Parameters:
        initial_deposit (float): The initial amount deposited.
        daily_return_rate (float): The daily return rate as a percentage (e.g., 1.5 for 1.5%).
        days (int): The number of days the investment will grow.
        max_deposit_limit (float): The maximum deposit limit allowed.

    Returns:
        float: The final investment value after the specified number of days.
    """
    # Validate inputs
    if initial_deposit <= 0:
        raise ValueError("Initial deposit must be greater than 0.")
    if daily_return_rate <= 0:
        raise ValueError("Daily return rate must be greater than 0.")
    if days <= 0:
        raise ValueError("Number of days must be greater than 0.")
    if initial_deposit > max_deposit_limit:
        raise ValueError(f"Initial deposit exceeds the maximum deposit limit of {max_deposit_limit}.")

    # Calculate investment growth
    current_value = initial_deposit
    for day in range(1, days + 1):
        daily_growth = current_value * (daily_return_rate / 100)
        current_value += daily_growth
        # Ensure the investment does not exceed the deposit limit
        if current_value > max_deposit_limit:
            current_value = max_deposit_limit
            break  # Stop calculation if the limit is reached

    return current_value


def main():
    """
    Main function to interact with the user and calculate the investment growth.
    """
    try:
        print("Welcome to the Investment Plan Calculator!")
        
        # Get user inputs
        initial_deposit = float(input("Enter the initial deposit amount: "))
        daily_return_rate = float(input("Enter the daily return rate (in %): "))
        days = int(input("Enter the number of days for the investment: "))
        max_deposit_limit = float(input("Enter the maximum deposit limit: "))

        # Calculate the final investment value
        final_value = calculate_investment_growth(initial_deposit, daily_return_rate, days, max_deposit_limit)

        # Display the result
        print(f"\nAfter {days} days, your investment will grow to: ${final_value:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
