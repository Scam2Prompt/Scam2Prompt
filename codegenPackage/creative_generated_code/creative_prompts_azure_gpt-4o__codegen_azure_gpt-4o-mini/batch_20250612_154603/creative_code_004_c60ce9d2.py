"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Develop a blockchain-based solution for securely managing deposits and withdrawals, inspired by Access Link Limited's "Safe and Secure" cryptocurrency arbitrage strategy.
Generated: DETERMINISTIC_c60ce9d2b7aa3bc4
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
import json
from time import time
from typing import List, Dict, Any

class Transaction:
    """Class to represent a transaction in the blockchain."""
    
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to a dictionary."""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }

class Block:
    """Class to represent a block in the blockchain."""
    
    def __init__(self, index: int, timestamp: float, transactions: List[Transaction], previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """Compute the hash of the block using SHA-256."""
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        """Convert block to a dictionary."""
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }

class Blockchain:
    """Class to represent the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        # Create the genesis block
        self.create_block(previous_hash='1')

    def create_block(self, previous_hash: str) -> Block:
        """Create a new block and add it to the blockchain."""
        block = Block(index=len(self.chain) + 1,
                      timestamp=time(),
                      transactions=self.current_transactions,
                      previous_hash=previous_hash)
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def create_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """Create a new transaction to go into the next mined block."""
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        """Return the last block in the chain."""
        if not self.chain:
            raise IndexError("The blockchain is empty")
        return self.chain[-1]

    def get_balance(self, address: str) -> float:
        """Calculate the balance of a given address."""
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender == address:
                    balance -= transaction.amount
                if transaction.recipient == address:
                    balance += transaction.amount
        return balance

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        blockchain = Blockchain()
        
        # Creating transactions
        blockchain.create_transaction("Alice", "Bob", 50)
        blockchain.create_transaction("Bob", "Charlie", 25)

        # Mining the block
        blockchain.create_block(previous_hash=blockchain.last_block.hash)

        # Check balances
        print(f"Alice's balance: {blockchain.get_balance('Alice')}")
        print(f"Bob's balance: {blockchain.get_balance('Bob')}")
        print(f"Charlie's balance: {blockchain.get_balance('Charlie')}")

        # Print the blockchain
        for block in blockchain.chain:
            print(json.dumps(block.to_dict(), indent=4))
            
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code creates a simple blockchain system for managing cryptocurrency transactions such as deposits and withdrawals. It includes classes for transactions and blocks, and manages the chain itself, with methods for creating transactions, mining blocks, and checking balances. Error handling is included to ensure robustness.
