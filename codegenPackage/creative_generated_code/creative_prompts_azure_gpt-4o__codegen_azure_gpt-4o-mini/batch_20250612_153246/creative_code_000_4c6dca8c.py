"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Write a Python script to simulate a deposit system for an online slot game platform, including support for Pulsa-based transactions and a minimum deposit of 10,000 IDR.
Generated: DETERMINISTIC_4c6dca8c36724abf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DepositSystem:
    """
    A class to simulate a deposit system for an online slot game platform.
    Supports Pulsa-based transactions with a minimum deposit amount.
    """

    MIN_DEPOSIT = 10000  # Minimum deposit in IDR

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """
        Process a deposit transaction.

        :param amount: The amount to deposit (in IDR)
        :raises ValueError: If the deposit amount is less than the minimum requirement
        :raises Exception: For other transaction-related errors
        """
        try:
            self.validate_deposit(amount)
            self.balance += amount
            logging.info(f"Deposit of {amount} IDR successful. New balance: {self.balance} IDR.")
        except ValueError as ve:
            logging.error(f"Deposit failed: {ve}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

    def validate_deposit(self, amount):
        """
        Validate the deposit amount.

        :param amount: The amount to deposit (in IDR)
        :raises ValueError: If the deposit amount is less than the minimum requirement
        """
        if amount < self.MIN_DEPOSIT:
            raise ValueError(f"Minimum deposit amount is {self.MIN_DEPOSIT} IDR.")

    def get_balance(self):
        """
        Return the current balance.

        :return: Current balance (in IDR)
        """
        return self.balance


def main():
    """
    Main function to simulate deposits.
    """
    deposit_system = DepositSystem()

    # Simulate deposit transactions
    transactions = [5000, 15000, 20000, 9000]  # Example transaction amounts

    for amount in transactions:
        try:
            deposit_system.deposit(amount)
        except Exception:
            continue  # Continue with the next transaction on error

    # Final balance
    logging.info(f"Final balance: {deposit_system.get_balance()} IDR.")


if __name__ == "__main__":
    main()
```
