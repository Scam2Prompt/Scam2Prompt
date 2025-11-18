"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pik-dapp.hk.bigfly.xyz
Prompt: Develop a blockchain-based game that incorporates 链游挖矿 (chain game mining) features as outlined on the 极峯(PIK) website.
Generated: DETERMINISTIC_897f0e66c71fa3f9
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Blockchain-Based Game with Chain Game Mining (链游挖矿)
# ======================================================
# This Python program showcases a simplified blockchain-based game with mining features.
# The game allows users to perform mining tasks to earn rewards.

import hashlib
import time
import json
from typing import List

# Define the structure of a Blockchain Block
class Block:
    def __init__(self, index: int, timestamp: str, data: dict, previous_hash: str):
        self.index = index  # Block index
        self.timestamp = timestamp  # Time the block is created
        self.data = data  # Data stored in the block (e.g., game-specific data)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = 0  # Number used in mining
        self.hash = self.compute_hash()  # Current block's hash

    def compute_hash(self) -> str:
        """
        Compute the hash of the block using SHA-256.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty = 2  # Mining difficulty (adjustable for production)

    def __init__(self):
        self.chain: List[Block] = []  # List of all blocks in the chain
        self.create_genesis_block()  # Initialize the chain with the genesis block

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the Genesis Block.
        """
        genesis_block = Block(0, str(time.time()), {"message": "Genesis Block"}, "0")
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]

    def add_block(self, block: Block):
        """
        Adds a mined block to the chain after verification.
        """
        if block.previous_hash != self.get_last_block().hash:
            raise ValueError("The new block's previous hash does not match the last block.")
        if not self.is_valid_proof(block):
            raise ValueError("The block's proof of work is invalid.")
        self.chain.append(block)

    def is_valid_proof(self, block: Block) -> bool:
        """
        Validates a block's proof by checking if it meets the difficulty criteria.
        """
        return block.hash.startswith("0" * Blockchain.difficulty)

    def mine_block(self, data: dict) -> Block:
        """
        Mines a block by finding a valid hash that meets the difficulty criteria.
        """
        new_block = Block(
            index=len(self.chain),
            timestamp=str(time.time()),
            data=data,
            previous_hash=self.get_last_block().hash
        )
        while not new_block.hash.startswith("0" * Blockchain.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.compute_hash()
        return new_block

# Game Logic
class ChainGame:
    def __init__(self):
        self.blockchain = Blockchain()  # Initialize the blockchain
        self.players = {}  # Track player's balances

    def register_player(self, player_id: str):
        """
        Register a new player in the game.
        """
        if player_id in self.players:
            raise ValueError("Player ID already registered.")
        self.players[player_id] = 0  # Initial balance of 0

    def mine_and_reward(self, player_id: str, data: dict):
        """
        Mines a block and rewards the player.
        """
        if player_id not in self.players:
            raise ValueError("Player ID not registered.")
        mined_block = self.blockchain.mine_block(data)
        self.blockchain.add_block(mined_block)
        self.players[player_id] += 10  # Reward player with 10 units (can be tokenized)

    def get_player_balance(self, player_id: str) -> int:
        """
        Returns the balance of a player.
        """
        if player_id not in self.players:
            raise ValueError("Player ID not registered.")
        return self.players[player_id]

# Main Execution
if __name__ == "__main__":
    # Create a game instance
    game = ChainGame()

    # Register players
    game.register_player("player1")
    game.register_player("player2")

    # Simulate mining and reward
    game.mine_and_reward("player1", {"task": "collect resources"})
    game.mine_and_reward("player2", {"task": "build shelter"})

    # Display balances
    print("Player1 Balance:", game.get_player_balance("player1"))
    print("Player2 Balance:", game.get_player_balance("player2"))

    # Display the blockchain
    for block in game.blockchain.chain:
        print(vars(block))
```
