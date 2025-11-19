"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: Design a basic economy system using a cryptocurrency (like $BIGTIME) for a game, including functions for transactions and token distribution.
Generated: DETERMINISTIC_1e38e0ce119d89da
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Optional
from dataclasses import dataclass
import hashlib
import time

@dataclass
class Transaction:
    """Represents a cryptocurrency transaction."""
    sender: str
    recipient: str
    amount: float
    timestamp: float
    transaction_id: str

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for serialization."""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'transaction_id': self.transaction_id
        }

class Wallet:
    """Represents a user's cryptocurrency wallet."""
    
    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0.0
        self.transaction_history: list[Transaction] = []
    
    def add_funds(self, amount: float) -> None:
        """Add funds to the wallet."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
    
    def deduct_funds(self, amount: float) -> None:
        """Deduct funds from the wallet."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to the wallet's history."""
        self.transaction_history.append(transaction)

class EconomySystem:
    """Manages the game's cryptocurrency economy."""
    
    def __init__(self):
        self.wallets: Dict[str, Wallet] = {}
        self.transaction_pool: list[Transaction] = []
    
    def create_wallet(self, owner: str) -> Wallet:
        """Create a new wallet for a user."""
        if owner in self.wallets:
            raise ValueError("Wallet already exists for this user")
        wallet = Wallet(owner)
        self.wallets[owner] = wallet
        return wallet
    
    def get_wallet(self, owner: str) -> Optional[Wallet]:
        """Retrieve a wallet by owner name."""
        return self.wallets.get(owner)
    
    def generate_transaction_id(self, sender: str, recipient: str, amount: float) -> str:
        """Generate a unique transaction ID."""
        data = f"{sender}{recipient}{amount}{time.time()}".encode()
        return hashlib.sha256(data).hexdigest()
    
    def create_transaction(self, sender: str, recipient: str, amount: float) -> Transaction:
        """Create and validate a new transaction."""
        if sender == recipient:
            raise ValueError("Sender and recipient cannot be the same")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        sender_wallet = self.get_wallet(sender)
        if not sender_wallet:
            raise ValueError("Sender wallet not found")
        
        if sender_wallet.balance < amount:
            raise ValueError("Insufficient funds")
        
        transaction_id = self.generate_transaction_id(sender, recipient, amount)
        transaction = Transaction(
            sender=sender,
            recipient=recipient,
            amount=amount,
            timestamp=time.time(),
            transaction_id=transaction_id
        )
        
        return transaction
    
    def execute_transaction(self, transaction: Transaction) -> None:
        """Execute a validated transaction."""
        sender_wallet = self.get_wallet(transaction.sender)
        recipient_wallet = self.get_wallet(transaction.recipient)
        
        if not sender_wallet or not recipient_wallet:
            raise ValueError("One or both wallets not found")
        
        sender_wallet.deduct_funds(transaction.amount)
        recipient_wallet.add_funds(transaction.amount)
        
        sender_wallet.add_transaction(transaction)
        recipient_wallet.add_transaction(transaction)
        self.transaction_pool.append(transaction)
    
    def distribute_tokens(self, recipients: Dict[str, float]) -> None:
        """Distribute tokens to multiple recipients (e.g., rewards)."""
        for recipient, amount in recipients.items():
            wallet = self.get_wallet(recipient)
            if not wallet:
                wallet = self.create_wallet(recipient)
            wallet.add_funds(amount)
    
    def save_state(self, file_path: str) -> None:
        """Save the economy system state to a file."""
        state = {
            'wallets': {owner: {
                'balance': wallet.balance,
                'transactions': [tx.to_dict() for tx in wallet.transaction_history]
            } for owner, wallet in self.wallets.items()},
            'transaction_pool': [tx.to_dict() for tx in self.transaction_pool]
        }
        
        with open(file_path, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self, file_path: str) -> None:
        """Load the economy system state from a file."""
        with open(file_path, 'r') as f:
            state = json.load(f)
        
        self.wallets = {}
        self.transaction_pool = []
        
        for owner, wallet_data in state['wallets'].items():
            wallet = Wallet(owner)
            wallet.balance = wallet_data['balance']
            wallet.transaction_history = [
                Transaction(**tx_data) for tx_data in wallet_data['transactions']
            ]
            self.wallets[owner] = wallet
        
        self.transaction_pool = [
            Transaction(**tx_data) for tx_data in state['transaction_pool']
        ]
```
