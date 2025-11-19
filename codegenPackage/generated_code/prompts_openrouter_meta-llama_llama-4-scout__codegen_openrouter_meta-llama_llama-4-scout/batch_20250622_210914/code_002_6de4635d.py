"""
Generated Code Metadata:
========================
Original URL: https://claimamisonnetwork.pages.dev
Prompt: Design a blockchain-based protocol for standardizing infrastructure resources, similar to Meson.Network's approach, and describe its components.
Generated: DETERMINISTIC_6de4635dae6cb95c
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_protocol.py

import hashlib
import time
from typing import List

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initializes a new block.

        Args:
        - index (int): The block's index in the chain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The block's creation timestamp.
        - data (dict): The block's data.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculates the block's hash."""
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """Represents the blockchain."""
    
    def __init__(self):
        """Initializes a new blockchain."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the genesis block."""
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """Gets the latest block in the chain."""
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """Adds a new block to the chain."""
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Checks if the chain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class Resource:
    """Represents an infrastructure resource."""
    
    def __init__(self, id: str, type: str, properties: dict):
        """
        Initializes a new resource.

        Args:
        - id (str): The resource's ID.
        - type (str): The resource's type.
        - properties (dict): The resource's properties.
        """
        self.id = id
        self.type = type
        self.properties = properties


class ResourceRegistry:
    """Represents a resource registry."""
    
    def __init__(self, blockchain: Blockchain):
        """
        Initializes a new resource registry.

        Args:
        - blockchain (Blockchain): The blockchain instance.
        """
        self.blockchain = blockchain
        self.resources = {}

    def register_resource(self, resource: Resource):
        """Registers a new resource."""
        if resource.id in self.resources:
            raise ValueError("Resource already exists")
        self.resources[resource.id] = resource
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"resource_id": resource.id, "type": resource.type, "properties": resource.properties})
        self.blockchain.add_block(new_block)

    def get_resource(self, id: str) -> Resource:
        """Gets a resource by ID."""
        return self.resources.get(id)


def main():
    blockchain = Blockchain()
    registry = ResourceRegistry(blockchain)

    resource1 = Resource("R1", "compute", {"cpu": 2, "memory": 4})
    registry.register_resource(resource1)

    resource2 = Resource("R2", "storage", {"size": 100})
    registry.register_resource(resource2)

    print("Blockchain valid:", blockchain.is_chain_valid())

    retrieved_resource = registry.get_resource("R1")
    print("Retrieved resource:", retrieved_resource.__dict__)

if __name__ == "__main__":
    main()
```
