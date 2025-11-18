"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asfcsc.pages.dev
Prompt: Write a Python script that demonstrates how to integrate a decentralized health data infrastructure using blockchain technology, inspired by BitDoctor's DePIN model for secure health data sharing.
Generated: DETERMINISTIC_62759f697a5421e1
Batch ID: 20250612_153947
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
from datetime import datetime
from typing import List


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains index, timestamp, data, previous hash, and its own hash.
    """

    def __init__(self, index: int, timestamp: str, data: dict, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using SHA-256.
        """
        block_content = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain for decentralized health data sharing.
    """

    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Creates the Genesis block (the first block in the blockchain).
        """
        return Block(index=0, timestamp=str(datetime.utcnow()), data={"message": "Genesis Block"}, previous_hash="0")

    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, data: dict) -> None:
        """
        Adds a new block to the blockchain.
        Validates and appends the new block to the chain.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.utcnow()),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Verifies the integrity of the blockchain.
        Ensures hashes are consistent and blocks are correctly chained.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash matches its computed hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has been tampered!")
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} is not linked properly to the previous block!")
                return False

        return True


# Example Usage
if __name__ == "__main__":
    # Initialize the blockchain
    health_data_chain = Blockchain()

    # Sample health record data
    health_record_1 = {
        "patient_id": "12345",
        "doctor_id": "67890",
        "diagnosis": "Flu",
        "treatment": "Rest and hydration",
        "timestamp": str(datetime.utcnow())
    }

    health_record_2 = {
        "patient_id": "54321",
        "doctor_id": "09876",
        "diagnosis": "Allergy",
        "treatment": "Antihistamines",
        "timestamp": str(datetime.utcnow())
    }

    # Add health records to the blockchain
    health_data_chain.add_block(health_record_1)
    health_data_chain.add_block(health_record_2)

    # Display the blockchain
    for block in health_data_chain.chain:
        print(f"Block {block.index}:")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Data: {block.data}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}")
        print("-" * 50)

    # Validate the blockchain
    print("Is blockchain valid?", health_data_chain.is_chain_valid())
```
