"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://revaluationway.com
Prompt: Write a code snippet for a simple escrow system for a cryptocurrency transaction, inspired by the escrow process mentioned on Revaluation Way.
Generated: DETERMINISTIC_60fb3254da7fb6e7
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class EscrowTransaction:
    """
    A class representing an escrow transaction for cryptocurrency.
    """

    def __init__(self, sender, receiver, amount):
        """
        Initialize an escrow transaction.

        Args:
            sender (str): The sender's unique identifier (e.g., wallet address).
            receiver (str): The receiver's unique identifier (e.g., wallet address).
            amount (float): The amount of cryptocurrency to be escrowed.

        Raises:
            ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        self.transaction_id = str(uuid.uuid4())  # Unique ID for the transaction
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.status = "PENDING"  # Initial status of the transaction
        self.created_at = datetime.utcnow()  # Timestamp for when the transaction is created
        self.released_at = None  # Timestamp for when the funds are released

    def release_funds(self):
        """
        Release funds to the receiver, completing the transaction.

        Raises:
            ValueError: If the transaction is not in a pending state.
        """
        if self.status != "PENDING":
            raise ValueError("Funds can only be released for a pending transaction.")

        self.status = "COMPLETED"
        self.released_at = datetime.utcnow()

    def cancel_transaction(self):
        """
        Cancel the escrow transaction, returning funds to the sender.

        Raises:
            ValueError: If the transaction is not in a pending state.
        """
        if self.status != "PENDING":
            raise ValueError("Transaction can only be canceled if it is pending.")

        self.status = "CANCELED"
        self.released_at = datetime.utcnow()

    def __str__(self):
        """
        Return a string representation of the transaction.
        """
        return (f"Transaction ID: {self.transaction_id}\n"
                f"Sender: {self.sender}\n"
                f"Receiver: {self.receiver}\n"
                f"Amount: {self.amount}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at}\n"
                f"Released At: {self.released_at if self.released_at else 'Not released'}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create an escrow transaction
        escrow = EscrowTransaction(sender="sender_wallet_123", receiver="receiver_wallet_456", amount=10.5)
        print(escrow)

        # Release funds
        escrow.release_funds()
        print("\nAfter releasing funds:")
        print(escrow)

        # Attempt to cancel (should raise an error as the transaction is completed)
        escrow.cancel_transaction()
    except ValueError as e:
        print(f"Error: {e}")
```
