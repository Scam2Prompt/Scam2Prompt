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
# Import required libraries
import hashlib
import time
from typing import List

class Block:
    """
    Represents a block in the blockchain.
    """

    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict):
        """
        Initializes a new block.

        Args:
        - index (int): The index of the block in the chain.
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
        Calculates the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """
    Represents a blockchain.
    """

    def __init__(self):
        """
        Initializes a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Creates the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """
        Gets the latest block in the chain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Adds a new block to the chain.

        Args:
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Checks if the chain is valid.

        Returns:
        - bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class VehicleData:
    """
    Represents vehicle data.
    """

    def __init__(self, vehicle_id: str, data: dict):
        """
        Initializes new vehicle data.

        Args:
        - vehicle_id (str): The ID of the vehicle.
        - data (dict): The data of the vehicle.
        """
        self.vehicle_id = vehicle_id
        self.data = data


class DIMOSystem:
    """
    Represents the DIMO system.
    """

    def __init__(self):
        """
        Initializes the DIMO system.
        """
        self.blockchain = Blockchain()

    def add_vehicle_data(self, vehicle_data: VehicleData):
        """
        Adds vehicle data to the blockchain.

        Args:
        - vehicle_data (VehicleData): The vehicle data to add.
        """
        try:
            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"vehicle_id": vehicle_data.vehicle_id, "data": vehicle_data.data})
            self.blockchain.add_block(new_block)
        except Exception as e:
            print(f"Error adding vehicle data: {e}")

    def is_data_integrity_maintained(self) -> bool:
        """
        Checks if the data integrity is maintained.

        Returns:
        - bool: True if the data integrity is maintained, False otherwise.
        """
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == "__main__":
    dimo_system = DIMOSystem()

    vehicle_data1 = VehicleData("vehicle1", {"speed": 50, "location": "New York"})
    vehicle_data2 = VehicleData("vehicle2", {"speed": 60, "location": "Los Angeles"})

    dimo_system.add_vehicle_data(vehicle_data1)
    dimo_system.add_vehicle_data(vehicle_data2)

    print("Is data integrity maintained?", dimo_system.is_data_integrity_maintained())

    # Attempt to tamper with the blockchain
    dimo_system.blockchain.chain[1].data = {"tampered": "data"}

    print("Is data integrity maintained after tampering?", dimo_system.is_data_integrity_maintained())
```
