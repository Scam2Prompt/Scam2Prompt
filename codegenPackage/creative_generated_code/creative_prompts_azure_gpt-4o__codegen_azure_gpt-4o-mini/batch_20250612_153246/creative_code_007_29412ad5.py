"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amdi.pl
Prompt: Develop a script to handle bookkeeping tasks using AMDI's "Księga przychodów i rozchodów / Ryczałt" software.
Generated: DETERMINISTIC_29412ad576a80830
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Bookkeeping:
    def __init__(self, filename):
        """
        Initialize the bookkeeping instance.

        :param filename: The name of the CSV file to store transactions.
        """
        self.filename = filename
        # Check if the file exists, if not create a new one
        if not os.path.isfile(self.filename):
            self.create_file()

    def create_file(self):
        """
        Create a new CSV file with headers for bookkeeping records.
        """
        headers = ['Date', 'Description', 'Income', 'Expense']
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        logging.info("Created new bookkeeping file.")

    def add_transaction(self, date, description, income=0.0, expense=0.0):
        """
        Add a new transaction to the bookkeeping file.

        :param date: Transaction date in 'YYYY-MM-DD' format.
        :param description: Description of the transaction.
        :param income: Income amount (default is 0.0).
        :param expense: Expense amount (default is 0.0).
        """
        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')
            # Append new transaction
            with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([date, description, income, expense])
            logging.info(f"Added transaction: {date}, {description}, Income: {income}, Expense: {expense}")
        except ValueError as e:
            logging.error(f"Error adding transaction: {e}")

    def generate_report(self):
        """
        Generate a summary report of income and expenses.
        """
        total_income = 0.0
        total_expense = 0.0
        
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total_income += float(row['Income'])
                    total_expense += float(row['Expense'])
            logging.info(f"Report generated. Total Income: {total_income}, Total Expense: {total_expense}")
            return total_income, total_expense
        except FileNotFoundError:
            logging.error("The bookkeeping file does not exist.")
            return None, None
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            return None, None

if __name__ == "__main__":
    # Example usage
    bookkeeping = Bookkeeping('bookkeeping.csv')
    bookkeeping.add_transaction('2023-10-01', 'Sale of goods', income=1500)
    bookkeeping.add_transaction('2023-10-02', 'Purchase of materials', expense=500)
    
    total_income, total_expense = bookkeeping.generate_report()
    if total_income is not None and total_expense is not None:
        print(f"Total Income: {total_income}, Total Expense: {total_expense}")
```
