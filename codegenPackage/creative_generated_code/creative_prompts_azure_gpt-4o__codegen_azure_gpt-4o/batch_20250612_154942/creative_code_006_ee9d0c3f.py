"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptodrop.eu
Prompt: Generate code to display a warning message when CryptoDrop detects suspicious activity in a cryptocurrency transaction.
Generated: DETERMINISTIC_ee9d0c3f62fe2fc5
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to handle warning messages
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Log output to the console
    ]
)

class CryptoDrop:
    """
    Class to simulate CryptoDrop detection system for cryptocurrency transactions.
    """

    def __init__(self):
        """
        Initialize CryptoDrop with default suspicious activity thresholds.
        """
        self.suspicious_threshold = 10000  # Example threshold for suspicious transactions (in USD)

    def detect_suspicious_activity(self, transaction):
        """
        Analyze a cryptocurrency transaction for suspicious activity.

        :param transaction: Dictionary containing transaction details.
                            Example: {'id': '123', 'amount': 12000, 'sender': 'abc', 'receiver': 'xyz'}
        :return: None
        """
        try:
            # Validate transaction format
            if not isinstance(transaction, dict):
                raise ValueError("Transaction should be a dictionary.")

            # Validate required keys
            required_keys = ['id', 'amount', 'sender', 'receiver']
            for key in required_keys:
                if key not in transaction:
                    raise KeyError(f"Missing required key: {key}")

            # Check if the transaction amount exceeds the suspicious threshold
            amount = transaction['amount']
            if amount > self.suspicious_threshold:
                self.display_warning(transaction)

        except (ValueError, KeyError) as e:
            logging.error(f"Error processing transaction: {e}")

    def display_warning(self, transaction):
        """
        Display a warning message for a suspicious transaction.

        :param transaction: Dictionary containing transaction details.
        :return: None
        """
        warning_message = (
            f"WARNING: Suspicious activity detected!\n"
            f"Transaction ID: {transaction['id']}\n"
            f"Amount: ${transaction['amount']:.2f}\n"
            f"Sender: {transaction['sender']}\n"
            f"Receiver: {transaction['receiver']}\n"
            f"Please investigate further."
        )
        logging.warning(warning_message)


if __name__ == "__main__":
    # Example usage of CryptoDrop

    # Initialize the CryptoDrop detection system
    crypto_drop = CryptoDrop()

    # Example transaction data
    transaction_data = {
        'id': 'tx12345',
        'amount': 15000,  # Amount in USD
        'sender': 'wallet_abc123',
        'receiver': 'wallet_xyz789'
    }

    # Detect suspicious activity
    crypto_drop.detect_suspicious_activity(transaction_data)
```
