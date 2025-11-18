"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Write code to calculate and display transaction fees in a blockchain-based marketplace like Pushd, with reduced fees for users holding native tokens.
Generated: DETERMINISTIC_b1570428b3759883
Batch ID: 20250612_152249
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

# Define constants
BASE_TRANSACTION_FEE = Decimal("0.02")  # Base transaction fee as a percentage (2%)
DISCOUNT_RATE = Decimal("0.50")         # Discount rate for native token holders as a percentage (50%)

# Function to calculate transaction fee
def calculate_transaction_fee(transaction_amount, holds_native_tokens=False):
    """
    Calculate the transaction fee for a given transaction amount.
    
    :param transaction_amount: Decimal - The amount of the transaction
    :param holds_native_tokens: bool - Whether the user holds native tokens for a discount
    
    :return: Decimal - The calculated transaction fee
    """
    try:
        # Validate input type
        if not isinstance(transaction_amount, Decimal):
            raise TypeError("Transaction amount must be a Decimal.")
        
        # Ensure the transaction amount is positive
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        # Determine applicable fee percentage
        fee_percentage = BASE_TRANSACTION_FEE
        if holds_native_tokens:
            fee_percentage *= (1 - DISCOUNT_RATE)  # Apply discount for native token holders
        
        # Calculate fee
        transaction_fee = transaction_amount * fee_percentage
        
        return transaction_fee
    
    except (TypeError, ValueError) as e:
        # Log error (for production systems, integrate logging frameworks)
        print(f"Error calculating transaction fee: {e}")
        return Decimal("0")  # Return 0 fee as fallback

# Function to display transaction fee
def display_transaction_fee(transaction_amount, holds_native_tokens):
    """
    Calculate and display the transaction fee for a given transaction amount.
    
    :param transaction_amount: Decimal - The amount of the transaction
    :param holds_native_tokens: bool - Whether the user holds native tokens for a discount
    """
    try:
        fee = calculate_transaction_fee(transaction_amount, holds_native_tokens)
        print(f"Transaction Amount: ${transaction_amount:.2f}")
        print(f"Transaction Fee: ${fee:.2f}")
        print(f"Discount Applied: {'Yes' if holds_native_tokens else 'No'}")
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")

# Example usage (in production, input validation should be more rigorous)
if __name__ == "__main__":
    try:
        # Sample transaction amounts
        transaction_amount_1 = Decimal("100.00")  # Example: $100.00 transaction
        transaction_amount_2 = Decimal("250.75")  # Example: $250.75 transaction
        
        # Display fees for users with and without native tokens
        display_transaction_fee(transaction_amount_1, holds_native_tokens=False)
        display_transaction_fee(transaction_amount_2, holds_native_tokens=True)
    except InvalidOperation as e:
        # Handle issues with Decimal operations
        print(f"Invalid transaction amount provided: {e}")
```
