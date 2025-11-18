"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvest.finance.blog
Prompt: Develop a Python program that simulates the process of securely sending and receiving Bitcoin, inspired by the mission of Coinbase Invest to make crypto accessible to everyone.
Generated: DETERMINISTIC_3e2344bfc14f9914
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import random
import string
import json
import os

class Wallet:
    """A class to represent a Bitcoin wallet."""

    def __init__(self):
        """Initialize a new wallet with a unique address and balance."""
        self.address = self.generate_address()
        self.balance = 0.0

    @staticmethod
    def generate_address() -> str:
        """Generate a unique Bitcoin address."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=34))

    def add_funds(self, amount: float):
        """Add funds to the wallet."""
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.balance += amount

    def send_funds(self, amount: float, recipient: 'Wallet'):
        """Send funds to another wallet."""
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        recipient.add_funds(amount)

class Transaction:
    """A class to represent a Bitcoin transaction."""

    def __init__(self, sender: Wallet, recipient: Wallet, amount: float):
        """Initialize a transaction with sender, recipient, and amount."""
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self) -> str:
        """Generate a unique transaction ID using a hash."""
        data = f"{self.sender.address}{self.recipient.address}{self.amount}{os.urandom(16)}"
        return hashlib.sha256(data.encode()).hexdigest()

    def execute(self):
        """Execute the transaction if funds are available."""
        try:
            self.sender.send_funds(self.amount, self.recipient)
            print(f"Transaction successful: {self.transaction_id}")
            print(f"New balance for sender: {self.sender.balance}")
            print(f"New balance for recipient: {self.recipient.balance}")
        except ValueError as e:
            print(f"Transaction failed: {e}")

def main():
    """Main function to simulate sending and receiving Bitcoin."""
    # Create wallets for sender and recipient
    sender_wallet = Wallet()
    recipient_wallet = Wallet()

    # Fund the sender's wallet
    sender_wallet.add_funds(10.0)  # Add 10 BTC for testing

    print(f"Sender Address: {sender_wallet.address}, Initial Balance: {sender_wallet.balance}")
    print(f"Recipient Address: {recipient_wallet.address}, Initial Balance: {recipient_wallet.balance}")

    # Create a transaction
    transaction_amount = 5.0  # Amount to send
    transaction = Transaction(sender_wallet, recipient_wallet, transaction_amount)

    # Execute the transaction
    transaction.execute()

if __name__ == "__main__":
    main()
```
