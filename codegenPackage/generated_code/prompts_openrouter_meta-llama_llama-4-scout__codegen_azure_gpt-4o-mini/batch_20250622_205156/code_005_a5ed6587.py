"""
Generated Code Metadata:
========================
Original URL: https://arbitriumltd.com
Prompt: "Design a high-level architecture for a blockchain-based system using Arbitrium Ltd's expert consulting services as a reference."
Generated: DETERMINISTIC_a5ed6587f0f32189
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Blockchain-Based System Architecture

This code outlines a high-level architecture for a blockchain-based system.
It includes classes for the main components: Blockchain, Block, and Transaction.
The architecture is designed to be modular, allowing for easy expansion and integration
with Arbitrium Ltd's expert consulting services.

"""

import hashlib
import json
from time import time
from typing import List, Dict, Any

class Transaction:
    """
    Represents a transaction in the blockchain.
    """

    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the transaction to a dictionary format.
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }


class Block:
    """
    Represents a block in the blockchain.
    """

    def __init__(self, index: int, transactions: List[Transaction], timestamp: float, previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.
        """
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the block to a dictionary format.
        """
        return {
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }


class Blockchain:
    """
    Represents the blockchain itself.
    """

    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        self.create_block(previous_hash='1')  # Genesis block

    def create_block(self, previous_hash: str) -> Block:
        """
        Create a new block in the blockchain.
        """
        index = len(self.chain) + 1
        timestamp = time()
        block = Block(index, self.current_transactions, timestamp, previous_hash)
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Add a new transaction to the list of transactions.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return self.last_block.index + 1  # Return the index of the block that will hold this transaction

    @property
    def last_block(self) -> Block:
        """
        Return the last block in the chain.
        """
        return self.chain[-1]

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the blockchain to a dictionary format.
        """
        return {
            'chain': [block.to_dict() for block in self.chain],
            'length': len(self.chain)
        }


# Example usage
if __name__ == "__main__":
    try:
        blockchain = Blockchain()
        blockchain.add_transaction(sender="Alice", recipient="Bob", amount=50)
        blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=25)
        blockchain.create_block(previous_hash=blockchain.last_block.hash)

        # Print the blockchain
        print(json.dumps(blockchain.to_dict(), indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
```
