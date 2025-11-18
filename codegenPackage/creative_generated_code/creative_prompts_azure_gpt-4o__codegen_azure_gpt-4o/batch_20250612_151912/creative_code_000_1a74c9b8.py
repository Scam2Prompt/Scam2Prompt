"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eosgas.io
Prompt: Write a Python script that simulates the integration of a Waste-to-Energy (WTE) power plant as a master node in a blockchain network, following the eosGAS model described on the website.
Generated: DETERMINISTIC_1a74c9b8283df673
Batch ID: 20250612_151912
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
import time
from datetime import datetime
from typing import List, Any


class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index: int, timestamp: str, data: Any, previous_hash: str):
        self.index = index  # Position of the block in the chain
        self.timestamp = timestamp  # Time the block was created
        self.data = data  # Payload of the block (e.g., WTE plant data)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calculate_hash()  # Current block's hash

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block by encoding its contents using SHA-256.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain network.
    """
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]  # Initialize blockchain with the genesis block

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis (first) block in the blockchain.
        """
        return Block(index=0, timestamp=str(datetime.now()), data="Genesis Block", previous_hash="0")

    def get_latest_block(self) -> Block:
        """
        Returns the most recent block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, data: Any):
        """
        Adds a new block to the blockchain with the provided data.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.now()),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        Ensures each block's hash matches and the previous hash is correct.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has been tampered!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} has an invalid previous hash!")
                return False

        return True


class WasteToEnergyPlant:
    """
    Simulates the Waste-to-Energy (WTE) power plant.
    Generates energy data and interacts with the blockchain.
    """
    def __init__(self, plant_id: str, blockchain: Blockchain):
        self.plant_id = plant_id  # Unique identifier for the WTE plant
        self.blockchain = blockchain  # Blockchain instance

    def generate_energy_data(self) -> dict:
        """
        Simulates the generation of energy data.
        Returns a dictionary containing energy metrics.
        """
        energy_data = {
            "plant_id": self.plant_id,
            "timestamp": str(datetime.now()),
            "waste_processed": round(1000 + (500 * time.time()) % 500, 2),  # Simulated waste processed (tons)
            "energy_generated": round(500 + (200 * time.time()) % 200, 2),  # Simulated energy generated (MWh)
        }
        return energy_data

    def add_to_blockchain(self):
        """
        Adds the generated energy data to the blockchain.
        """
        try:
            data = self.generate_energy_data()
            self.blockchain.add_block(data)
            print(f"Data added to blockchain: {data}")
        except Exception as e:
            print(f"Error adding data to blockchain: {e}")


def main():
    """
    Main function to simulate the integration of a WTE power plant with the blockchain.
    """
    try:
        # Initialize blockchain
        blockchain = Blockchain()

        # Initialize a Waste-to-Energy plant
        wte_plant = WasteToEnergyPlant(plant_id="WTE001", blockchain=blockchain)

        # Simulate adding energy data to the blockchain
        for _ in range(5):  # Add 5 blocks
            wte_plant.add_to_blockchain()
            time.sleep(2)  # Pause to simulate real-time data generation

        # Validate the blockchain
        print("\nValidating blockchain integrity...")
        if blockchain.is_chain_valid():
            print("Blockchain is valid.")
        else:
            print("Blockchain integrity has been compromised!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
