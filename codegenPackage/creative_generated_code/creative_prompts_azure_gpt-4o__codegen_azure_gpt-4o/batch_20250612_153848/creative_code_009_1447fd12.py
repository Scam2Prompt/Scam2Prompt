"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xenchain.io
Prompt: Provide code to implement Xenchain Protocol for tracking transaction history and analytics in an e-commerce platform.
Generated: DETERMINISTIC_1447fd12d8181e0f
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
from typing import List, Dict

class Transaction:
    """
    Represents a single transaction in the Xenchain Protocol.
    """
    def __init__(self, transaction_id: str, user_id: str, product_id: str, amount: float, timestamp: float = None):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.product_id = product_id
        self.amount = amount
        self.timestamp = timestamp if timestamp else time.time()

    def to_dict(self) -> Dict:
        """
        Converts the transaction object to a dictionary for JSON serialization.
        """
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "amount": self.amount,
            "timestamp": self.timestamp
        }


class XenchainProtocol:
    """
    Implements the Xenchain Protocol for tracking transaction history and analytics.
    """
    def __init__(self):
        self.transactions = []  # In-memory transaction log

    def add_transaction(self, transaction: Transaction):
        """
        Adds a transaction to the protocol.
        """
        if not isinstance(transaction, Transaction):
            raise TypeError("Invalid transaction object")
        self.transactions.append(transaction)

    def get_transaction_history(self, user_id: str = None) -> List[Dict]:
        """
        Retrieves transaction history. If user_id is provided, filters by user.
        """
        if user_id:
            return [txn.to_dict() for txn in self.transactions if txn.user_id == user_id]
        return [txn.to_dict() for txn in self.transactions]

    def compute_analytics(self) -> Dict:
        """
        Computes basic analytics like total sales, total transactions, and average transaction value.
        """
        if not self.transactions:
            return {"total_sales": 0, "total_transactions": 0, "average_transaction_value": 0}
        
        total_sales = sum(txn.amount for txn in self.transactions)
        total_transactions = len(self.transactions)
        average_transaction_value = total_sales / total_transactions if total_transactions > 0 else 0

        return {
            "total_sales": total_sales,
            "total_transactions": total_transactions,
            "average_transaction_value": average_transaction_value
        }

    def save_to_file(self, file_path: str):
        """
        Saves the transaction log to a file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([txn.to_dict() for txn in self.transactions], file, indent=4)
        except (IOError, OSError) as e:
            raise RuntimeError(f"Error saving to file: {str(e)}")

    def load_from_file(self, file_path: str):
        """
        Loads the transaction log from a file.
        """
        try:
            with open(file_path, 'r') as file:
                transactions = json.load(file)
                self.transactions = [
                    Transaction(
                        transaction_id=txn["transaction_id"],
                        user_id=txn["user_id"],
                        product_id=txn["product_id"],
                        amount=txn["amount"],
                        timestamp=txn["timestamp"]
                    ) for txn in transactions
                ]
        except (IOError, OSError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Error loading from file: {str(e)}")


# Example usage (not part of production code, for demonstration only):
if __name__ == "__main__":
    xenchain = XenchainProtocol()

    # Adding transactions
    xenchain.add_transaction(Transaction("txn001", "user001", "prod001", 100.0))
    xenchain.add_transaction(Transaction("txn002", "user002", "prod002", 200.0))
    xenchain.add_transaction(Transaction("txn003", "user001", "prod003", 150.0))

    # Retrieving history
    print("Transaction History for user001:")
    print(xenchain.get_transaction_history("user001"))

    # Computing analytics
    print("Analytics:")
    print(xenchain.compute_analytics())

    # Saving and loading transactions
    xenchain.save_to_file("transactions.json")
    xenchain.load_from_file("transactions.json")
```
