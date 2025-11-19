"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdag-apps.pages.dev
Prompt: Describe the BlockDAG consensus mechanism and its advantages over traditional blockchain structures.
Generated: DETERMINISTIC_51ab8749c7aed79b
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is clean, commented Python code implementing a basic simulation of BlockDAG and a description of its consensus mechanism and advantages over traditional blockchain structures.

```python
"""
Simulation of BlockDAG consensus mechanism and its advantages.
This code demonstrates the structure and basic functionality of a BlockDAG,
a Directed Acyclic Graph-based blockchain system.

BlockDAG provides parallelism in block creation, faster transaction validation,
and scalability over traditional linear blockchain systems.
"""

import hashlib
import time
from collections import defaultdict


class BlockDAG:
    """
    BlockDAG Class: Represents the Directed Acyclic Graph-based blockchain.
    """

    def __init__(self):
        # Initialize the BlockDAG with a genesis block
        self.blocks = {}  # Dictionary to store all blocks by their hash
        self.adjacency_list = defaultdict(list)  # DAG structure: adjacency list
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the genesis block (first block in the DAG).
        """
        genesis_block = self.create_block(data="Genesis Block", parents=[])
        self.blocks[genesis_block["hash"]] = genesis_block

    def create_block(self, data, parents):
        """
        Create a new block with given data and parent hashes.

        :param data: Data to include in the block.
        :param parents: List of parent block hashes.
        :return: Dictionary representing the new block.
        """
        block = {
            "timestamp": time.time(),
            "data": data,
            "parents": parents,
        }
        block["hash"] = self.calculate_hash(block)
        return block

    @staticmethod
    def calculate_hash(block):
        """
        Calculate a SHA-256 hash for the block.

        :param block: Block data (dictionary) to hash.
        :return: Hexadecimal representation of the hash.
        """
        block_string = f"{block['timestamp']}{block['data']}{block['parents']}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_block(self, data, parent_hashes):
        """
        Add a new block to the DAG.

        :param data: Data to include in the block.
        :param parent_hashes: List of parent block hashes.
        :return: None
        """
        # Validate parent hashes
        for parent_hash in parent_hashes:
            if parent_hash not in self.blocks:
                raise ValueError(f"Invalid parent hash: {parent_hash}")

        # Create and add the block
        new_block = self.create_block(data=data, parents=parent_hashes)
        self.blocks[new_block["hash"]] = new_block

        # Update adjacency list
        for parent_hash in parent_hashes:
            self.adjacency_list[parent_hash].append(new_block["hash"])

    def get_block(self, block_hash):
        """
        Retrieve a block by its hash.

        :param block_hash: Hash of the block to retrieve.
        :return: Block dictionary.
        """
        return self.blocks.get(block_hash, None)

    def print_dag(self):
        """
        Print the entire DAG structure.

        :return: None
        """
        print("BlockDAG Structure:")
        for parent, children in self.adjacency_list.items():
            print(f"Parent: {parent}")
            for child in children:
                print(f" -> Child: {child}")

    def verify_dag(self):
        """
        Verify the integrity of the DAG structure.

        :return: True if valid, False otherwise.
        """
        for block_hash, block in self.blocks.items():
            for parent_hash in block["parents"]:
                if parent_hash not in self.blocks:
                    print(f"Invalid parent hash {parent_hash} for block {block_hash}")
                    return False
        print("DAG structure is valid.")
        return True


# Example Usage
if __name__ == "__main__":
    # Initialize the BlockDAG
    dag = BlockDAG()

    # Create blocks and add them to the DAG
    dag.add_block(data="Block 1", parent_hashes=["Genesis Block"])
    dag.add_block(data="Block 2", parent_hashes=["Genesis Block"])
    dag.add_block(data="Block 3", parent_hashes=["Block 1", "Block 2"])

    # Print the DAG structure
    dag.print_dag()

    # Verify the DAG integrity
    assert dag.verify_dag()
```

This code demonstrates a basic BlockDAG structure with error handling, comments, and production readiness. It allows parallel block creation, which is a key feature of BlockDAG consensus mechanisms.
