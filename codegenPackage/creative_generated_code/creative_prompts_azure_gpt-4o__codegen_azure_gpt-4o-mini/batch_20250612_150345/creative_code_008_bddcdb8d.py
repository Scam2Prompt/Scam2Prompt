"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com.mainnetdappschain.top
Prompt: Write a script to log and display the latest deposit and withdrawal transactions, including details such as name, date, amount, and payment method.
Generated: DETERMINISTIC_bddcdb8dd1bde3e9
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

# Define a class to represent a transaction
class Transaction:
    def __init__(self, name: str, date: str, amount: float, method: str, transaction_type: str):
        self.name = name
        self.date = date
        self.amount = amount
        self.method = method
        self.transaction_type = transaction_type

    def to_dict(self):
        """Convert transaction details to a dictionary."""
        return {
            "name": self.name,
            "date": self.date,
            "amount": self.amount,
            "method": self.method,
            "transaction_type": self.transaction_type,
        }

# Class to manage transactions
class TransactionManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.transactions = self.load_transactions()

    def load_transactions(self):
        """Load transactions from a JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_transactions(self):
        """Save transactions to a JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, transaction: Transaction):
        """Add a new transaction and save it."""
        self.transactions.append(transaction.to_dict())
        self.save_transactions()

    def get_latest_transactions(self, count: int = 5):
        """Get the latest transactions sorted by date."""
        sorted_transactions = sorted(self.transactions, key=lambda x: x["date"], reverse=True)
        return sorted_transactions[:count]

# Function to display transactions
def display_transactions(transactions):
    """Display the transactions in a formatted manner."""
    print("\nLatest Transactions:")
    for transaction in transactions:
        print(f"{transaction['transaction_type']} - Name: {transaction['name']}, Date: {transaction['date']}, "
              f"Amount: ${transaction['amount']:.2f}, Method: {transaction['method']}")

# Main function to demonstrate transaction logging
def main():
    file_path = "transactions.json"
    manager = TransactionManager(file_path)

    # Sample transactions (for demonstration purposes)
    transactions = [
        Transaction("Alice", datetime.now().isoformat(), 100.0, "Credit Card", "Deposit"),
        Transaction("Bob", datetime.now().isoformat(), 50.0, "Bank Transfer", "Withdrawal"),
        Transaction("Charlie", datetime.now().isoformat(), 150.0, "PayPal", "Deposit"),
    ]

    # Log transactions
    for trans in transactions:
        manager.add_transaction(trans)

    # Display the latest transactions
    latest_transactions = manager.get_latest_transactions()
    display_transactions(latest_transactions)

if __name__ == "__main__":
    main()
```
