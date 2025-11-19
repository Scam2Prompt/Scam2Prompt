"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Develop a feature for a bookkeeping system that tracks profitability and personal wealth growth for sole proprietors and corporations, inspired by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_f5ca1b5f3d280e97
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bookkeeping_system.py

class Transaction:
    """Represents a single financial transaction."""

    def __init__(self, date, description, amount, transaction_type):
        """
        Initializes a Transaction object.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Brief description of the transaction.
            amount (float): Amount of the transaction.
            transaction_type (str): Type of transaction (income or expense).
        """
        self.date = date
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date} - {self.description}: {self.amount:.2f} ({self.transaction_type})"


class Account:
    """Represents a financial account."""

    def __init__(self, name, initial_balance=0.0):
        """
        Initializes an Account object.

        Args:
            name (str): Name of the account.
            initial_balance (float, optional): Initial balance of the account. Defaults to 0.0.
        """
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def add_transaction(self, transaction):
        """
        Adds a transaction to the account.

        Args:
            transaction (Transaction): Transaction to add.
        """
        self.transactions.append(transaction)
        if transaction.transaction_type == "income":
            self.balance += transaction.amount
        elif transaction.transaction_type == "expense":
            self.balance -= transaction.amount

    def get_balance(self):
        """Returns the current balance of the account."""
        return self.balance

    def get_transaction_history(self):
        """Returns a list of all transactions in the account."""
        return self.transactions


class BookkeepingSystem:
    """Represents a bookkeeping system for tracking profitability and personal wealth growth."""

    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0.0):
        """
        Creates a new account in the bookkeeping system.

        Args:
            name (str): Name of the account.
            initial_balance (float, optional): Initial balance of the account. Defaults to 0.0.
        """
        if name in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[name] = Account(name, initial_balance)

    def add_transaction(self, account_name, transaction):
        """
        Adds a transaction to an account in the bookkeeping system.

        Args:
            account_name (str): Name of the account.
            transaction (Transaction): Transaction to add.
        """
        if account_name not in self.accounts:
            raise ValueError("Account does not exist")
        self.accounts[account_name].add_transaction(transaction)

    def get_account_balance(self, account_name):
        """
        Returns the current balance of an account in the bookkeeping system.

        Args:
            account_name (str): Name of the account.

        Returns:
            float: Current balance of the account.
        """
        if account_name not in self.accounts:
            raise ValueError("Account does not exist")
        return self.accounts[account_name].get_balance()

    def get_account_transaction_history(self, account_name):
        """
        Returns a list of all transactions in an account in the bookkeeping system.

        Args:
            account_name (str): Name of the account.

        Returns:
            list: List of transactions in the account.
        """
        if account_name not in self.accounts:
            raise ValueError("Account does not exist")
        return self.accounts[account_name].get_transaction_history()


def main():
    bookkeeping_system = BookkeepingSystem()

    while True:
        print("\nBookkeeping System Menu:")
        print("1. Create Account")
        print("2. Add Transaction")
        print("3. Get Account Balance")
        print("4. Get Account Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account name: ")
            initial_balance = float(input("Enter initial balance (default=0.0): ") or 0.0)
            bookkeeping_system.create_account(name, initial_balance)
            print(f"Account '{name}' created successfully")
        elif choice == "2":
            account_name = input("Enter account name: ")
            date = input("Enter transaction date (YYYY-MM-DD): ")
            description = input("Enter transaction description: ")
            amount = float(input("Enter transaction amount: "))
            transaction_type = input("Enter transaction type (income/expense): ")
            transaction = Transaction(date, description, amount, transaction_type)
            bookkeeping_system.add_transaction(account_name, transaction)
            print(f"Transaction added to account '{account_name}' successfully")
        elif choice == "3":
            account_name = input("Enter account name: ")
            try:
                balance = bookkeeping_system.get_account_balance(account_name)
                print(f"Account '{account_name}' balance: {balance:.2f}")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            account_name = input("Enter account name: ")
            try:
                transactions = bookkeeping_system.get_account_transaction_history(account_name)
                for transaction in transactions:
                    print(transaction)
            except ValueError as e:
                print(str(e))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
