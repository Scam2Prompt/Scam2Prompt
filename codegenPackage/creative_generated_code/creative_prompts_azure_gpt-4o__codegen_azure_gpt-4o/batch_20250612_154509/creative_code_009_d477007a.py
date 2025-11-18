"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale.seesawprotocol.io
Prompt: Create a Python script to calculate interest earned on USDT holdings in wallets that offer passive income in Nigeria, as described on Crypto-Wallet.ng.
Generated: DETERMINISTIC_d477007a0051e307
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate interest earned on USDT holdings in wallets offering passive income.
This script takes the initial USDT balance, annual interest rate, and holding duration in days
to compute the total interest earned.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

def calculate_interest(balance, annual_rate, days_held):
    """
    Calculate the interest earned on USDT holdings.

    Parameters:
    balance (float): The initial USDT balance.
    annual_rate (float): Annual interest rate in percentage (e.g., 12.5 for 12.5%).
    days_held (int): Duration of holding in days.

    Returns:
    float: The interest earned.
    """
    try:
        # Convert annual percentage rate to a daily rate
        daily_rate = annual_rate / 100 / 365

        if balance <= 0 or annual_rate < 0 or days_held <= 0:
            raise ValueError("Inputs must be positive values.")

        # Calculate interest earned
        interest_earned = balance * daily_rate * days_held
        return interest_earned

    except Exception as e:
        raise ValueError(f"Error calculating interest: {e}")


def main():
    """
    Main function to handle user inputs and display results.
    """
    try:
        print("Welcome to the USDT Interest Calculator (Crypto-Wallet.ng)")

        # Get user inputs
        balance = float(input("Enter your USDT balance: "))
        annual_rate = float(input("Enter annual interest rate (e.g., 12.5 for 12.5%): "))
        days_held = int(input("Enter holding duration in days: "))

        # Calculate interest earned
        interest = calculate_interest(balance, annual_rate, days_held)

        # Display results
        print(f"\nWith a balance of {balance} USDT, an annual interest rate of {annual_rate}%")
        print(f"and a holding duration of {days_held} days, you will earn {interest:.2f} USDT in interest.")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main function
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
        sys.exit()
```
