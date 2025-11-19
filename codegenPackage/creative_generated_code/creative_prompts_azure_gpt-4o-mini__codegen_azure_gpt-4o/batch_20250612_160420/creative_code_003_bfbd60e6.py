"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgdr.com
Prompt: What are the best practices for coding a ledger application based on the guidelines from ledgdr.com?
Generated: DETERMINISTIC_bfbd60e60eb5b92b
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Ledger Application
This is a clean, production-ready Python implementation of a ledger application based on best practices.
The application allows users to add, view, and retrieve transactions.
"""

import datetime
import json


class Ledger:
    """
    A class representing a ledger application that records financial transactions.
    """
    def __init__(self, filename="ledger.json"):
        # Initialize the ledger with a file for persistence
        self.filename = filename
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        """
        Load transactions from the file if it exists.
        """
        try:
            with open(self.filename, "r") as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            # File does not exist, initialize an empty transaction list
            self.transactions = []
        except json.JSONDecodeError:
            # Handle corrupted file gracefully
            print("Warning: Ledger file is corrupted. Starting with a blank ledger.")
            self.transactions = []

    def save_transactions(self):
        """
        Save transactions to the file for persistence.
        """
        try:
            with open(self.filename, "w") as file:
                json.dump(self.transactions, file, indent=4)
        except IOError as e:
            # Handle file-related errors
            print(f"Error saving transactions: {e}")

    def add_transaction(self, amount, description=""):
        """
        Add a new transaction to the ledger.
        :param amount: Transaction amount (positive for income, negative for expense)
        :param description: Optional description of the transaction
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a numeric value.")

        transaction = {
            "date": datetime.datetime.now().isoformat(),
            "amount": amount,
            "description": description
        }
        self.transactions.append(transaction)
        self.save_transactions()

    def get_all_transactions(self):
        """
        Retrieve all transactions as a list.
        :return: List of all transactions
        """
        return self.transactions

    def get_balance(self):
        """
        Calculate the current balance based on all transactions.
        :return: Current balance
        """
        return sum(transaction["amount"] for transaction in self.transactions)


# Main code for running the ledger application (example usage)
def main():
    """
    Main function for the ledger application.
    """
    ledger = Ledger()

    print("Welcome to the Ledger Application!")
    while True:
        print("\nOptions:")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. View Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                # Add a transaction
                amount = float(input("Enter transaction amount (use negative for expense): "))
                description = input("Enter a description (optional): ")
                ledger.add_transaction(amount, description)
                print("Transaction added successfully!")
            elif choice == "2":
                # View all transactions
                transactions = ledger.get_all_transactions()
                print("\nAll Transactions:")
                for transaction in transactions:
                    print(f"{transaction['date']} | {transaction['amount']} | {transaction['description']}")
            elif choice == "3":
                # View current balance
                balance = ledger.get_balance()
                print(f"\nCurrent Balance: {balance}")
            elif choice == "4":
                # Exit the application
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice! Please choose a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
