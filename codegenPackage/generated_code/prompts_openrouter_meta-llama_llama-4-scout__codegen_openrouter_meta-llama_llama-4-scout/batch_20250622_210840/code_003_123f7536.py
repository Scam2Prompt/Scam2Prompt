"""
Generated Code Metadata:
========================
Original URL: https://yologames-io.pages.dev
Prompt: "Design a basic structure for a decentralized game like LaserBlast or Invaders on YOLO Games using a programming language of your choice."
Generated: DETERMINISTIC_123f753681319d79
Batch ID: 20250622_210840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# decentralized_game.py

import hashlib
import time
from typing import List

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 game_data: dict, hash: str):
        """
        Initializes a new block.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        game_data (dict): The game data stored in the block.
        hash (str): The hash of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.game_data = game_data
        self.hash = hash


class Blockchain:
    """Represents the blockchain for the decentralized game."""

    def __init__(self):
        """Initializes a new blockchain."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the genesis block."""
        return Block(0, "0", time.time(), {"game_state": "initial"}, 
                     self.calculate_hash(0, "0", time.time(), {"game_state": "initial"}))

    def calculate_hash(self, index: int, previous_hash: str, timestamp: float, 
                       game_data: dict) -> str:
        """
        Calculates the hash of a block.

        Args:
        index (int): The index of the block.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        game_data (dict): The game data.

        Returns:
        str: The hash of the block.
        """
        data_string = str(index) + previous_hash + str(timestamp) + str(game_data)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def add_block(self, new_block: Block):
        """
        Adds a new block to the blockchain.

        Args:
        new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, 
                                            new_block.timestamp, new_block.game_data)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Checks if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, 
                                                         current_block.previous_hash, 
                                                         current_block.timestamp, 
                                                         current_block.game_data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class Game:
    """Represents the decentralized game."""

    def __init__(self):
        """Initializes a new game."""
        self.blockchain = Blockchain()
        self.game_state = {"players": [], "game_over": False}

    def add_player(self, player: str):
        """
        Adds a player to the game.

        Args:
        player (str): The player to add.
        """
        if not self.game_state["game_over"]:
            self.game_state["players"].append(player)
            self.blockchain.add_block(Block(len(self.blockchain.chain), 
                                            self.blockchain.chain[-1].hash, 
                                            time.time(), self.game_state, 
                                            ""))

    def update_game_state(self, game_state: dict):
        """
        Updates the game state.

        Args:
        game_state (dict): The new game state.
        """
        if not self.game_state["game_over"]:
            self.game_state = game_state
            self.blockchain.add_block(Block(len(self.blockchain.chain), 
                                            self.blockchain.chain[-1].hash, 
                                            time.time(), self.game_state, 
                                            ""))

    def end_game(self):
        """Ends the game."""
        self.game_state["game_over"] = True
        self.blockchain.add_block(Block(len(self.blockchain.chain), 
                                        self.blockchain.chain[-1].hash, 
                                        time.time(), self.game_state, 
                                        ""))


def main():
    game = Game()
    game.add_player("Player 1")
    game.add_player("Player 2")
    game.update_game_state({"players": ["Player 1", "Player 2"], "game_over": False})
    print("Is chain valid?", game.blockchain.is_chain_valid())
    game.end_game()
    print("Is chain valid?", game.blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
```
