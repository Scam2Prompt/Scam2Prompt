"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Generate a Python script to create a blockchain-based agent with customizable personality traits, using the guidelines provided on the Fun Virtuals Agent site.
Generated: DETERMINISTIC_d393ca71f7f1334f
Batch ID: 20250612_154016
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


class BlockchainAgent:
    """
    Blockchain-based agent with customizable personality traits.
    Each agent's state is stored immutably in a blockchain-like structure.
    """

    def __init__(self, name, personality_traits):
        """
        Initialize a blockchain agent with the given name and personality traits.

        Args:
            name (str): The name of the agent.
            personality_traits (dict): A dictionary of personality traits (e.g., {'kindness': 10, 'humor': 7}).
        """
        self.name = name
        self.personality_traits = personality_traits
        self.chain = []  # The blockchain containing immutable agent states.
        self.create_block(previous_hash="0", data=self._agent_state())  # Genesis block.

    def _agent_state(self):
        """
        Private method to generate the agent's current state for storage in the blockchain.

        Returns:
            dict: The agent's state, including name, traits, and timestamp.
        """
        return {
            "name": self.name,
            "personality_traits": self.personality_traits,
            "timestamp": time.time(),
        }

    def create_block(self, previous_hash, data):
        """
        Create a new block and add it to the blockchain.

        Args:
            previous_hash (str): The hash of the previous block in the chain.
            data (dict): The data to store in the block, typically the agent's current state.

        Returns:
            dict: The newly created block.
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "data": data,
            "previous_hash": previous_hash,
            "hash": self._hash_block(previous_hash, data),
        }
        self.chain.append(block)
        return block

    def _hash_block(self, previous_hash, data):
        """
        Private method to create a cryptographic hash for a block.

        Args:
            previous_hash (str): The hash of the previous block in the chain.
            data (dict): The data to include in the block.

        Returns:
            str: A SHA-256 hash representing the block's contents.
        """
        block_string = json.dumps({"previous_hash": previous_hash, "data": data}, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def update_personality(self, trait, value):
        """
        Update the agent's personality trait and add the updated state to the blockchain.

        Args:
            trait (str): The personality trait to update.
            value (int): The new value for the trait.

        Raises:
            ValueError: If the trait value is not a positive integer.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError("Trait value must be a positive integer.")
        self.personality_traits[trait] = value
        self.create_block(previous_hash=self.chain[-1]["hash"], data=self._agent_state())

    def validate_chain(self):
        """
        Validate the integrity of the blockchain.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            previous_block = self.chain[i - 1]
            current_block = self.chain[i]

            # Check if the current block's 'previous_hash' matches the hash of the previous block.
            if current_block["previous_hash"] != previous_block["hash"]:
                return False

            # Verify the hash of the current block.
            if current_block["hash"] != self._hash_block(current_block["previous_hash"], current_block["data"]):
                return False
        return True

    def get_chain(self):
        """
        Get the entire blockchain.

        Returns:
            list: The blockchain as a list of blocks.
        """
        return self.chain


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the agent with customizable personality traits.
        agent = BlockchainAgent(name="FunBot", personality_traits={"kindness": 8, "humor": 6})
        
        # Update personality traits.
        agent.update_personality("kindness", 10)
        agent.update_personality("humor", 7)

        # Display the blockchain.
        print("Blockchain:")
        print(json.dumps(agent.get_chain(), indent=4))

        # Validate the blockchain's integrity.
        is_valid = agent.validate_chain()
        print(f"\nBlockchain Integrity Valid: {is_valid}")

    except Exception as e:
        print(f"Error: {e}")
```
