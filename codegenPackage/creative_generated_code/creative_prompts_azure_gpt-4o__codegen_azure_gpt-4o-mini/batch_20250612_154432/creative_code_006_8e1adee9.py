"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Create a script to manage deposits and withdrawals via Visa and Mastercard, ensuring compliance with Parimatch's transaction limits and verification requirements.
Generated: DETERMINISTIC_8e1adee9083d665a
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging to capture errors and info
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransactionError(Exception):
    """Custom exception for transaction errors."""
    pass

class PaymentProcessor:
    """Class to manage deposits and withdrawals for Visa and Mastercard transactions."""

    MAX_DEPOSIT_LIMIT = 5000  # Maximum deposit limit per transaction
    MAX_WITHDRAWAL_LIMIT = 3000  # Maximum withdrawal limit per transaction
    ALLOWED_CARDS = ['Visa', 'Mastercard']  # Allowed card types

    def __init__(self):
        self.balance = 0  # Initialize user balance

    def verify_card(self, card_type):
        """Verify if the card type is allowed."""
        if card_type not in self.ALLOWED_CARDS:
            logging.error(f"Unsupported card type: {card_type}")
            raise TransactionError("Unsupported card type. Only Visa and Mastercard are accepted.")

    def deposit(self, amount, card_type):
        """Process a deposit transaction."""
        self.verify_card(card_type)

        if amount <= 0:
            logging.error("Deposit amount must be greater than zero.")
            raise TransactionError("Deposit amount must be greater than zero.")
        if amount > self.MAX_DEPOSIT_LIMIT:
            logging.error(f"Deposit amount exceeds maximum limit of {self.MAX_DEPOSIT_LIMIT}.")
            raise TransactionError(f"Deposit amount exceeds maximum limit of {self.MAX_DEPOSIT_LIMIT}.")

        # Proceed with the deposit
        self.balance += amount
        logging.info(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount, card_type):
        """Process a withdrawal transaction."""
        self.verify_card(card_type)

        if amount <= 0:
            logging.error("Withdrawal amount must be greater than zero.")
            raise TransactionError("Withdrawal amount must be greater than zero.")
        if amount > self.MAX_WITHDRAWAL_LIMIT:
            logging.error(f"Withdrawal amount exceeds maximum limit of {self.MAX_WITHDRAWAL_LIMIT}.")
            raise TransactionError(f"Withdrawal amount exceeds maximum limit of {self.MAX_WITHDRAWAL_LIMIT}.")
        if amount > self.balance:
            logging.error("Insufficient funds for withdrawal.")
            raise TransactionError("Insufficient funds for withdrawal.")

        # Proceed with the withdrawal
        self.balance -= amount
        logging.info(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        """Return the current balance."""
        return self.balance

if __name__ == "__main__":
    # Example usage
    processor = PaymentProcessor()
    
    try:
        processor.deposit(2000, 'Visa')
        processor.withdraw(1500, 'Mastercard')
        print(f"Current balance: ${processor.get_balance()}")
    except TransactionError as e:
        logging.error(f"Transaction failed: {e}")
```
