"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Write a Python function that can automate the bookkeeping process for small businesses, incorporating best practices mentioned by Lund & Kieck.
Generated: DETERMINISTIC_51b9c606043963c2
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import List, Dict

class BookkeepingError(Exception):
    """Custom exception for bookkeeping errors."""
    pass

class Bookkeeping:
    def __init__(self, filename: str):
        """
        Initialize the bookkeeping system with a specified CSV file.

        :param filename: The name of the CSV file to store transactions.
        """
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """Create the CSV file with headers if it does not exist."""
        if not os.path.isfile(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Description', 'Amount', 'Category'])

    def add_transaction(self, description: str, amount: float, category: str):
        """
        Add a transaction to the bookkeeping system.

        :param description: A brief description of the transaction.
        :param amount: The amount of the transaction (positive for income, negative for expenses).
        :param category: The category of the transaction (e.g., 'Sales', 'Utilities').
        :raises BookkeepingError: If the transaction is invalid.
        """
        if not isinstance(amount, (int, float)):
            raise BookkeepingError("Amount must be a number.")
        if amount == 0:
            raise BookkeepingError("Amount cannot be zero.")
        if not description or not category:
            raise BookkeepingError("Description and category cannot be empty.")

        transaction = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), description, amount, category]
        self.write_transaction(transaction)

    def write_transaction(self, transaction: List):
        """Write a transaction to the CSV file."""
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(transaction)

    def get_summary(self) -> Dict[str, float]:
        """
        Generate a summary of transactions by category.

        :return: A dictionary with categories as keys and total amounts as values.
        """
        summary = {}
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    category = row['Category']
                    amount = float(row['Amount'])
                    if category in summary:
                        summary[category] += amount
                    else:
                        summary[category] = amount
        except FileNotFoundError:
            raise BookkeepingError("Transaction file not found.")
        except Exception as e:
            raise BookkeepingError(f"An error occurred while reading the file: {e}")

        return summary

# Example usage:
if __name__ == "__main__":
    bookkeeping = Bookkeeping('transactions.csv')
    try:
        bookkeeping.add_transaction('Website Development', 1500.00, 'Sales')
        bookkeeping.add_transaction('Office Supplies', -200.00, 'Expenses')
        summary = bookkeeping.get_summary()
        print("Transaction Summary:", summary)
    except BookkeepingError as e:
        print(f"Error: {e}")
```
