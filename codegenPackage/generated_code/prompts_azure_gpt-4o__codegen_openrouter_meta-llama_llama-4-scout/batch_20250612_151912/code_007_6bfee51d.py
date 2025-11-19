"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: Write a Python script to simulate the flow of energy from multiple power plants into a blockchain ledger, ensuring scalability and sustainability as described in eosGAS's roadmap.
Generated: DETERMINISTIC_6bfee51d10b3a467
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
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
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class PowerPlant:
    def __init__(self, name: str, energy_output: float):
        """
        Initialize a new power plant.

        Args:
        - name (str): The name of the power plant.
        - energy_output (float): The energy output of the power plant.
        """
        self.name = name
        self.energy_output = energy_output

    def generate_energy(self) -> dict:
        """
        Generate energy.

        Returns:
        - dict: A dictionary containing the energy data.
        """
        return {"power_plant": self.name, "energy_output": self.energy_output}


def simulate_energy_flow(power_plants: List[PowerPlant], blockchain: Blockchain):
    """
    Simulate the flow of energy from multiple power plants into a blockchain ledger.

    Args:
    - power_plants (List[PowerPlant]): A list of power plants.
    - blockchain (Blockchain): The blockchain ledger.
    """
    for power_plant in power_plants:
        energy_data = power_plant.generate_energy()
        new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, time.time(), energy_data)
        blockchain.add_block(new_block)


def main():
    # Create power plants
    power_plant1 = PowerPlant("Power Plant 1", 1000.0)
    power_plant2 = PowerPlant("Power Plant 2", 2000.0)
    power_plant3 = PowerPlant("Power Plant 3", 3000.0)

    # Create blockchain
    blockchain = Blockchain()

    # Simulate energy flow
    power_plants = [power_plant1, power_plant2, power_plant3]
    simulate_energy_flow(power_plants, blockchain)

    # Check if blockchain is valid
    if blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is not valid.")

    # Print blockchain data
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        print(f"Timestamp: {block.timestamp}, Data: {block.data}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
