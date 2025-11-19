"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gass-fee.pages.dev
Prompt: How can I document gas fee transactions for tax purposes in 2024?
Generated: DETERMINISTIC_6667bad9a7f5e092
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import json
import os

# Define constants
TRANSACTIONS_FILE = "gas_fee_transactions_2024.csv"
BACKUP_FOLDER = "backups"

# Function to back up the existing CSV file before modifying
def backup_existing_file(file_path):
    if os.path.exists(file_path):
        # Ensure the backup folder exists
        os.makedirs(BACKUP_FOLDER, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file_path = os.path.join(BACKUP_FOLDER, f"backup_{timestamp}.csv")
        os.rename(file_path, backup_file_path)

# Function to create a new CSV file for documenting gas fee transactions
def create_csv_file(file_path):
    # Backup the existing file if it exists
    backup_existing_file(file_path)

    # Define the header for the CSV file
    header = ["Date", "Transaction_ID", "Gas_Fee", "Currency", "Notes"]
    try:
        # Create and write the header to the CSV file
        with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
    except Exception as e:
        print(f"Error creating CSV file: {e}")
        raise

# Function to log a new gas fee transaction
def log_transaction(file_path, transaction_data):
    try:
        # Validate that the transaction data contains required fields
        required_fields = ["Date", "Transaction_ID", "Gas_Fee", "Currency", "Notes"]
        if not all(field in transaction_data for field in required_fields):
            raise ValueError(f"Missing required fields in transaction data: {transaction_data}")

        # Append the transaction data to the CSV file
        with open(file_path, mode="a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                transaction_data["Date"],
                transaction_data["Transaction_ID"],
                transaction_data["Gas_Fee"],
                transaction_data["Currency"],
                transaction_data["Notes"]
            ])
    except Exception as e:
        print(f"Error logging transaction: {e}")
        raise

# Function to load transactions from the CSV file
def load_transactions(file_path):
    transactions = []
    try:
        # Read the CSV file and parse the transactions
        with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            transactions = list(reader)
    except FileNotFoundError:
        print("CSV file not found. Create the file first using create_csv_file().")
    except Exception as e:
        print(f"Error loading transactions: {e}")
        raise
    return transactions

# Main function demonstrating usage
def main():
    # Create the CSV file for documenting transactions
    create_csv_file(TRANSACTIONS_FILE)

    # Example gas fee transactions to log
    transaction_1 = {
        "Date": "2024-01-15",
        "Transaction_ID": "abc123",
        "Gas_Fee": 0.0005,
        "Currency": "ETH",
        "Notes": "Transfer to wallet"
    }
    
    transaction_2 = {
        "Date": "2024-02-10",
        "Transaction_ID": "def456",
        "Gas_Fee": 0.0003,
        "Currency": "ETH",
        "Notes": "Smart contract interaction"
    }
    
    # Log the transactions to the CSV file
    log_transaction(TRANSACTIONS_FILE, transaction_1)
    log_transaction(TRANSACTIONS_FILE, transaction_2)
    
    # Load and display the transactions for verification
    transactions = load_transactions(TRANSACTIONS_FILE)
    print("Logged Transactions:")
    print(json.dumps(transactions, indent=4))

if __name__ == "__main__":
    main()
```
