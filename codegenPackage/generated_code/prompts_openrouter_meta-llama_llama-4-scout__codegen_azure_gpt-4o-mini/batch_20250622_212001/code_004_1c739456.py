"""
Generated Code Metadata:
========================
Original URL: https://fortistk.com
Prompt: "Generate code for a self-reinforcing, antifragile, and perpetually evolving security system for decentralized financial ecosystems."
Generated: DETERMINISTIC_1c739456934d2353
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import time
from typing import Any, Dict, List, Optional

class Transaction:
    """Class representing a financial transaction in the decentralized system."""
    
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the transaction to a dictionary."""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

class Block:
    """Class representing a block in the blockchain."""
    
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate the hash of the block."""
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the block to a dictionary."""
        return {
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'hash': self.hash
        }

class Blockchain:
    """Class representing the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        self.create_block(previous_hash='1')  # Genesis block
    
    def create_block(self, previous_hash: str) -> Block:
        """Create a new block and add it to the chain."""
        block = Block(index=len(self.chain) + 1, transactions=self.current_transactions, previous_hash=previous_hash)
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block
    
    def add_transaction(self, sender: str, recipient: str, amount: float) -> Optional[str]:
        """Add a transaction to the list of transactions."""
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return self.last_block.hash
    
    @property
    def last_block(self) -> Block:
        """Return the last block in the chain."""
        return self.chain[-1]

def main():
    """Main function to demonstrate the blockchain functionality."""
    try:
        # Create a new blockchain
        blockchain = Blockchain()
        
        # Add transactions
        blockchain.add_transaction(sender="Alice", recipient="Bob", amount=50)
        blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=25)
        
        # Create a new block
        blockchain.create_block(previous_hash=blockchain.last_block.hash)
        
        # Print the blockchain
        for block in blockchain.chain:
            print(json.dumps(block.to_dict(), indent=4))
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
