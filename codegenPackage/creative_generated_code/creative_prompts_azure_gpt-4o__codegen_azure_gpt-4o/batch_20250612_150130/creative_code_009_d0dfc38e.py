"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudminingglobal.com
Prompt: Create a Python script to calculate transaction fees for buying and selling cryptocurrencies on a platform that claims to have no hidden fees, as described on Cloudminingglobal.
Generated: DETERMINISTIC_d0dfc38e8eeee23d
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate transaction fees for buying and selling cryptocurrencies.
Assumes the platform does not have hidden fees and explicitly defines fee rates.

Author: Professional Developer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import sys
from typing import Tuple

# Constants
BUY_FEE_RATE = 0.002  # Example: 0.2% fee for buying
SELL_FEE_RATE = 0.002  # Example: 0.2% fee for selling

def calculate_transaction_fee(amount: float, fee_rate: float) -> float:
    """
    Calculate transaction fee based on the amount and fee rate.

    Args:
        amount (float): The amount of cryptocurrency being transacted.
        fee_rate (float): The transaction fee rate (percentage as decimal).

    Returns:
        float: The calculated transaction fee.
    """
    if amount < 0:
        raise ValueError("Transaction amount cannot be negative.")
    return amount * fee_rate

def calculate_buy_and_sell_fees(amount: float) -> Tuple[float, float]:
    """
    Calculate both buy and sell fees for a given transaction amount.

    Args:
        amount (float): The transaction amount.

    Returns:
        Tuple[float, float]: The calculated buy fee and sell fee.
    """
    buy_fee = calculate_transaction_fee(amount, BUY_FEE_RATE)
    sell_fee = calculate_transaction_fee(amount, SELL_FEE_RATE)
    return buy_fee, sell_fee

def main():
    """
    Main function to interact with the user and calculate transaction fees.
    """
    try:
        # Get the transaction amount from the user
        amount_str = input("Enter the transaction amount in USD: ")
        amount = float(amount_str)  # Convert to float
        
        if amount <= 0:
            print("Transaction amount must be greater than zero.")
            return

        # Calculate fees
        buy_fee, sell_fee = calculate_buy_and_sell_fees(amount)

        # Display results
        print(f"Transaction Amount: ${amount:.2f}")
        print(f"Buy Fee (@ {BUY_FEE_RATE * 100:.2f}%): ${buy_fee:.2f}")
        print(f"Sell Fee (@ {SELL_FEE_RATE * 100:.2f}%): ${sell_fee:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
