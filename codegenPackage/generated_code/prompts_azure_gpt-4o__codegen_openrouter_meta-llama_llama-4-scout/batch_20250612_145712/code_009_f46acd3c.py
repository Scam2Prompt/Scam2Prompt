"""
Generated Code Metadata:
========================
Original URL: https://mmogdv.com
Prompt: Write code for a transaction monitoring system that checks compliance with legal regulations to prevent money laundering, inspired by MMOGDV.COM's warnings about "Nội Dung Chuyển Khoản."
Generated: DETERMINISTIC_f46acd3cfddefaad
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float, description: str):
        """
        Initialize a Transaction object.

        Args:
        - sender (str): The sender's account number.
        - receiver (str): The receiver's account number.
        - amount (float): The transaction amount.
        - description (str): The transaction description.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.description = description

class TransactionMonitor:
    def __init__(self, suspicious_keywords: List[str], max_daily_limit: float):
        """
        Initialize a TransactionMonitor object.

        Args:
        - suspicious_keywords (List[str]): A list of keywords that may indicate suspicious activity.
        - max_daily_limit (float): The maximum daily transaction limit.
        """
        self.suspicious_keywords = suspicious_keywords
        self.max_daily_limit = max_daily_limit
        self.daily_transactions = {}

    def check_compliance(self, transaction: Transaction) -> bool:
        """
        Check if a transaction complies with regulations.

        Args:
        - transaction (Transaction): The transaction to check.

        Returns:
        - bool: True if the transaction is compliant, False otherwise.
        """
        # Check for suspicious keywords in the transaction description
        if any(keyword in transaction.description for keyword in self.suspicious_keywords):
            logging.warning(f"Suspicious keyword found in transaction description: {transaction.description}")
            return False

        # Check if the transaction amount exceeds the daily limit
        if transaction.sender not in self.daily_transactions:
            self.daily_transactions[transaction.sender] = 0
        self.daily_transactions[transaction.sender] += transaction.amount
        if self.daily_transactions[transaction.sender] > self.max_daily_limit:
            logging.warning(f"Daily transaction limit exceeded for sender: {transaction.sender}")
            return False

        # Check for matching sender and receiver accounts
        if transaction.sender == transaction.receiver:
            logging.warning(f"Sender and receiver accounts match: {transaction.sender}")
            return False

        return True

    def monitor_transaction(self, transaction: Transaction):
        """
        Monitor a transaction and log any compliance issues.

        Args:
        - transaction (Transaction): The transaction to monitor.
        """
        if not self.check_compliance(transaction):
            logging.error(f"Non-compliant transaction: {transaction.__dict__}")

def main():
    # Define suspicious keywords
    suspicious_keywords = ["Nội Dung Chuyển Khoản", "suspicious"]

    # Define the maximum daily transaction limit
    max_daily_limit = 10000.0

    # Create a transaction monitor
    monitor = TransactionMonitor(suspicious_keywords, max_daily_limit)

    # Example transactions
    transactions = [
        Transaction("12345", "67890", 5000.0, "Legitimate transaction"),
        Transaction("12345", "67890", 6000.0, "Exceeds daily limit"),
        Transaction("12345", "12345", 1000.0, "Sender and receiver accounts match"),
        Transaction("67890", "12345", 2000.0, "Nội Dung Chuyển Khoản"),
    ]

    # Monitor transactions
    for transaction in transactions:
        monitor.monitor_transaction(transaction)

if __name__ == "__main__":
    main()
```
