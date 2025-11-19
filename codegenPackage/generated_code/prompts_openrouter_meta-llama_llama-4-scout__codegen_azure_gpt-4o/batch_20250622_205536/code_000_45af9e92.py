"""
Generated Code Metadata:
========================
Original URL: https://sdstarfx.com
Prompt: Write a Python script to calculate the potential profit from a Forex trade using S D STAR FX LTD's commission and spread rates.
Generated: DETERMINISTIC_45af9e92ba62083d
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Forex Profit Calculator Script

This script calculates the potential profit from a Forex trade, taking into account 
S D STAR FX LTD's commission and spread rates.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_forex_profit(trade_amount, entry_price, exit_price, commission_rate, spread_rate):
    """
    Calculate the potential profit from a Forex trade.

    Parameters:
        trade_amount (float): The amount of money being traded (in base currency).
        entry_price (float): The price at which the trade is entered.
        exit_price (float): The price at which the trade is exited.
        commission_rate (float): The commission rate charged by the broker (as a percentage).
        spread_rate (float): The spread rate charged by the broker (as a percentage).

    Returns:
        float: The potential profit from the trade.
    """
    try:
        # Validate inputs
        if trade_amount <= 0 or entry_price <= 0 or exit_price <= 0:
            raise ValueError("Trade amount, entry price, and exit price must be positive numbers.")
        if commission_rate < 0 or spread_rate < 0:
            raise ValueError("Commission rate and spread rate must be non-negative numbers.")

        # Calculate gross profit
        gross_profit = trade_amount * (exit_price - entry_price)

        # Calculate commission cost
        commission_cost = trade_amount * commission_rate / 100

        # Calculate spread cost
        spread_cost = trade_amount * spread_rate / 100

        # Calculate net profit
        net_profit = gross_profit - commission_cost - spread_cost

        return net_profit

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the Forex profit calculation.
    """
    try:
        # User inputs
        print("Welcome to the Forex Profit Calculator!")
        trade_amount = float(input("Enter the trade amount (in base currency): "))
        entry_price = float(input("Enter the entry price: "))
        exit_price = float(input("Enter the exit price: "))
        commission_rate = float(input("Enter the commission rate (as a percentage): "))
        spread_rate = float(input("Enter the spread rate (as a percentage): "))

        # Calculate potential profit
        profit = calculate_forex_profit(trade_amount, entry_price, exit_price, commission_rate, spread_rate)

        # Display the result
        print(f"\nThe potential profit from this trade is: {profit:.2f} (base currency)")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
