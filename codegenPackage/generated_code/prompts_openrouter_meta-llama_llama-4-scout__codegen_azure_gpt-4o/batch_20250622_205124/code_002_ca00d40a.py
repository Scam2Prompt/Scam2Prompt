"""
Generated Code Metadata:
========================
Original URL: https://amlwd.com
Prompt: Design a simple blockchain-based system for carbon emission governance, incorporating features for trust establishment, value representation, and trust transfer.
Generated: DETERMINISTIC_ca00d40a247fb073
Batch ID: 20250622_205124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import json


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains:
    - Index: Position in the chain
    - Timestamp: Time of creation
    - Data: Carbon emission data
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
        Includes index, timestamp, data, and previous hash.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Provides methods for adding blocks, validating the chain, and transferring trust.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (Genesis Block).
        """
        return Block(0, time.time(), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain by checking hashes and previous hash links.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def transfer_trust(self, sender, receiver, value):
        """
        Simulates trust transfer between entities.
        Adds a block representing the trust transfer.
        """
        trust_data = {
            "sender": sender,
            "receiver": receiver,
            "value": value,
            "timestamp": time.time(),
        }
        self.add_block(trust_data)


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    carbon_chain = Blockchain()

    # Add a block representing carbon emission data
    carbon_chain.add_block({"entity": "Factory A", "emissions": 100, "unit": "tons"})

    # Transfer trust between entities
    carbon_chain.transfer_trust("Factory A", "Factory B", 50)

    # Validate the blockchain
    print("Is blockchain valid?", carbon_chain.is_chain_valid())

    # Print the blockchain
    for block in carbon_chain.chain:
        print(f"Block {block.index}: {block.data}")
```
