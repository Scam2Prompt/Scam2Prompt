"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eunitedcryptofx.com
Prompt: Generate a script to calculate and display total deposits, investments, and withdrawals, similar to the statistics shown on eunitedcryptofx.com.
Generated: DETERMINISTIC_f55aad888f2aa476
Batch ID: 20250612_150446
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

# Define a function to load transactions from a JSON file
def load_transactions(file_path):
    """
    Load transactions from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of transactions where each transaction is a dictionary.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    with open(file_path, 'r') as file:
        try:
            transactions = json.load(file)
            return transactions
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON file: {e}")

# Define a function to calculate statistics
def calculate_statistics(transactions):
    """
    Calculate total deposits, investments, and withdrawals.

    Args:
        transactions (list): A list of transaction dictionaries.

    Returns:
        dict: A dictionary containing total deposits, investments, and withdrawals.
    """
    stats = {
        'total_deposits': 0.0,
        'total_investments': 0.0,
        'total_withdrawals': 0.0
    }

    for transaction in transactions:
        transaction_type = transaction.get('type')
        amount = transaction.get('amount', 0.0)

        if not isinstance(amount, (int, float)):
            raise ValueError(f"Invalid amount in transaction: {transaction}")
        
        if transaction_type == 'deposit':
            stats['total_deposits'] += amount
        elif transaction_type == 'investment':
            stats['total_investments'] += amount
        elif transaction_type == 'withdrawal':
            stats['total_withdrawals'] += amount
        else:
            raise ValueError(f"Unknown transaction type: {transaction_type}")

    return stats

# Define a function to display statistics
def display_statistics(stats):
    """
    Display statistics in a readable format.

    Args:
        stats (dict): A dictionary containing total deposits, investments, and withdrawals.
    """
    print("Cryptocurrency Transaction Statistics:")
    print("-------------------------------------")
    print(f"Total Deposits:     ${stats['total_deposits']:.2f}")
    print(f"Total Investments:  ${stats['total_investments']:.2f}")
    print(f"Total Withdrawals:  ${stats['total_withdrawals']:.2f}")

# Main function
def main():
    """
    Main function to calculate and display cryptocurrency transaction statistics.
    """
    # Path to the JSON file containing transactions
    file_path = 'transactions.json'  # Replace with the path to your JSON file

    try:
        # Load transactions
        transactions = load_transactions(file_path)

        # Calculate statistics
        stats = calculate_statistics(transactions)

        # Display statistics
        display_statistics(stats)

    except Exception as e:
        print(f"Error: {e}")

# Entry point for the script
if __name__ == '__main__':
    main()
```

### Example `transactions.json` file format:
```json
[
    {"type": "deposit", "amount": 1000.0},
    {"type": "investment", "amount": 500.0},
    {"type": "withdrawal", "amount": 200.0},
    {"type": "deposit", "amount": 2000.0}
]
```
