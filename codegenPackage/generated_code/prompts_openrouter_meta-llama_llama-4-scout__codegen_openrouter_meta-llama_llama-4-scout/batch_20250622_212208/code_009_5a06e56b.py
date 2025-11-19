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
# blockchain_union_chain.py

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index, previous_hash, timestamp, data):
        """
        Initializes a new block.

        Args:
            index (int): The index of the block in the chain.
            previous_hash (str): The hash of the previous block.
            timestamp (float): The timestamp of the block.
            data (str): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block.

        Returns:
            str: The hash of the block.
        """
        import hashlib
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data
        return hashlib.sha256(data_string.encode()).hexdigest()


class UnionChain:
    """Represents a union chain (alliance chain) in blockchain technology."""
    
    def __init__(self):
        """
        Initializes a new union chain.
        """
        self.chain = [self.create_genesis_block()]
        self.participants = {}

    def create_genesis_block(self):
        """
        Creates the genesis block of the chain.

        Returns:
            Block: The genesis block.
        """
        return Block(0, "0", 1643723400, "Genesis Block")

    def add_block(self, new_block):
        """
        Adds a new block to the chain.

        Args:
            new_block (Block): The new block to add.

        Raises:
            ValueError: If the new block is not valid.
        """
        if new_block.index == len(self.chain):
            new_block.previous_hash = self.chain[-1].hash
            new_block.hash = new_block.calculate_hash()
            self.chain.append(new_block)
        else:
            raise ValueError("Invalid block")

    def add_participant(self, name, node_id):
        """
        Adds a participant to the union chain.

        Args:
            name (str): The name of the participant.
            node_id (str): The node ID of the participant.
        """
        self.participants[name] = node_id

    def get_chain(self):
        """
        Gets the current state of the chain.

        Returns:
            list: The list of blocks in the chain.
        """
        return self.chain

    def get_participants(self):
        """
        Gets the participants in the union chain.

        Returns:
            dict: A dictionary of participants.
        """
        return self.participants


def main():
    # Create a new union chain
    union_chain = UnionChain()

    # Add participants
    union_chain.add_participant("Node 1", "node1")
    union_chain.add_participant("Node 2", "node2")

    # Create and add new blocks
    new_block1 = Block(1, union_chain.get_chain()[-1].hash, 1643723401, "Transaction 1")
    union_chain.add_block(new_block1)

    new_block2 = Block(2, union_chain.get_chain()[-1].hash, 1643723402, "Transaction 2")
    union_chain.add_block(new_block2)

    # Print the current state of the chain
    print("Union Chain:")
    for block in union_chain.get_chain():
        print(f"Block {block.index} - Hash: {block.hash}")

    # Print the participants
    print("\nParticipants:")
    for name, node_id in union_chain.get_participants().items():
        print(f"{name}: {node_id}")


if __name__ == "__main__":
    main()
```
