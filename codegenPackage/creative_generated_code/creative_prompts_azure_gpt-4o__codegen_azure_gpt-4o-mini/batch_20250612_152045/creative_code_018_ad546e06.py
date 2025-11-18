"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Generate code for integrating a banking software system with RD/FD account management, as outlined by MDA Tech Sys.
Generated: DETERMINISTIC_ad546e061a6810aa
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    """Class to represent a bank account with RD/FD management."""

    def __init__(self, account_number: str, account_type: str, balance: float = 0.0):
        """
        Initialize a new bank account.

        :param account_number: Unique identifier for the account.
        :param account_type: Type of the account ('RD' or 'FD').
        :param balance: Initial balance of the account.
        """
        self.account_number = account_number
        self.account_type = account_type.upper()
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        if amount <= 0:
            logging.error("Deposit amount must be positive.")
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        logging.info(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        if amount <= 0:
            logging.error("Withdrawal amount must be positive.")
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            logging.error("Insufficient funds for withdrawal.")
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        logging.info(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")

    def get_balance(self) -> float:
        """Return the current balance of the account."""
        return self.balance


class AccountManager:
    """Class to manage multiple bank accounts."""

    def __init__(self):
        """Initialize the account manager with an empty account list."""
        self.accounts: Dict[str, BankAccount] = {}

    def create_account(self, account_number: str, account_type: str) -> None:
        """Create a new bank account."""
        if account_number in self.accounts:
            logging.error("Account already exists.")
            raise ValueError("Account already exists.")
        if account_type not in ['RD', 'FD']:
            logging.error("Invalid account type.")
            raise ValueError("Invalid account type. Must be 'RD' or 'FD'.")
        self.accounts[account_number] = BankAccount(account_number, account_type)
        logging.info(f"Created account {account_number} of type {account_type}.")

    def get_account(self, account_number: str) -> BankAccount:
        """Retrieve an account by its account number."""
        if account_number not in self.accounts:
            logging.error(f"Account not found: {account_number}")
            raise ValueError("Account not found.")
        return self.accounts[account_number]

    def perform_transaction(self, account_number: str, transaction_type: str, amount: float) -> None:
        """Perform a deposit or withdrawal transaction on an account."""
        account = self.get_account(account_number)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            logging.error("Invalid transaction type.")
            raise ValueError("Invalid transaction type. Must be 'deposit' or 'withdraw'.")


# Example usage
if __name__ == "__main__":
    manager = AccountManager()
    
    try:
        # Create accounts
        manager.create_account('123456789', 'FD')
        manager.create_account('987654321', 'RD')

        # Perform transactions
        manager.perform_transaction('123456789', 'deposit', 1000.0)
        manager.perform_transaction('987654321', 'withdraw', 500.0)

        # Retrieve account balance
        fd_account = manager.get_account('123456789')
        rd_account = manager.get_account('987654321')
        print(f"FD Account Balance: {fd_account.get_balance()}")
        print(f"RD Account Balance: {rd_account.get_balance()}")

    except ValueError as e:
        logging.error(f"An error occurred: {e}")
```
