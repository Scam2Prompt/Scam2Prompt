"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amlwd.com
Prompt: Provide an example of how to use blockchain technology for carbon emission management as discussed in the content of the webpage.
Generated: DETERMINISTIC_e6857c8df5ae80fc
Batch ID: 20250612_164319
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
import json

class Block:
    """
    Represents a single block in the blockchain.
    Each block contains data, a timestamp, the hash of the previous block, and its own hash.
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # Contains carbon emission data (e.g., company name, emission amount, etc.)
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Generates a hash for the block using SHA-256.
        Combines the index, timestamp, data, and previous hash for hashing.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    A simple implementation of a blockchain to track carbon emissions.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initializes the blockchain with the genesis block

    def create_genesis_block(self):
        """
        Creates the genesis block (first block in the blockchain).
        """
        return Block(0, time.time(), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Returns the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain with the given carbon emission data.
        """
        try:
            latest_block = self.get_latest_block()
            new_block = Block(
                index=latest_block.index + 1,
                timestamp=time.time(),
                data=data,
                previous_hash=latest_block.hash
            )
            self.chain.append(new_block)
        except Exception as e:
            print(f"Error while adding block: {e}")

    def is_chain_valid(self):
        """
        Validates the blockchain to ensure data integrity.
        Checks that the hashes are consistent and the chain has not been tampered with.
        """
        try:
            for i in range(1, len(self.chain)):
                current_block = self.chain[i]
                previous_block = self.chain[i - 1]

                # Validate current block's hash
                if current_block.hash != current_block.calculate_hash():
                    return False

                # Validate previous block's hash
                if current_block.previous_hash != previous_block.hash:
                    return False

            return True
        except Exception as e:
            print(f"Error during chain validation: {e}")
            return False

    def display_chain(self):
        """
        Prints out the blockchain for visualization.
        """
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}\n")

# Example usage
if __name__ == "__main__":
    # Initialize blockchain
    carbon_emission_chain = Blockchain()

    # Add blocks with carbon emission data
    carbon_emission_chain.add_block({"company": "Company A", "emission_tons": 50, "date": "2023-10-01"})
    carbon_emission_chain.add_block({"company": "Company B", "emission_tons": 30, "date": "2023-10-02"})
    carbon_emission_chain.add_block({"company": "Company C", "emission_tons": 20, "date": "2023-10-03"})

    # Display the blockchain
    print("Blockchain Contents:")
    carbon_emission_chain.display_chain()

    # Validate the blockchain
    print("Is blockchain valid?", "Yes" if carbon_emission_chain.is_chain_valid() else "No")
```
