"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Write a Python function that can automate the bookkeeping process for small businesses, incorporating best practices mentioned by Lund & Kieck.
Generated: DETERMINISTIC_51b9c606043963c2
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime
from typing import List, Dict

class BookkeepingError(Exception):
    """Custom exception for bookkeeping errors."""
    pass

class Bookkeeper:
    def __init__(self, filename: str):
        """
        Initialize the Bookkeeper with a file to store transactions.
        
        :param filename: Path to the CSV file that stores transaction records.
        """
        self.filename = filename

    def record_transaction(self, date: str, description: str, amount: float, transaction_type: str) -> None:
        """
        Record a transaction in the bookkeeping system.

        :param date: Date of the transaction in 'YYYY-MM-DD' format.
        :param description: Description of the transaction.
        :param amount: Amount of the transaction.
        :param transaction_type: Type of transaction ('income' or 'expense').
        :raises BookkeepingError: If the transaction type is invalid or if writing to the file fails.
        """
        if transaction_type not in ['income', 'expense']:
            raise BookkeepingError("Transaction type must be 'income' or 'expense'.")

        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')
            
            # Prepare transaction data
            transaction = {
                'date': date,
                'description': description,
                'amount': amount,
                'type': transaction_type
            }

            # Write transaction to CSV file
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=transaction.keys())
                if file.tell() == 0:  # File is empty, write header
                    writer.writeheader()
                writer.writerow(transaction)

        except ValueError as e:
            raise BookkeepingError(f"Invalid date format: {e}")
        except IOError as e:
            raise BookkeepingError(f"Failed to write to file: {e}")

    def get_summary(self) -> Dict[str, float]:
        """
        Get a summary of income and expenses.

        :return: A dictionary with total income and total expenses.
        :raises BookkeepingError: If reading from the file fails.
        """
        income_total = 0.0
        expenses_total = 0.0
        
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    amount = float(row['amount'])
                    if row['type'] == 'income':
                        income_total += amount
                    elif row['type'] == 'expense':
                        expenses_total += amount

        except IOError as e:
            raise BookkeepingError(f"Failed to read from file: {e}")
        
        return {
            'total_income': income_total,
            'total_expenses': expenses_total,
            'net_profit': income_total - expenses_total
        }
```
