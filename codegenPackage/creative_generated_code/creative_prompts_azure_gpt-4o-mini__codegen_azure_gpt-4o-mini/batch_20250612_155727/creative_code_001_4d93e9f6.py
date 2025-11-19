"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-ag.github.io
Prompt: Generate a code snippet that demonstrates how to integrate sustainability initiatives into a blockchain application, inspired by Meteora Crypto's approach to minimizing carbon footprint.
Generated: DETERMINISTIC_4d93e9f6516466c6
Batch ID: 20250612_155727
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
from datetime import datetime


class Block:
    """Class representing a block in the blockchain."""

    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce

    def compute_hash(self):
        """Compute the SHA-256 hash of the block."""
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """Class representing the blockchain."""

    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, nonce, previous_hash=None):
        """Create a new block and add it to the chain."""
        index = len(self.chain) + 1
        timestamp = str(datetime.now())
        block = Block(index, previous_hash or self.chain[-1].compute_hash(), timestamp, data=None, nonce=nonce)
        self.chain.append(block)
        return block

    def get_last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

    def add_sustainability_initiative(self, initiative):
        """Add a sustainability initiative to the blockchain."""
        last_block = self.get_last_block()
        nonce = self.proof_of_work(last_block)
        
        # Create a block with the sustainability initiative data
        block_data = {
            'initiative': initiative,
            'effort': 'Reduce carbon footprint',
            'timestamp': str(datetime.now())
        }
        
        new_block = self.create_block(nonce, last_block.compute_hash())
        new_block.data = block_data
        
        return new_block

    def proof_of_work(self, last_block):
        """Simple proof of work algorithm that finds a nonce."""
        nonce = 0
        while not self.valid_proof(last_block, nonce):
            nonce += 1
        return nonce

    @staticmethod
    def valid_proof(last_block, nonce):
        """Validates the proof of work by checking the hash of the block."""
        guess = f'{last_block.compute_hash()}{nonce}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Example difficulty


# Example usage of the Blockchain with sustainability initiatives

def main():
    try:
        # Initialize blockchain
        my_blockchain = Blockchain()
        
        # Add sustainability initiatives
        initiative_1 = "Planting trees in urban areas"
        block_1 = my_blockchain.add_sustainability_initiative(initiative_1)
        print(f"Added Block: {block_1.index} with data: {block_1.data}")

        initiative_2 = "Recycling programs in schools"
        block_2 = my_blockchain.add_sustainability_initiative(initiative_2)
        print(f"Added Block: {block_2.index} with data: {block_2.data}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
```
