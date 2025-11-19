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
import json
from time import time
from typing import List, Dict


class Block:
    """
    Class to represent a single block in the blockchain.
    """

    def __init__(self, index: int, timestamp: float, data: dict, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using SHA-256.
        :return: The calculated hash as a hexadecimal string.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """
    Class to represent the blockchain.
    """

    def __init__(self):
        self.chain: List[Block] = []
        self.create_block(previous_hash='0')  # Create the genesis block

    def create_block(self, data: dict, previous_hash: str) -> Block:
        """
        Creates a new block and adds it to the chain.
        :param data: The data to be stored in the block (e.g., carbon emission data).
        :param previous_hash: The hash of the previous block.
        :return: The newly created block.
        """
        index = len(self.chain) + 1
        timestamp = time()
        block = Block(index, timestamp, data, previous_hash)
        self.chain.append(block)
        return block

    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the chain.
        :return: The latest Block object.
        """
        return self.chain[-1]

    def validate_chain(self) -> bool:
        """
        Validates the entire blockchain by ensuring hashes are correct.
        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the current block is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash is correct
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Example usage of the Blockchain class for carbon emission management
def main():
    # Initialize the blockchain for carbon emissions
    carbon_blockchain = Blockchain()

    try:
        # Example data for carbon emissions
        emission_data = {
            'company_id': 'XYZ123',
            'timestamp': time(),
            'emission_amount': 150.5,  # Example: 150.5 tons of CO2
            'verified': True
        }

        # Create a new block with the carbon emission data
        carbon_blockchain.create_block(data=emission_data, previous_hash=carbon_blockchain.get_latest_block().hash)

        # Validate the blockchain
        is_valid = carbon_blockchain.validate_chain()
        print(f"Blockchain is valid: {is_valid}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
