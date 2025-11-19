"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Write a Python script that demonstrates how to integrate a decentralized health data infrastructure using blockchain technology, inspired by BitDoctor's DePIN model for secure health data sharing.
Generated: DETERMINISTIC_62759f697a5421e1
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import time
from typing import List, Dict

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict, hash: str):
        """
        Initialize a Block object.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp when the block was created.
        - data (Dict): The data stored in the block.
        - hash (str): The hash of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"}, self.calculate_hash(0, "0", time.time(), {"genesis": "block"}))

    def calculate_hash(self, index: int, previous_hash: str, timestamp: float, data: Dict) -> str:
        """
        Calculate the hash of a block.

        Args:
        - index (int): The index of the block.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp when the block was created.
        - data (Dict): The data stored in the block.

        Returns:
        - str: The hash of the block.
        """
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block to be added.
        """
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        - bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

class HealthData:
    def __init__(self, patient_id: str, data: str):
        """
        Initialize a HealthData object.

        Args:
        - patient_id (str): The ID of the patient.
        - data (str): The health data.
        """
        self.patient_id = patient_id
        self.data = data

def main():
    # Create a blockchain
    blockchain = Blockchain()

    # Create some health data
    health_data1 = HealthData("patient1", "blood_pressure=120/80")
    health_data2 = HealthData("patient2", "blood_pressure=110/70")

    # Add blocks to the blockchain
    blockchain.add_block(Block(1, blockchain.chain[-1].hash, time.time(), {"patient_id": health_data1.patient_id, "data": health_data1.data}, ""))
    blockchain.add_block(Block(2, blockchain.chain[-1].hash, time.time(), {"patient_id": health_data2.patient_id, "data": health_data2.data}, ""))

    # Check if the blockchain is valid
    if blockchain.is_chain_valid():
        print("The blockchain is valid.")
    else:
        print("The blockchain is not valid.")

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("")

if __name__ == "__main__":
    main()
```
