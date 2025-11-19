"""
Generated Code Metadata:
========================
Original URL: https://blockdag-presalesclaim.pages.dev
Prompt: Provide a Python implementation of a Directed Acyclic Graph (DAG) structure suitable for an offchain Proof of Work (PoW) blockchain, as described in BlockDAG's Dev Release 36.
Generated: DETERMINISTIC_836af3aa9d286f2e
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
import hashlib

class Block:
    """Represents a block in the DAG."""
    
    def __init__(self, 
                 block_id: str, 
                 parent_ids: List[str], 
                 timestamp: int, 
                 data: str):
        """
        Initializes a new block.

        Args:
        block_id (str): Unique identifier for the block.
        parent_ids (List[str]): List of parent block IDs.
        timestamp (int): Timestamp of the block.
        data (str): Data stored in the block.
        """
        self.block_id = block_id
        self.parent_ids = parent_ids
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculates the hash of the block."""
        data_string = str(self.block_id) + str(self.parent_ids) + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class DAG:
    """Represents a Directed Acyclic Graph (DAG) structure."""
    
    def __init__(self):
        """Initializes an empty DAG."""
        self.blocks: Dict[str, Block] = {}

    def add_block(self, block: Block) -> None:
        """
        Adds a new block to the DAG.

        Args:
        block (Block): The block to add.

        Raises:
        ValueError: If a block with the same ID already exists.
        """
        if block.block_id in self.blocks:
            raise ValueError("Block with the same ID already exists.")
        self.blocks[block.block_id] = block

    def get_block(self, block_id: str) -> Block:
        """
        Retrieves a block by its ID.

        Args:
        block_id (str): The ID of the block to retrieve.

        Returns:
        Block: The block with the given ID.

        Raises:
        KeyError: If the block does not exist.
        """
        try:
            return self.blocks[block_id]
        except KeyError:
            raise KeyError("Block does not exist.")

    def is_valid(self, block: Block) -> bool:
        """
        Checks if a block is valid.

        Args:
        block (Block): The block to check.

        Returns:
        bool: True if the block is valid, False otherwise.
        """
        # Check if all parent blocks exist in the DAG
        for parent_id in block.parent_ids:
            if parent_id not in self.blocks:
                return False
        return True

    def topological_sort(self) -> List[Block]:
        """
        Performs a topological sort on the DAG.

        Returns:
        List[Block]: A list of blocks in topological order.

        Raises:
        ValueError: If the DAG contains a cycle.
        """
        visited = set()
        ordering = []

        def dfs(block_id: str) -> None:
            if block_id in visited:
                if block_id in ordering:
                    raise ValueError("DAG contains a cycle.")
                return
            visited.add(block_id)
            block = self.blocks[block_id]
            for parent_id in block.parent_ids:
                dfs(parent_id)
            ordering.append(block_id)

        for block_id in self.blocks:
            if block_id not in visited:
                dfs(block_id)

        return [self.blocks[block_id] for block_id in ordering]


def main() -> None:
    # Example usage
    dag = DAG()

    block1 = Block("block1", [], 1643723400, "Transaction 1")
    block2 = Block("block2", ["block1"], 1643723410, "Transaction 2")
    block3 = Block("block3", ["block1"], 1643723420, "Transaction 3")
    block4 = Block("block4", ["block2", "block3"], 1643723430, "Transaction 4")

    dag.add_block(block1)
    dag.add_block(block2)
    dag.add_block(block3)
    dag.add_block(block4)

    try:
        sorted_blocks = dag.topological_sort()
        for block in sorted_blocks:
            print(f"Block {block.block_id} - Hash: {block.hash}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
