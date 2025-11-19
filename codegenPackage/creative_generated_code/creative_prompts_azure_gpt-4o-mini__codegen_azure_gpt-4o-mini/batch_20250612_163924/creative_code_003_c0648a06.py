"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptolinknet.com
Prompt: Create a simple application that demonstrates how blockchain technology improves transparency in supply chains, as described on CryptoLinkNet.
Generated: DETERMINISTIC_c0648a06d078c652
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Blockchain Supply Chain Transparency Example

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
    """Class to manage the blockchain."""
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, data, previous_hash=None):
        """Creates a new block in the blockchain."""
        index = len(self.chain) + 1
        timestamp = time()
        hash = self.hash_block(index, previous_hash, timestamp, data)
        block = Block(index, previous_hash, timestamp, data, hash)
        self.chain.append(block)
        return block

    def hash_block(self, index, previous_hash, timestamp, data):
        """Returns the SHA-256 hash of a block."""
        block_string = f"{index}{previous_hash}{timestamp}{data}".encode()
        return sha256(block_string).hexdigest()

    def get_chain(self):
        """Returns the entire blockchain."""
        return [block.__dict__ for block in self.chain]

def main():
    """Main function to demonstrate the blockchain supply chain."""
    # Create blockchain instance
    blockchain = Blockchain()

    # Sample supply chain data
    supply_chain_data = [
        {"item": "Laptop", "supplier": "Supplier A", "status": "Manufactured"},
        {"item": "Laptop", "supplier": "Supplier B", "status": "Shipped"},
        {"item": "Laptop", "supplier": "Supplier C", "status": "Delivered"},
    ]

    # Create blocks for each step in the supply chain
    try:
        for data in supply_chain_data:
            block = blockchain.create_block(data)
            print(f"Block {block.index} created:")
            print(block)

        # Display the full blockchain
        print("\nComplete Blockchain:")
        print(json.dumps(blockchain.get_chain(), indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
