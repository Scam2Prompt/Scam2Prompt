"""
Generated Code Metadata:
========================
Original URL: https://dutton.co.nz
Prompt: "Generate a simple accounting ledger template using Python."
Generated: DETERMINISTIC_24f5fda9ba26ea0c
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# accounting_ledger.py

class Transaction:
    """Represents a single transaction in the ledger."""

    def __init__(self, date, description, debit_account, credit_account, amount):
        """
        Initializes a Transaction object.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Brief description of the transaction.
            debit_account (str): Account being debited.
            credit_account (str): Account being credited.
            amount (float): Transaction amount.
        """
        self.date = date
        self.description = description
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.amount = amount


class Account:
    """Represents an account in the ledger."""

    def __init__(self, name, balance=0.0):
        """
        Initializes an Account object.

        Args:
            name (str): Name of the account.
            balance (float, optional): Initial balance. Defaults to 0.0.
        """
        self.name = name
        self.balance = balance
        self.transactions = []

    def debit(self, amount):
        """Decreases the account balance by the given amount."""
        self.balance -= amount

    def credit(self, amount):
        """Increases the account balance by the given amount."""
        self.balance += amount


class Ledger:
    """Represents a simple accounting ledger."""

    def __init__(self):
        """Initializes a Ledger object."""
        self.accounts = {}

    def add_account(self, name, balance=0.0):
        """
        Adds a new account to the ledger.

        Args:
            name (str): Name of the account.
            balance (float, optional): Initial balance. Defaults to 0.0.

        Raises:
            ValueError: If an account with the same name already exists.
        """
        if name in self.accounts:
            raise ValueError(f"Account '{name}' already exists.")
        self.accounts[name] = Account(name, balance)

    def get_account(self, name):
        """
        Retrieves an account from the ledger.

        Args:
            name (str): Name of the account.

        Returns:
            Account: The account object, or None if not found.
        """
        return self.accounts.get(name)

    def record_transaction(self, date, description, debit_account, credit_account, amount):
        """
        Records a transaction in the ledger.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Brief description of the transaction.
            debit_account (str): Account being debited.
            credit_account (str): Account being credited.
            amount (float): Transaction amount.

        Raises:
            ValueError: If either account does not exist.
        """
        debit = self.get_account(debit_account)
        credit = self.get_account(credit_account)

        if debit is None:
            raise ValueError(f"Account '{debit_account}' does not exist.")
        if credit is None:
            raise ValueError(f"Account '{credit_account}' does not exist.")

        transaction = Transaction(date, description, debit_account, credit_account, amount)
        debit.debit(amount)
        credit.credit(amount)
        debit.transactions.append(transaction)
        credit.transactions.append(transaction)

    def print_ledger(self):
        """Prints the current state of the ledger."""
        for account in self.accounts.values():
            print(f"Account: {account.name}")
            print(f"Balance: {account.balance:.2f}")
            print("Transactions:")
            for transaction in account.transactions:
                if transaction.debit_account == account.name:
                    print(f"  - {transaction.date} {transaction.description} (debit) -{transaction.amount:.2f}")
                else:
                    print(f"  + {transaction.date} {transaction.description} (credit) +{transaction.amount:.2f}")
            print()


def main():
    ledger = Ledger()

    while True:
        print("1. Add account")
        print("2. Record transaction")
        print("3. Print ledger")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter account name: ")
            balance = float(input("Enter initial balance: "))
            ledger.add_account(name, balance)
        elif choice == "2":
            date = input("Enter transaction date (YYYY-MM-DD): ")
            description = input("Enter transaction description: ")
            debit_account = input("Enter debit account: ")
            credit_account = input("Enter credit account: ")
            amount = float(input("Enter transaction amount: "))
            ledger.record_transaction(date, description, debit_account, credit_account, amount)
        elif choice == "3":
            ledger.print_ledger()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
