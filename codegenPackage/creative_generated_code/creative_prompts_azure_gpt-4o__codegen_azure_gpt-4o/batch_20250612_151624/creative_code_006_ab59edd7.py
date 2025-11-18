"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.tax
Prompt: Create a function to export cryptocurrency transactions in a format suitable for tax filing, inspired by the capabilities of Sui.tax.
Generated: DETERMINISTIC_ab59edd7471b896d
Batch ID: 20250612_151624
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

def export_crypto_transactions(transactions, file_path):
    """
    Exports cryptocurrency transactions to a CSV file suitable for tax filing.

    Args:
        transactions (list of dict): A list of transaction dictionaries.
            Each dictionary should have the following keys:
            - date (str): ISO 8601 date string (e.g., '2023-01-01').
            - type (str): Type of transaction (e.g., 'buy', 'sell', 'transfer').
            - asset (str): Name of the cryptocurrency asset (e.g., 'BTC', 'ETH').
            - quantity (float): Quantity of the asset involved.
            - price (float): Price per unit of the asset (in USD or fiat currency).
            - fee (float): Transaction fee (in USD or fiat currency).
        file_path (str): Path to the output CSV file.

    Returns:
        None

    Raises:
        ValueError: If any transaction dictionary lacks required keys or has invalid data.
    """
    # Define the header for the CSV file
    csv_header = ['Date', 'Type', 'Asset', 'Quantity', 'Price Per Unit', 'Fee', 'Total Value']

    try:
        # Validate transactions format
        for transaction in transactions:
            required_keys = {'date', 'type', 'asset', 'quantity', 'price', 'fee'}
            if not required_keys.issubset(transaction.keys()):
                raise ValueError(f"Transaction {transaction} is missing required keys.")
            if not isinstance(transaction['date'], str) or not isinstance(transaction['type'], str) or not isinstance(transaction['asset'], str):
                raise ValueError(f"Transaction {transaction} has invalid string data.")
            if not isinstance(transaction['quantity'], (int, float)) or not isinstance(transaction['price'], (int, float)) or not isinstance(transaction['fee'], (int, float)):
                raise ValueError(f"Transaction {transaction} has invalid numeric data.")

        # Write transactions to the CSV file
        with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_header)  # Write the header row

            for transaction in transactions:
                # Calculate the total value (quantity * price per unit)
                total_value = transaction['quantity'] * transaction['price']

                # Write the transaction data
                writer.writerow([
                    transaction['date'],
                    transaction['type'],
                    transaction['asset'],
                    transaction['quantity'],
                    transaction['price'],
                    transaction['fee'],
                    total_value
                ])

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while exporting transactions: {e}")
        raise

# Example usage
if __name__ == "__main__":
    sample_transactions = [
        {
            'date': '2023-01-01',
            'type': 'buy',
            'asset': 'BTC',
            'quantity': 0.5,
            'price': 30000.0,
            'fee': 50.0
        },
        {
            'date': '2023-02-01',
            'type': 'sell',
            'asset': 'ETH',
            'quantity': 2.0,
            'price': 2000.0,
            'fee': 20.0
        },
    ]

    output_file_path = "crypto_transactions.csv"
    export_crypto_transactions(sample_transactions, output_file_path)
    print(f"Transactions exported successfully to {output_file_path}")
```
