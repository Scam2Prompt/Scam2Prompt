"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-aml.com
Prompt: Explain how to use AMLBot's dashboard for managing and filtering transactions in a cryptocurrency wallet application.
Generated: DETERMINISTIC_ae51d5b6d2158919
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

class Transaction:
    """Class to represent a cryptocurrency transaction."""
    
    def __init__(self, tx_id: str, amount: float, timestamp: str, tx_type: str):
        """
        Initialize a new transaction.

        Args:
            tx_id (str): Unique identifier for the transaction.
            amount (float): Amount of cryptocurrency involved.
            timestamp (str): Time when the transaction occurred.
            tx_type (str): Type of transaction ('incoming' or 'outgoing').
        """
        self.tx_id = tx_id
        self.amount = amount
        self.timestamp = timestamp
        self.tx_type = tx_type

    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary format for easy representation."""
        return {
            'tx_id': self.tx_id,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'tx_type': self.tx_type
        }


class Wallet:
    """Class to manage the cryptocurrency wallet and its transactions."""
    
    def __init__(self):
        """Initialize wallet with an empty transaction list."""
        self.transactions: List[Transaction] = []

    def add_transaction(self, tx: Transaction) -> None:
        """Add a new transaction to the wallet.

        Args:
            tx (Transaction): The transaction to add.

        Raises:
            ValueError: If the transaction is invalid.
        """
        if not isinstance(tx, Transaction):
            logging.error("Invalid transaction type")
            raise ValueError("Invalid transaction type")
        self.transactions.append(tx)
        logging.info(f"Transaction {tx.tx_id} added successfully.")

    def filter_transactions(self, tx_type: str = None, amount_threshold: float = None) -> List[Dict[str, Any]]:
        """Filter transactions based on type and amount.

        Args:
            tx_type (str, optional): Type of transaction to filter ('incoming' or 'outgoing').
            amount_threshold (float, optional): Minimum amount for transactions to include.

        Returns:
            List[Dict[str, Any]]: List of filtered transactions in dictionary format.
        """
        filtered_transactions = []

        for tx in self.transactions:
            if tx_type and tx.tx_type != tx_type:
                continue
            if amount_threshold and tx.amount < amount_threshold:
                continue
            filtered_transactions.append(tx.to_dict())

        logging.info(f"Filtered transactions count: {len(filtered_transactions)}")
        return filtered_transactions

    def get_all_transactions(self) -> List[Dict[str, Any]]:
        """Get all transactions in the wallet.

        Returns:
            List[Dict[str, Any]]: List of all transactions in dictionary format.
        """
        logging.info(f"Total transactions count: {len(self.transactions)}")
        return [tx.to_dict() for tx in self.transactions]


# Example usage of the Wallet class
if __name__ == "__main__":
    # Create a new wallet instance
    wallet = Wallet()
    
    # Add some transactions
    wallet.add_transaction(Transaction('tx1', 0.5, '2023-10-21 10:00', 'incoming'))
    wallet.add_transaction(Transaction('tx2', 1.0, '2023-10-22 10:00', 'outgoing'))
    wallet.add_transaction(Transaction('tx3', 0.75, '2023-10-23 10:00', 'incoming'))

    # Get and print all transactions
    all_transactions = wallet.get_all_transactions()
    print("All Transactions:", all_transactions)

    # Filter transactions based on type
    incoming_transactions = wallet.filter_transactions(tx_type='incoming')
    print("Incoming Transactions:", incoming_transactions)

    # Filter transactions based on amount
    high_value_transactions = wallet.filter_transactions(amount_threshold=0.6)
    print("High Value Transactions:", high_value_transactions)
```
