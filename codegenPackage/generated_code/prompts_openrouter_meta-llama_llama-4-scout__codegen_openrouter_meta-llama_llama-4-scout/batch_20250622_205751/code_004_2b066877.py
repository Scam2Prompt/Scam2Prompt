"""
Generated Code Metadata:
========================
Original URL: https://bafkreibgcum43j7d4mubge4izowokrtbcswc6llh62jjklhh7g5bzrfd6e.ipfs.dweb.link
Prompt: "Design a basic example of a blockchain-based AI compute resource allocation system inspired by OpenGPU."
Generated: DETERMINISTIC_2b0668771435db67
Batch ID: 20250622_205751
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
from typing import List, Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict, hash: str):
        """
        Initialize a Block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (Dict): The data stored in the block.
        hash (str): The hash of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"}, self.calculate_hash(0, "0", time.time(), {"genesis": "block"}))

    def calculate_hash(self, index: int, previous_hash: str, timestamp: float, data: Dict) -> str:
        """
        Calculate the hash of a block.

        Args:
        index (int): The index of the block.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (Dict): The data stored in the block.

        Returns:
        str: The hash of the block.
        """
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

class ComputeResource:
    def __init__(self, id: str, capacity: int):
        """
        Initialize a ComputeResource.

        Args:
        id (str): The ID of the compute resource.
        capacity (int): The capacity of the compute resource.
        """
        self.id = id
        self.capacity = capacity
        self.allocated = 0

    def allocate(self, amount: int) -> bool:
        """
        Allocate compute resource.

        Args:
        amount (int): The amount to allocate.

        Returns:
        bool: True if allocation is successful, False otherwise.
        """
        if self.allocated + amount <= self.capacity:
            self.allocated += amount
            return True
        return False

    def deallocate(self, amount: int) -> bool:
        """
        Deallocate compute resource.

        Args:
        amount (int): The amount to deallocate.

        Returns:
        bool: True if deallocation is successful, False otherwise.
        """
        if self.allocated - amount >= 0:
            self.allocated -= amount
            return True
        return False

class AIComputeResourceAllocationSystem:
    def __init__(self):
        """
        Initialize an AIComputeResourceAllocationSystem.
        """
        self.blockchain = Blockchain()
        self.compute_resources: Dict[str, ComputeResource] = {}

    def add_compute_resource(self, id: str, capacity: int):
        """
        Add a compute resource.

        Args:
        id (str): The ID of the compute resource.
        capacity (int): The capacity of the compute resource.
        """
        self.compute_resources[id] = ComputeResource(id, capacity)

    def allocate_compute_resource(self, id: str, amount: int) -> bool:
        """
        Allocate a compute resource.

        Args:
        id (str): The ID of the compute resource.
        amount (int): The amount to allocate.

        Returns:
        bool: True if allocation is successful, False otherwise.
        """
        if id in self.compute_resources:
            return self.compute_resources[id].allocate(amount)
        return False

    def deallocate_compute_resource(self, id: str, amount: int) -> bool:
        """
        Deallocate a compute resource.

        Args:
        id (str): The ID of the compute resource.
        amount (int): The amount to deallocate.

        Returns:
        bool: True if deallocation is successful, False otherwise.
        """
        if id in self.compute_resources:
            return self.compute_resources[id].deallocate(amount)
        return False

    def add_block(self, data: Dict):
        """
        Add a new block to the blockchain.

        Args:
        data (Dict): The data to store in the block.
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.chain[-1].hash, time.time(), data, "")
        self.blockchain.add_block(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        return self.blockchain.is_chain_valid()

# Example usage
if __name__ == "__main__":
    system = AIComputeResourceAllocationSystem()
    system.add_compute_resource("resource1", 100)
    print(system.allocate_compute_resource("resource1", 50))  # Should print: True
    print(system.allocate_compute_resource("resource1", 60))  # Should print: False
    print(system.deallocate_compute_resource("resource1", 20))  # Should print: True
    system.add_block({"allocation": "resource1 50"})
    print(system.is_chain_valid())  # Should print: True
```
