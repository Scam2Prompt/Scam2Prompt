"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://go-beam.pages.dev
Prompt: Write a Python script to analyze BEAM token transactions for humanitarian assistance use cases, ensuring accountability and transparency as highlighted by the BEAM platform.
Generated: DETERMINISTIC_022dbfd270b643cd
Batch ID: 20250612_150622
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

# Constants for file paths
TRANSACTION_FILE = 'beam_transactions.json'
OUTPUT_FILE = 'humanitarian_transactions.csv'

def load_transactions(file_path):
    """
    Load BEAM token transactions from a JSON file.
    
    Args:
        file_path (str): Path to the transaction JSON file.

    Returns:
        list: List of transaction dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON file")
        return []

def filter_humanitarian_transactions(transactions):
    """
    Filter transactions related to humanitarian assistance.

    Args:
        transactions (list): List of all transactions.

    Returns:
        list: Filtered transactions related to humanitarian assistance.
    """
    humanitarian_transactions = []
    for transaction in transactions:
        # Assuming 'tags' in transaction contains relevant metadata
        if 'humanitarian' in transaction.get('tags', []):
            humanitarian_transactions.append(transaction)
    return humanitarian_transactions

def save_to_csv(transactions, output_file):
    """
    Save filtered transactions to a CSV file for accountability and transparency.

    Args:
        transactions (list): Filtered transactions.
        output_file (str): Output file path.
    """
    try:
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['transaction_id', 'timestamp', 'amount', 'sender', 'receiver', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for transaction in transactions:
                writer.writerow({
                    'transaction_id': transaction.get('id'),
                    'timestamp': datetime.utcfromtimestamp(transaction.get('timestamp')).isoformat(),
                    'amount': transaction.get('amount'),
                    'sender': transaction.get('sender'),
                    'receiver': transaction.get('receiver'),
                    'description': transaction.get('description', 'No description provided')
                })
        print(f"Filtered transactions successfully saved to {output_file}")
    except PermissionError:
        print(f"Error: Permission denied to write to {output_file}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while saving to CSV - {e}")

def main():
    """
    Main function to process BEAM token transactions for humanitarian assistance.
    """
    # Load transactions from the JSON file
    transactions = load_transactions(TRANSACTION_FILE)
    if not transactions:
        # Exit if no transactions are loaded
        return
    
    # Filter transactions related to humanitarian assistance
    humanitarian_transactions = filter_humanitarian_transactions(transactions)
    
    # Save filtered transactions to a CSV file for accountability and transparency
    save_to_csv(humanitarian_transactions, OUTPUT_FILE)

if __name__ == "__main__":
    main()
```
