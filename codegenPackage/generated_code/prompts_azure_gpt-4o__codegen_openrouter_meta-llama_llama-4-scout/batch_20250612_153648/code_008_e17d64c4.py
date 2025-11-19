"""
Generated Code Metadata:
========================
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Implement a Solana-based transaction tracker that flags bots with >=25% failure rates and attributes 50% of their volume to the final score.
Generated: DETERMINISTIC_e17d64c416420f10
Batch ID: 20250612_153648
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
from collections import defaultdict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Transaction:
    def __init__(self, sender: str, success: bool, volume: float):
        """
        Initialize a Transaction object.

        Args:
        - sender (str): The sender's address.
        - success (bool): Whether the transaction was successful.
        - volume (float): The transaction volume.
        """
        self.sender = sender
        self.success = success
        self.volume = volume

class TransactionTracker:
    def __init__(self):
        """
        Initialize a TransactionTracker object.
        """
        self.transactions: Dict[str, List[Transaction]] = defaultdict(list)

    def add_transaction(self, transaction: Transaction):
        """
        Add a transaction to the tracker.

        Args:
        - transaction (Transaction): The transaction to add.
        """
        self.transactions[transaction.sender].append(transaction)

    def calculate_failure_rate(self, sender: str) -> float:
        """
        Calculate the failure rate for a given sender.

        Args:
        - sender (str): The sender's address.

        Returns:
        - float: The failure rate.
        """
        transactions = self.transactions[sender]
        if not transactions:
            return 0.0

        failed_transactions = sum(1 for tx in transactions if not tx.success)
        return failed_transactions / len(transactions)

    def calculate_score(self, sender: str) -> float:
        """
        Calculate the score for a given sender.

        Args:
        - sender (str): The sender's address.

        Returns:
        - float: The score.
        """
        transactions = self.transactions[sender]
        if not transactions:
            return 0.0

        total_volume = sum(tx.volume for tx in transactions)
        failed_transactions = sum(1 for tx in transactions if not tx.success)

        # Flag bots with >= 25% failure rates and attribute 50% of their volume to the final score
        failure_rate = failed_transactions / len(transactions)
        if failure_rate >= 0.25:
            return total_volume * 0.5
        else:
            return total_volume

    def flag_bots(self) -> List[str]:
        """
        Flag senders with >= 25% failure rates.

        Returns:
        - List[str]: A list of flagged senders.
        """
        flagged_senders = []
        for sender, transactions in self.transactions.items():
            failure_rate = self.calculate_failure_rate(sender)
            if failure_rate >= 0.25:
                logging.warning(f"Flagged bot: {sender} with failure rate {failure_rate:.2f}")
                flagged_senders.append(sender)
        return flagged_senders

def main():
    tracker = TransactionTracker()

    # Example transactions
    transactions = [
        Transaction("sender1", True, 100.0),
        Transaction("sender1", False, 50.0),
        Transaction("sender1", True, 200.0),
        Transaction("sender2", False, 100.0),
        Transaction("sender2", False, 200.0),
        Transaction("sender2", False, 300.0),
    ]

    for tx in transactions:
        tracker.add_transaction(tx)

    flagged_senders = tracker.flag_bots()
    for sender in flagged_senders:
        score = tracker.calculate_score(sender)
        logging.info(f"Score for flagged bot {sender}: {score:.2f}")

if __name__ == "__main__":
    main()
```
