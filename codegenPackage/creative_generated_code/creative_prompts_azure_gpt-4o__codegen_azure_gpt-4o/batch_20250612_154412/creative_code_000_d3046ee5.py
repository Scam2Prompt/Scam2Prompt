"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Write Python code to simulate a blockchain system using blocks and hashes, incorporating the principles explained on the "블록과 해시" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_d3046ee54b3c10fa
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index, previous_hash, data, timestamp=None):
        """
        Initializes a new block.
        :param index: The block's position in the chain (integer).
        :param previous_hash: Hash of the previous block in the chain (string).
        :param data: Data to store in the block (string).
        :param timestamp: Timestamp of block creation (defaults to current time).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash for the block using SHA-256.
        :return: The computed hash (string).
        """
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        """
        Returns a string representation of the block.
        """
        return (f"Block #{self.index}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash}\n")


class Blockchain:
    """
    Represents the blockchain as a collection of linked blocks.
    """
    def __init__(self):
        """
        Initializes the blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the genesis block.
        :return: The genesis block (Block).
        """
        return Block(index=0, previous_hash="0", data="Genesis Block", timestamp=time.time())
    
    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        :param data: Data to store in the new block (string).
        """
        previous_block = self.chain[-1]
        new_block = Block(index=previous_block.index + 1,
                          previous_hash=previous_block.hash,
                          data=data,
                          timestamp=time.time())
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                print(f"Block #{current_block.index} has an invalid hash.")
                return False
            
            # Check if previous hash matches
            if current_block.previous_hash != previous_block.hash:
                print(f"Block #{current_block.index} has an invalid previous hash.")
                return False
        
        return True

    def __str__(self):
        """
        Returns a string representation of the entire blockchain.
        """
        return "\n".join(str(block) for block in self.chain)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize blockchain
        blockchain = Blockchain()
        print("Blockchain initialized with Genesis Block:")
        print(blockchain)
        print("\nAdding new blocks...\n")

        # Add blocks with sample data
        blockchain.add_block("First block data")
        blockchain.add_block("Second block data")
        blockchain.add_block("Third block data")

        print(blockchain)

        # Validate blockchain integrity
        print("\nValidating blockchain integrity...")
        if blockchain.is_chain_valid():
            print("Blockchain is valid.")
        else:
            print("Blockchain is invalid.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
