"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsblifi.net
Prompt: How can Base Bridge's speed and security features be leveraged in a blockchain-based payment system? Provide a code example.
Generated: DETERMINISTIC_81be89bb66c85908
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from time import time
from typing import List, Dict, Any

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float):
        """
        Initialize a transaction with sender, recipient, and amount.
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Block:
    def __init__(self, index: int, timestamp: float, transactions: List[Transaction], previous_hash: str):
        """
        Initialize a block with an index, timestamp, transactions, and previous hash.
        """
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block and an empty list of transactions.
        """
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        self.create_block(previous_hash='1')  # Create the genesis block

    def create_block(self, previous_hash: str) -> Block:
        """
        Create a new block in the blockchain.
        """
        block = Block(index=len(self.chain) + 1, 
                      timestamp=time(), 
                      transactions=self.current_transactions, 
                      previous_hash=previous_hash)
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Add a transaction to the list of current transactions.
        """
        try:
            if amount <= 0:
                raise ValueError("Transaction amount must be positive")
            transaction = Transaction(sender, recipient, amount)
            self.current_transactions.append(transaction)
            return self.last_block.index + 1  # Return the index of the block that will hold this transaction
        except Exception as e:
            print(f"Error adding transaction: {e}")
            return -1

    @property
    def last_block(self) -> Block:
        """
        Return the last block in the blockchain.
        """
        return self.chain[-1]

# Example usage of the Blockchain class:
if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Add transactions
    blockchain.add_transaction(sender="Alice", recipient="Bob", amount=50.0)
    blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=25.0)

    # Create a new block to include the transactions
    blockchain.create_block(previous_hash=blockchain.last_block.hash)

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} Hash: {block.hash}")
        for tx in block.transactions:
            print(f"  Transaction: {tx.sender} -> {tx.recipient} : {tx.amount}")
```
