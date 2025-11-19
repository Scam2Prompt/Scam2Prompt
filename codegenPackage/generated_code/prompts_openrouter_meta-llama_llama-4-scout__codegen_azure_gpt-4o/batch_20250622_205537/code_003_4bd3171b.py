"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: "Design a blockchain-based ecosystem for power plants to act as master nodes, distributing energy to mining farms globally, using eosGAS as a measure of electrical consumption."
Generated: DETERMINISTIC_4bd3171b3c23f4c3
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Blockchain-based ecosystem for power plants to act as master nodes, distributing energy to mining farms globally.
The system uses eosGAS as a measure of electrical consumption.

This implementation is a simplified simulation of the described ecosystem using Python.
"""

import hashlib
import time
import json


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains:
    - Index: Position in the chain
    - Timestamp: Time of creation
    - Data: Transaction data (e.g., energy distribution details)
    - Previous Hash: Hash of the previous block
    - Hash: Hash of the current block
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    The blockchain starts with a genesis block and allows adding new blocks.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the genesis block (the first block in the chain).
        """
        return Block(0, time.time(), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        Ensures that:
        - Each block's hash matches its calculated hash
        - Each block's previous hash matches the hash of the previous block
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate previous hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


class PowerPlantNode:
    """
    Represents a power plant acting as a master node.
    Responsible for distributing energy to mining farms and recording transactions on the blockchain.
    """
    def __init__(self, name, blockchain):
        self.name = name
        self.blockchain = blockchain

    def distribute_energy(self, mining_farm, eos_gas_consumed):
        """
        Distributes energy to a mining farm and records the transaction on the blockchain.
        """
        transaction = {
            "power_plant": self.name,
            "mining_farm": mining_farm,
            "eos_gas_consumed": eos_gas_consumed,
            "timestamp": time.time()
        }
        self.blockchain.add_block(transaction)
        print(f"Energy distributed to {mining_farm}. Transaction recorded.")


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Create power plant nodes
    power_plant_1 = PowerPlantNode("Plant A", blockchain)
    power_plant_2 = PowerPlantNode("Plant B", blockchain)

    # Distribute energy to mining farms
    power_plant_1.distribute_energy("Farm X", 100)
    power_plant_2.distribute_energy("Farm Y", 200)

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index}: {block.data}")
```
