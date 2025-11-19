"""
Generated Code Metadata:
========================
Original URL: https://blockdaggs.pages.dev
Prompt: Explain the mechanics of the BlockDAG proof-of-work system and its security benefits.
Generated: DETERMINISTIC_ef993e232951cead
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Block:
    """
    Represents a single block in the BlockDAG structure.
    Each block contains a unique identifier, a reference to its parent blocks,
    and a proof-of-work value.
    """
    def __init__(self, block_id, parent_ids, proof_of_work):
        self.block_id = block_id  # Unique identifier for the block
        self.parent_ids = parent_ids  # List of parent block IDs
        self.proof_of_work = proof_of_work  # Proof-of-work value

    def __repr__(self):
        return f"Block(id={self.block_id}, parents={self.parent_ids}, pow={self.proof_of_work})"


class BlockDAG:
    """
    Represents a BlockDAG structure for managing blocks in a decentralized system.
    It allows for multiple parent blocks, enhancing scalability and security.
    """
    def __init__(self):
        self.blocks = {}  # Dictionary to store blocks by their IDs

    def add_block(self, block):
        """
        Adds a new block to the BlockDAG.
        
        :param block: Block instance to be added
        :raises ValueError: If the block ID already exists
        """
        if block.block_id in self.blocks:
            raise ValueError(f"Block with ID {block.block_id} already exists.")
        self.blocks[block.block_id] = block

    def validate_block(self, block):
        """
        Validates a block's proof-of-work and its parent blocks.
        
        :param block: Block instance to be validated
        :return: True if valid, False otherwise
        """
        # Here we would implement the actual proof-of-work validation logic
        # For demonstration, we assume the proof-of-work is valid if it's a positive integer
        if block.proof_of_work <= 0:
            return False
        
        # Check if all parent blocks exist in the BlockDAG
        for parent_id in block.parent_ids:
            if parent_id not in self.blocks:
                return False
        
        return True

    def mine_block(self, parent_ids):
        """
        Simulates the mining of a new block with a proof-of-work.
        
        :param parent_ids: List of parent block IDs
        :return: Newly created Block instance
        """
        block_id = len(self.blocks) + 1  # Simple ID generation
        proof_of_work = self._generate_proof_of_work()  # Simulate proof-of-work generation
        new_block = Block(block_id, parent_ids, proof_of_work)

        if self.validate_block(new_block):
            self.add_block(new_block)
            return new_block
        else:
            raise RuntimeError("Failed to mine a valid block.")

    def _generate_proof_of_work(self):
        """
        Simulates the generation of a proof-of-work value.
        
        :return: A positive integer representing the proof-of-work
        """
        import random
        return random.randint(1, 100)  # Simulated proof-of-work value


# Example usage
if __name__ == "__main__":
    try:
        dag = BlockDAG()
        # Mining a block with no parents (genesis block)
        genesis_block = dag.mine_block([])
        print(f"Mined: {genesis_block}")

        # Mining a new block with the genesis block as a parent
        new_block = dag.mine_block([genesis_block.block_id])
        print(f"Mined: {new_block}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
