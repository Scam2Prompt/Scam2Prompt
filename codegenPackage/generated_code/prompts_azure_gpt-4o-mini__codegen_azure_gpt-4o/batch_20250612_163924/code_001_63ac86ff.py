"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Write a Python script that calculates the actual interest from DeFi yield rates, considering the nuances of APY as discussed in the article.
Generated: DETERMINISTIC_63ac86ff1cb36fc3
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate actual interest from DeFi yield rates based on APY (Annual Percentage Yield).
This script assumes compound interest and allows the user to specify the principal amount, APY, 
and the compounding frequency (e.g., daily, weekly, monthly).

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import argparse

def calculate_actual_interest(principal, apy, compounding_frequency, duration_in_days):
    """
    Calculate the actual interest earned based on APY and compounding frequency.

    Args:
        principal (float): The initial amount of money deposited.
        apy (float): The annual percentage yield (in percentage, e.g., 5 for 5% APY).
        compounding_frequency (int): The number of compounding periods per year (e.g., 365 for daily).
        duration_in_days (int): The duration of the investment in days.

    Returns:
        float: The total interest earned over the specified duration.
    """
    try:
        # Convert APY from percentage to decimal
        apy_decimal = apy / 100

        # Calculate the effective interest rate per compounding period
        rate_per_period = apy_decimal / compounding_frequency

        # Calculate the total number of compounding periods for the given duration
        total_periods = (duration_in_days / 365) * compounding_frequency

        # Calculate the final amount using the compound interest formula
        final_amount = principal * (1 + rate_per_period) ** total_periods

        # Calculate the interest earned
        interest_earned = final_amount - principal

        return interest_earned
    except Exception as e:
        raise ValueError(f"Error calculating interest: {e}")


def main():
    """
    Main function to parse user input and calculate interest.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Calculate actual interest from DeFi yield rates.")
    parser.add_argument("principal", type=float, help="Initial deposit amount (principal).")
    parser.add_argument("apy", type=float, help="Annual Percentage Yield (APY) in percentage.")
    parser.add_argument("compounding_frequency", type=int, help="Number of compounding periods per year (e.g., 365 for daily).")
    parser.add_argument("duration_in_days", type=int, help="Duration of the investment in days.")

    # Parse arguments
    args = parser.parse_args()

    try:
        # Calculate interest
        interest = calculate_actual_interest(
            principal=args.principal,
            apy=args.apy,
            compounding_frequency=args.compounding_frequency,
            duration_in_days=args.duration_in_days
        )

        # Output the result
        print(f"Interest earned over {args.duration_in_days} days: ${interest:.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
