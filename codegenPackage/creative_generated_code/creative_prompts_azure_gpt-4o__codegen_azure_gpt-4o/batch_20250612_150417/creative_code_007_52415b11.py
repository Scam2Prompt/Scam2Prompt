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
from datetime import datetime
from typing import List, Dict


class Transaction:
    """
    A class representing a transaction (withdrawal or payout).
    """
    def __init__(self, user_id: int, payment_method: str, amount: float, transaction_type: str):
        """
        Initialize a Transaction object.
        
        :param user_id: Unique identifier for the user
        :param payment_method: Payment method used (e.g., 'PayPal', 'Bank Transfer')
        :param amount: Amount of the transaction
        :param transaction_type: Type of transaction ('withdrawal' or 'payout')
        """
        self.user_id = user_id
        self.payment_method = payment_method
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def to_dict(self) -> Dict:
        """
        Convert the transaction to a dictionary format for easy display.
        
        :return: Dictionary representation of the transaction
        """
        return {
            "user_id": self.user_id,
            "payment_method": self.payment_method,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "timestamp": self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }


class TransactionTracker:
    """
    A class to track recent withdrawals and payouts.
    """
    def __init__(self, max_transactions: int = 100):
        """
        Initialize a TransactionTracker object.
        
        :param max_transactions: Maximum number of recent transactions to keep track of
        """
        self.max_transactions = max_transactions
        self.transactions: List[Transaction] = []

    def add_transaction(self, user_id: int, payment_method: str, amount: float, transaction_type: str):
        """
        Add a new transaction to the tracker.
        
        :param user_id: Unique identifier for the user
        :param payment_method: Payment method used (e.g., 'PayPal', 'Bank Transfer')
        :param amount: Amount of the transaction
        :param transaction_type: Type of transaction ('withdrawal' or 'payout')
        """
        if transaction_type not in ['withdrawal', 'payout']:
            raise ValueError("Invalid transaction type. Must be 'withdrawal' or 'payout'.")
        
        # Create and add the new transaction
        transaction = Transaction(user_id, payment_method, amount, transaction_type)
        self.transactions.append(transaction)
        
        # Remove the oldest transaction if we exceed the maximum count
        if len(self.transactions) > self.max_transactions:
            self.transactions.pop(0)

    def get_recent_transactions(self) -> List[Dict]:
        """
        Get a list of recent transactions in dictionary format.
        
        :return: List of recent transactions
        """
        return [transaction.to_dict() for transaction in self.transactions]


# Example usage:
if __name__ == "__main__":
    tracker = TransactionTracker(max_transactions=10)
    
    # Adding some sample transactions
    tracker.add_transaction(user_id=1, payment_method="PayPal", amount=100.0, transaction_type="withdrawal")
    tracker.add_transaction(user_id=2, payment_method="Bank Transfer", amount=200.0, transaction_type="payout")
    tracker.add_transaction(user_id=3, payment_method="Payoneer", amount=150.0, transaction_type="withdrawal")
    
    # Retrieve and display recent transactions
    recent_transactions = tracker.get_recent_transactions()
    for transaction in recent_transactions:
        print(transaction)
```
