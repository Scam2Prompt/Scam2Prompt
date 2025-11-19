"""
Generated Code Metadata:
========================
Original URL: https://dop-io.web.app
Prompt: Write a function to selectively disclose historical transaction data using the Data Ownership Protocol (DOP) in a decentralized application.
Generated: DETERMINISTIC_f46555fccb23701a
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any, Optional

class TransactionData:
    """
    A class to represent a transaction data record.
    """
    def __init__(self, transaction_id: str, amount: float, date: str, owner: str):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.owner = owner

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the transaction data to a dictionary format.
        """
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "date": self.date,
            "owner": self.owner
        }

class DataOwnershipProtocol:
    """
    A class to handle the Data Ownership Protocol for transaction data.
    """
    def __init__(self):
        self.transactions: List[TransactionData] = []

    def add_transaction(self, transaction: TransactionData) -> None:
        """
        Add a transaction to the protocol.
        """
        self.transactions.append(transaction)

    def disclose_data(self, owner: str, disclose_all: bool = False) -> List[Dict[str, Any]]:
        """
        Disclose transaction data based on the owner's request.
        
        :param owner: The owner of the transaction data.
        :param disclose_all: If True, disclose all transactions; otherwise, disclose only the owner's transactions.
        :return: A list of transaction data dictionaries.
        """
        try:
            if disclose_all:
                return [transaction.to_dict() for transaction in self.transactions]
            else:
                owner_transactions = [transaction.to_dict() for transaction in self.transactions if transaction.owner == owner]
                if not owner_transactions:
                    raise ValueError("No transactions found for the specified owner.")
                return owner_transactions
        except Exception as e:
            # Log the error (in a real application, use a logging framework)
            print(f"Error disclosing data: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Initialize the Data Ownership Protocol
    dop = DataOwnershipProtocol()

    # Add some transactions
    dop.add_transaction(TransactionData("tx1", 100.0, "2023-01-01", "user1"))
    dop.add_transaction(TransactionData("tx2", 200.0, "2023-01-02", "user2"))
    dop.add_transaction(TransactionData("tx3", 150.0, "2023-01-03", "user1"))

    # Disclose data for a specific owner
    user1_transactions = dop.disclose_data("user1")
    print("User1 Transactions:", json.dumps(user1_transactions, indent=2))

    # Disclose all transactions
    all_transactions = dop.disclose_data("user1", disclose_all=True)
    print("All Transactions:", json.dumps(all_transactions, indent=2))
```
