"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdag---networks.pages.dev
Prompt: Explain the mechanics of the BlockDAG consensus mechanism and how it differs from traditional blockchain technologies as outlined on the BlockDAG Network site.
Generated: DETERMINISTIC_023c94636a4377e1
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Block:
    """
    Class representing a single block in a BlockDAG.
    Each block contains a unique identifier, a list of parent blocks,
    and a payload of data.
    """

    def __init__(self, block_id, parents, data):
        """
        Initialize a new Block.

        :param block_id: Unique identifier for the block
        :param parents: List of parent block identifiers
        :param data: Data payload contained in the block
        """
        self.block_id = block_id
        self.parents = parents
        self.data = data

    def __repr__(self):
        return f"Block(id={self.block_id}, parents={self.parents})"


class BlockDAG:
    """
    Class representing a BlockDAG structure.
    The BlockDAG allows multiple blocks to be created in parallel.
    """

    def __init__(self):
        """
        Initialize a new BlockDAG with an empty set of blocks.
        """
        self.blocks = {}

    def add_block(self, block_id, parents, data):
        """
        Add a new block to the BlockDAG.

        :param block_id: Unique identifier for the block
        :param parents: List of parent block identifiers
        :param data: Data payload contained in the block
        :raises ValueError: If the block already exists or parents do not exist
        """
        if block_id in self.blocks:
            raise ValueError(f"Block {block_id} already exists.")
        
        # Check if all parent blocks exist
        for parent in parents:
            if parent not in self.blocks:
                raise ValueError(f"Parent block {parent} does not exist.")

        # Create and store the new block
        new_block = Block(block_id, parents, data)
        self.blocks[block_id] = new_block

    def get_block(self, block_id):
        """
        Retrieve a block by its identifier.

        :param block_id: Unique identifier for the block
        :returns: Block object if found, otherwise None
        """
        return self.blocks.get(block_id)

    def display_structure(self):
        """
        Display the structure of the BlockDAG for debugging purposes.
        """
        for block_id, block in self.blocks.items():
            print(f"Block ID: {block_id}, Parents: {block.parents}, Data: {block.data}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize BlockDAG
        block_dag = BlockDAG()

        # Add blocks to the BlockDAG
        block_dag.add_block("block1", [], "Genesis Block")
        block_dag.add_block("block2", ["block1"], "Second Block")
        block_dag.add_block("block3", ["block1"], "Third Block")
        block_dag.add_block("block4", ["block2", "block3"], "Fourth Block")

        # Display the BlockDAG structure
        block_dag.display_structure()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
