"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betlahze.vip
Prompt: Generate a code snippet for a secure transaction system for a casino platform that supports cryptocurrency payments, similar to the features offered by BaxBet.
Generated: DETERMINISTIC_5cf774e9c71841e2
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import json
import logging
import time
from typing import Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
SECRET_KEY = "your_secure_secret_key"  # Replace this with a strong, secure key
SUPPORTED_CRYPTOCURRENCIES = ["BTC", "ETH", "USDT"]  # List of supported currencies

class TransactionError(Exception):
    """Custom exception for transaction errors."""
    pass

class Transaction:
    """Class representing a cryptocurrency transaction."""

    def __init__(self, user_id: str, amount: float, currency: str):
        """
        Initialize a new transaction.
        
        :param user_id: Unique identifier for the user.
        :param amount: Transaction amount in the specified currency.
        :param currency: Cryptocurrency used for the transaction.
        """
        self.transaction_id = self._generate_transaction_id()
        self.user_id = user_id
        self.amount = amount
        self.currency = currency
        self.timestamp = int(time.time())
    
    def _generate_transaction_id(self) -> str:
        """
        Generate a unique transaction ID using HMAC and a timestamp.
        
        :return: Unique transaction ID.
        """
        message = f"{self.user_id}:{time.time()}"
        transaction_id = hmac.new(
            key=SECRET_KEY.encode(),
            msg=message.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()
        return transaction_id

    def is_valid_currency(self) -> bool:
        """
        Validate if the transaction currency is supported.
        
        :return: True if currency is valid, False otherwise.
        """
        return self.currency in SUPPORTED_CRYPTOCURRENCIES

    def to_dict(self) -> Dict[str, Optional[str]]:
        """
        Convert transaction details to dictionary format.
        
        :return: Dictionary containing transaction details.
        """
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "currency": self.currency,
            "timestamp": self.timestamp,
        }

def process_transaction(user_id: str, amount: float, currency: str) -> Dict[str, Optional[str]]:
    """
    Process a cryptocurrency transaction.

    :param user_id: Unique identifier for the user making the transaction.
    :param amount: Transaction amount in the specified currency.
    :param currency: Cryptocurrency used for the transaction.
    :return: Dictionary containing transaction details or error message.
    """
    try:
        # Validate input
        if amount <= 0:
            raise TransactionError("Transaction amount must be greater than zero.")
        
        # Create and validate transaction
        transaction = Transaction(user_id, amount, currency)
        if not transaction.is_valid_currency():
            raise TransactionError(f"Unsupported currency: {currency}. Supported currencies are {SUPPORTED_CRYPTOCURRENCIES}.")
        
        # Log transaction details
        logging.info(f"Processing transaction: {transaction.to_dict()}")
        
        # Return transaction details
        return transaction.to_dict()
    
    except TransactionError as e:
        logging.error(f"Transaction error: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    user_id = "user123"
    amount = 100.50
    currency = "BTC"
    
    result = process_transaction(user_id, amount, currency)
    print(json.dumps(result, indent=4))
```

This code provides a secure cryptocurrency transaction system with error handling, logging, and support for specific cryptocurrencies. It generates unique transaction IDs and validates the currency used. Replace `SECRET_KEY` with a secure key for production use.
