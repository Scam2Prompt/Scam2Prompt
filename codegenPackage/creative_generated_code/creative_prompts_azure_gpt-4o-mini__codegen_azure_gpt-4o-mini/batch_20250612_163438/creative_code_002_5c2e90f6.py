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
import logging

# Setting up logging for tracking errors and important events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SlotDepositError(Exception):
    """Custom exception for slot deposit errors."""
    pass

def handle_slot_deposit(amount: float, payment_method: str) -> str:
    """
    Handles slot deposit transactions.

    Parameters:
        amount (float): The deposit amount.
        payment_method (str): The payment method used (e.g., "QRIS").

    Returns:
        str: Confirmation message upon successful deposit.

    Raises:
        SlotDepositError: If the deposit amount is below the minimum requirement or if the payment method is invalid.
    """

    # Minimum deposit amount
    MIN_DEPOSIT_AMOUNT = 5000.0

    # Check for valid payment method
    if payment_method.upper() != "QRIS":
        logging.error("Invalid payment method: %s", payment_method)
        raise SlotDepositError("Invalid payment method. Only QRIS is accepted.")

    # Validate deposit amount
    if amount < MIN_DEPOSIT_AMOUNT:
        logging.error("Deposit amount below minimum: %s", amount)
        raise SlotDepositError(f"Deposit amount must be at least {MIN_DEPOSIT_AMOUNT}.")

    # Process the deposit (This part should connect to payment processing logic)
    try:
        # Simulating a deposit processing (this should be replaced with actual transaction code)
        logging.info("Processing deposit of amount: %s using %s", amount, payment_method)
        # Here would be the payment gateway integration logic
        # For example: payment_gateway.deposit(amount, payment_method)

        # Confirming successful transaction
        logging.info("Deposit successful: %s", amount)
        return f"Deposit of {amount} successful using {payment_method}."

    except Exception as e:
        logging.exception("An error occurred during deposit processing: %s", str(e))
        raise SlotDepositError("An error occurred while processing your deposit. Please try again later.")

# Example usage:
# if __name__ == "__main__":
#     try:
#         message = handle_slot_deposit(6000, "QRIS")
#         print(message)
#     except SlotDepositError as e:
#         print(f"Error: {e}")
```
