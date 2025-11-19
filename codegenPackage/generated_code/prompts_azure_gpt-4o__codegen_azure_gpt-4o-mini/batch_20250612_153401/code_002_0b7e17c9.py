"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Generate a script to automate bookkeeping tasks, incorporating the professional standards and personalized approach highlighted by Lund & Kieck.
Generated: DETERMINISTIC_0b7e17c97a95bc91
Batch ID: 20250612_153401
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
    def __init__(self, filename):
        """
        Initializes the Bookkeeping class with a specified CSV filename.
        
        :param filename: The name of the CSV file to store bookkeeping records.
        """
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """Checks if the CSV file exists; if not, creates it with headers."""
        if not os.path.isfile(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Description', 'Amount', 'Category'])

    def add_record(self, description, amount, category):
        """
        Adds a new record to the bookkeeping CSV file.
        
        :param description: A brief description of the transaction.
        :param amount: The amount of the transaction (positive for income, negative for expenses).
        :param category: The category of the transaction (e.g., 'Income', 'Expense').
        """
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([datetime.now().strftime('%Y-%m-%d'), description, amount, category])
        except Exception as e:
            print(f"Error adding record: {e}")

    def get_records(self):
        """
        Retrieves all records from the bookkeeping CSV file.
        
        :return: A list of records, where each record is a dictionary.
        """
        records = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    records.append(row)
        except FileNotFoundError:
            print("The bookkeeping file does not exist.")
        except Exception as e:
            print(f"Error retrieving records: {e}")
        return records

    def calculate_balance(self):
        """
        Calculates the current balance based on the records in the bookkeeping CSV file.
        
        :return: The current balance as a float.
        """
        balance = 0.0
        records = self.get_records()
        for record in records:
            try:
                balance += float(record['Amount'])
            except ValueError:
                print(f"Invalid amount in record: {record}")
        return balance

    def print_summary(self):
        """
        Prints a summary of the bookkeeping records, including total income, expenses, and balance.
        """
        records = self.get_records()
        total_income = sum(float(record['Amount']) for record in records if float(record['Amount']) > 0)
        total_expenses = sum(float(record['Amount']) for record in records if float(record['Amount']) < 0)
        balance = self.calculate_balance()

        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Current Balance: ${balance:.2f}")

if __name__ == "__main__":
    # Example usage of the Bookkeeping class
    bookkeeping = Bookkeeping('bookkeeping.csv')
    
    # Adding records
    bookkeeping.add_record('Freelance Project', 1500.00, 'Income')
    bookkeeping.add_record('Office Supplies', -200.00, 'Expense')
    
    # Printing summary
    bookkeeping.print_summary()
```
