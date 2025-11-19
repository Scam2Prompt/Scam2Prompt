"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Explain the concept of a distributed ledger in the context of blockchain, including its benefits and how it works.
Generated: DETERMINISTIC_8b344e8ce6b81963
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Distributed Ledger and Blockchain Explanation

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


class Blockchain:
    """Represents a blockchain."""
    
    def __init__(self):
        """
        Initializes a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the genesis block.

        Returns:
            Block: The genesis block.
        """
        return Block(0, "0", 1643723400, "Genesis Block")

    def get_latest_block(self):
        """
        Gets the latest block in the chain.

        Returns:
            Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the chain.

        Args:
            new_block (Block): The new block to add.

        Raises:
            ValueError: If the new block is not valid.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        if new_block.hash != new_block.calculate_hash():
            raise ValueError("Invalid block")
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Checks if the chain is valid.

        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


def main():
    try:
        blockchain = Blockchain()
        blockchain.add_block(Block(1, blockchain.get_latest_block().hash, 1643723401, "Transaction 1"))
        blockchain.add_block(Block(2, blockchain.get_latest_block().hash, 1643723402, "Transaction 2"))

        print("Blockchain valid:", blockchain.is_chain_valid())

        # Attempt to tamper with the blockchain
        blockchain.chain[1].data = "Tampered transaction"
        print("Blockchain valid after tampering:", blockchain.is_chain_valid())

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
