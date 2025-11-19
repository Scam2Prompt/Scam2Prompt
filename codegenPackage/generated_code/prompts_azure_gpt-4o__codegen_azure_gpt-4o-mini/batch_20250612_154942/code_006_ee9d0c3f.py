"""
Generated Code Metadata:
========================
Original URL: https://cryptodrop.eu
Prompt: Generate code to display a warning message when CryptoDrop detects suspicious activity in a cryptocurrency transaction.
Generated: DETERMINISTIC_ee9d0c3f62fe2fc5
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import time

# Configure logging to display warning messages
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoDrop:
    def __init__(self):
        # Initialize a list to store transaction history
        self.transaction_history = []

    def log_transaction(self, transaction):
        """
        Logs a transaction and checks for suspicious activity.
        
        Args:
            transaction (dict): A dictionary containing transaction details.
        """
        try:
            # Validate transaction format
            if not self.validate_transaction(transaction):
                raise ValueError("Invalid transaction format")

            # Add transaction to history
            self.transaction_history.append(transaction)

            # Check for suspicious activity
            if self.detect_suspicious_activity(transaction):
                self.display_warning(transaction)

        except Exception as e:
            logging.error(f"Error logging transaction: {e}")

    def validate_transaction(self, transaction):
        """
        Validates the transaction format.
        
        Args:
            transaction (dict): A dictionary containing transaction details.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        required_keys = ['id', 'amount', 'timestamp', 'sender', 'receiver']
        return all(key in transaction for key in required_keys)

    def detect_suspicious_activity(self, transaction):
        """
        Detects suspicious activity based on transaction details.
        
        Args:
            transaction (dict): A dictionary containing transaction details.
        
        Returns:
            bool: True if suspicious, False otherwise.
        """
        # Example criteria for suspicious activity
        if transaction['amount'] > 10000:  # Large transaction amount
            return True
        if transaction['timestamp'] < time.time() - 3600:  # Transaction older than 1 hour
            return True
        return False

    def display_warning(self, transaction):
        """
        Displays a warning message for suspicious transactions.
        
        Args:
            transaction (dict): A dictionary containing transaction details.
        """
        logging.warning(f"Suspicious activity detected in transaction ID {transaction['id']}! "
                        f"Amount: {transaction['amount']}, Sender: {transaction['sender']}, "
                        f"Receiver: {transaction['receiver']}")

# Example usage
if __name__ == "__main__":
    crypto_drop = CryptoDrop()
    
    # Simulated transactions
    transactions = [
        {'id': 'tx1', 'amount': 5000, 'timestamp': time.time(), 'sender': 'Alice', 'receiver': 'Bob'},
        {'id': 'tx2', 'amount': 15000, 'timestamp': time.time(), 'sender': 'Charlie', 'receiver': 'Dave'},
        {'id': 'tx3', 'amount': 200, 'timestamp': time.time() - 4000, 'sender': 'Eve', 'receiver': 'Frank'},
    ]

    for tx in transactions:
        crypto_drop.log_transaction(tx)
```
