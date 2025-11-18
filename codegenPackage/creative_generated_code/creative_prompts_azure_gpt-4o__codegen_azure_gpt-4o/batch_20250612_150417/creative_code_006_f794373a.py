"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: Develop a Python program to track and display recent deposit and withdrawal transactions, similar to the transaction history shown on MaxProfit's website.
Generated: DETERMINISTIC_f794373a9ce37bb6
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime


class Transaction:
    """
    Represents a single banking transaction (deposit or withdrawal).
    """
    def __init__(self, transaction_type, amount):
        """
        Initializes a transaction instance.
        
        Args:
            transaction_type (str): Either 'deposit' or 'withdrawal'.
            amount (float): The amount involved in the transaction.
        """
        if transaction_type not in ['deposit', 'withdrawal']:
            raise ValueError("Transaction type must be either 'deposit' or 'withdrawal'")
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero")

        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()  # Record the transaction time

    def __str__(self):
        """
        Returns a string representation of the transaction.
        """
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.capitalize()} of ${self.amount:.2f}"


class TransactionTracker:
    """
    Tracks and displays recent deposit and withdrawal transactions.
    """
    def __init__(self):
        """
        Initializes the tracker with an empty transaction history.
        """
        self.transactions = []  # List to store transaction history

    def add_transaction(self, transaction_type, amount):
        """
        Adds a transaction to the history.
        
        Args:
            transaction_type (str): Either 'deposit' or 'withdrawal'.
            amount (float): The amount of the transaction.
        """
        try:
            transaction = Transaction(transaction_type, amount)
            self.transactions.append(transaction)
        except ValueError as e:
            print(f"Error adding transaction: {e}")

    def get_recent_transactions(self, limit=10):
        """
        Retrieves the most recent transactions up to a specified limit.
        
        Args:
            limit (int): Number of recent transactions to retrieve. Default is 10.
        
        Returns:
            list: A list of string representations of the recent transactions.
        """
        return [str(txn) for txn in self.transactions[-limit:]]

    def display_transactions(self, limit=10):
        """
        Displays the most recent transactions.
        
        Args:
            limit (int): Number of recent transactions to display. Default is 10.
        """
        recent_transactions = self.get_recent_transactions(limit)
        if not recent_transactions:
            print("No transactions found.")
        else:
            print("Recent Transactions:")
            for txn in recent_transactions:
                print(txn)


# Example usage
if __name__ == "__main__":
    tracker = TransactionTracker()

    # Adding some transactions
    tracker.add_transaction('deposit', 1000.0)
    tracker.add_transaction('withdrawal', 200.0)
    tracker.add_transaction('deposit', 500.0)

    # Display the last 5 transactions
    tracker.display_transactions(limit=5)
```
