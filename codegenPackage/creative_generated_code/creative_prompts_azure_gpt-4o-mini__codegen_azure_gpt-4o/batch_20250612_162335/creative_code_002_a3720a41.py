"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://transactionfinder.in
Prompt: Can you provide code examples for creating a transaction tracking tool based on the methods discussed on Transaction Finder?
Generated: DETERMINISTIC_a3720a41b45f5259
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Transaction Tracking Tool

This tool is designed to track and manage financial transactions.
It provides functionality to create, view, and search transactions.
"""

import json
from datetime import datetime


class Transaction:
    """
    Represents a single financial transaction.
    """

    def __init__(self, transaction_id, amount, transaction_type, description=None):
        """
        Initialize a Transaction object.
        
        :param transaction_id: Unique identifier for the transaction.
        :param amount: Amount of the transaction.
        :param transaction_type: Type of transaction ('credit' or 'debit').
        :param description: Optional description or note for the transaction.
        """
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.timestamp = datetime.now()  # Auto-generated timestamp

    def to_dict(self):
        """
        Converts the transaction object to a dictionary for storage or display.

        :return: Dictionary representation of the transaction.
        """
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "description": self.description,
            "timestamp": self.timestamp.isoformat(),
        }


class TransactionTracker:
    """
    Core class for managing transactions.
    """

    def __init__(self):
        """
        Initialize the transaction tracker with an empty transaction list.
        """
        self.transactions = []

    def add_transaction(self, transaction):
        """
        Add a new transaction to the tracker.

        :param transaction: Transaction object to be added.
        """
        if not isinstance(transaction, Transaction):
            raise ValueError("Invalid transaction object. Must be an instance of Transaction.")
        self.transactions.append(transaction)

    def list_transactions(self):
        """
        List all transactions stored in the tracker.

        :return: List of all transactions as dictionaries.
        """
        return [transaction.to_dict() for transaction in self.transactions]

    def find_transaction_by_id(self, transaction_id):
        """
        Find a transaction by its unique ID.

        :param transaction_id: The ID of the transaction to find.
        :return: Dictionary representation of the transaction (if found), or None.
        """
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction.to_dict()
        return None

    def save_to_file(self, file_path):
        """
        Save all transactions to a JSON file.

        :param file_path: Path to the file where transactions will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([transaction.to_dict() for transaction in self.transactions], file, indent=4)
        except Exception as e:
            print(f"Error saving transactions to file: {e}")

    def load_from_file(self, file_path):
        """
        Load transactions from a JSON file.

        :param file_path: Path to the file where transactions are stored.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.transactions = [
                    Transaction(
                        transaction_id=entry["transaction_id"],
                        amount=entry["amount"],
                        transaction_type=entry["transaction_type"],
                        description=entry.get("description")
                    )
                    for entry in data
                ]
        except FileNotFoundError:
            print("File not found. No transactions loaded.")
        except json.JSONDecodeError:
            print("Error decoding JSON. No transactions loaded.")
        except Exception as e:
            print(f"Error loading transactions from file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = TransactionTracker()

    # Adding transactions
    tracker.add_transaction(Transaction(transaction_id="T001", amount=100.5, transaction_type="credit", description="Salary"))
    tracker.add_transaction(Transaction(transaction_id="T002", amount=20.0, transaction_type="debit", description="Groceries"))

    # Listing all transactions
    print("All transactions:")
    print(tracker.list_transactions())

    # Finding a specific transaction
    print("Find transaction by ID (T001):")
    print(tracker.find_transaction_by_id("T001"))

    # Save transactions to file
    tracker.save_to_file("transactions.json")

    # Load transactions from file
    new_tracker = TransactionTracker()
    new_tracker.load_from_file("transactions.json")
    print("Loaded transactions:")
    print(new_tracker.list_transactions())
```
