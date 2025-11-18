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

Certainly! Below is a Python script that manages and tracks investment transactions, with an emphasis on 24/7 functionality, including weekend trading support.

```python
import datetime
import logging
import json
import os

# Set up logging for tracking purposes
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("investment_transactions.log"),
        logging.StreamHandler()
    ]
)

# Define file to store transaction records
TRANSACTION_FILE = "transactions.json"

# Ensure the transactions file exists
if not os.path.exists(TRANSACTION_FILE):
    with open(TRANSACTION_FILE, "w") as file:
        json.dump([], file)

class InvestmentTransactionManager:
    """
    A class to manage and track investment transactions.
    Supports 24/7 operations including weekends.
    """

    def __init__(self):
        """
        Initialize the transaction manager.
        """
        self.transactions = self.load_transactions()

    def load_transactions(self):
        """
        Load existing transactions from the file.
        :return: List of transactions.
        """
        try:
            with open(TRANSACTION_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error loading transactions: {e}")
            return []

    def save_transactions(self):
        """
        Save transactions to the file.
        """
        try:
            with open(TRANSACTION_FILE, "w") as file:
                json.dump(self.transactions, file, indent=4)
            logging.info("Transactions saved successfully.")
        except Exception as e:
            logging.error(f"Error saving transactions: {e}")

    def add_transaction(self, transaction_id, amount, transaction_type, description=""):
        """
        Add a new investment transaction.
        :param transaction_id: Unique transaction ID.
        :param amount: Transaction amount.
        :param transaction_type: Type of transaction ('buy', 'sell', etc.).
        :param description: Optional transaction description.
        """
        try:
            transaction = {
                "transaction_id": transaction_id,
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "amount": amount,
                "type": transaction_type,
                "description": description
            }
            self.transactions.append(transaction)
            self.save_transactions()
            logging.info(f"Transaction added: {transaction}")
        except Exception as e:
            logging.error(f"Error adding transaction: {e}")

    def get_transactions(self, start_date=None, end_date=None):
        """
        Retrieve transactions optionally filtered by date range.
        :param start_date: Start date (ISO format string).
        :param end_date: End date (ISO format string).
        :return: List of filtered transactions.
        """
        try:
            filtered_transactions = self.transactions

            if start_date:
                start_date_obj = datetime.datetime.fromisoformat(start_date)
                filtered_transactions = [
                    t for t in filtered_transactions 
                    if datetime.datetime.fromisoformat(t["timestamp"]) >= start_date_obj
                ]
            
            if end_date:
                end_date_obj = datetime.datetime.fromisoformat(end_date)
                filtered_transactions = [
                    t for t in filtered_transactions 
                    if datetime.datetime.fromisoformat(t["timestamp"]) <= end_date_obj
                ]

            return filtered_transactions
        except Exception as e:
            logging.error(f"Error retrieving transactions: {e}")
            return []

    def delete_transaction(self, transaction_id):
        """
        Delete a transaction by its ID.
        :param transaction_id: Unique transaction ID.
        """
        try:
            self.transactions = [
                t for t in self.transactions if t["transaction_id"] != transaction_id
            ]
            self.save_transactions()
            logging.info(f"Transaction deleted: {transaction_id}")
        except Exception as e:
            logging.error(f"Error deleting transaction: {e}")

if __name__ == "__main__":
    # Create an instance of the transaction manager
    manager = InvestmentTransactionManager()

    # Example usage
    manager.add_transaction(
        transaction_id="TX12345",
        amount=5000.00,
        transaction_type="buy",
        description="Initial investment in FUND-X LTD"
    )

    # Retrieve all transactions
    all_transactions = manager.get_transactions()
    logging.info(f"All transactions: {all_transactions}")

    # Retrieve transactions within a specific date range
    filtered_transactions = manager.get_transactions(
        start_date="2023-01-01T00:00:00",
        end_date="2023-12-31T23:59:59"
    )
    logging.info(f"Filtered transactions: {filtered_transactions}")

    # Delete a transaction
    manager.delete_transaction("TX12345")
```

This script handles investment transactions by storing them in a JSON file, supports error handling, logs all operations, and maintains readability and flexibility for future production use.
