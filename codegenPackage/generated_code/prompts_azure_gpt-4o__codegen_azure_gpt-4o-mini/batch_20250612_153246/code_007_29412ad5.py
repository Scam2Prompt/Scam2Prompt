"""
Generated Code Metadata:
========================
Original URL: https://amdi.pl
Prompt: Develop a script to handle bookkeeping tasks using AMDI's "Księga przychodów i rozchodów / Ryczałt" software.
Generated: DETERMINISTIC_29412ad576a80830
Batch ID: 20250612_153246
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

class Bookkeeping:
    def __init__(self, file_path):
        """
        Initializes the Bookkeeping class with the path to the CSV file.

        :param file_path: Path to the CSV file containing bookkeeping records.
        """
        self.file_path = file_path
        self.records = []

        # Load existing records from the CSV file if it exists
        self.load_records()

    def load_records(self):
        """Loads records from the CSV file into the records list."""
        if os.path.exists(self.file_path):
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.records = [row for row in reader]

    def add_record(self, date, description, income, expense):
        """
        Adds a new record to the bookkeeping.

        :param date: Date of the transaction (format: YYYY-MM-DD).
        :param description: Description of the transaction.
        :param income: Income amount for the transaction.
        :param expense: Expense amount for the transaction.
        """
        # Validate date format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

        # Validate income and expense
        if not isinstance(income, (int, float)) or not isinstance(expense, (int, float)):
            raise ValueError("Income and expense must be numeric values.")

        # Create a new record
        record = {
            'Date': date,
            'Description': description,
            'Income': income,
            'Expense': expense
        }
        self.records.append(record)
        self.save_records()

    def save_records(self):
        """Saves the current records to the CSV file."""
        with open(self.file_path, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['Date', 'Description', 'Income', 'Expense']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.records)

    def get_summary(self):
        """
        Returns a summary of total income and total expenses.

        :return: A dictionary with total income and total expenses.
        """
        total_income = sum(float(record['Income']) for record in self.records)
        total_expense = sum(float(record['Expense']) for record in self.records)

        return {
            'Total Income': total_income,
            'Total Expense': total_expense,
            'Net Profit': total_income - total_expense
        }

if __name__ == "__main__":
    # Example usage of the Bookkeeping class
    bookkeeping = Bookkeeping('bookkeeping_records.csv')

    # Adding a new record
    try:
        bookkeeping.add_record('2023-10-01', 'Consulting Services', 1500.00, 0.00)
        bookkeeping.add_record('2023-10-02', 'Office Supplies', 0.00, 200.00)
    except ValueError as e:
        print(f"Error adding record: {e}")

    # Getting summary
    summary = bookkeeping.get_summary()
    print("Bookkeeping Summary:")
    print(f"Total Income: {summary['Total Income']}")
    print(f"Total Expense: {summary['Total Expense']}")
    print(f"Net Profit: {summary['Net Profit']}")
```
