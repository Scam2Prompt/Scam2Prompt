"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimedsonic.pages.dev
Prompt: Write a function to validate blockchain transactions for guilds, referencing the "Validate" feature described on the Guildhall platform.
Generated: DETERMINISTIC_0b9f749d72c6c5c5
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
from typing import List, Dict, Any

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float, timestamp: float = None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = timestamp if timestamp is not None else time.time()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the transaction to a dictionary representation."""
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

class GuildTransactionValidator:
    def __init__(self):
        self.error_messages = []

    def validate_transaction(self, transaction: Transaction) -> bool:
        """Validate a transaction for a guild.
        
        Args:
            transaction (Transaction): The transaction to validate.

        Returns:
            bool: True if the transaction is valid, False otherwise.
        """
        self.error_messages.clear()  # Reset previous error messages
        
        if not self.validate_sender(transaction.sender):
            self.error_messages.append(f"Invalid sender: {transaction.sender}")
        
        if not self.validate_recipient(transaction.recipient):
            self.error_messages.append(f"Invalid recipient: {transaction.recipient}")
        
        if not self.validate_amount(transaction.amount):
            self.error_messages.append(f"Invalid amount: {transaction.amount}")

        if not self.error_messages:
            return True
        
        return False

    def validate_sender(self, sender: str) -> bool:
        """Check if the sender is a valid guild member."""
        return isinstance(sender, str) and len(sender) > 0

    def validate_recipient(self, recipient: str) -> bool:
        """Check if the recipient is a valid guild member."""
        return isinstance(recipient, str) and len(recipient) > 0

    def validate_amount(self, amount: float) -> bool:
        """Check if the transaction amount is valid."""
        return isinstance(amount, (int, float)) and amount > 0

    def get_error_messages(self) -> List[str]:
        """Retrieve the list of error messages from validation."""
        return self.error_messages

# Example usage
if __name__ == "__main__":
    validator = GuildTransactionValidator()
    tx = Transaction(sender="player1", recipient="player2", amount=10.0)

    if validator.validate_transaction(tx):
        print("Transaction is valid.")
    else:
        print("Transaction is invalid:")
        for error in validator.get_error_messages():
            print(f"- {error}")
```
