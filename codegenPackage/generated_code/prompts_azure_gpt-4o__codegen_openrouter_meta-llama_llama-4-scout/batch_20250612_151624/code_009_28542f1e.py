"""
Generated Code Metadata:
========================
Original URL: https://sui.tax
Prompt: Write code to validate and format exported cryptocurrency transaction data for tax purposes, inspired by the tools provided by Sui.tax.
Generated: DETERMINISTIC_28542f1e91e6c998
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict

class Transaction:
    def __init__(self, 
                 transaction_id: str, 
                 date: str, 
                 cryptocurrency: str, 
                 amount: float, 
                 fee: float, 
                 sender: str, 
                 recipient: str):
        """
        Initialize a Transaction object.

        Args:
        - transaction_id (str): Unique transaction ID.
        - date (str): Date of the transaction in ISO 8601 format.
        - cryptocurrency (str): Cryptocurrency used in the transaction.
        - amount (float): Amount of cryptocurrency transferred.
        - fee (float): Transaction fee.
        - sender (str): Sender's wallet address.
        - recipient (str): Recipient's wallet address.
        """
        self.transaction_id = transaction_id
        self.date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        self.cryptocurrency = cryptocurrency
        self.amount = amount
        self.fee = fee
        self.sender = sender
        self.recipient = recipient

    def to_dict(self) -> Dict:
        """
        Convert the Transaction object to a dictionary.

        Returns:
        - Dict: Transaction data as a dictionary.
        """
        return {
            "transaction_id": self.transaction_id,
            "date": self.date.isoformat(),
            "cryptocurrency": self.cryptocurrency,
            "amount": self.amount,
            "fee": self.fee,
            "sender": self.sender,
            "recipient": self.recipient
        }

def validate_transaction_data(data: List[Dict]) -> List[Transaction]:
    """
    Validate and convert transaction data to Transaction objects.

    Args:
    - data (List[Dict]): List of transaction data dictionaries.

    Returns:
    - List[Transaction]: List of validated Transaction objects.

    Raises:
    - ValueError: If required fields are missing or have incorrect types.
    """
    required_fields = ["transaction_id", "date", "cryptocurrency", "amount", "fee", "sender", "recipient"]
    transactions = []

    for transaction_data in data:
        try:
            # Check for required fields
            if not all(field in transaction_data for field in required_fields):
                raise ValueError("Missing required fields")

            # Validate data types
            if not isinstance(transaction_data["transaction_id"], str):
                raise ValueError("Transaction ID must be a string")
            if not isinstance(transaction_data["date"], str):
                raise ValueError("Date must be a string")
            if not isinstance(transaction_data["cryptocurrency"], str):
                raise ValueError("Cryptocurrency must be a string")
            if not isinstance(transaction_data["amount"], (int, float)):
                raise ValueError("Amount must be a number")
            if not isinstance(transaction_data["fee"], (int, float)):
                raise ValueError("Fee must be a number")
            if not isinstance(transaction_data["sender"], str):
                raise ValueError("Sender must be a string")
            if not isinstance(transaction_data["recipient"], str):
                raise ValueError("Recipient must be a string")

            transaction = Transaction(
                transaction_data["transaction_id"],
                transaction_data["date"],
                transaction_data["cryptocurrency"],
                transaction_data["amount"],
                transaction_data["fee"],
                transaction_data["sender"],
                transaction_data["recipient"]
            )
            transactions.append(transaction)
        except ValueError as e:
            print(f"Invalid transaction data: {transaction_data}. Error: {e}")

    return transactions

def format_transactions_for_tax(transactions: List[Transaction]) -> List[Dict]:
    """
    Format Transaction objects for tax purposes.

    Args:
    - transactions (List[Transaction]): List of Transaction objects.

    Returns:
    - List[Dict]: List of formatted transaction data dictionaries.
    """
    formatted_transactions = []

    for transaction in transactions:
        formatted_transaction = {
            "date": transaction.date.isoformat(),
            "cryptocurrency": transaction.cryptocurrency,
            "type": "sale" if transaction.recipient != "" else "transfer",
            "amount": transaction.amount,
            "fee": transaction.fee,
            "proceeds": transaction.amount - transaction.fee,
            "sender": transaction.sender,
            "recipient": transaction.recipient
        }
        formatted_transactions.append(formatted_transaction)

    return formatted_transactions

def main():
    # Example usage
    transaction_data = [
        {
            "transaction_id": "12345",
            "date": "2022-01-01T12:00:00.000",
            "cryptocurrency": "BTC",
            "amount": 1.0,
            "fee": 0.01,
            "sender": "0x12345",
            "recipient": "0x67890"
        },
        {
            "transaction_id": "67890",
            "date": "2022-01-02T13:00:00.000",
            "cryptocurrency": "ETH",
            "amount": 10.0,
            "fee": 0.1,
            "sender": "0x67890",
            "recipient": ""
        }
    ]

    try:
        transactions = validate_transaction_data(transaction_data)
        formatted_transactions = format_transactions_for_tax(transactions)
        print(json.dumps(formatted_transactions, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
