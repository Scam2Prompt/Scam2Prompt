"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Summarize the role of 'blocks' and 'hashes' in blockchain security and provide a code example that simulates a basic blockchain structure.
Generated: DETERMINISTIC_b71fbff8ea8f168b
Batch ID: 20250612_163924
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
    Each block contains essential data, including its hash, previous block's hash, timestamp, and other information.
    """
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index  # Position of the block in the chain
        self.previous_hash = previous_hash  # Hash of the previous block
        self.data = data  # Data stored in the block (e.g., transactions)
        self.timestamp = timestamp or time.time()  # Time when the block is created
        self.hash = self.calculate_hash()  # Hash of the current block
    
    def calculate_hash(self):
        """
        Generate a hash for the block using its properties.
        The hash ensures data integrity and links the block to the previous one.
        """
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    Represents the entire blockchain structure.
    The blockchain is a linked list of blocks, with each block pointing to the previous one via its hash.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize the chain with the genesis block
    
    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the genesis block.
        """
        return Block(index=0, previous_hash="0", data="Genesis Block", timestamp=time.time())
    
    def get_latest_block(self):
        """
        Retrieves the most recent block in the blockchain.
        """
        return self.chain[-1]
    
    def add_block(self, new_data):
        """
        Adds a new block to the blockchain with the provided data.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            data=new_data,
            timestamp=time.time()
        )
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        Ensures that hashes and previous_hash values are consistent and correct.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Validate the current block's hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has been tampered with!")
                return False
            
            # Validate the hash chain
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} is not linked correctly to the previous block!")
                return False
        
        return True

# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    my_blockchain = Blockchain()
    
    # Add some blocks with data
    my_blockchain.add_block("First transaction data")
    my_blockchain.add_block("Second transaction data")
    my_blockchain.add_block("Third transaction data")
    
    # Print the blockchain
    for block in my_blockchain.chain:
        print(f"Block {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Data: {block.data}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Hash: {block.hash}")
        print("-" * 30)
    
    # Validate the blockchain
    print("Is blockchain valid?", my_blockchain.is_chain_valid())
```
