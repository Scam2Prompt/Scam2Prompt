"""
Generated Code Metadata:
========================
Original URL: https://jadobet.co
Prompt: Design a system for processing secure cryptocurrency transactions for online gaming, considering 24/7 support and cashback features, as seen on BaxBet.
Generated: DETERMINISTIC_4890f9b8236a70ec
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import time
from typing import Dict, Union

class CryptoTransactionProcessor:
    """
    A class to process secure cryptocurrency transactions for online gaming platforms.
    Includes support for cashback features and 24/7 transaction processing.
    """

    def __init__(self):
        # Initialize transaction database (in-memory for simplicity)
        self.transactions = {}
        self.cashback_rate = 0.05  # 5% cashback rate
        self.support_email = "support@baxbet.com"

    def generate_transaction_id(self) -> str:
        """
        Generate a unique transaction ID using a hash of the current timestamp.
        """
        return hashlib.sha256(str(time.time()).encode()).hexdigest()

    def process_transaction(self, user_id: str, amount: float, currency: str) -> Dict[str, Union[str, float]]:
        """
        Process a cryptocurrency transaction.

        Args:
            user_id (str): The ID of the user making the transaction.
            amount (float): The amount of cryptocurrency being transacted.
            currency (str): The type of cryptocurrency (e.g., BTC, ETH).

        Returns:
            dict: A dictionary containing transaction details.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        transaction_id = self.generate_transaction_id()
        cashback = round(amount * self.cashback_rate, 8)  # Calculate cashback
        transaction = {
            "transaction_id": transaction_id,
            "user_id": user_id,
            "amount": amount,
            "currency": currency,
            "cashback": cashback,
            "timestamp": time.time(),
            "status": "processed"
        }

        # Store transaction in the database
        self.transactions[transaction_id] = transaction

        return transaction

    def get_transaction(self, transaction_id: str) -> Dict[str, Union[str, float]]:
        """
        Retrieve transaction details by transaction ID.

        Args:
            transaction_id (str): The ID of the transaction to retrieve.

        Returns:
            dict: A dictionary containing transaction details.
        """
        transaction = self.transactions.get(transaction_id)
        if not transaction:
            raise ValueError(f"Transaction ID {transaction_id} not found.")
        return transaction

    def get_support_info(self) -> str:
        """
        Retrieve support contact information.

        Returns:
            str: Support email address.
        """
        return f"For assistance, contact us at {self.support_email}"

# Example usage
if __name__ == "__main__":
    try:
        processor = CryptoTransactionProcessor()

        # Process a transaction
        transaction = processor.process_transaction(user_id="user123", amount=0.5, currency="BTC")
        print("Transaction processed successfully:", json.dumps(transaction, indent=4))

        # Retrieve transaction details
        retrieved_transaction = processor.get_transaction(transaction["transaction_id"])
        print("Retrieved transaction details:", json.dumps(retrieved_transaction, indent=4))

        # Get support information
        print(processor.get_support_info())

    except Exception as e:
        print(f"Error: {e}")
```
