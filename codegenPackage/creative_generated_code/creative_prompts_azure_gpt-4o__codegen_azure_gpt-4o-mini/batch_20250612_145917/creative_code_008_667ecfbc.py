"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-labs.vercel.app
Prompt: Design a blockchain-based payment system using Sonic's infrastructure that supports real-time payments with sub-second confirmation times and low transaction costs.
Generated: DETERMINISTIC_667ecfbc6959016d
Batch ID: 20250612_145917
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
from collections import deque
from typing import List, Dict, Any


class Transaction:
    """Class to represent a payment transaction."""

    def __init__(self, sender: str, receiver: str, amount: float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp,
        }


class Block:
    """Class to represent a block in the blockchain."""

    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.block_hash = self.hash_block()

    def hash_block(self) -> str:
        """Hash the block's contents."""
        block_string = f"{self.index}{[t.to_dict() for t in self.transactions]}{self.previous_hash}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """Class to manage the blockchain."""

    def __init__(self):
        self.chain = []
        self.pending_transactions = deque()
        self.create_block(previous_hash='0')  # Create the genesis block

    def create_block(self, previous_hash: str) -> Block:
        """Create a new block and add it to the chain."""
        block = Block(index=len(self.chain), transactions=list(self.pending_transactions), previous_hash=previous_hash)
        self.pending_transactions.clear()  # Clear the pending transactions after block creation
        self.chain.append(block)
        return block

    def add_transaction(self, transaction: Transaction) -> bool:
        """Add a transaction to the pending transactions."""
        if transaction.amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        self.pending_transactions.append(transaction)
        return True

    def mine(self) -> Block:
        """Mine a new block and add it to the blockchain."""
        if not self.pending_transactions:
            raise Exception("No transactions to mine.")

        last_block = self.chain[-1]
        new_block = self.create_block(previous_hash=last_block.block_hash)
        return new_block


# Example usage
if __name__ == "__main__":
    # Create blockchain instance
    blockchain = Blockchain()

    # Add transactions
    try:
        blockchain.add_transaction(Transaction(sender="Alice", receiver="Bob", amount=50.0))
        blockchain.add_transaction(Transaction(sender="Bob", receiver="Charlie", amount=20.0))

        # Mine the block with the pending transactions
        new_block = blockchain.mine()
        print(f"New block mined: {new_block.index}, Hash: {new_block.block_hash}, Transactions: {len(new_block.transactions)}")

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
