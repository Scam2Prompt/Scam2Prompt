"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Write code to implement a financial accounting solution inspired by the techniques mentioned on Alwakeel Academy's website.
Generated: DETERMINISTIC_e6492c498925fc2e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Transaction:
    """Class to represent a financial transaction."""
    
    def __init__(self, amount: float, transaction_type: str, description: str = ""):
        """
        Initialize a new transaction.

        :param amount: The amount of the transaction.
        :param transaction_type: The type of transaction ('income' or 'expense').
        :param description: A brief description of the transaction.
        """
        if transaction_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.date = datetime.datetime.now()

    def __repr__(self):
        return f"{self.transaction_type.capitalize()} of {self.amount} on {self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.description}"


class Account:
    """Class to represent a financial account."""
    
    def __init__(self, account_name: str):
        """
        Initialize a new account.

        :param account_name: The name of the account.
        """
        self.account_name = account_name
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        """
        Add a transaction to the account.

        :param transaction: The transaction to add.
        """
        self.transactions.append(transaction)

    def get_balance(self) -> float:
        """
        Calculate the current balance of the account.

        :return: The current balance.
        """
        balance = 0.0
        for transaction in self.transactions:
            if transaction.transaction_type == 'income':
                balance += transaction.amount
            elif transaction.transaction_type == 'expense':
                balance -= transaction.amount
        return balance

    def get_transaction_history(self) -> List[Dict[str, Optional[str]]]:
        """
        Get the transaction history of the account.

        :return: A list of transactions with details.
        """
        return [{'date': t.date, 'type': t.transaction_type, 'amount': t.amount, 'description': t.description} for t in self.transactions]


class AccountingSystem:
    """Class to manage multiple accounts in the accounting system."""
    
    def __init__(self):
        """Initialize the accounting system with an empty account list."""
        self.accounts: Dict[str, Account] = {}

    def create_account(self, account_name: str):
        """
        Create a new account.

        :param account_name: The name of the account to create.
        """
        if account_name in self.accounts:
            raise ValueError(f"Account '{account_name}' already exists.")
        self.accounts[account_name] = Account(account_name)

    def add_transaction_to_account(self, account_name: str, transaction: Transaction):
        """
        Add a transaction to a specified account.

        :param account_name: The name of the account.
        :param transaction: The transaction to add.
        """
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")
        self.accounts[account_name].add_transaction(transaction)

    def get_account_balance(self, account_name: str) -> float:
        """
        Get the balance of a specified account.

        :param account_name: The name of the account.
        :return: The current balance of the account.
        """
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")
        return self.accounts[account_name].get_balance()

    def get_account_transaction_history(self, account_name: str) -> List[Dict[str, Optional[str]]]:
        """
        Get the transaction history of a specified account.

        :param account_name: The name of the account.
        :return: A list of transactions for the account.
        """
        if account_name not in self.accounts:
            raise ValueError(f"Account '{account_name}' does not exist.")
        return self.accounts[account_name].get_transaction_history()


# Example usage
if __name__ == "__main__":
    accounting_system = AccountingSystem()
    
    # Create accounts
    accounting_system.create_account("Personal")
    accounting_system.create_account("Business")

    # Add transactions
    accounting_system.add_transaction_to_account("Personal", Transaction(1000.0, 'income', "Salary"))
    accounting_system.add_transaction_to_account("Personal", Transaction(200.0, 'expense', "Groceries"))
    accounting_system.add_transaction_to_account("Business", Transaction(5000.0, 'income', "Client Payment"))
    accounting_system.add_transaction_to_account("Business", Transaction(1500.0, 'expense', "Office Supplies"))

    # Get balances
    print("Personal Account Balance:", accounting_system.get_account_balance("Personal"))
    print("Business Account Balance:", accounting_system.get_account_balance("Business"))

    # Get transaction history
    print("Personal Account Transactions:", accounting_system.get_account_transaction_history("Personal"))
    print("Business Account Transactions:", accounting_system.get_account_transaction_history("Business"))
```
