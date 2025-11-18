"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coniproasset.com
Prompt: Create a Python program to generate a report of weekly transactions and active accounts for a cryptocurrency investment platform, inspired by the statistics shared on the Coni Pro Asset website.
Generated: DETERMINISTIC_10a0fd4806151a42
Batch ID: 20250612_154542
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
import os

# Define a class to represent a transaction
class Transaction:
    def __init__(self, account_id, transaction_type, amount, timestamp):
        self.account_id = account_id
        self.transaction_type = transaction_type  # "deposit" or "withdrawal"
        self.amount = amount
        self.timestamp = timestamp

# Define a function to load transactions from a CSV file
def load_transactions(file_path):
    """
    Load transactions from a given CSV file.
    Assumes the CSV file has the following columns:
    account_id,transaction_type,amount,timestamp
    
    :param file_path: Path to the CSV file
    :return: List of Transaction objects
    """
    transactions = []
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(Transaction(
                    account_id=row['account_id'],
                    transaction_type=row['transaction_type'],
                    amount=float(row['amount']),
                    timestamp=datetime.datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
                ))
    except Exception as e:
        raise ValueError(f"Error reading transactions: {e}")
    
    return transactions

# Define a function to generate the weekly report
def generate_weekly_report(transactions):
    """
    Generate a report summarizing transactions and active accounts from the past week.
    
    :param transactions: List of Transaction objects
    :return: A dictionary containing the report data
    """
    report = {
        'total_deposits': 0,
        'total_withdrawals': 0,
        'total_transaction_volume': 0,
        'active_accounts': set()
    }
    
    one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    
    for transaction in transactions:
        if transaction.timestamp >= one_week_ago:
            report['total_transaction_volume'] += transaction.amount
            
            if transaction.transaction_type == 'deposit':
                report['total_deposits'] += transaction.amount
            elif transaction.transaction_type == 'withdrawal':
                report['total_withdrawals'] += transaction.amount
            
            report['active_accounts'].add(transaction.account_id)
    
    report['active_accounts'] = len(report['active_accounts'])  # Count of active accounts
    return report

# Define a function to save the report to a file
def save_report(report, file_path):
    """
    Save the report to a file in CSV format.
    
    :param report: Dictionary containing the report data
    :param file_path: Path to the output CSV file
    """
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Metric', 'Value'])
            writer.writerow(['Total Deposits', report['total_deposits']])
            writer.writerow(['Total Withdrawals', report['total_withdrawals']])
            writer.writerow(['Total Transaction Volume', report['total_transaction_volume']])
            writer.writerow(['Active Accounts', report['active_accounts']])
    except Exception as e:
        raise ValueError(f"Error saving report: {e}")

# Main function
def main():
    """
    Main function to execute the program.
    Loads transactions, generates the report, and saves the report to a file.
    """
    input_file = 'transactions.csv'
    output_file = 'weekly_report.csv'
    
    try:
        # Load transactions
        transactions = load_transactions(input_file)
        
        # Generate weekly report
        report = generate_weekly_report(transactions)
        
        # Save the report
        save_report(report, output_file)
        
        print(f"Weekly report saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()
```
