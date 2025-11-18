"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantomwallet.io
Prompt: Develop code to implement a directed acyclic graph (DAG) structure for recording event blocks in a Fantom blockchain node.
Generated: DETERMINISTIC_fde8feb882f49313
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EventBlock:
    """
    Class representing an event block in the DAG structure.
    Each event block contains a unique ID, a timestamp, and a list of parent blocks.
    """
    
    def __init__(self, block_id, timestamp, parents=None):
        if parents is None:
            parents = []

        self.block_id = block_id
        self.timestamp = timestamp
        self.parents = parents  # List of parent EventBlocks

    def add_parent(self, parent_block):
        """
        Add a parent block.
        :param parent_block: EventBlock instance to be added as a parent.
        """
        if not isinstance(parent_block, EventBlock):
            raise ValueError("Parent must be an instance of EventBlock")
        self.parents.append(parent_block)

    def __repr__(self):
        return f"EventBlock(block_id={self.block_id}, timestamp={self.timestamp}, parents={[p.block_id for p in self.parents]})"


class DAG:
    """
    Class representing a Directed Acyclic Graph (DAG) for event blocks.
    It manages event blocks and ensures the acyclic property of the graph.
    """
    
    def __init__(self):
        self.blocks = {}  # Dictionary to hold blocks by their ID

    def add_block(self, block):
        """
        Add a new event block to the DAG.
        :param block: EventBlock instance to be added.
        :raises ValueError: If the block ID already exists.
        """
        if block.block_id in self.blocks:
            raise ValueError(f"Block ID {block.block_id} already exists in the DAG.")
        
        # Check for cycles
        if self._causes_cycle(block):
            raise ValueError("Adding this block would create a cycle in the DAG.")

        self.blocks[block.block_id] = block

    def _causes_cycle(self, new_block):
        """
        Check if adding a new block would cause a cycle in the DAG.
        :param new_block: The EventBlock to check for potential cycles.
        :return: True if adding the block would create a cycle, False otherwise.
        """
        visited = set()

        def visit(block):
            if block.block_id in visited:
                return True  # Cycle detected
            visited.add(block.block_id)
            for parent in block.parents:
                if visit(parent):
                    return True
            visited.remove(block.block_id)
            return False

        return visit(new_block)

    def __repr__(self):
        return f"DAG(blocks={[str(block) for block in self.blocks.values()]})"


# Example Usage
if __name__ == "__main__":
    try:
        dag = DAG()
        
        # Create event blocks
        block1 = EventBlock(block_id="1", timestamp="2023-10-01T00:00:00Z")
        block2 = EventBlock(block_id="2", timestamp="2023-10-01T01:00:00Z", parents=[block1])
        block3 = EventBlock(block_id="3", timestamp="2023-10-01T02:00:00Z", parents=[block1, block2])
        
        # Add blocks to the DAG
        dag.add_block(block1)
        dag.add_block(block2)
        dag.add_block(block3)

        print(dag)

    except ValueError as e:
        print(f"Error: {e}")
```
