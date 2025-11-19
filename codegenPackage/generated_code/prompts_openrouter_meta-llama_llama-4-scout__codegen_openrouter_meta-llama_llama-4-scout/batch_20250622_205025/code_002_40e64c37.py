"""
Generated Code Metadata:
========================
Original URL: https://mythetawallet.com
Prompt: Generate a list of Theta and TFuel transfer transactions in the last 24 hours based on the provided data.
Generated: DETERMINISTIC_40e64c379bfd222c
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict

class Transaction:
    def __init__(self, id: int, token: str, amount: float, timestamp: datetime):
        """
        Initialize a Transaction object.

        Args:
        id (int): Unique transaction ID.
        token (str): Token type (Theta or TFuel).
        amount (float): Transaction amount.
        timestamp (datetime): Transaction timestamp.
        """
        self.id = id
        self.token = token
        self.amount = amount
        self.timestamp = timestamp

def get_transactions(data: List[Dict]) -> List[Transaction]:
    """
    Convert raw transaction data into a list of Transaction objects.

    Args:
    data (List[Dict]): Raw transaction data.

    Returns:
    List[Transaction]: List of Transaction objects.
    """
    transactions = []
    for item in data:
        try:
            timestamp = datetime.fromtimestamp(item['timestamp'])
            transaction = Transaction(item['id'], item['token'], item['amount'], timestamp)
            transactions.append(transaction)
        except KeyError as e:
            print(f"Error: Missing key {e} in transaction data")
        except Exception as e:
            print(f"Error processing transaction: {e}")
    return transactions

def filter_transactions_by_token(transactions: List[Transaction], token: str) -> List[Transaction]:
    """
    Filter transactions by token type.

    Args:
    transactions (List[Transaction]): List of transactions.
    token (str): Token type (Theta or TFuel).

    Returns:
    List[Transaction]: Filtered list of transactions.
    """
    return [t for t in transactions if t.token == token]

def filter_transactions_by_time(transactions: List[Transaction], hours: int) -> List[Transaction]:
    """
    Filter transactions by time.

    Args:
    transactions (List[Transaction]): List of transactions.
    hours (int): Time range in hours.

    Returns:
    List[Transaction]: Filtered list of transactions.
    """
    time_threshold = datetime.now() - timedelta(hours=hours)
    return [t for t in transactions if t.timestamp >= time_threshold]

def main(data: List[Dict]):
    try:
        # Convert raw data to Transaction objects
        transactions = get_transactions(data)

        # Filter transactions by token and time
        theta_transactions = filter_transactions_by_token(transactions, 'Theta')
        tfuel_transactions = filter_transactions_by_token(transactions, 'TFuel')

        theta_transactions_last_24h = filter_transactions_by_time(theta_transactions, 24)
        tfuel_transactions_last_24h = filter_transactions_by_time(tfuel_transactions, 24)

        # Print results
        print("Theta transactions in the last 24 hours:")
        for t in theta_transactions_last_24h:
            print(f"ID: {t.id}, Amount: {t.amount}, Timestamp: {t.timestamp}")

        print("\nTFuel transactions in the last 24 hours:")
        for t in tfuel_transactions_last_24h:
            print(f"ID: {t.id}, Amount: {t.amount}, Timestamp: {t.timestamp}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    data = [
        {'id': 1, 'token': 'Theta', 'amount': 10.0, 'timestamp': 1662014400},
        {'id': 2, 'token': 'TFuel', 'amount': 5.0, 'timestamp': 1662014400},
        {'id': 3, 'token': 'Theta', 'amount': 20.0, 'timestamp': 1662100800},
        {'id': 4, 'token': 'TFuel', 'amount': 15.0, 'timestamp': 1662187200},
        {'id': 5, 'token': 'Theta', 'amount': 30.0, 'timestamp': 1662273600},
    ]
    main(data)
```
