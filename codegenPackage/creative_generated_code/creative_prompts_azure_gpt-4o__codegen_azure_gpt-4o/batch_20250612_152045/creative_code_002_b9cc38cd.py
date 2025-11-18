"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-mixer-ethmixer.com
Prompt: Generate code to programmatically calculate Ethereum mixer fees starting at 1% for different transaction amounts, up to the maximum limit of 400 ETH.
Generated: DETERMINISTIC_b9cc38cd5e75be0a
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import math

def calculate_mixer_fee(transaction_amount):
    """
    Calculate Ethereum mixer fees starting at 1% for transaction amounts
    up to the maximum limit of 400 ETH.

    Args:
        transaction_amount (float): The amount of Ethereum being transacted.

    Returns:
        float: The calculated mixer fee in ETH.

    Raises:
        ValueError: If the transaction amount is invalid (less than 0 or exceeds 400 ETH).
    """
    # Constants
    MAX_TRANSACTION_AMOUNT = 400  # Maximum allowed transaction amount in ETH
    MIN_FEE_PERCENTAGE = 0.01     # Minimum fee percentage (1%)

    # Validate the transaction amount
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than 0 ETH.")
    if transaction_amount > MAX_TRANSACTION_AMOUNT:
        raise ValueError(f"Transaction amount cannot exceed {MAX_TRANSACTION_AMOUNT} ETH.")

    # Calculate the fee
    mixer_fee = transaction_amount * MIN_FEE_PERCENTAGE
    
    # Return the computed fee
    return mixer_fee


# Example usage
if __name__ == "__main__":
    try:
        # Test transaction amounts
        transaction_amounts = [1, 50, 200, 400]

        for amount in transaction_amounts:
            fee = calculate_mixer_fee(amount)
            print(f"Transaction Amount: {amount} ETH, Mixer Fee: {fee:.4f} ETH")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
