"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance-stake.vercel.app
Prompt: Generate a Python script to calculate estimated daily compound interest for crypto staking based on APR, following the use case outlined on the Binance Stake APR Calculator page.
Generated: DETERMINISTIC_dc6830ced72be96a
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate estimated daily compound interest for crypto staking based on APR.
This script assumes the staking rewards are compounded daily.

Usage:
    - Input the principal amount, annual percentage rate (APR), and the number of days.
    - The script will calculate the estimated daily interest and total amount after the given days.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import sys

def calculate_compound_interest(principal, apr, days):
    """
    Calculate the future value of an investment with daily compounded interest.

    Parameters:
        principal (float): The initial amount of the investment.
        apr (float): Annual Percentage Rate (APR) in percentage (e.g., 10 for 10% APR).
        days (int): The number of days for which interest is calculated.

    Returns:
        tuple: A tuple containing total amount and estimated daily interest.
    """
    try:
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        if apr <= 0:
            raise ValueError("APR must be greater than 0.")
        if days <= 0:
            raise ValueError("Number of days must be greater than 0.")

        # Convert APR from percentage to decimal
        daily_rate = apr / 100 / 365  # Daily interest rate

        # Calculate compound interest formula: A = P * (1 + r)^t
        total_amount = principal * (1 + daily_rate) ** days

        # Calculate estimated daily interest
        estimated_daily_interest = total_amount - principal

        return round(total_amount, 2), round(estimated_daily_interest / days, 6)
    except ValueError as e:
        print(f"Input Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to handle user input and display results.
    """
    try:
        print("Crypto Staking Daily Compound Interest Calculator")
        
        # Get user input for principal, APR, and days
        principal = float(input("Enter the principal amount (e.g., 1000): "))
        apr = float(input("Enter the annual APR in percentage (e.g., 10): "))
        days = int(input("Enter the number of days to stake (e.g., 30): "))

        # Calculate compound interest
        total_amount, daily_interest = calculate_compound_interest(principal, apr, days)

        # Display results
        print(f"\nResults:")
        print(f"Total Amount after {days} days: ${total_amount}")
        print(f"Estimated Daily Interest: ${daily_interest}")

    except ValueError:
        print("Invalid input. Please ensure all inputs are numeric.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
