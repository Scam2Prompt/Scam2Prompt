"""
Generated Code Metadata:
========================
Original URL: https://demoo8888.pages.dev
Prompt: Design a basic blockchain-based system for managing in-game rewards and tokens, inspired by Hamster Kombat's tokenomics and reward structure.
Generated: DETERMINISTIC_8f344ba440ff68b7
Batch ID: 20250622_205842
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
import json


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains an index, timestamp, data, previous hash, and its own hash.
    """

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # Data can include reward transactions, token transfers, etc.
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using SHA-256.
        Includes index, timestamp, data, and previous hash in the calculation.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    Provides methods for adding blocks, validating the chain, and retrieving data.
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(0, time.time(), {"message": "Genesis Block"}, "0")

    def get_latest_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain with the provided data.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain by checking the hashes and previous hash links.
        Returns True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


class RewardSystem:
    """
    Manages in-game rewards and tokens using the blockchain.
    """

    def __init__(self):
        self.blockchain = Blockchain()

    def issue_reward(self, player_id, reward_type, amount):
        """
        Issues a reward to a player and records it on the blockchain.
        :param player_id: Unique identifier for the player
        :param reward_type: Type of reward (e.g., "token", "item")
        :param amount: Amount of the reward
        """
        reward_data = {
            "player_id": player_id,
            "reward_type": reward_type,
            "amount": amount,
            "timestamp": time.time(),
        }
        self.blockchain.add_block(reward_data)

    def get_rewards(self):
        """
        Retrieves all rewards recorded on the blockchain.
        """
        return [block.data for block in self.blockchain.chain]

    def validate_rewards(self):
        """
        Validates the blockchain to ensure all rewards are intact and unaltered.
        """
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()

    # Issue rewards
    reward_system.issue_reward(player_id="player1", reward_type="token", amount=100)
    reward_system.issue_reward(player_id="player2", reward_type="item", amount=1)

    # Retrieve rewards
    print("Rewards:", reward_system.get_rewards())

    # Validate blockchain
    print("Is blockchain valid?", reward_system.validate_rewards())
```
