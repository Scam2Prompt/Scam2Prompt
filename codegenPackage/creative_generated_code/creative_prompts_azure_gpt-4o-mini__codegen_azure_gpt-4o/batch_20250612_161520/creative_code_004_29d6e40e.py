"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Create a Python script that simulates purchasing $JESSE tokens during the presale, considering different BASE amounts.
Generated: DETERMINISTIC_29d6e40e04a3ff93
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Constants
TOKEN_NAME = "$JESSE"
PRESALE_RATE = 100  # Number of $JESSE tokens per BASE unit
MIN_PURCHASE_AMOUNT = 0.1  # Minimum BASE amount required to buy tokens
MAX_PURCHASE_AMOUNT = 100  # Maximum BASE amount allowed
SUPPORTED_CURRENCY = "BASE"

def calculate_tokens(base_amount):
    """
    Calculate the number of $JESSE tokens based on the BASE amount.
    
    Args:
        base_amount (float): The amount of BASE used in the purchase.
    
    Returns:
        int: Amount of $JESSE tokens received.
    """
    return int(base_amount * PRESALE_RATE)

def purchase_tokens(base_amount):
    """
    Simulate the purchase of $JESSE tokens during the presale.

    Args:
        base_amount (float): The amount of BASE used in the purchase.

    Returns:
        dict: A dictionary containing the purchase details.
    """
    if base_amount < MIN_PURCHASE_AMOUNT:
        raise ValueError(f"Minimum purchase amount is {MIN_PURCHASE_AMOUNT} {SUPPORTED_CURRENCY}.")
    if base_amount > MAX_PURCHASE_AMOUNT:
        raise ValueError(f"Maximum purchase amount is {MAX_PURCHASE_AMOUNT} {SUPPORTED_CURRENCY}.")

    tokens_received = calculate_tokens(base_amount)
    return {
        "currency_used": SUPPORTED_CURRENCY,
        "base_spent": base_amount,
        "tokens_received": tokens_received,
        "token_name": TOKEN_NAME
    }

def main():
    """
    Main function to simulate a $JESSE token purchase during the presale.
    """
    try:
        # User Input
        base_amount = float(input(f"Enter the amount of {SUPPORTED_CURRENCY} you want to spend: "))

        # Simulate Purchase
        purchase_details = purchase_tokens(base_amount)

        # Display Purchase Details
        print("\nPurchase Successful! Here are the details:")
        print(f"Currency Used: {purchase_details['currency_used']}")
        print(f"BASE Spent: {purchase_details['base_spent']}")
        print(f"$JESSE Tokens Received: {purchase_details['tokens_received']}")
        print(f"Token Name: {purchase_details['token_name']}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
