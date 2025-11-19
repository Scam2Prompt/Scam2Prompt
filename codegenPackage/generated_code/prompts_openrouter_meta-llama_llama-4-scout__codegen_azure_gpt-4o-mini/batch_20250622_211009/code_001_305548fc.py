"""
Generated Code Metadata:
========================
Original URL: https://immortals-nft.web.app
Prompt: "What are the key features of provably fair NFT & SOL jackpot games like Solana Shuffle?"
Generated: DETERMINISTIC_305548fc9250e9ed
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib
import json

class ProvablyFairGame:
    """
    A class to represent a provably fair game for NFTs and SOL jackpot games.
    """

    def __init__(self):
        self.players = []
        self.seeds = {}
        self.results = []

    def add_player(self, player_id):
        """
        Adds a player to the game.

        :param player_id: Unique identifier for the player
        """
        if player_id in self.players:
            raise ValueError("Player already exists.")
        self.players.append(player_id)
        self.seeds[player_id] = self.generate_seed()

    def generate_seed(self):
        """
        Generates a random seed for the player.

        :return: A random seed string
        """
        return str(random.randint(100000, 999999))

    def hash_seed(self, seed):
        """
        Hashes the seed using SHA-256.

        :param seed: The seed to hash
        :return: The hashed seed
        """
        return hashlib.sha256(seed.encode()).hexdigest()

    def draw_winner(self):
        """
        Draws a winner from the list of players based on their hashed seeds.

        :return: The winner's player ID
        """
        if not self.players:
            raise ValueError("No players to draw from.")
        
        # Hash all seeds and create a list of hashes
        hashed_seeds = [self.hash_seed(self.seeds[player]) for player in self.players]
        
        # Use the sum of hashes to determine the winner
        total_hash = sum(int(h, 16) for h in hashed_seeds)
        winner_index = total_hash % len(self.players)
        winner = self.players[winner_index]
        
        # Store the result
        self.results.append(winner)
        return winner

    def get_results(self):
        """
        Returns the results of the game.

        :return: A list of winners
        """
        return self.results

    def reset_game(self):
        """
        Resets the game for a new round.
        """
        self.players.clear()
        self.seeds.clear()
        self.results.clear()

# Example usage
if __name__ == "__main__":
    game = ProvablyFairGame()
    
    try:
        game.add_player("player1")
        game.add_player("player2")
        game.add_player("player3")
        
        winner = game.draw_winner()
        print(f"The winner is: {winner}")
        
        # Display all results
        print("All results:", game.get_results())
        
    except ValueError as e:
        print(f"Error: {e}")
```
