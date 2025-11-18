"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earn-gummyonsol.pages.dev
Prompt: Write a function to simulate $Gummy token transactions based on the tokenomics model described on the webpage.
Generated: DETERMINISTIC_c13466fac398a65a
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants representing tokenomics parameters
TRANSACTION_FEE_PERCENTAGE = 2.0  # 2% transaction fee
BURN_PERCENTAGE = 1.0            # 1% tokens are burned from the transaction fee
REWARD_PERCENTAGE = 0.5          # 0.5% tokens are redistributed as rewards

class GummyTokenTransactionError(Exception):
    """Custom exception for Gummy token transactions."""
    pass

def simulate_gummy_transaction(sender_balance, recipient_balance, transaction_amount):
    """
    Simulates a Gummy token transaction based on tokenomics.

    Parameters:
        sender_balance (float): The balance of the sender before the transaction.
        recipient_balance (float): The balance of the recipient before the transaction.
        transaction_amount (float): The amount of tokens to be transferred.

    Returns:
        tuple: Updated sender_balance, recipient_balance, and total supply adjustment.

    Raises:
        GummyTokenTransactionError: If the sender balance is insufficient or if the transaction amount is invalid.
    """
    try:
        # Validate inputs
        if transaction_amount <= 0:
            raise GummyTokenTransactionError("Transaction amount must be greater than 0.")
        if sender_balance < transaction_amount:
            raise GummyTokenTransactionError("Sender does not have enough tokens.")

        # Calculate transaction fee
        transaction_fee = (TRANSACTION_FEE_PERCENTAGE / 100) * transaction_amount

        # Calculate burn and reward amounts
        burn_amount = (BURN_PERCENTAGE / 100) * transaction_amount
        reward_amount = (REWARD_PERCENTAGE / 100) * transaction_amount

        # Update balances
        sender_balance -= transaction_amount  # Deduct full transaction amount from sender
        recipient_balance += transaction_amount - transaction_fee  # Add amount minus fee to recipient

        # Adjust total supply (burn removes tokens from circulation)
        total_supply_adjustment = -burn_amount  # Negative adjustment for burning

        logging.info(f"Transaction completed successfully. Sender: {sender_balance}, Recipient: {recipient_balance}, Burned: {burn_amount}, Reward: {reward_amount}.")
        return sender_balance, recipient_balance, total_supply_adjustment
    except GummyTokenTransactionError as e:
        logging.error(f"Transaction error: {e}")
        return sender_balance, recipient_balance, 0  # Return original balances and no supply adjustment in case of error

# Example run (if needed for testing purposes)
if __name__ == "__main__":
    sender_balance = 1000.0
    recipient_balance = 500.0
    transaction_amount = 100.0

    updated_sender, updated_recipient, supply_adjustment = simulate_gummy_transaction(sender_balance, recipient_balance, transaction_amount)
    print(f"Updated Sender Balance: {updated_sender}")
    print(f"Updated Recipient Balance: {updated_recipient}")
    print(f"Total Supply Adjustment: {supply_adjustment}")
```
