"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soonverse.pages.dev
Prompt: Provide code examples for implementing blockchain-based ownership of in-game assets, as described in the SoonVerse platform.
Generated: DETERMINISTIC_967282abe89d50e5
Batch ID: 20250612_145831
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

class Block:
    """Class representing a single block in the blockchain."""
    
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return json.dumps(self.__dict__, sort_keys=True)


class Blockchain:
    """Class representing the blockchain."""

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # Create the genesis block
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash=None):
        """Creates a new block in the blockchain."""
        block = Block(
            index=len(self.chain) + 1,
            previous_hash=previous_hash or self.hash(self.chain[-1]),
            timestamp=time(),
            data=self.current_transactions,
            hash=self.hash(proof)
        )
        self.current_transactions = []
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        """Creates a SHA-256 hash of a block."""
        block_string = json.dumps(block.__dict__, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def new_transaction(self, sender, recipient, asset_id):
        """Adds a new transaction to the list."""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'asset_id': asset_id
        })
        return self.last_block.index + 1

    @property
    def last_block(self):
        """Returns the last block in the chain."""
        return self.chain[-1]


def main():
    """Main function to run the blockchain."""
    # Initialize the blockchain
    blockchain = Blockchain()

    # Adding transactions (example)
    try:
        blockchain.new_transaction(sender="UserA", recipient="UserB", asset_id="Asset001")
        blockchain.new_transaction(sender="UserB", recipient="UserC", asset_id="Asset002")
        
        # Create a new block
        new_block = blockchain.create_block(proof=200)
        
        # Display the blockchain
        print("Blockchain:")
        for block in blockchain.chain:
            print(block)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
