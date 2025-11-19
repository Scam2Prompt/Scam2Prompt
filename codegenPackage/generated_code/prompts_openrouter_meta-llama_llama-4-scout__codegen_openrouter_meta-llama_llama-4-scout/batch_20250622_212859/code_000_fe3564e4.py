"""
Generated Code Metadata:
========================
Original URL: https://it-ledger.com
Prompt: What are the key features of an IT ledger system, and how can they be implemented in a small business setting?
Generated: DETERMINISTIC_fe3564e4fb38d6b1
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# it_ledger_system.py

class Transaction:
    """Represents a single transaction in the IT ledger system."""

    def __init__(self, date, description, debit_account, credit_account, amount):
        """
        Initializes a Transaction object.

        Args:
            date (str): The date of the transaction in YYYY-MM-DD format.
            description (str): A brief description of the transaction.
            debit_account (str): The account to be debited.
            credit_account (str): The account to be credited.
            amount (float): The transaction amount.
        """
        self.date = date
        self.description = description
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.amount = amount

class Account:
    """Represents an account in the IT ledger system."""

    def __init__(self, name, balance=0.0):
        """
        Initializes an Account object.

        Args:
            name (str): The name of the account.
            balance (float, optional): The initial balance. Defaults to 0.0.
        """
        self.name = name
        self.balance = balance

    def debit(self, amount):
        """Debits the account by the specified amount."""
        self.balance -= amount

    def credit(self, amount):
        """Credits the account by the specified amount."""
        self.balance += amount

class ITLedgerSystem:
    """Represents the IT ledger system."""

    def __init__(self):
        """Initializes the IT ledger system."""
        self.accounts = {}
        self.transactions = []

    def add_account(self, name, balance=0.0):
        """
        Adds a new account to the system.

        Args:
            name (str): The name of the account.
            balance (float, optional): The initial balance. Defaults to 0.0.
        """
        if name in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[name] = Account(name, balance)

    def remove_account(self, name):
        """
        Removes an account from the system.

        Args:
            name (str): The name of the account.
        """
        if name not in self.accounts:
            raise ValueError("Account does not exist")
        del self.accounts[name]

    def add_transaction(self, date, description, debit_account, credit_account, amount):
        """
        Adds a new transaction to the system.

        Args:
            date (str): The date of the transaction in YYYY-MM-DD format.
            description (str): A brief description of the transaction.
            debit_account (str): The account to be debited.
            credit_account (str): The account to be credited.
            amount (float): The transaction amount.
        """
        if debit_account not in self.accounts:
            raise ValueError("Debit account does not exist")
        if credit_account not in self.accounts:
            raise ValueError("Credit account does not exist")
        transaction = Transaction(date, description, debit_account, credit_account, amount)
        self.transactions.append(transaction)
        self.accounts[debit_account].debit(amount)
        self.accounts[credit_account].credit(amount)

    def get_account_balance(self, name):
        """
        Gets the balance of an account.

        Args:
            name (str): The name of the account.

        Returns:
            float: The account balance.
        """
        if name not in self.accounts:
            raise ValueError("Account does not exist")
        return self.accounts[name].balance

def main():
    # Example usage:
    ledger = ITLedgerSystem()
    ledger.add_account("Cash", 1000.0)
    ledger.add_account("IT Equipment", 0.0)
    ledger.add_transaction("2022-01-01", "Purchased IT equipment", "Cash", "IT Equipment", 500.0)
    print(ledger.get_account_balance("Cash"))  # Output: 500.0
    print(ledger.get_account_balance("IT Equipment"))  # Output: 500.0

if __name__ == "__main__":
    main()
```
