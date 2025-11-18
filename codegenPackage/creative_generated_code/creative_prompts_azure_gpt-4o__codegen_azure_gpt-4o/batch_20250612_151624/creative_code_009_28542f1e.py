"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.tax
Prompt: Write code to validate and format exported cryptocurrency transaction data for tax purposes, inspired by the tools provided by Sui.tax.
Generated: DETERMINISTIC_28542f1e91e6c998
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
import os
import json
from datetime import datetime

# Define constants for validation
SUPPORTED_CURRENCIES = {"BTC", "ETH", "USDT", "SUI"}
TRANSACTION_TYPES = {"buy", "sell", "transfer", "stake"}
DATE_FORMAT = "%Y-%m-%d"

class CryptoTransactionValidator:
    """
    Class to validate and format cryptocurrency transactions for tax purposes.
    """

    @staticmethod
    def validate_transaction(transaction):
        """
        Validate a single transaction dictionary.
        Args:
            transaction (dict): The transaction data to be validated.
        Returns:
            bool: True if the transaction is valid, False otherwise.
        """
        try:
            # Check required fields
            required_fields = ["date", "currency", "amount", "type", "price_per_unit"]
            for field in required_fields:
                if field not in transaction:
                    raise ValueError(f"Missing required field: {field}")

            # Validate date format
            datetime.strptime(transaction["date"], DATE_FORMAT)

            # Validate currency
            if transaction["currency"] not in SUPPORTED_CURRENCIES:
                raise ValueError(f"Unsupported currency: {transaction['currency']}")

            # Validate transaction type
            if transaction["type"] not in TRANSACTION_TYPES:
                raise ValueError(f"Invalid transaction type: {transaction['type']}")

            # Validate numeric fields
            if float(transaction["amount"]) <= 0:
                raise ValueError("Amount must be greater than 0")
            if float(transaction["price_per_unit"]) < 0:
                raise ValueError("Price per unit must not be negative")

            return True
        except (ValueError, KeyError) as e:
            print(f"Validation Error: {e}")
            return False

    @staticmethod
    def format_transaction(transaction):
        """
        Format a transaction dictionary for tax export.
        Args:
            transaction (dict): The transaction data to be formatted.
        Returns:
            dict: The formatted transaction data.
        """
        formatted_transaction = {
            "Transaction Date": transaction["date"],
            "Currency": transaction["currency"],
            "Transaction Type": transaction["type"],
            "Amount": float(transaction["amount"]),
            "Price Per Unit (USD)": float(transaction["price_per_unit"]),
            "Total Value (USD)": float(transaction["amount"]) * float(transaction["price_per_unit"]),
        }
        return formatted_transaction


def process_transaction_file(input_file, output_file):
    """
    Process a CSV file of transactions, validate and format the data, and export it to a new CSV file.
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        transactions = []
        with open(input_file, mode="r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                if CryptoTransactionValidator.validate_transaction(row):
                    formatted_transaction = CryptoTransactionValidator.format_transaction(row)
                    transactions.append(formatted_transaction)

        if len(transactions) == 0:
            print("No valid transactions found. Output file will not be created.")
            return

        # Write validated and formatted transactions to output file
        with open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
            fieldnames = [
                "Transaction Date", "Currency", "Transaction Type",
                "Amount", "Price Per Unit (USD)", "Total Value (USD)"
            ]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)

        print(f"Processed transactions exported to '{output_file}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Input and output file paths (replace with actual paths)
    input_file = "input_transactions.csv"
    output_file = "formatted_transactions.csv"

    process_transaction_file(input_file, output_file)
```
