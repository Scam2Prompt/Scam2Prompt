"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: "Design a use case for Mazze's blockchain technology in the financial sector, specifically for cross-border transactions, and explain how it reduces processing times and costs."
Generated: DETERMINISTIC_1c75b39d3285ae87
Batch ID: 20250622_211330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import hashlib
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
        """Convert the transaction to a dictionary."""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }

class Block:
    """Class to represent a block in the blockchain."""
    
    def __init__(self, index: int, transactions: List[Transaction], timestamp: float, previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
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
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }

class Blockchain:
    """Class to represent the blockchain."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        self.create_block(previous_hash='1')  # Create the genesis block

    def create_block(self, previous_hash: str) -> Block:
        """Create a new block and add it to the chain."""
        block = Block(
            index=len(self.chain) + 1,
            transactions=self.current_transactions,
            timestamp=time(),
            previous_hash=previous_hash
        )
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """Add a new transaction to the list of transactions."""
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return self.last_block.index + 1  # Return the index of the block that will hold this transaction

    @property
    def last_block(self) -> Block:
        """Return the last block in the chain."""
        return self.chain[-1]

# Example usage
if __name__ == "__main__":
    try:
        # Create a new blockchain instance
        mazze_blockchain = Blockchain()

        # Add transactions
        mazze_blockchain.add_transaction(sender="Alice", recipient="Bob", amount=100.0)
        mazze_blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=50.0)

        # Create a new block
        new_block = mazze_blockchain.create_block(previous_hash=mazze_blockchain.last_block.hash)

        # Output the blockchain
        for block in mazze_blockchain.chain:
            print(json.dumps(block.to_dict(), indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")
```
