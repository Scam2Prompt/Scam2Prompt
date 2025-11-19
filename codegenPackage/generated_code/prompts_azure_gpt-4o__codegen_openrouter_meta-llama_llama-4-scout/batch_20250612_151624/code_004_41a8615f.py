"""
Generated Code Metadata:
========================
Original URL: https://sui.tax
Prompt: Write a script to process exported cryptocurrency transaction data for tax calculations, ensuring compatibility with features like those on Sui.tax.
Generated: DETERMINISTIC_41a8615f8daede0c
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Cryptocurrency Transaction Processor for Tax Calculations

This script processes exported cryptocurrency transaction data for tax calculations.
It is designed to be compatible with features similar to those on Sui.tax.

Author: [Your Name]
Date: [Today's Date]
"""

import csv
import json
from datetime import datetime
from typing import List, Dict

class Transaction:
    def __init__(self, date: str, type: str, amount: float, price: float, fee: float = 0.0):
        """
        Initialize a Transaction object.

        Args:
        - date (str): Date of the transaction in YYYY-MM-DD format.
        - type (str): Type of the transaction (buy/sell).
        - amount (float): Amount of cryptocurrency transacted.
        - price (float): Price of the cryptocurrency at the time of transaction.
        - fee (float, optional): Transaction fee. Defaults to 0.0.
        """
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.type = type.lower()
        self.amount = amount
        self.price = price
        self.fee = fee

    def __repr__(self):
        return f"Transaction(date={self.date}, type={self.type}, amount={self.amount}, price={self.price}, fee={self.fee})"


def load_transactions_from_csv(file_path: str) -> List[Transaction]:
    """
    Load transactions from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - List[Transaction]: A list of Transaction objects.

    Raises:
    - FileNotFoundError: If the file does not exist.
    - csv.Error: If there is an error parsing the CSV file.
    """
    try:
        transactions = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = Transaction(
                    date=row['date'],
                    type=row['type'],
                    amount=float(row['amount']),
                    price=float(row['price']),
                    fee=float(row.get('fee', 0.0))
                )
                transactions.append(transaction)
        return transactions
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except csv.Error as e:
        print(f"Error: Failed to parse CSV file - {e}")
        return []


def load_transactions_from_json(file_path: str) -> List[Transaction]:
    """
    Load transactions from a JSON file.

    Args:
    - file_path (str): Path to the JSON file.

    Returns:
    - List[Transaction]: A list of Transaction objects.

    Raises:
    - FileNotFoundError: If the file does not exist.
    - json.JSONDecodeError: If there is an error parsing the JSON file.
    """
    try:
        transactions = []
        with open(file_path, 'r') as file:
            data = json.load(file)
            for transaction_data in data:
                transaction = Transaction(
                    date=transaction_data['date'],
                    type=transaction_data['type'],
                    amount=transaction_data['amount'],
                    price=transaction_data['price'],
                    fee=transaction_data.get('fee', 0.0)
                )
                transactions.append(transaction)
        return transactions
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file - {e}")
        return []


def calculate_gains(transactions: List[Transaction]) -> Dict[str, float]:
    """
    Calculate gains from a list of transactions.

    Args:
    - transactions (List[Transaction]): A list of Transaction objects.

    Returns:
    - Dict[str, float]: A dictionary with 'total_gains' and 'total_fees'.
    """
    total_gains = 0.0
    total_fees = 0.0
    buy_amounts = {}

    for transaction in transactions:
        if transaction.type == 'buy':
            if transaction.amount in buy_amounts:
                buy_amounts[transaction.amount] += transaction.amount * transaction.price
            else:
                buy_amounts[transaction.amount] = transaction.amount * transaction.price
            total_fees += transaction.fee
        elif transaction.type == 'sell':
            if transaction.amount in buy_amounts:
                buy_price = buy_amounts[transaction.amount] / transaction.amount
                gain = (transaction.price - buy_price) * transaction.amount
                total_gains += gain
                buy_amounts[transaction.amount] -= transaction.amount * buy_price
            else:
                print(f"Warning: Sold {transaction.amount} without a corresponding buy.")

    return {'total_gains': total_gains, 'total_fees': total_fees}


def main():
    # Example usage
    csv_transactions = load_transactions_from_csv('transactions.csv')
    json_transactions = load_transactions_from_json('transactions.json')

    csv_gains = calculate_gains(csv_transactions)
    json_gains = calculate_gains(json_transactions)

    print("CSV Gains:", csv_gains)
    print("JSON Gains:", json_gains)


if __name__ == "__main__":
    main()
```
