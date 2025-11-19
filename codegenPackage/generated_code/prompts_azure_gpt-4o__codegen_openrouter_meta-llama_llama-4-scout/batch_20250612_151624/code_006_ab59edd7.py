"""
Generated Code Metadata:
========================
Original URL: https://sui.tax
Prompt: Create a function to export cryptocurrency transactions in a format suitable for tax filing, inspired by the capabilities of Sui.tax.
Generated: DETERMINISTIC_ab59edd7471b896d
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict

class Transaction:
    def __init__(self, date: str, description: str, amount: float, cryptocurrency: str, 
                 transaction_type: str, fee: float = 0.0):
        """
        Initialize a Transaction object.

        Args:
        - date (str): The date of the transaction in YYYY-MM-DD format.
        - description (str): A description of the transaction.
        - amount (float): The amount of cryptocurrency involved in the transaction.
        - cryptocurrency (str): The type of cryptocurrency involved in the transaction.
        - transaction_type (str): The type of transaction (e.g., buy, sell, transfer).
        - fee (float, optional): The transaction fee. Defaults to 0.0.
        """
        self.date = date
        self.description = description
        self.amount = amount
        self.cryptocurrency = cryptocurrency
        self.transaction_type = transaction_type
        self.fee = fee

def export_transactions_to_csv(transactions: List[Transaction], filename: str) -> None:
    """
    Export a list of transactions to a CSV file.

    Args:
    - transactions (List[Transaction]): A list of Transaction objects.
    - filename (str): The name of the CSV file to export to.

    Raises:
    - ValueError: If the filename is empty or not a string.
    - Exception: If an error occurs while writing to the CSV file.
    """
    if not isinstance(filename, str) or not filename:
        raise ValueError("Filename must be a non-empty string")

    fieldnames = ["Date", "Description", "Amount", "Cryptocurrency", "Transaction Type", "Fee"]
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in transactions:
                writer.writerow({
                    "Date": transaction.date,
                    "Description": transaction.description,
                    "Amount": transaction.amount,
                    "Cryptocurrency": transaction.cryptocurrency,
                    "Transaction Type": transaction.transaction_type,
                    "Fee": transaction.fee
                })
    except Exception as e:
        raise Exception(f"Error exporting transactions to CSV: {str(e)}")

def export_transactions_to_turbotax(transactions: List[Transaction], filename: str) -> None:
    """
    Export a list of transactions to a TurboTax-compatible CSV file.

    Args:
    - transactions (List[Transaction]): A list of Transaction objects.
    - filename (str): The name of the CSV file to export to.

    Raises:
    - ValueError: If the filename is empty or not a string.
    - Exception: If an error occurs while writing to the CSV file.
    """
    if not isinstance(filename, str) or not filename:
        raise ValueError("Filename must be a non-empty string")

    fieldnames = ["Date", "Description", "Proceeds", "Cost Basis", "Gain/Loss", "Cryptocurrency"]
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in transactions:
                if transaction.transaction_type.lower() == "sell":
                    writer.writerow({
                        "Date": transaction.date,
                        "Description": transaction.description,
                        "Proceeds": transaction.amount,
                        "Cost Basis": 0.0,  # This would need to be calculated based on buy transactions
                        "Gain/Loss": transaction.amount,  # This would need to be calculated based on buy and sell transactions
                        "Cryptocurrency": transaction.cryptocurrency
                    })
    except Exception as e:
        raise Exception(f"Error exporting transactions to TurboTax CSV: {str(e)}")

def main():
    transactions: List[Transaction] = [
        Transaction("2022-01-01", "Buy Bitcoin", 1000.0, "BTC", "buy"),
        Transaction("2022-01-15", "Sell Bitcoin", 1500.0, "BTC", "sell", 10.0),
    ]

    export_transactions_to_csv(transactions, "cryptocurrency_transactions.csv")
    export_transactions_to_turbotax(transactions, "turbotax_cryptocurrency_transactions.csv")

if __name__ == "__main__":
    main()
```
