"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bscbhn.com
Prompt: Write code to implement a secure transaction system for transferring funds between users, inspired by the "Transferir" functionality on https://bscbhn.com.
Generated: DETERMINISTIC_01533c1eea112f29
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import decimal
from datetime import datetime
from hashlib import sha256

class TransactionError(Exception):
    """Custom exception for transaction errors."""
    pass

class SecureTransactionSystem:
    """
    A class representing a secure transaction system to transfer funds between users.
    """
    def __init__(self):
        self.users = {}  # Dictionary to store user balances by user ID
        
    def create_user(self, username: str) -> str:
        """
        Creates a new user with a unique ID and initializes their balance to 0.

        Args:
            username (str): The username of the new user.

        Returns:
            str: The unique user ID generated for the new user.
        """
        user_id = str(uuid.uuid4())  # Generate unique user ID
        self.users[user_id] = {
            "username": username,
            "balance": decimal.Decimal("0.00"),
            "transactions": []
        }
        return user_id

    def get_balance(self, user_id: str) -> decimal.Decimal:
        """
        Retrieves the balance of the specified user.

        Args:
            user_id (str): The ID of the user whose balance is to be retrieved.

        Returns:
            decimal.Decimal: The user's current balance.
        """
        self._validate_user(user_id)
        return self.users[user_id]["balance"]

    def transfer_funds(self, sender_id: str, receiver_id: str, amount: decimal.Decimal, description: str = "") -> str:
        """
        Transfers funds securely from one user to another.

        Args:
            sender_id (str): The ID of the sender user.
            receiver_id (str): The ID of the receiver user.
            amount (decimal.Decimal): The amount to transfer.
            description (str): Optional description of the transaction.

        Returns:
            str: A transaction ID for the completed transfer.

        Raises:
            TransactionError: If validation or transfer fails.
        """
        self._validate_user(sender_id)
        self._validate_user(receiver_id)
        self._validate_amount(amount)
        
        if sender_id == receiver_id:
            raise TransactionError("Sender and receiver cannot be the same user.")

        if self.users[sender_id]["balance"] < amount:
            raise TransactionError("Insufficient balance in sender's account.")

        # Deduct funds from sender and add to receiver
        self.users[sender_id]["balance"] -= amount
        self.users[receiver_id]["balance"] += amount

        # Generate a unique transaction ID and record transaction
        transaction_id = str(uuid.uuid4())
        transaction_details = {
            "transaction_id": transaction_id,
            "timestamp": datetime.utcnow(),
            "amount": amount,
            "description": description,
            "sender_id": sender_id,
            "receiver_id": receiver_id
        }
        self.users[sender_id]["transactions"].append(transaction_details)
        self.users[receiver_id]["transactions"].append(transaction_details)

        return transaction_id

    def get_user_transactions(self, user_id: str) -> list:
        """
        Retrieves a list of all transactions for a given user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: A list of transaction details.
        """
        self._validate_user(user_id)
        return self.users[user_id]["transactions"]

    def _validate_user(self, user_id: str):
        """
        Validates that the provided user ID exists in the system.

        Args:
            user_id (str): The ID of the user.

        Raises:
            TransactionError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise TransactionError(f"User ID '{user_id}' does not exist.")

    def _validate_amount(self, amount: decimal.Decimal):
        """
        Validates that the provided amount is a positive decimal number.

        Args:
            amount (decimal.Decimal): The amount to validate.

        Raises:
            TransactionError: If the amount is invalid.
        """
        if amount <= decimal.Decimal("0.00"):
            raise TransactionError("Transaction amount must be greater than zero.")

# Example usage:
if __name__ == "__main__":
    system = SecureTransactionSystem()

    # Create users
    alice_id = system.create_user("Alice")
    bob_id = system.create_user("Bob")

    # Add funds to Alice's account (for demonstration purposes)
    system.users[alice_id]["balance"] += decimal.Decimal("100.00")

    # Perform a transaction
    try:
        transaction_id = system.transfer_funds(alice_id, bob_id, decimal.Decimal("25.50"), "Payment for services")
        print(f"Transaction successful. ID: {transaction_id}")
    except TransactionError as e:
        print(f"Transaction failed: {e}")

    # Retrieve and print balances
    print(f"Alice's balance: {system.get_balance(alice_id)}")
    print(f"Bob's balance: {system.get_balance(bob_id)}")

    # Print Alice's transactions
    print("Alice's transactions:")
    for transaction in system.get_user_transactions(alice_id):
        print(transaction)
```
