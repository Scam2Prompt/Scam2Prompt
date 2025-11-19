"""
Generated Code Metadata:
========================
Original URL: https://apps-shibabudz.pages.dev
Prompt: "Develop a simple transaction history log system in Python that records and displays user transactions similar to the ones listed on Shibabudz."
Generated: DETERMINISTIC_ae42d1ba5d6c3cd1
Batch ID: 20250622_211048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class Transaction:
    """Represents a single transaction."""

    def __init__(self, user_id, transaction_type, amount, currency):
        """
        Initializes a Transaction object.

        Args:
            user_id (str): Unique identifier for the user.
            transaction_type (str): Type of transaction (e.g., "deposit", "withdrawal").
            amount (float): Transaction amount.
            currency (str): Currency used in the transaction.
        """
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.currency = currency
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Converts the transaction to a dictionary."""
        return {
            "user_id": self.user_id,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "currency": self.currency,
            "timestamp": self.timestamp,
        }


class TransactionLog:
    """Manages a log of user transactions."""

    def __init__(self, log_file="transaction_log.json"):
        """
        Initializes a TransactionLog object.

        Args:
            log_file (str): File path to store the transaction log.
        """
        self.log_file = log_file
        self.load_log()

    def load_log(self):
        """Loads the transaction log from the log file."""
        try:
            with open(self.log_file, "r") as file:
                self.log = json.load(file)
        except FileNotFoundError:
            self.log = []

    def save_log(self):
        """Saves the transaction log to the log file."""
        with open(self.log_file, "w") as file:
            json.dump(self.log, file, indent=4)

    def add_transaction(self, transaction):
        """
        Adds a transaction to the log.

        Args:
            transaction (Transaction): Transaction to add.
        """
        self.log.append(transaction.to_dict())
        self.save_log()

    def get_transactions(self, user_id=None):
        """
        Retrieves transactions from the log.

        Args:
            user_id (str): Optional user ID to filter transactions.

        Returns:
            list: List of transactions.
        """
        if user_id:
            return [t for t in self.log if t["user_id"] == user_id]
        return self.log


def main():
    log = TransactionLog()

    while True:
        print("\n1. Add transaction")
        print("2. Display transactions")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            transaction_type = input("Enter transaction type: ")
            amount = float(input("Enter transaction amount: "))
            currency = input("Enter currency: ")

            transaction = Transaction(user_id, transaction_type, amount, currency)
            log.add_transaction(transaction)
            print("Transaction added successfully!")
        elif choice == "2":
            user_id = input("Enter user ID (leave blank for all): ")
            if user_id:
                transactions = log.get_transactions(user_id)
            else:
                transactions = log.get_transactions()

            if transactions:
                for transaction in transactions:
                    print(f"User ID: {transaction['user_id']}")
                    print(f"Transaction Type: {transaction['transaction_type']}")
                    print(f"Amount: {transaction['amount']} {transaction['currency']}")
                    print(f"Timestamp: {transaction['timestamp']}")
                    print("-" * 30)
            else:
                print("No transactions found.")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
