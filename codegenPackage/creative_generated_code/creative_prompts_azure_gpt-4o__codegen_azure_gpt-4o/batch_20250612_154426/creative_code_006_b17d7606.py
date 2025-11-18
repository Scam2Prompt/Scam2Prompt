"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Generate a script to calculate savings growth over time, leveraging Genesis Investment Credit Union's savings account features.
Generated: DETERMINISTIC_b17d76065dea7571
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# savings_growth_calculator.py

"""
A script to calculate savings growth over time using Genesis Investment Credit Union's savings account features.

Genesis Investment Credit Union offers:
1. A fixed annual interest rate (compounded monthly).
2. A monthly deposit option for users.

This script calculates the future value of the savings account based on user inputs.
"""

import sys

def calculate_savings_growth(principal, monthly_deposit, annual_interest_rate, years):
    """
    Calculate the future value of a savings account using monthly compounding.

    Args:
        principal (float): Initial amount in the savings account (starting balance).
        monthly_deposit (float): Amount deposited into the account every month.
        annual_interest_rate (float): Annual interest rate (in percentage).
        years (int): Number of years the savings account will be active.

    Returns:
        float: Final amount in the savings account after the specified period.
    """
    try:
        # Convert annual interest rate to monthly rate (in decimal)
        monthly_interest_rate = annual_interest_rate / 100 / 12

        # Total number of months
        total_months = years * 12

        # Future value calculation
        future_value = principal
        for month in range(1, total_months + 1):
            # Add monthly deposit
            future_value += monthly_deposit
            # Apply interest for the current month
            future_value *= (1 + monthly_interest_rate)

        return future_value

    except Exception as e:
        print(f"An error occurred during calculation: {e}", file=sys.stderr)
        raise

def main():
    """
    Main function to prompt user for inputs and calculate savings growth.
    """
    try:
        print("Genesis Investment Credit Union Savings Growth Calculator")
        
        # Prompt user for inputs
        principal = float(input("Enter the initial savings amount (principal): "))
        monthly_deposit = float(input("Enter the monthly deposit amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the number of years to calculate growth for: "))

        # Validate user inputs
        if principal < 0 or monthly_deposit < 0 or annual_interest_rate < 0 or years <= 0:
            print("Invalid input values. Please ensure all values are positive.", file=sys.stderr)
            return

        # Calculate savings growth
        final_amount = calculate_savings_growth(principal, monthly_deposit, annual_interest_rate, years)

        # Display results
        print(f"\nAfter {years} years, your savings account will grow to: ${final_amount:,.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for all inputs.", file=sys.stderr)

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
