"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Generate a script to automate bookkeeping tasks, incorporating the professional standards and personalized approach highlighted by Lund & Kieck.
Generated: DETERMINISTIC_0b7e17c97a95bc91
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script to automate bookkeeping tasks, adhering to professional standards and best practices:

```python
import csv
import os
from datetime import datetime

# Define constants and configuration
BOOKKEEPING_FOLDER = "bookkeeping_records"
TRANSACTIONS_FILE = "transactions.csv"
SUMMARY_FILE = "summary.txt"
DATE_FORMAT = "%Y-%m-%d"

# Ensure the bookkeeping folder exists
if not os.path.exists(BOOKKEEPING_FOLDER):
    os.makedirs(BOOKKEEPING_FOLDER)

def log_transaction(transaction_date, description, amount, transaction_type):
    """
    Logs a transaction to the bookkeeping file.

    Args:
        transaction_date (str): Date of the transaction (YYYY-MM-DD).
        description (str): Description of the transaction.
        amount (float): Amount of the transaction.
        transaction_type (str): Type of the transaction ('income' or 'expense').
    """
    try:
        # Validate transaction_type
        if transaction_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'.")

        # Write transaction to the CSV file
        file_path = os.path.join(BOOKKEEPING_FOLDER, TRANSACTIONS_FILE)
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([transaction_date, description, amount, transaction_type])
        print("Transaction logged successfully.")
    except Exception as e:
        print(f"Error logging transaction: {e}")

def generate_summary():
    """
    Generates a summary of all transactions (total income, total expenses, net balance).

    Creates a summary file in the bookkeeping folder.
    """
    try:
        file_path = os.path.join(BOOKKEEPING_FOLDER, TRANSACTIONS_FILE)
        if not os.path.exists(file_path):
            print("No transactions found. Summary cannot be generated.")
            return

        total_income = 0
        total_expenses = 0

        # Read transactions and calculate totals
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                transaction_type = row[3]
                amount = float(row[2])
                if transaction_type == 'income':
                    total_income += amount
                elif transaction_type == 'expense':
                    total_expenses += amount

        # Generate net balance
        net_balance = total_income - total_expenses

        # Write summary to a text file
        summary_path = os.path.join(BOOKKEEPING_FOLDER, SUMMARY_FILE)
        with open(summary_path, mode='w', encoding='utf-8') as summary_file:
            summary_file.write("Bookkeeping Summary\n")
            summary_file.write("===================\n")
            summary_file.write(f"Total Income: ${total_income:.2f}\n")
            summary_file.write(f"Total Expenses: ${total_expenses:.2f}\n")
            summary_file.write(f"Net Balance: ${net_balance:.2f}\n")
        print("Summary generated successfully.")
    except Exception as e:
        print(f"Error generating summary: {e}")

def main():
    """
    Main function to demonstrate the bookkeeping automation script.
    """
    while True:
        print("\nBookkeeping Automation")
        print("=======================")
        print("1. Log Transaction")
        print("2. Generate Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                # Collect transaction details
                transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
                datetime.strptime(transaction_date, DATE_FORMAT)  # Validate date format
                description = input("Enter transaction description: ")
                amount = float(input("Enter transaction amount: "))
                transaction_type = input("Enter transaction type ('income' or 'expense'): ").lower()
                log_transaction(transaction_date, description, amount, transaction_type)
            except ValueError as ve:
                print(f"Invalid input: {ve}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '2':
            generate_summary()
        elif choice == '3':
            print("Exiting bookkeeping automation. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
