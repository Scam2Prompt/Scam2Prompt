"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.androidwidget.com
Prompt: Develop a blockchain-based solution for secure logistics and green transportation, referencing the SHEIN case study mentioned on the Tornado Cash site.
Generated: DETERMINISTIC_261e183e16562572
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from hashlib import sha256
import json
import time

class Block:
    """Class representing a block in the blockchain."""
    
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index  # Block index
        self.previous_hash = previous_hash  # Hash of the previous block
        self.timestamp = timestamp  # Timestamp of block creation
        self.data = data  # Data contained in the block
        self.nonce = nonce  # Nonce for proof of work

    def compute_hash(self):
        """Compute the SHA-256 hash of the block."""
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return sha256(block_string).hexdigest()


class Blockchain:
    """Class representing the blockchain."""

    def __init__(self):
        self.chain = []  # List to hold the blockchain
        self.create_block(nonce=0, previous_hash='0')  # Create the genesis block

    def create_block(self, nonce, previous_hash):
        """Create a new block and add it to the chain."""
        block = Block(len(self.chain), previous_hash, time.time(), "Logistics and Transportation Data", nonce)
        self.chain.append(block)
        return block

    def get_latest_block(self):
        """Get the latest block in the blockchain."""
        return self.chain[-1]

    def proof_of_work(self, previous_nonce):
        """Simple proof of work algorithm."""
        nonce = 0
        while not self.valid_proof(previous_nonce, nonce):
            nonce += 1
        return nonce

    @staticmethod
    def valid_proof(previous_nonce, nonce, difficulty=2):
        """Validate the proof of work by checking the hash prefix."""
        guess = f'{previous_nonce}{nonce}'.encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:difficulty] == "0" * difficulty

    def add_transaction(self, transaction):
        """Add a transaction to the blockchain."""
        self.create_block(nonce=self.proof_of_work(self.get_latest_block().nonce), previous_hash=self.get_latest_block().compute_hash())

# Example usage of the Blockchain class
if __name__ == "__main__":
    try:
        # Create a new blockchain instance
        blockchain = Blockchain()
        
        # Simulate adding a transaction
        transaction_data = {
            "sender": "SenderAddress",
            "recipient": "RecipientAddress",
            "amount": 100
        }
        
        blockchain.add_transaction(transaction_data)

        # Print the blockchain
        for block in blockchain.chain:
            print(f'Block {block.index} Hash: {block.compute_hash()}')
            print(f'Block Data: {block.data}')

    except Exception as e:
        print(f"An error occurred: {e}")
```
