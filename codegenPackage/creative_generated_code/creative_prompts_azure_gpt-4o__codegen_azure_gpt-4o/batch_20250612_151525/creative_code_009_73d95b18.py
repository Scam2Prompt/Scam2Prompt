"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Write a script to calculate the long-term financial benefits of "Paying Yourself First," incorporating principles from Ahmeti Wealth Management's educational content.
Generated: DETERMINISTIC_73d95b187bed2091
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Pay Yourself First Financial Calculator

This script calculates the long-term financial benefits of "Paying Yourself First," 
a principle that emphasizes saving a fixed percentage of your income before spending on daily expenses.
The calculation incorporates compound interest to demonstrate the growth in savings over time.

Author: Expert Programmer
Date: YYYY-MM-DD

Note:
- Replace placeholder values with actual user inputs for production use.
- This script assumes monthly contributions to savings and annual compound interest.

"""

import sys

def calculate_future_value(monthly_savings, annual_interest_rate, years):
    """
    Calculate the future value of savings using compound interest.

    Args:
        monthly_savings (float): The amount saved each month.
        annual_interest_rate (float): The annual interest rate (as a percentage).
        years (int): The number of years to save.

    Returns:
        float: The future value of the savings.
    """
    try:
        # Convert annual interest rate to monthly rate
        monthly_rate = annual_interest_rate / 100 / 12
        months = years * 12

        # Compound interest formula with monthly contributions
        future_value = 0
        for month in range(1, months + 1):
            # Value grows with interest and contribution each month
            future_value = (future_value + monthly_savings) * (1 + monthly_rate)

        return future_value
    except Exception as e:
        print(f"An error occurred during calculation: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main program to prompt user input and calculate the long-term financial benefits
    of "Paying Yourself First."
    """
    try:
        print("Welcome to the Pay Yourself First Calculator!")

        # User inputs
        monthly_savings = float(input("Enter the amount you plan to save each month ($): "))
        annual_interest_rate = float(input("Enter the expected annual interest rate (in %, e.g., 5 for 5%): "))
        years = int(input("Enter the number of years you plan to save: "))

        if monthly_savings <= 0 or annual_interest_rate < 0 or years <= 0:
            print("Invalid input. Please ensure all inputs are positive and greater than zero.", file=sys.stderr)
            sys.exit(1)

        # Calculate future value
        future_value = calculate_future_value(monthly_savings, annual_interest_rate, years)

        # Display results
        print("\nResults:")
        print(f"By saving ${monthly_savings:.2f} every month for {years} years at an annual interest rate of {annual_interest_rate:.2f}%,")
        print(f"your savings will grow to approximately ${future_value:,.2f}.")
    except ValueError:
        print("Invalid input. Please enter numeric values for the savings amount, interest rate, and years.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
