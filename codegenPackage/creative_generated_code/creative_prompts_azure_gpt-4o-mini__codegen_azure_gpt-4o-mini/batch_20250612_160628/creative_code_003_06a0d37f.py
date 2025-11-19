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
import json
import os
from datetime import datetime

class BookkeepingApp:
    """A simple bookkeeping application for managing financial transactions."""

    def __init__(self, filename='transactions.json'):
        """Initialize the application with a specified filename for storing transactions."""
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self):
        """Load transactions from a JSON file. If the file does not exist, return an empty list."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Unable to decode JSON. Returning empty transaction list.")
                    return []
        return []

    def save_transactions(self):
        """Save transactions to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, amount, category, description):
        """Add a new transaction to the list."""
        transaction = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'category': category,
            'description': description
        }
        self.transactions.append(transaction)
        self.save_transactions()
        print("Transaction added successfully.")

    def view_transactions(self):
        """Display all transactions."""
        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            print(f"Date: {transaction['date']}, Amount: {transaction['amount']}, "
                  f"Category: {transaction['category']}, Description: {transaction['description']}")

    def total_amount(self):
        """Calculate and return the total amount of all transactions."""
        return sum(transaction['amount'] for transaction in self.transactions)

    def filter_transactions(self, category):
        """Filter transactions by category and display them."""
        filtered = [t for t in self.transactions if t['category'] == category]

        if not filtered:
            print(f"No transactions found for category: {category}")
            return

        for transaction in filtered:
            print(f"Date: {transaction['date']}, Amount: {transaction['amount']}, "
                  f"Description: {transaction['description']}")

def main():
    app = BookkeepingApp()

    while True:
        print("\nSimple Bookkeeping Application")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Total Amount")
        print("4. Filter Transactions by Category")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            try:
                amount = float(input("Enter transaction amount: "))
                category = input("Enter transaction category: ")
                description = input("Enter transaction description: ")
                app.add_transaction(amount, category, description)
            except ValueError:
                print("Error: Invalid input for amount. Please enter a numeric value.")
        
        elif choice == '2':
            app.view_transactions()
        
        elif choice == '3':
            total = app.total_amount()
            print(f"Total amount of all transactions: {total}")
        
        elif choice == '4':
            category = input("Enter category to filter: ")
            app.filter_transactions(category)
        
        elif choice == '5':
            print("Exiting the application.")
            break
        
        else:
            print("Error: Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
```
