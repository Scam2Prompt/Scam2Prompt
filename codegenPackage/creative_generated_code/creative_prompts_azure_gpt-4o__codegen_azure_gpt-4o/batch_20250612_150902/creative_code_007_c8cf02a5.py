"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hugfytxytugugvytfuyjgykb.pages.dev
Prompt: Create a function to calculate transaction fees (4%) for Arbinu token transfers based on the tokenomics described.
Generated: DETERMINISTIC_c8cf02a527bdc5ec
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal, InvalidOperation

def calculate_transaction_fee(amount):
    """
    Calculate the transaction fee for Arbinu token transfers based on tokenomics.
    
    Arbinu token has a fixed 4% transaction fee for every transfer.
    
    Args:
        amount (Decimal or float or int): The amount of Arbinu tokens to be transferred.
    
    Returns:
        Decimal: The transaction fee for the transfer.
    
    Raises:
        ValueError: If the input `amount` is not a positive number.
    """
    try:
        # Ensure the amount is a valid Decimal
        amount = Decimal(amount)
    except InvalidOperation:
        raise ValueError("Input amount must be a number.")

    # Validate that the input amount is positive
    if amount <= 0:
        raise ValueError("The transfer amount must be greater than zero.")

    # Define the transaction fee rate (4%)
    fee_rate = Decimal("0.04")

    # Calculate the transaction fee
    transaction_fee = amount * fee_rate

    return transaction_fee

# Example Usage:
if __name__ == "__main__":
    try:
        transfer_amount = input("Enter the transfer amount: ")
        fee = calculate_transaction_fee(transfer_amount)
        print(f"The transaction fee for transferring {transfer_amount} Arbinu tokens is {fee:.2f} tokens.")
    except ValueError as e:
        print(f"Error: {e}")
```
