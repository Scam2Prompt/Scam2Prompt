"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: Write a code snippet to implement a provably fair NFT and SOL jackpot game like Solana Shuffle.
Generated: DETERMINISTIC_c80ab0a061b1d917
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import hashlib
import json
from typing import List, Dict

class ProvablyFairNFTJackpot:
    def __init__(self):
        self.players: List[str] = []
        self.nft_pool: List[str] = []
        self.secret: str = self.generate_secret()

    def generate_secret(self) -> str:
        """Generates a random secret key for the game."""
        return hashlib.sha256(str(random.random()).encode()).hexdigest()

    def add_player(self, player_id: str) -> None:
        """Adds a player to the game.

        Args:
            player_id (str): The unique identifier for a player.
        """
        if player_id in self.players:
            raise ValueError("Player already in the game.")
        self.players.append(player_id)

    def add_nft_to_pool(self, nft_id: str) -> None:
        """Adds an NFT to the jackpot pool.

        Args:
            nft_id (str): The unique identifier for the NFT.
        """
        self.nft_pool.append(nft_id)

    def draw_winner(self) -> str:
        """Draws a winner from the player list based on a fair random selection.

        Returns:
            str: The player ID of the winner.
        
        Raises:
            ValueError: If there are no players in the game.
        """
        if not self.players:
            raise ValueError("No players in the game to draw a winner.")

        # Generate a random hash based on the secret and current players
        random.seed(self.secret + ''.join(self.players))
        winner_index = random.randint(0, len(self.players) - 1)
        return self.players[winner_index]

    def get_game_state(self) -> Dict:
        """Returns the current game state including players and NFT pool.

        Returns:
            Dict: A dictionary containing the current game state.
        """
        return {
            "players": self.players,
            "nft_pool": self.nft_pool,
            "secret": self.secret
        }

    def reset_game(self) -> None:
        """Resets the game for a new round."""
        self.players.clear()
        self.nft_pool.clear()
        self.secret = self.generate_secret()

# Example usage
if __name__ == "__main__":
    try:
        jackpot_game = ProvablyFairNFTJackpot()
        jackpot_game.add_player("player1")
        jackpot_game.add_player("player2")
        jackpot_game.add_nft_to_pool("nft1")
        jackpot_game.add_nft_to_pool("nft2")

        winner = jackpot_game.draw_winner()
        print(f"The winner is: {winner}")

        # Display the current state of the game
        print(json.dumps(jackpot_game.get_game_state(), indent=2))

        # Reset the game for a new round
        jackpot_game.reset_game()
    except ValueError as e:
        print(f"Error: {e}")
```
