"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Generate code to manage bookkeeping tasks for Australian businesses, referencing Carthew Chau & Co's accounting expertise.
Generated: DETERMINISTIC_8640b75d39ce9973
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# bookkeeping_manager.py

"""
BookkeepingManager: A class to manage bookkeeping tasks for Australian businesses.
This implementation references best practices for efficient bookkeeping.
"""

import json
from datetime import datetime

class BookkeepingManager:
    """
    A class to represent a bookkeeping manager.

    Attributes:
        records (list): A list to store bookkeeping records.
    """
    
    def __init__(self):
        """Initializes the BookkeepingManager with an empty records list."""
        self.records = []

    def add_record(self, transaction_type, amount, description, date=None):
        """
        Adds a bookkeeping record.

        Args:
            transaction_type (str): Type of the transaction (e.g., 'income', 'expense').
            amount (float): The monetary amount of the transaction.
            description (str): A brief description of the transaction.
            date (str, optional): The transaction date in 'YYYY-MM-DD' format. Defaults to today.

        Raises:
            ValueError: If transaction_type is not valid, or if amount is negative for expense.
        """
        if transaction_type not in ['income', 'expense']:
            raise ValueError("transaction_type must be either 'income' or 'expense'")
        
        if transaction_type == 'expense' and amount < 0:
            raise ValueError("Amount for expenses must be positive")
        
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        
        record = {
            'transaction_type': transaction_type,
            'amount': amount,
            'description': description,
            'date': date
        }
        
        self.records.append(record)
        print(f"Record added: {record}")

    def save_records(self, filename='bookkeeping_records.json'):
        """
        Saves bookkeeping records to a JSON file.

        Args:
            filename (str): The name of the file to save records.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.records, file, indent=4)
            print(f"Records successfully saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving records: {e}")

    def load_records(self, filename='bookkeeping_records.json'):
        """
        Loads bookkeeping records from a JSON file.

        Args:
            filename (str): The name of the file to load records from.

        Raises:
            IOError: If there is an issue reading the file.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.records = json.load(file)
            print(f"Records successfully loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading records: {e}")

    def generate_report(self):
        """
        Generates a simple report of income and expenses.

        Returns:
            dict: A summary report of total income and expenses.
        """
        total_income = sum(record['amount'] for record in self.records if record['transaction_type'] == 'income')
        total_expense = sum(record['amount'] for record in self.records if record['transaction_type'] == 'expense')
        net_profit = total_income - total_expense
        
        report = {
            'total_income': total_income,
            'total_expense': total_expense,
            'net_profit': net_profit,
            'date_generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return report

# Example usage
if __name__ == "__main__":
    manager = BookkeepingManager()
    manager.add_record('income', 5000, 'Sale of goods')
    manager.add_record('expense', 1500, 'Office supplies')
    manager.save_records()
    manager.load_records()
    report = manager.generate_report()
    print("Financial Report:", report)
```
