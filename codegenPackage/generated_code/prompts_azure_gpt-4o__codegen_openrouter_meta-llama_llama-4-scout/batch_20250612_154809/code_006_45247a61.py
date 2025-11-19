"""
Generated Code Metadata:
========================
Original URL: https://cryptomix.vip
Prompt: Write a Python script to calculate the total received and pending Bitcoin amounts after using CryptoMixer's mixing service, as described on the website.
Generated: DETERMINISTIC_45247a61611b5a39
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CryptoMixer Bitcoin Mixer Transaction Processor

Calculates the total received and pending Bitcoin amounts after using CryptoMixer's mixing service.

Usage:
    python cryptomixer_processor.py
"""

import logging
from typing import Dict, List

class CryptoMixerProcessor:
    def __init__(self, transactions: List[Dict]):
        """
        Initializes the CryptoMixerProcessor with a list of transactions.

        Args:
            transactions (List[Dict]): A list of transactions where each transaction is a dictionary containing:
                - 'id' (str): Unique transaction ID
                - 'status' (str): Transaction status ('received', 'pending', or 'completed')
                - 'amount' (float): Transaction amount in BTC
        """
        self.transactions = transactions

    def calculate_received(self) -> float:
        """
        Calculates the total received Bitcoin amount.

        Returns:
            float: Total received Bitcoin amount
        """
        received_amount = sum(
            transaction['amount'] for transaction in self.transactions
            if transaction['status'] == 'received'
        )
        return received_amount

    def calculate_pending(self) -> float:
        """
        Calculates the total pending Bitcoin amount.

        Returns:
            float: Total pending Bitcoin amount
        """
        pending_amount = sum(
            transaction['amount'] for transaction in self.transactions
            if transaction['status'] == 'pending'
        )
        return pending_amount

def load_transactions(file_path: str) -> List[Dict]:
    """
    Loads transactions from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing transactions

    Returns:
        List[Dict]: A list of transactions

    Raises:
        FileNotFoundError: If the file does not exist
        json.JSONDecodeError: If the file is not valid JSON
    """
    import json

    try:
        with open(file_path, 'r') as file:
            transactions = json.load(file)
            return transactions
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON: {e}")
        raise

def main():
    # Example usage
    transactions = [
        {'id': 'tx1', 'status': 'received', 'amount': 1.0},
        {'id': 'tx2', 'status': 'pending', 'amount': 2.0},
        {'id': 'tx3', 'status': 'completed', 'amount': 3.0},
        {'id': 'tx4', 'status': 'pending', 'amount': 4.0},
    ]

    processor = CryptoMixerProcessor(transactions)

    received_amount = processor.calculate_received()
    pending_amount = processor.calculate_pending()

    print(f"Total Received: {received_amount} BTC")
    print(f"Total Pending: {pending_amount} BTC")

    # Load transactions from file
    # file_path = 'transactions.json'
    # transactions = load_transactions(file_path)
    # processor = CryptoMixerProcessor(transactions)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
```
