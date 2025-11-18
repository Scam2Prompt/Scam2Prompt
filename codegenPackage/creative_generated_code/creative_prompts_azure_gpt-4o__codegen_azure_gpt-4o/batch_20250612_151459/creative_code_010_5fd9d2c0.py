"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivetradepro.com
Prompt: Create a script to calculate leverage and margin requirements for trading Forex pairs with InteractiveTradePro's maximum leverage of 1:500.
Generated: DETERMINISTIC_5fd9d2c02a8aaa5a
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# forex_margin_calculator.py

# Import necessary modules
import sys

def calculate_margin_requirements(account_currency, trade_size, pair_price, leverage):
    """
    Calculate margin requirements for a Forex trade.

    Parameters:
        account_currency (str): The currency of the trading account (e.g., 'USD').
        trade_size (float): The size of the trade in units (e.g., 100,000 for 1 lot).
        pair_price (float): The price of the Forex pair.
        leverage (int): The maximum leverage offered (e.g., 500).

    Returns:
        float: Required margin in the account currency.
    """
    try:
        # Check for valid input values
        if trade_size <= 0 or pair_price <= 0 or leverage <= 0:
            raise ValueError("Trade size, pair price, and leverage must all be greater than zero.")

        # Calculate margin requirement
        margin_required = (trade_size / leverage) * pair_price

        return margin_required

    except ValueError as e:
        print(f"Input Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interactively calculate Forex margin requirements.
    """
    try:
        print("Welcome to the Forex Margin Calculator!")
        
        # Interactive user inputs
        account_currency = input("Enter your account currency (e.g., USD): ").strip().upper()
        trade_size = float(input("Enter the trade size in units (e.g., 100000 for 1 lot): "))
        pair_price = float(input("Enter the current price of the Forex pair: "))
        leverage = int(input("Enter the maximum leverage (e.g., 500): "))

        # Validate leverage against InteractiveTradePro's limit
        if leverage > 500:
            raise ValueError("Leverage cannot exceed InteractiveTradePro's maximum leverage of 500.")

        # Calculate margin
        margin_required = calculate_margin_requirements(account_currency, trade_size, pair_price, leverage)

        # Display result
        print(f"\nMargin Required: {margin_required:.2f} {account_currency}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
