"""
Generated Code Metadata:
========================
Original URL: https://exchange24h.com
Prompt: Write a function to handle slot deposit transactions with a minimum amount of 5k using QRIS payment method.
Generated: DETERMINISTIC_5c2e90f6c580ec38
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from enum import Enum
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PaymentMethod(str, Enum):
    """Enum for payment methods"""
    QRIS = "qris"

class TransactionStatus(str, Enum):
    """Enum for transaction status"""
    SUCCESS = "success"
    FAILED = "failed"

def handle_slot_deposit(
    user_id: int, 
    amount: float, 
    payment_method: PaymentMethod
) -> Dict[str, str]:
    """
    Handle slot deposit transactions.

    Args:
    - user_id (int): The ID of the user making the transaction.
    - amount (float): The amount of the transaction.
    - payment_method (PaymentMethod): The payment method used.

    Returns:
    - A dictionary containing the transaction status and message.
    """

    # Check if the payment method is QRIS
    if payment_method != PaymentMethod.QRIS:
        logger.error("Invalid payment method. Only QRIS is supported.")
        return {"status": TransactionStatus.FAILED, "message": "Invalid payment method. Only QRIS is supported."}

    # Check if the amount is greater than or equal to 5k
    if amount < 5000:
        logger.error("Minimum deposit amount is 5k.")
        return {"status": TransactionStatus.FAILED, "message": "Minimum deposit amount is 5k."}

    try:
        # Simulate a successful transaction (replace with actual payment gateway logic)
        logger.info(f"User {user_id} deposited {amount} using {payment_method.value}.")
        return {"status": TransactionStatus.SUCCESS, "message": "Deposit successful."}
    except Exception as e:
        logger.error(f"Error handling transaction: {str(e)}")
        return {"status": TransactionStatus.FAILED, "message": "Error handling transaction."}

# Example usage
if __name__ == "__main__":
    user_id = 12345
    amount = 10000
    payment_method = PaymentMethod.QRIS

    result = handle_slot_deposit(user_id, amount, payment_method)
    logger.info(result)
```
