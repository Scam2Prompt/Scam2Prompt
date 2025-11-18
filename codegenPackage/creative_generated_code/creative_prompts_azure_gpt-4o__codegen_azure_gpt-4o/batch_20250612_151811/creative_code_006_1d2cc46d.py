"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Write a script to manage daily financial transactions such as recording sales, purchases, receipts, and payments, ensuring accurate bookkeeping as described in Eximious Global's administrative support services.
Generated: DETERMINISTIC_1d2cc46d7f28e475
Batch ID: 20250612_151811
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

class FinancialTransactionManager:
    """
    A class to manage daily financial transactions such as recording sales, purchases, 
    receipts, and payments, ensuring accurate bookkeeping.
    """

    def __init__(self, data_file="transactions.json"):
        """
        Initializes the manager with a file to store transactions.
        :param data_file: The file where transactions will be stored.
        """
        self.data_file = data_file
        if not os.path.exists(data_file):
            # Create the file if it does not exist
            with open(data_file, "w") as f:
                json.dump([], f)

    def load_transactions(self):
        """
        Loads transactions from the file.
        :return: List of transactions.
        """
        try:
            with open(self.data_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_transactions(self, transactions):
        """
        Saves transactions to the file.
        :param transactions: List of transactions to save.
        """
        try:
            with open(self.data_file, "w") as f:
                json.dump(transactions, f, indent=4)
        except Exception as e:
            print(f"Error saving transactions: {e}")

    def add_transaction(self, transaction_type, amount, description=""):
        """
        Adds a new transaction to the file.
        :param transaction_type: Type of transaction (e.g., 'sale', 'purchase', 'receipt', 'payment').
        :param amount: Amount involved in the transaction.
        :param description: Optional description of the transaction.
        """
        if transaction_type not in {"sale", "purchase", "receipt", "payment"}:
            raise ValueError("Invalid transaction type. Must be one of: 'sale', 'purchase', 'receipt', 'payment'.")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "description": description
        }

        transactions = self.load_transactions()
        transactions.append(transaction)
        self.save_transactions(transactions)

    def view_transactions(self):
        """
        Displays all transactions in a readable format.
        """
        transactions = self.load_transactions()
        if not transactions:
            print("No transactions recorded.")
        else:
            print("Transactions:")
            for idx, transaction in enumerate(transactions, 1):
                print(f"{idx}. Date: {transaction['date']}, Type: {transaction['type']}, "
                      f"Amount: ${transaction['amount']:.2f}, Description: {transaction['description']}")

    def filter_transactions(self, transaction_type):
        """
        Filters transactions by type and displays them.
        :param transaction_type: Type of transactions to filter (e.g., 'sale', 'purchase', 'receipt', 'payment').
        """
        if transaction_type not in {"sale", "purchase", "receipt", "payment"}:
            raise ValueError("Invalid transaction type. Must be one of: 'sale', 'purchase', 'receipt', 'payment'.")

        transactions = self.load_transactions()
        filtered = [t for t in transactions if t["type"] == transaction_type]

        if not filtered:
            print(f"No transactions found for type: {transaction_type}")
        else:
            print(f"{transaction_type.capitalize()} Transactions:")
            for idx, transaction in enumerate(filtered, 1):
                print(f"{idx}. Date: {transaction['date']}, Amount: ${transaction['amount']:.2f}, "
                      f"Description: {transaction['description']}")

# Example usage:
if __name__ == "__main__":
    manager = FinancialTransactionManager()

    try:
        # Add a transaction
        manager.add_transaction("sale", 100.50, "Sold product A")
        manager.add_transaction("purchase", 45.75, "Bought materials")
        
        # View all transactions
        manager.view_transactions()
        
        # Filter transactions by type
        manager.filter_transactions("sale")
    except Exception as e:
        print(f"Error: {e}")
```
