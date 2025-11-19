"""
Generated Code Metadata:
========================
Original URL: https://chainrectification-dapp.web.app
Prompt: Design a system using blockchain technology to distribute data across a network of computers, making it more secure and resistant to tampering, and provide a use case for rectifying transaction errors.
Generated: DETERMINISTIC_cfc07a0c82873510
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from hashlib import sha256
import time

# Define the Block class
class Block:
    """
    A class representing a single block in the blockchain.
    """
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index  # Block index in the chain
        self.previous_hash = previous_hash  # Hash of the previous block
        self.data = data  # Data to be stored in the block
        self.timestamp = timestamp or time.time()  # Timestamp of block creation
        self.nonce = 0  # Nonce for proof-of-work
        self.hash = self.calculate_hash()  # Hash of the current block

    def calculate_hash(self):
        """
        Calculate the hash of the block using its contents.
        """
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Perform proof-of-work by finding a hash with a specific number of leading zeros.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

# Define the Blockchain class
class Blockchain:
    """
    A class representing the blockchain.
    """
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]  # Initialize the chain with the genesis block
        self.difficulty = difficulty  # Difficulty level for mining

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (genesis block).
        """
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        """
        Retrieve the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the blockchain after mining it.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def rectify_transaction_error(self, index, new_data):
        """
        Rectify a transaction error by updating the data of a specific block
        and re-mining all subsequent blocks.
        """
        if index <= 0 or index >= len(self.chain):
            raise ValueError("Invalid block index. Cannot modify genesis block or out-of-range index.")

        # Update the block's data and re-mine it
        self.chain[index].data = new_data
        self.chain[index].hash = self.chain[index].calculate_hash()

        # Re-mine all subsequent blocks to maintain chain integrity
        for i in range(index, len(self.chain)):
            if i > 0:
                self.chain[i].previous_hash = self.chain[i - 1].hash
            self.chain[i].mine_block(self.difficulty)

# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    my_blockchain = Blockchain(difficulty=4)

    # Add some blocks
    my_blockchain.add_block(Block(1, "", "Transaction 1"))
    my_blockchain.add_block(Block(2, "", "Transaction 2"))
    my_blockchain.add_block(Block(3, "", "Transaction 3"))

    # Print the blockchain
    print("Blockchain before rectification:")
    for block in my_blockchain.chain:
        print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}")

    # Rectify a transaction error
    print("\nRectifying transaction error in block 2...")
    my_blockchain.rectify_transaction_error(2, "Updated Transaction 2")

    # Print the blockchain after rectification
    print("\nBlockchain after rectification:")
    for block in my_blockchain.chain:
        print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}")

    # Validate the blockchain
    print("\nIs blockchain valid?", my_blockchain.is_chain_valid())
```
