"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitesignaltrade.net
Prompt: Write code to implement a feature for tracking recent withdrawals and payouts, similar to the user ID and payment method display on Elite Signal Trade's platform.
Generated: DETERMINISTIC_52415b113ffcf475
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class Transaction:
    """Represents a financial transaction."""
    
    def __init__(self, user_id: str, amount: float, method: str, transaction_type: str):
        """
        Initializes a new Transaction.

        :param user_id: The ID of the user making the transaction.
        :param amount: The amount of the transaction.
        :param method: The payment method used for the transaction.
        :param transaction_type: The type of transaction ('withdrawal' or 'payout').
        """
        self.user_id = user_id
        self.amount = amount
        self.method = method
        self.transaction_type = transaction_type
        self.timestamp = datetime.datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Converts the transaction to a dictionary format for easy display."""
        return {
            'user_id': self.user_id,
            'amount': self.amount,
            'method': self.method,
            'transaction_type': self.transaction_type,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

class TransactionTracker:
    """Tracks recent withdrawals and payouts."""

    def __init__(self):
        """Initializes the TransactionTracker with an empty transaction list."""
        self.transactions: List[Transaction] = []

    def add_transaction(self, user_id: str, amount: float, method: str, transaction_type: str):
        """
        Adds a new transaction to the tracker.

        :param user_id: The ID of the user making the transaction.
        :param amount: The amount of the transaction.
        :param method: The payment method used for the transaction.
        :param transaction_type: The type of transaction ('withdrawal' or 'payout').
        :raises ValueError: If the transaction amount is negative or invalid type is provided.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        if transaction_type not in ['withdrawal', 'payout']:
            raise ValueError("Transaction type must be 'withdrawal' or 'payout'.")

        transaction = Transaction(user_id, amount, method, transaction_type)
        self.transactions.append(transaction)

    def get_recent_transactions(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieves the most recent transactions up to the specified limit.

        :param limit: The maximum number of transactions to return.
        :return: A list of recent transactions in dictionary format.
        :raises ValueError: If limit is less than zero.
        """
        if limit < 0:
            raise ValueError("Limit must be a non-negative integer.")
        
        # Return the most recent transactions sorted by timestamp
        return [transaction.to_dict() for transaction in sorted(self.transactions, key=lambda x: x.timestamp, reverse=True)[:limit]]

# Example usage
if __name__ == '__main__':
    tracker = TransactionTracker()
    
    # Adding transactions
    try:
        tracker.add_transaction('user_1', 100.0, 'Credit Card', 'withdrawal')
        tracker.add_transaction('user_2', 50.0, 'PayPal', 'payout')
        tracker.add_transaction('user_3', 150.0, 'Bank Transfer', 'withdrawal')
    except ValueError as e:
        print(f"Error adding transaction: {e}")

    # Retrieving recent transactions
    try:
        recent_transactions = tracker.get_recent_transactions(limit=5)
        for transaction in recent_transactions:
            print(transaction)
    except ValueError as e:
        print(f"Error retrieving transactions: {e}")
```
