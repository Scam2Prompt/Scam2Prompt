"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Write a Python code to manage financial accounting data for small businesses, including tools for financial reporting and analysis.
Generated: DETERMINISTIC_7c1573cdd8d1a189
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_accounting.py

class Transaction:
    """Represents a financial transaction."""

    def __init__(self, date, description, amount, type):
        """
        Initializes a Transaction object.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
            type (str): Type of the transaction (income or expense).
        """
        self.date = date
        self.description = description
        self.amount = amount
        self.type = type

    def __repr__(self):
        return f"Transaction('{self.date}', '{self.description}', {self.amount}, '{self.type}')"


class FinancialAccount:
    """Represents a financial account."""

    def __init__(self, name, balance=0.0):
        """
        Initializes a FinancialAccount object.

        Args:
            name (str): Name of the account.
            balance (float, optional): Initial balance of the account. Defaults to 0.0.
        """
        self.name = name
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction):
        """
        Adds a transaction to the account.

        Args:
            transaction (Transaction): Transaction to add.

        Raises:
            ValueError: If the transaction type is invalid.
        """
        if transaction.type not in ['income', 'expense']:
            raise ValueError("Invalid transaction type")

        self.transactions.append(transaction)
        if transaction.type == 'income':
            self.balance += transaction.amount
        elif transaction.type == 'expense':
            self.balance -= transaction.amount

    def get_balance(self):
        """Returns the current balance of the account."""
        return self.balance

    def get_transactions(self):
        """Returns a list of transactions in the account."""
        return self.transactions


class FinancialReport:
    """Represents a financial report."""

    def __init__(self, accounts):
        """
        Initializes a FinancialReport object.

        Args:
            accounts (list[FinancialAccount]): List of financial accounts.
        """
        self.accounts = accounts

    def generate_income_statement(self):
        """
        Generates an income statement.

        Returns:
            dict: Income statement data.
        """
        income_statement = {}
        for account in self.accounts:
            income = sum(t.amount for t in account.transactions if t.type == 'income')
            expenses = sum(t.amount for t in account.transactions if t.type == 'expense')
            net_income = income - expenses
            income_statement[account.name] = {
                'income': income,
                'expenses': expenses,
                'net_income': net_income
            }
        return income_statement

    def generate_balance_sheet(self):
        """
        Generates a balance sheet.

        Returns:
            dict: Balance sheet data.
        """
        balance_sheet = {}
        for account in self.accounts:
            balance_sheet[account.name] = account.get_balance()
        return balance_sheet


def main():
    try:
        # Create financial accounts
        account1 = FinancialAccount('Cash', 1000.0)
        account2 = FinancialAccount('Bank', 5000.0)

        # Add transactions
        account1.add_transaction(Transaction('2022-01-01', 'Initial deposit', 1000.0, 'income'))
        account1.add_transaction(Transaction('2022-01-02', 'Rent payment', 500.0, 'expense'))
        account2.add_transaction(Transaction('2022-01-03', 'Sales revenue', 2000.0, 'income'))

        # Create financial report
        report = FinancialReport([account1, account2])

        # Generate financial statements
        income_statement = report.generate_income_statement()
        balance_sheet = report.generate_balance_sheet()

        # Print financial statements
        print("Income Statement:")
        for account, data in income_statement.items():
            print(f"Account: {account}")
            print(f"Income: ${data['income']:.2f}")
            print(f"Expenses: ${data['expenses']:.2f}")
            print(f"Net Income: ${data['net_income']:.2f}")
            print()

        print("Balance Sheet:")
        for account, balance in balance_sheet.items():
            print(f"Account: {account}, Balance: ${balance:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
