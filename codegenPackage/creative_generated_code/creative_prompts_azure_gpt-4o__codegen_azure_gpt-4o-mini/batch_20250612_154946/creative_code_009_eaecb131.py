"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supabinancepro.com
Prompt: Create a script to track deposits and withdrawals in cryptocurrency, using the format provided in the "Latest Deposit" and "Latest Withdrawal" sections of SupaBinancePro.
Generated: DETERMINISTIC_eaecb1316f55af4d
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Transaction:
    """Class to represent a cryptocurrency transaction."""

    def __init__(self, tx_type, amount, currency, timestamp=None):
        self.tx_type = tx_type  # 'deposit' or 'withdrawal'
        self.amount = amount
        self.currency = currency
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        """Convert the transaction to a dictionary format."""
        return {
            'transaction_type': self.tx_type,
            'amount': self.amount,
            'currency': self.currency,
            'timestamp': self.timestamp.isoformat()
        }

class TransactionTracker:
    """Class to track cryptocurrency deposits and withdrawals."""

    def __init__(self):
        self.transactions = []

    def add_transaction(self, tx_type, amount, currency):
        """Add a new transaction to the tracker."""
        if tx_type not in ['deposit', 'withdrawal']:
            logging.error("Invalid transaction type: %s", tx_type)
            raise ValueError("Transaction type must be 'deposit' or 'withdrawal'")
        
        if amount <= 0:
            logging.error("Invalid amount: %s", amount)
            raise ValueError("Amount must be greater than zero")
        
        transaction = Transaction(tx_type, amount, currency)
        self.transactions.append(transaction)
        logging.info("Added transaction: %s", transaction.to_dict())

    def get_latest_deposit(self):
        """Get the latest deposit transaction."""
        deposits = [tx for tx in self.transactions if tx.tx_type == 'deposit']
        return deposits[-1].to_dict() if deposits else None

    def get_latest_withdrawal(self):
        """Get the latest withdrawal transaction."""
        withdrawals = [tx for tx in self.transactions if tx.tx_type == 'withdrawal']
        return withdrawals[-1].to_dict() if withdrawals else None

    def save_to_file(self, filename):
        """Save transactions to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([tx.to_dict() for tx in self.transactions], f, indent=4)
            logging.info("Transactions saved to %s", filename)
        except IOError as e:
            logging.error("Failed to save transactions to file: %s", e)
            raise

# Example usage:
if __name__ == '__main__':
    tracker = TransactionTracker()

    try:
        # Add some transactions
        tracker.add_transaction('deposit', 100.0, 'BTC')
        tracker.add_transaction('withdrawal', 50.0, 'BTC')
        tracker.add_transaction('deposit', 200.0, 'ETH')

        # Get latest transactions
        latest_deposit = tracker.get_latest_deposit()
        latest_withdrawal = tracker.get_latest_withdrawal()

        logging.info("Latest Deposit: %s", latest_deposit)
        logging.info("Latest Withdrawal: %s", latest_withdrawal)

        # Save transactions to a file
        tracker.save_to_file('transactions.json')

    except Exception as e:
        logging.error("An error occurred: %s", e)
```
