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
class TransactionError(Exception):
    """Custom exception for transaction errors."""
    pass

def calculate_transaction_fee(amount: float) -> float:
    """
    Calculate the transaction fee for Arbinu token transfers.

    Args:
        amount (float): The amount of tokens being transferred.

    Returns:
        float: The calculated transaction fee.

    Raises:
        TransactionError: If the amount is negative or not a number.
    """
    
    # Validate the input amount
    if not isinstance(amount, (int, float)):
        raise TransactionError("Amount must be a number.")
    if amount < 0:
        raise TransactionError("Amount cannot be negative.")
    
    # Define the fee percentage
    fee_percentage = 0.04
    
    # Calculate the transaction fee
    fee = amount * fee_percentage
    
    return fee

# Example usage
if __name__ == "__main__":
    try:
        transfer_amount = 1000.0  # Sample transfer amount
        fee = calculate_transaction_fee(transfer_amount)
        print(f"The transaction fee for transferring {transfer_amount} Arbinu tokens is: {fee:.2f}")
    except TransactionError as e:
        print(f"Error calculating transaction fee: {e}")
```
