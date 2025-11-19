"""
Generated Code Metadata:
========================
Original URL: https://cryptofitties.com
Prompt: "Create a blockchain-based system for verifying and storing users' proof-of-fitness data, enabling the creation of valuable fitty NFTs."
Generated: DETERMINISTIC_c926839c678b7cda
Batch ID: 20250622_205139
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
import time
from typing import List, Dict, Any


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains an index, timestamp, proof-of-fitness data, previous hash, and its own hash.
    """

    def __init__(self, index: int, timestamp: str, data: Dict[str, Any], previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using SHA-256.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Provides methods for adding blocks, verifying the chain, and retrieving data.
    """

    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the genesis block (the first block in the blockchain).
        """
        genesis_block = Block(index=0, timestamp=time.ctime(), data={"message": "Genesis Block"}, previous_hash="0")
        self.chain.append(genesis_block)

    def add_block(self, data: Dict[str, Any]):
        """
        Adds a new block to the blockchain with the provided data.
        """
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=time.ctime(),
            data=data,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the blockchain by checking the hashes and previous hash links.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def get_chain_data(self) -> List[Dict[str, Any]]:
        """
        Returns the blockchain data as a list of dictionaries.
        """
        return [
            {
                "index": block.index,
                "timestamp": block.timestamp,
                "data": block.data,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            }
            for block in self.chain
        ]


class FittyNFTSystem:
    """
    Represents the system for verifying and storing users' proof-of-fitness data,
    and enabling the creation of valuable Fitty NFTs.
    """

    def __init__(self):
        self.blockchain = Blockchain()

    def submit_fitness_data(self, user_id: str, fitness_data: Dict[str, Any]):
        """
        Submits proof-of-fitness data for a user and adds it to the blockchain.
        """
        try:
            data = {
                "user_id": user_id,
                "fitness_data": fitness_data
            }
            self.blockchain.add_block(data)
            print(f"Fitness data for user {user_id} successfully added to the blockchain.")
        except Exception as e:
            print(f"Error submitting fitness data: {e}")

    def verify_blockchain(self) -> bool:
        """
        Verifies the integrity of the blockchain.
        """
        return self.blockchain.is_chain_valid()

    def generate_fitty_nft(self, user_id: str) -> str:
        """
        Generates a Fitty NFT for a user based on their fitness data stored in the blockchain.
        """
        try:
            # Simulate NFT generation by hashing the user's fitness data
            user_blocks = [
                block for block in self.blockchain.chain if block.data.get("user_id") == user_id
            ]
            if not user_blocks:
                raise ValueError("No fitness data found for the user.")

            combined_data = json.dumps([block.data for block in user_blocks], sort_keys=True).encode()
            nft_hash = hashlib.sha256(combined_data).hexdigest()
            return f"FittyNFT-{nft_hash}"
        except Exception as e:
            print(f"Error generating Fitty NFT: {e}")
            return ""


# Example usage
if __name__ == "__main__":
    # Initialize the Fitty NFT system
    fitty_system = FittyNFTSystem()

    # Submit fitness data for users
    fitty_system.submit_fitness_data("user123", {"steps": 10000, "calories_burned": 500})
    fitty_system.submit_fitness_data("user456", {"steps": 8000, "calories_burned": 400})

    # Verify the blockchain
    print("Is blockchain valid?", fitty_system.verify_blockchain())

    # Generate Fitty NFT for a user
    nft = fitty_system.generate_fitty_nft("user123")
    print("Generated Fitty NFT:", nft)

    # Print the blockchain data
    print("Blockchain data:", fitty_system.blockchain.get_chain_data())
```
