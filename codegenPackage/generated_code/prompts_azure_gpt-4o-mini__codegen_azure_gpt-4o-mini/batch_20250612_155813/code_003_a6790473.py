"""
Generated Code Metadata:
========================
Original URL: https://dimo-chains.pages.dev
Prompt: Explain how blockchain technology is utilized in DIMO to ensure privacy and security for connected vehicles.
Generated: DETERMINISTIC_a6790473188035f0
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime

class Block:
    """
    Represents a single block in the blockchain.
    Each block contains data, a timestamp, a hash of the previous block, and its own hash.
    """
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.utcnow().isoformat()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Provides methods to add new blocks and validate the chain.
    """
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, data, previous_hash=None):
        """
        Creates a new block and adds it to the blockchain.
        Args:
            data (dict): The data to be stored in the block.
            previous_hash (str): The hash of the previous block.
        Returns:
            Block: The newly created block.
        """
        index = len(self.chain) + 1
        block = Block(index, data, previous_hash or self.chain[-1].hash)
        self.chain.append(block)
        return block

    def get_last_block(self):
        """
        Returns the last block in the blockchain.
        Returns:
            Block: The last block in the chain.
        """
        return self.chain[-1]

    def validate_chain(self):
        """
        Validates the entire blockchain to ensure integrity.
        Returns:
            bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Check if the current block's previous hash is correct
            if current.previous_hash != previous.hash:
                return False

            # Check if the current block's hash is correct
            if current.hash != current.calculate_hash():
                return False

        return True


# Example usage
if __name__ == "__main__":
    try:
        # Create a new blockchain instance
        dimo_blockchain = Blockchain()

        # Simulate adding vehicle data to the blockchain
        vehicle_data_1 = {
            "vehicle_id": "ABC123",
            "owner": "John Doe",
            "location": "37.7749 N, 122.4194 W",
            "status": "active"
        }

        # Add the first block with vehicle data
        dimo_blockchain.create_block(data=vehicle_data_1)

        # Add another block with updated vehicle data
        vehicle_data_2 = {
            "vehicle_id": "ABC123",
            "owner": "John Doe",
            "location": "37.7749 N, 122.4194 W",
            "status": "inactive"
        }
        dimo_blockchain.create_block(data=vehicle_data_2)

        # Validate the blockchain
        if dimo_blockchain.validate_chain():
            print("Blockchain is valid.")
        else:
            print("Blockchain is invalid.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
