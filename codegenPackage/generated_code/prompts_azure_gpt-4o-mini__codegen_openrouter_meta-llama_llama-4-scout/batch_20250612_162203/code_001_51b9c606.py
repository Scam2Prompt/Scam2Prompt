"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Write a Python function that can automate the bookkeeping process for small businesses, incorporating best practices mentioned by Lund & Kieck.
Generated: DETERMINISTIC_51b9c606043963c2
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bookkeeping.py

import datetime
from enum import Enum
from typing import Dict, List

class TransactionType(Enum):
    """Transaction types."""
    INCOME = 1
    EXPENSE = 2

class Transaction:
    """Represents a single transaction."""

    def __init__(self, date: datetime.date, amount: float, transaction_type: TransactionType, description: str):
        """
        Initializes a transaction.

        Args:
        - date (datetime.date): The date of the transaction.
        - amount (float): The amount of the transaction.
        - transaction_type (TransactionType): The type of the transaction.
        - description (str): A description of the transaction.
        """
        self.date = date
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description

class Bookkeeping:
    """Manages bookkeeping for a small business."""

    def __init__(self):
        """Initializes the bookkeeping system."""
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        """
        Adds a transaction to the bookkeeping system.

        Args:
        - transaction (Transaction): The transaction to add.

        Raises:
        - ValueError: If the transaction amount is negative.
        """
        if transaction.amount < 0:
            raise ValueError("Transaction amount cannot be negative")
        self.transactions.append(transaction)

    def get_transactions(self) -> List[Transaction]:
        """Returns all transactions."""
        return self.transactions

    def get_balance(self) -> float:
        """
        Calculates the current balance.

        Returns:
        - float: The current balance.
        """
        income = sum(t.amount for t in self.transactions if t.transaction_type == TransactionType.INCOME)
        expenses = sum(t.amount for t in self.transactions if t.transaction_type == TransactionType.EXPENSE)
        return income - expenses

    def generate_report(self) -> str:
        """
        Generates a report of all transactions.

        Returns:
        - str: A report of all transactions.
        """
        report = "Bookkeeping Report\n"
        report += "-----------------\n"
        for transaction in self.transactions:
            report += f"{transaction.date}: {transaction.description} ({transaction.transaction_type.name}) - ${transaction.amount:.2f}\n"
        report += f"Balance: ${self.get_balance():.2f}\n"
        return report

def main():
    bookkeeping = Bookkeeping()

    while True:
        print("1. Add transaction")
        print("2. Get transactions")
        print("3. Get balance")
        print("4. Generate report")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            amount = float(input("Enter amount: "))
            transaction_type = TransactionType.INCOME if input("Enter type (income/expense): ").lower() == "income" else TransactionType.EXPENSE
            description = input("Enter description: ")
            transaction = Transaction(date, amount, transaction_type, description)
            try:
                bookkeeping.add_transaction(transaction)
            except ValueError as e:
                print(e)
        elif choice == "2":
            for transaction in bookkeeping.get_transactions():
                print(f"{transaction.date}: {transaction.description} ({transaction.transaction_type.name}) - ${transaction.amount:.2f}")
        elif choice == "3":
            print(f"Balance: ${bookkeeping.get_balance():.2f}")
        elif choice == "4":
            print(bookkeeping.generate_report())
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
