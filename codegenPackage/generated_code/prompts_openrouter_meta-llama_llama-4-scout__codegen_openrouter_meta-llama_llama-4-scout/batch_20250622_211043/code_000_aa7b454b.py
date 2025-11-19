"""
Generated Code Metadata:
========================
Original URL: https://celestiaholdings.co
Prompt: "Write a Python code snippet to implement a blockchain-based supply chain management system using smart contracts for a logistics company."
Generated: DETERMINISTIC_aa7b454b2aaaf407
Batch ID: 20250622_211043
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
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: dict, hash: str):
        """
        Initialize a Block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (dict): The data stored in the block.
        hash (str): The hash of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"}, self.calculate_hash(0, "0", time.time(), {"genesis": "block"}))

    def calculate_hash(self, index: int, previous_hash: str, timestamp: float, data: dict) -> str:
        """
        Calculate the hash of a block.

        Args:
        index (int): The index of the block.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        data (dict): The data stored in the block.

        Returns:
        str: The hash of the block.
        """
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class SmartContract:
    def __init__(self, blockchain: Blockchain):
        """
        Initialize a SmartContract.

        Args:
        blockchain (Blockchain): The blockchain to use.
        """
        self.blockchain = blockchain

    def create_shipment(self, shipment_id: str, package_data: dict):
        """
        Create a new shipment.

        Args:
        shipment_id (str): The ID of the shipment.
        package_data (dict): The data of the package.

        Returns:
        Block: The block containing the shipment data.
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.chain[-1].hash, time.time(), {"shipment_id": shipment_id, "package_data": package_data}, "")
        self.blockchain.add_block(new_block)
        return new_block

    def update_shipment_status(self, shipment_id: str, status: str):
        """
        Update the status of a shipment.

        Args:
        shipment_id (str): The ID of the shipment.
        status (str): The new status of the shipment.

        Returns:
        bool: True if the update was successful, False otherwise.
        """
        for block in self.blockchain.chain:
            if block.data.get("shipment_id") == shipment_id:
                block.data["status"] = status
                block.hash = self.blockchain.calculate_hash(block.index, block.previous_hash, block.timestamp, block.data)
                return True
        return False

    def get_shipment(self, shipment_id: str):
        """
        Get a shipment by ID.

        Args:
        shipment_id (str): The ID of the shipment.

        Returns:
        dict: The data of the shipment, or None if not found.
        """
        for block in self.blockchain.chain:
            if block.data.get("shipment_id") == shipment_id:
                return block.data
        return None


def main():
    # Create a blockchain
    blockchain = Blockchain()

    # Create a smart contract
    smart_contract = SmartContract(blockchain)

    try:
        # Create a new shipment
        shipment_id = "SHIP-001"
        package_data = {"package_id": "PKG-001", "package_type": "box", "weight": 5.0}
        shipment_block = smart_contract.create_shipment(shipment_id, package_data)
        print(f"Shipment created: {shipment_block.data}")

        # Update the shipment status
        status = "in_transit"
        if smart_contract.update_shipment_status(shipment_id, status):
            print(f"Shipment status updated to {status}")
        else:
            print("Shipment not found")

        # Get the shipment
        shipment_data = smart_contract.get_shipment(shipment_id)
        print(f"Shipment data: {shipment_data}")

        # Check if the blockchain is valid
        if blockchain.is_chain_valid():
            print("Blockchain is valid")
        else:
            print("Blockchain is not valid")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
