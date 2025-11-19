"""
Generated Code Metadata:
========================
Original URL: https://theprofit-bitcoin.com
Prompt: Write code to simulate a demo account for a decentralized finance platform, allowing users to test peer-to-peer transactions without intermediaries, as described on Profit Bitcoin.
Generated: DETERMINISTIC_bdc0dc07dbcdebc6
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Transaction:
    sender_id: str
    receiver_id: str
    amount: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    transaction_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: str = "pending"

@dataclass
class UserAccount:
    user_id: str
    name: str
    balance: float = 0.0
    transactions: List[Transaction] = field(default_factory=list)

class DeFiDemoPlatform:
    def __init__(self):
        self.accounts: Dict[str, UserAccount] = {}
    
    def create_account(self, name: str, initial_balance: float = 1000.0) -> UserAccount:
        """Create a new demo account with initial balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        user_id = str(uuid.uuid4())
        account = UserAccount(user_id=user_id, name=name, balance=initial_balance)
        self.accounts[user_id] = account
        return account
    
    def get_account(self, user_id: str) -> Optional[UserAccount]:
        """Retrieve an account by user ID."""
        return self.accounts.get(user_id)
    
    def execute_transaction(self, sender_id: str, receiver_id: str, amount: float) -> Transaction:
        """Execute a peer-to-peer transaction between accounts."""
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
        
        sender = self.accounts.get(sender_id)
        receiver = self.accounts.get(receiver_id)
        
        if not sender or not receiver:
            raise ValueError("Sender or receiver account not found")
        
        if sender.balance < amount:
            raise ValueError("Insufficient balance")
        
        transaction = Transaction(
            sender_id=sender_id,
            receiver_id=receiver_id,
            amount=amount
        )
        
        sender.balance -= amount
        receiver.balance += amount
        
        transaction.status = "completed"
        sender.transactions.append(transaction)
        receiver.transactions.append(transaction)
        
        return transaction
    
    def get_transaction_history(self, user_id: str) -> List[Transaction]:
        """Retrieve transaction history for an account."""
        account = self.accounts.get(user_id)
        if not account:
            raise ValueError("Account not found")
        return account.transactions
    
    def get_balance(self, user_id: str) -> float:
        """Get current balance for an account."""
        account = self.accounts.get(user_id)
        if not account:
            raise ValueError("Account not found")
        return account.balance
    
    def reset_demo(self) -> None:
        """Reset all demo accounts and transactions."""
        self.accounts.clear()

# Example usage
if __name__ == "__main__":
    platform = DeFiDemoPlatform()
    
    # Create demo accounts
    alice = platform.create_account("Alice", 1000.0)
    bob = platform.create_account("Bob", 500.0)
    
    # Execute a transaction
    try:
        transaction = platform.execute_transaction(alice.user_id, bob.user_id, 200.0)
        print(f"Transaction completed: {transaction.transaction_id}")
    except ValueError as e:
        print(f"Transaction failed: {str(e)}")
    
    # Check balances
    print(f"Alice's balance: {platform.get_balance(alice.user_id)}")
    print(f"Bob's balance: {platform.get_balance(bob.user_id)}")
    
    # Get transaction history
    print("Alice's transactions:")
    for tx in platform.get_transaction_history(alice.user_id):
        print(f"{tx.timestamp}: Sent {tx.amount} to {tx.receiver_id}")
```
