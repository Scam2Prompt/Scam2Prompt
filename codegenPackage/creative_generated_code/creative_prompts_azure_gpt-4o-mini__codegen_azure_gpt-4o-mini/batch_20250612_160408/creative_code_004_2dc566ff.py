"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: How does Bitcoin function as a disintermediator of banks, and what implications does this have for financial transactions?
Generated: DETERMINISTIC_2dc566fff36ea39c
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import json
from time import time
from uuid import uuid4

class Transaction:
    """Class to represent a financial transaction."""
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Block:
    """Class to represent a block in the blockchain."""
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.hash_block()  # Automatically generate hash for the block

    def hash_block(self):
        """Creates SHA-256 hash of a block."""
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """Class to represent the blockchain."""
    def __init__(self):
        self.chain = []  # List to hold the blockchain
        self.current_transactions = []  # List to hold current transactions
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof, previous_hash):
        """Creates a new block in the blockchain."""
        block = Block(len(self.chain) + 1, self.current_transactions, time(), previous_hash)
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)  # Add the new block to the chain
        return block

    def add_transaction(self, sender, recipient, amount):
        """Adds a transaction to the list of current transactions."""
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction.__dict__)  # Store as a dictionary
        return self.last_block.index + 1  # Return the index of the block that will hold this transaction

    @property
    def last_block(self):
        """Returns the last block in the blockchain."""
        return self.chain[-1]

def main():
    """Main function to demonstrate the blockchain."""
    # Create an instance of the Blockchain
    blockchain = Blockchain()

    # Add transactions
    try:
        blockchain.add_transaction(sender="Alice", recipient="Bob", amount=50)
        blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=25)

        # Create a new block with a dummy proof and previous hash
        previous_hash = blockchain.last_block.hash
        blockchain.create_block(proof=200, previous_hash=previous_hash)

        # Print the blockchain
        for block in blockchain.chain:
            print(f'Index: {block.index}, Transactions: {block.transactions}, Hash: {block.hash}')

    except Exception as e:
        # Handle any potential errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
