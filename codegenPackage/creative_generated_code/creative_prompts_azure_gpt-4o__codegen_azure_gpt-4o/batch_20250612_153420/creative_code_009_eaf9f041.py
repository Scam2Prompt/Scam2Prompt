"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutinvvault.com
Prompt: Write a script to analyze daily transactions and active accounts data for an investment platform, referencing metrics from Sprout Inv. Vault.
Generated: DETERMINISTIC_eaf9f041b9af0514
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import csv
from datetime import datetime

# Function to read daily transactions data from a CSV file
def read_transactions(file_path):
    """
    Reads daily transactions data from a CSV file and returns it as a list of dictionaries.
    
    :param file_path: Path to the transactions CSV file.
    :return: List of transaction records as dictionaries.
    """
    try:
        transactions = []
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                transactions.append(row)
        return transactions
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading transactions file: {e}")
        return []

# Function to read active accounts data from a JSON file
def read_active_accounts(file_path):
    """
    Reads active accounts data from a JSON file and returns it as a list of dictionaries.
    
    :param file_path: Path to the active accounts JSON file.
    :return: List of active account records as dictionaries.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as json_file:
            active_accounts = json.load(json_file)
        return active_accounts
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON file at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading active accounts file: {e}")
        return []

# Function to analyze transactions and active accounts
def analyze_data(transactions, active_accounts):
    """
    Analyzes transactions and active accounts data and prints summary metrics.
    
    :param transactions: List of transaction records.
    :param active_accounts: List of active account records.
    """
    if not transactions:
        print("No transactions available for analysis.")
        return
    
    if not active_accounts:
        print("No active accounts available for analysis.")
        return

    # Metrics calculation
    total_transactions = len(transactions)
    total_active_accounts = len(active_accounts)
    total_transaction_amount = sum(float(txn['amount']) for txn in transactions if 'amount' in txn)
    average_transaction_amount = total_transaction_amount / total_transactions if total_transactions > 0 else 0

    # Print analysis summary
    print("=== Daily Transactions Analysis ===")
    print(f"Total Transactions: {total_transactions}")
    print(f"Total Transaction Amount: ${total_transaction_amount:.2f}")
    print(f"Average Transaction Amount: ${average_transaction_amount:.2f}")
    print("\n=== Active Accounts Analysis ===")
    print(f"Total Active Accounts: {total_active_accounts}")

# Main function to orchestrate the analysis workflow
def main():
    """
    Main function to orchestrate reading data, analyzing it, and providing metrics summary.
    """
    # File paths (update paths as appropriate for production)
    transactions_file_path = 'transactions.csv'  # Path to transactions CSV file
    active_accounts_file_path = 'active_accounts.json'  # Path to active accounts JSON file

    # Read data
    transactions = read_transactions(transactions_file_path)
    active_accounts = read_active_accounts(active_accounts_file_path)

    # Analyze data
    analyze_data(transactions, active_accounts)

# Entry point for the script
if __name__ == "__main__":
    # Print start message with a timestamp
    print(f"Analysis started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Execute the main function
    main()
    
    # Print end message with a timestamp
    print(f"Analysis completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
```
