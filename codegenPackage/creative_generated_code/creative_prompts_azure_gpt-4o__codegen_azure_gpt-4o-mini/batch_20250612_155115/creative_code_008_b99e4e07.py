"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fund-x.link
Prompt: Generate a script to manage and track investment transactions 24/7, as described on FUND-X LTD's website, including weekend trading support.
Generated: DETERMINISTIC_b99e4e07183ae488
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import logging

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class InvestmentTransaction:
    """Class to represent an investment transaction."""
    
    def __init__(self, transaction_id, amount, transaction_type, timestamp=None):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp or datetime.datetime.now()

    def to_dict(self):
        """Converts the transaction to a dictionary for easy JSON serialization."""
        return {
            'transaction_id': self.transaction_id,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'timestamp': self.timestamp.isoformat()
        }

class TransactionManager:
    """Class to manage and track investment transactions."""
    
    def __init__(self, storage_file='transactions.json'):
        self.storage_file = storage_file
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        """Loads transactions from a JSON file."""
        try:
            with open(self.storage_file, 'r') as file:
                self.transactions = json.load(file)
                logger.info("Transactions loaded successfully.")
        except FileNotFoundError:
            logger.warning("Transaction file not found. Starting with an empty transaction list.")
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")
            self.transactions = []

    def save_transactions(self):
        """Saves transactions to a JSON file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.transactions, file, indent=4)
                logger.info("Transactions saved successfully.")
        except Exception as e:
            logger.error(f"Error saving transactions: {e}")

    def add_transaction(self, amount, transaction_type):
        """Adds a new transaction to the list."""
        transaction_id = len(self.transactions) + 1
        transaction = InvestmentTransaction(
            transaction_id=transaction_id,
            amount=amount,
            transaction_type=transaction_type
        )
        self.transactions.append(transaction.to_dict())
        self.save_transactions()

    def get_transactions(self):
        """Returns a list of all transactions."""
        return self.transactions

def main():
    """Main function to run the transaction manager."""
    manager = TransactionManager()

    while True:
        print("\nInvestment Transaction Manager")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter transaction amount: "))
                transaction_type = input("Enter transaction type (buy/sell): ").strip().lower()
                if transaction_type not in ['buy', 'sell']:
                    raise ValueError("Transaction type must be 'buy' or 'sell'.")
                manager.add_transaction(amount, transaction_type)
                print("Transaction added successfully.")
            except ValueError as e:
                logger.error(f"Invalid input: {e}")
                print(f"Error: {e}")
        elif choice == '2':
            transactions = manager.get_transactions()
            print("\nTransactions:")
            for transaction in transactions:
                print(transaction)
        elif choice == '3':
            logger.info("Exiting the transaction manager.")
            break
        else:
            logger.warning("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
