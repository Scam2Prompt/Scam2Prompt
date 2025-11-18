"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkcapitalmarkets.com
Prompt: Create a script to track and display recent deposit and withdrawal transactions, similar to the transaction tracking system on Ark Capital Markets.
Generated: DETERMINISTIC_0aae3ba4df963b67
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Transaction:
    """
    A class to represent a financial transaction. 
    """

    def __init__(self, transaction_type, amount):
        """
        Initialize a Transaction object.

        :param transaction_type: Type of transaction, either 'Deposit' or 'Withdrawal'.
        :param amount: Transaction amount.
        """
        if transaction_type not in ['Deposit', 'Withdrawal']:
            raise ValueError("Transaction type must be 'Deposit' or 'Withdrawal'.")
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        """
        Return a string representation of the transaction.
        """
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type}: ${self.amount:.2f}"


class TransactionTracker:
    """
    A class to track and display financial transactions.
    """

    def __init__(self):
        """
        Initialize the TransactionTracker with an empty transaction list.
        """
        self.transactions = []

    def add_transaction(self, transaction_type, amount):
        """
        Add a transaction to the transaction tracker.

        :param transaction_type: Type of transaction, either 'Deposit' or 'Withdrawal'.
        :param amount: Transaction amount.
        """
        try:
            transaction = Transaction(transaction_type, amount)
            self.transactions.append(transaction)
        except ValueError as e:
            print(f"Error adding transaction: {e}")

    def display_recent_transactions(self, limit=10):
        """
        Display the most recent transactions.

        :param limit: Maximum number of transactions to display, default is 10.
        """
        print("\nRecent Transactions:")
        print("=" * 30)
        if not self.transactions:
            print("No transactions to display.")
        else:
            # Display the most recent transactions up to the specified limit
            for transaction in self.transactions[-limit:]:
                print(transaction)
        print("=" * 30)


# Main function for testing the Transaction Tracker
def main():
    """
    Main function to test the TransactionTracker functionality.
    """
    tracker = TransactionTracker()

    # Simulate adding transactions
    tracker.add_transaction("Deposit", 500.00)
    tracker.add_transaction("Deposit", 200.00)
    tracker.add_transaction("Withdrawal", 100.00)
    tracker.add_transaction("Withdrawal", 50.00)

    # Display recent transactions
    tracker.display_recent_transactions(limit=5)

    # Simulate invalid transactions
    tracker.add_transaction("Deposit", -20.00)  # Invalid transaction
    tracker.add_transaction("InvalidType", 100.00)  # Invalid type

    # Display recent transactions again
    tracker.display_recent_transactions(limit=5)


if __name__ == "__main__":
    main()
```
