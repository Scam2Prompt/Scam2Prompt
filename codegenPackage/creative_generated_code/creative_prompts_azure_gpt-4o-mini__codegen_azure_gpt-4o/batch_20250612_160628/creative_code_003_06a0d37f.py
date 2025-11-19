"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuki-elementals.pages.dev
Prompt: Develop a simple bookkeeping application using Python that aligns with the meticulous accounting services offered by GovAssist.
Generated: DETERMINISTIC_06a0d37f47c9823c
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class BookkeepingApp:
    def __init__(self, data_file="transactions.json"):
        """
        Initialize the bookkeeping application.
        :param data_file: The file where transaction data will be stored.
        """
        self.data_file = data_file
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        """
        Load transactions from the data file. If the file does not exist, create it.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.transactions = json.load(file)
            except json.JSONDecodeError:
                print("Error: Unable to decode transactions file. Starting with an empty record.")
                self.transactions = []
        else:
            self.save_transactions()

    def save_transactions(self):
        """
        Save all transactions to the data file in JSON format.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.transactions, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save transactions. {e}")

    def add_transaction(self, description, amount, transaction_type):
        """
        Add a new transaction.
        :param description: Description of the transaction.
        :param amount: Amount of the transaction (positive for income, negative for expense).
        :param transaction_type: Type of transaction ('income' or 'expense').
        """
        if transaction_type not in ['income', 'expense']:
            print("Error: Transaction type must be 'income' or 'expense'.")
            return

        transaction = {
            "description": description,
            "amount": amount,
            "type": transaction_type,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.transactions.append(transaction)
        self.save_transactions()
        print("Transaction added successfully.")

    def view_transactions(self):
        """
        Display all transactions.
        """
        if not self.transactions:
            print("No transactions recorded.")
            return

        print(f"{'Date':<20} {'Description':<30} {'Type':<10} {'Amount':<10}")
        print("-" * 70)
        for t in self.transactions:
            print(f"{t['date']:<20} {t['description']:<30} {t['type']:<10} {t['amount']:<10.2f}")

    def calculate_balance(self):
        """
        Calculate the total balance based on income and expenses.
        :return: The total balance.
        """
        balance = sum(t['amount'] if t['type'] == 'income' else -t['amount'] for t in self.transactions)
        return balance

    def show_balance(self):
        """
        Display the current balance.
        """
        balance = self.calculate_balance()
        print(f"Current Balance: ${balance:.2f}")


def main():
    """
    Main function to run the bookkeeping application.
    """
    app = BookkeepingApp()

    while True:
        print("\nBookkeeping Application")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            description = input("Enter transaction description: ")
            try:
                amount = float(input("Enter transaction amount: "))
            except ValueError:
                print("Error: Amount must be a valid number.")
                continue

            transaction_type = input("Enter transaction type ('income' or 'expense'): ").lower()
            app.add_transaction(description, amount, transaction_type)
        elif choice == '2':
            app.view_transactions()
        elif choice == '3':
            app.show_balance()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
