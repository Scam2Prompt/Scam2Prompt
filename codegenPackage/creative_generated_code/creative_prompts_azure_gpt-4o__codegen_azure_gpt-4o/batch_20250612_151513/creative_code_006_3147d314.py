"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Write a Python script to reconcile bank statements and generate a general ledger report for small businesses, as part of the accounting services provided by Hispanic Services.
Generated: DETERMINISTIC_3147d3149000f297
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime

# Define constants for file paths
BANK_STATEMENT_FILE = "bank_statement.csv"
GENERAL_LEDGER_FILE = "general_ledger.csv"
RECONCILIATION_REPORT_FILE = "reconciliation_report.csv"

def read_csv(file_path):
    """
    Reads a CSV file and returns its contents as a list of dictionaries.
    Each dictionary represents a row, with keys as column headers.
    
    :param file_path: Path to the CSV file
    :return: List of dictionaries representing the CSV data
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except Exception as e:
        print(f"Error: Unable to read file {file_path}. Exception: {e}")
        return []

def write_csv(file_path, data, headers):
    """
    Writes a list of dictionaries into a CSV file.
    
    :param file_path: Path to the CSV file
    :param data: List of dictionaries representing the data
    :param headers: List of column headers for the CSV file
    """
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"File successfully written: {file_path}")
    except Exception as e:
        print(f"Error: Unable to write file {file_path}. Exception: {e}")

def reconcile(bank_statement, ledger):
    """
    Reconciles bank statement transactions against the general ledger.
    
    :param bank_statement: List of transactions from the bank statement
    :param ledger: List of transactions from the general ledger
    :return: List of discrepancies between the bank statement and ledger
    """
    discrepancies = []

    # Convert both datasets into sets for easier reconciliation
    bank_transactions = {(row['Date'], row['Description'], float(row['Amount'])) for row in bank_statement}
    ledger_transactions = {(row['Date'], row['Description'], float(row['Amount'])) for row in ledger}

    # Transactions in the bank statement but not in the ledger
    for transaction in bank_transactions - ledger_transactions:
        discrepancies.append({
            "Date": transaction[0],
            "Description": transaction[1],
            "Amount": transaction[2],
            "Issue": "Not in ledger"
        })

    # Transactions in the ledger but not in the bank statement
    for transaction in ledger_transactions - bank_transactions:
        discrepancies.append({
            "Date": transaction[0],
            "Description": transaction[1],
            "Amount": transaction[2],
            "Issue": "Not in bank statement"
        })

    return discrepancies

def generate_reconciliation_report(discrepancies):
    """
    Generates a reconciliation report and saves it to a file.
    
    :param discrepancies: List of discrepancies found during reconciliation
    """
    headers = ["Date", "Description", "Amount", "Issue"]
    write_csv(RECONCILIATION_REPORT_FILE, discrepancies, headers)

def main():
    """
    Main function to perform bank statement reconciliation and generate a report.
    """
    try:
        print("Reading bank statement...")
        bank_statement = read_csv(BANK_STATEMENT_FILE)

        print("Reading general ledger...")
        ledger = read_csv(GENERAL_LEDGER_FILE)

        if not bank_statement or not ledger:
            print("Error: Unable to proceed due to missing or invalid data.")
            return

        print("Reconciling bank statement with general ledger...")
        discrepancies = reconcile(bank_statement, ledger)

        if discrepancies:
            print(f"Discrepancies found: {len(discrepancies)}")
            generate_reconciliation_report(discrepancies)
        else:
            print("No discrepancies found. Everything is reconciled!")

    except Exception as e:
        print(f"Error: An unexpected problem occurred. Exception: {e}")

if __name__ == "__main__":
    main()
```
