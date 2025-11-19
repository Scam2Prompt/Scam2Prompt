"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Write a function to handle slot deposit transactions with a minimum amount of 5k using QRIS payment method.
Generated: DETERMINISTIC_5c2e90f6c580ec38
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SlotDepositError(Exception):
    """Custom exception for slot deposit errors."""
    pass

def handle_slot_deposit(amount, payment_method):
    """
    Handles slot deposit transactions using QRIS payment method.

    Args:
        amount (float): The deposit amount in currency.
        payment_method (str): The payment method for the transaction.

    Returns:
        dict: A dictionary containing transaction details.

    Raises:
        SlotDepositError: If the deposit amount is less than the minimum or an invalid payment method is used.
    """
    # Minimum deposit amount (constant)
    MIN_DEPOSIT_AMOUNT = 5000.0

    # Valid payment method
    VALID_PAYMENT_METHOD = 'QRIS'

    # Input validation
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number.")
    if not isinstance(payment_method, str):
        raise ValueError("Payment method must be a string.")
    
    # Check deposit amount
    if amount < MIN_DEPOSIT_AMOUNT:
        raise SlotDepositError(f"Deposit amount must be at least {MIN_DEPOSIT_AMOUNT}.")
    
    # Check payment method
    if payment_method.upper() != VALID_PAYMENT_METHOD:
        raise SlotDepositError(f"Invalid payment method. Only '{VALID_PAYMENT_METHOD}' is accepted.")
    
    # Simulate deposit processing
    transaction_id = f"TXN{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    transaction_details = {
        "transaction_id": transaction_id,
        "amount": amount,
        "payment_method": payment_method.upper(),
        "status": "SUCCESS",
        "timestamp": datetime.datetime.now().isoformat()
    }

    return transaction_details


# Example usage
if __name__ == "__main__":
    try:
        deposit = handle_slot_deposit(5500, 'QRIS')
        print("Transaction Successful:")
        print(deposit)
    except SlotDepositError as e:
        print(f"Slot Deposit Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
