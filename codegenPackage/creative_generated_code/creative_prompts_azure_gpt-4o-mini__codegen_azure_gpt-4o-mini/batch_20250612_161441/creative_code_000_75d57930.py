"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resourcesdapps.pages.dev
Prompt: How can I use blockchain rectification techniques to resolve crypto-related issues effectively?
Generated: DETERMINISTIC_75d57930d3343942
Batch ID: 20250612_161441
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

class Blockchain:
    def __init__(self):
        """Initialize the blockchain and create the genesis block."""
        self.chain = []
        self.current_transactions = []
        
        # Create the genesis block
        self.new_block(previous_hash='1', nonce=100)

    def new_block(self, nonce, previous_hash=None):
        """Create a new block in the Blockchain.

        :param nonce: The proof of work for the block.
        :param previous_hash: Hash of the previous block.
        :return: New Block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        # Reset the current list of transactions
        self.current_transactions = []
        
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Add a new transaction to the list of transactions.

        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param amount: Amount to be transferred.
        :return: The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Create a SHA-256 hash of a Block.

        :param block: Block to be hashed.
        :return: Hash of the block.
        """
        # Convert the block to a JSON string
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the blockchain."""
        return self.chain[-1]

    def validate_chain(self):
        """Validate the blockchain to ensure integrity.

        :return: True if valid, False otherwise.
        """
        # Check all blocks in the chain
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            prev_block = self.chain[i - 1]

            # Check if the previous hash is correct
            if block['previous_hash'] != self.hash(prev_block):
                return False

            # Check if the hash of the block is correct
            block_data = block.copy()
            block_data.pop('hash', None)  # Remove hash for validation
            if block['hash'] != self.hash(block_data):
                return False

        return True

if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Create some transactions
    blockchain.new_transaction("Alice", "Bob", 50)
    blockchain.new_transaction("Bob", "Charlie", 25)
    
    # Create a new block with proof of work
    new_block = blockchain.new_block(nonce=12345)
    
    # Validate the blockchain
    if blockchain.validate_chain():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")

    # Print the blockchain
    print(json.dumps(blockchain.chain, indent=4))
```
