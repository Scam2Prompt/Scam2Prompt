"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchase1-blockdag-network.pages.dev
Prompt: Describe the features of the BlockDAG Network and how it differs from traditional blockchain systems.
Generated: DETERMINISTIC_900045ea44a80022
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BlockDAG:
    """
    A class representing a BlockDAG network.
    
    BlockDAG is a directed acyclic graph structure that allows for multiple blocks to be added
    at the same time, in contrast to traditional blockchains which are linear in nature.
    """

    def __init__(self):
        """
        Initializes an empty BlockDAG structure.
        """
        self.blocks = {}  # Dictionary to hold blocks, indexed by block ID
        self.edges = []   # List to hold edges (dependencies) between blocks

    def add_block(self, block_id, parent_ids):
        """
        Adds a new block to the BlockDAG.
        
        Parameters:
            block_id (str): Unique identifier for the new block.
            parent_ids (list): List of block IDs that are parents of this block.
        
        Raises:
            ValueError: If the block_id already exists or if any parent_id does not exist.
        """
        if block_id in self.blocks:
            raise ValueError(f"Block ID '{block_id}' already exists.")
        
        for parent_id in parent_ids:
            if parent_id not in self.blocks:
                raise ValueError(f"Parent block ID '{parent_id}' does not exist.")
        
        self.blocks[block_id] = {'id': block_id, 'parents': parent_ids}
        self.edges.extend((parent_id, block_id) for parent_id in parent_ids)

    def get_block(self, block_id):
        """
        Retrieves a block by its ID.
        
        Parameters:
            block_id (str): Unique identifier of the block to retrieve.
        
        Returns:
            dict: The block details if found, otherwise raises KeyError.
        
        Raises:
            KeyError: If the block_id does not exist.
        """
        if block_id not in self.blocks:
            raise KeyError(f"Block ID '{block_id}' not found.")
        
        return self.blocks[block_id]

    def get_all_blocks(self):
        """
        Returns all blocks in the BlockDAG.
        
        Returns:
            dict: All blocks stored in the BlockDAG.
        """
        return self.blocks

    def __repr__(self):
        """
        Returns a string representation of the BlockDAG.
        
        Returns:
            str: A visual representation of the BlockDAG structure.
        """
        return f"BlockDAG with {len(self.blocks)} blocks."

# Example usage
if __name__ == "__main__":
    try:
        dag = BlockDAG()
        dag.add_block("block_1", [])
        dag.add_block("block_2", ["block_1"])
        dag.add_block("block_3", ["block_1"])
        
        print(dag.get_all_blocks())
    except Exception as e:
        print(f"An error occurred: {e}")
```
