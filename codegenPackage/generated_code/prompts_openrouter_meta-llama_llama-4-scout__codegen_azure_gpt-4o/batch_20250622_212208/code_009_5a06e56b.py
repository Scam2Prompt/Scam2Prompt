"""
Generated Code Metadata:
========================
Original URL: https://geokukt.cn
Prompt: Describe the architecture and benefits of a union chain (alliance chain) in the context of blockchain technology, and propose a use case for such a chain in a specific industry.
Generated: DETERMINISTIC_5a06e56b8b16654f
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Union Chain (Alliance Chain) Architecture and Use Case

This script provides a high-level implementation of a union chain in the context of blockchain technology.
A union chain is a permissioned blockchain where multiple organizations collaborate, sharing control and governance.
The script demonstrates a simplified architecture and a use case for the supply chain industry.

Key Features:
- Permissioned access
- Shared governance
- Transparency and immutability
- Efficient consensus mechanism
"""

import hashlib
import json
from datetime import datetime


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains:
    - Index: Position in the chain
    - Timestamp: Time of creation
    - Data: Transaction or record details
    - Previous Hash: Hash of the previous block
    - Hash: Current block's hash
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        Combines index, timestamp, data, and previous hash for hashing.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class UnionChain:
    """
    Represents the union chain (alliance chain).
    - Permissioned blockchain with shared governance.
    - Includes methods for adding blocks and validating the chain.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the chain (Genesis Block).
        """
        return Block(0, str(datetime.now()), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the chain.
        - Validates the previous hash.
        - Ensures immutability.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.now()),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        - Ensures hashes match and blocks are linked correctly.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate previous hash linkage
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Example Use Case: Supply Chain Management
def supply_chain_demo():
    """
    Demonstrates the use of a union chain in the supply chain industry.
    - Tracks product movement across multiple organizations.
    - Ensures transparency and accountability.
    """
    print("Initializing Union Chain for Supply Chain Management...")
    supply_chain = UnionChain()

    # Adding blocks representing product movement
    supply_chain.add_block({"product_id": "12345", "location": "Factory", "status": "Manufactured"})
    supply_chain.add_block({"product_id": "12345", "location": "Warehouse", "status": "Stored"})
    supply_chain.add_block({"product_id": "12345", "location": "Retail Store", "status": "Available for Sale"})

    # Display the blockchain
    print("\nBlockchain:")
    for block in supply_chain.chain:
        print(f"Index: {block.index}, Timestamp: {block.timestamp}, Data: {block.data}, Hash: {block.hash}")

    # Validate the blockchain
    print("\nValidating Blockchain Integrity...")
    if supply_chain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain integrity compromised!")


# Run the supply chain demo
if __name__ == "__main__":
    supply_chain_demo()
```
