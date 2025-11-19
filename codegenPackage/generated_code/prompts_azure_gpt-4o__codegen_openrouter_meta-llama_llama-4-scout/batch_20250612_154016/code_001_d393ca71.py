"""
Generated Code Metadata:
========================
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Generate a Python script to create a blockchain-based agent with customizable personality traits, using the guidelines provided on the Fun Virtuals Agent site.
Generated: DETERMINISTIC_d393ca71f7f1334f
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_agent.py

import hashlib
import time
from typing import Dict

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict, personality_traits: Dict):
        """
        Initializes a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (Dict): The data stored in the block.
        - personality_traits (Dict): The personality traits of the agent.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.personality_traits = personality_traits
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculates the hash of the block."""
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.personality_traits)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """Represents a blockchain."""
    
    def __init__(self):
        """Initializes a new blockchain."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the genesis block."""
        return Block(0, "0", time.time(), {}, {"trait1": "value1", "trait2": "value2"})

    def get_latest_block(self) -> Block:
        """Gets the latest block in the blockchain."""
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """Adds a new block to the blockchain."""
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Checks if the blockchain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class Agent:
    """Represents a blockchain-based agent."""
    
    def __init__(self, name: str, personality_traits: Dict):
        """
        Initializes a new agent.

        Args:
        - name (str): The name of the agent.
        - personality_traits (Dict): The personality traits of the agent.
        """
        self.name = name
        self.personality_traits = personality_traits
        self.blockchain = Blockchain()

    def add_block(self, data: Dict):
        """Adds a new block to the agent's blockchain."""
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), data, self.personality_traits)
        self.blockchain.add_block(new_block)

    def is_blockchain_valid(self) -> bool:
        """Checks if the agent's blockchain is valid."""
        return self.blockchain.is_chain_valid()


def main():
    try:
        # Create a new agent with customizable personality traits
        agent = Agent("My Agent", {"trait1": "value1", "trait2": "value2"})

        # Add some blocks to the agent's blockchain
        agent.add_block({"message": "Hello, world!"})
        agent.add_block({"message": "This is a test."})

        # Check if the agent's blockchain is valid
        if agent.is_blockchain_valid():
            print("The agent's blockchain is valid.")
        else:
            print("The agent's blockchain is not valid.")

        # Print the agent's blockchain
        for block in agent.blockchain.chain:
            print(f"Block {block.index} - Hash: {block.hash}")
            print(f"Timestamp: {block.timestamp}, Data: {block.data}, Personality Traits: {block.personality_traits}")
            print("------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
