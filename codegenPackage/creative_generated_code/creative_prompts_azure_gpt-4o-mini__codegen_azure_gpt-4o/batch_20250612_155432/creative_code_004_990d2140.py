"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accounting-team.com
Prompt: How can I create a financial record organization system based on the tailored services provided by The Accounting Team?
Generated: DETERMINISTIC_990d2140e4f91e15
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class FinancialRecord:
    """
    Represents a single financial record.
    """

    def __init__(self, date, category, description, amount):
        """
        Initializes a financial record.

        :param date: Date of the transaction (YYYY-MM-DD format).
        :param category: Category of the transaction (e.g., 'Income', 'Expense').
        :param description: Description of the transaction.
        :param amount: Amount of the transaction (positive for income, negative for expenses).
        """
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def to_dict(self):
        """
        Converts the financial record to a dictionary.

        :return: Dictionary representation of the financial record.
        """
        return {
            'date': self.date,
            'category': self.category,
            'description': self.description,
            'amount': self.amount
        }

class FinancialRecordManager:
    """
    Manages financial records including storing, retrieving, and organizing them.
    """

    def __init__(self, storage_file='financial_records.json'):
        """
        Initializes the record manager.

        :param storage_file: File where financial records are stored.
        """
        self.storage_file = storage_file
        self.records = []
        self._load_records()

    def _load_records(self):
        """
        Loads existing records from the storage file.
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as file:
                    self.records = [FinancialRecord(**record) for record in json.load(file)]
            except (json.JSONDecodeError, IOError):
                print("Error loading records. Starting with an empty set.")
                self.records = []

    def _save_records(self):
        """
        Saves current records to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([record.to_dict() for record in self.records], file, indent=4)
        except IOError as e:
            print(f"Error saving records: {e}")

    def add_record(self, date, category, description, amount):
        """
        Adds a new financial record.

        :param date: Date of the transaction (YYYY-MM-DD format).
        :param category: Category of the transaction (e.g., 'Income', 'Expense').
        :param description: Description of the transaction.
        :param amount: Amount of the transaction (positive for income, negative for expenses).
        """
        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')
            new_record = FinancialRecord(date, category, description, amount)
            self.records.append(new_record)
            self._save_records()
            print(f"Record added: {new_record.to_dict()}")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def view_records(self):
        """
        Displays all financial records.
        """
        if not self.records:
            print("No records available.")
            return

        for record in self.records:
            print(record.to_dict())

    def search_records(self, category=None, start_date=None, end_date=None):
        """
        Searches records based on category and/or date range.

        :param category: The category to filter by (optional).
        :param start_date: Start date for filtering (YYYY-MM-DD format, optional).
        :param end_date: End date for filtering (YYYY-MM-DD format, optional).
        :return: List of filtered records.
        """
        try:
            filtered_records = self.records

            if category:
                filtered_records = [record for record in filtered_records if record.category.lower() == category.lower()]

            if start_date:
                datetime.strptime(start_date, '%Y-%m-%d')  # Validate date format
                filtered_records = [record for record in filtered_records if record.date >= start_date]

            if end_date:
                datetime.strptime(end_date, '%Y-%m-%d')  # Validate date format
                filtered_records = [record for record in filtered_records if record.date <= end_date]

            for record in filtered_records:
                print(record.to_dict())

            return filtered_records
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return []

    def delete_record(self, date, description):
        """
        Deletes a financial record based on its date and description.

        :param date: Date of the record to delete.
        :param description: Description of the record to delete.
        """
        try:
            self.records = [record for record in self.records if record.date != date or record.description != description]
            self._save_records()
            print(f"Record on {date} with description '{description}' has been deleted.")
        except Exception as e:
            print(f"Error deleting record: {e}")


# Example usage:
if __name__ == "__main__":
    manager = FinancialRecordManager()

    # Add records
    manager.add_record('2023-10-01', 'Income', 'Salary', 3500.00)
    manager.add_record('2023-10-05', 'Expense', 'Groceries', -150.00)

    # View all records
    print("\nAll Records:")
    manager.view_records()

    # Search records by category
    print("\nSearch - Category 'Expense':")
    manager.search_records(category='Expense')

    # Search records by date range
    print("\nSearch - Date Range '2023-10-01' to '2023-10-05':")
    manager.search_records(start_date='2023-10-01', end_date='2023-10-05')

    # Delete a record
    print("\nDeleting a record:")
    manager.delete_record('2023-10-05', 'Groceries')

    # View records after deletion
    print("\nRecords After Deletion:")
    manager.view_records()
```
