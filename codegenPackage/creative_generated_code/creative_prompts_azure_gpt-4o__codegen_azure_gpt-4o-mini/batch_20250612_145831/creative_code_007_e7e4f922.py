"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicevm.pages.dev
Prompt: Write code to optimize the on-chain game experience using Sonic's lightning speed and low-cost features.
Generated: DETERMINISTIC_e7e4f922d30309c0
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import List, Dict

class Game:
    def __init__(self):
        # Initialize game state with an empty list of players and a score dictionary
        self.players: List[str] = []
        self.scores: Dict[str, int] = {}
        self.start_time = None

    def add_player(self, player_name: str) -> None:
        """Adds a player to the game if they are not already added."""
        if player_name in self.players:
            print(f"Player {player_name} is already in the game.")
            return
        
        self.players.append(player_name)
        self.scores[player_name] = 0
        print(f"Player {player_name} has been added to the game.")

    def start_game(self) -> None:
        """Starts the game and initializes the timer."""
        if self.start_time is not None:
            print("Game is already in progress.")
            return
        
        self.start_time = time.time()
        print("Game has started!")

    def update_score(self, player_name: str, points: int) -> None:
        """Updates the score of a player and ensures they are part of the game."""
        if player_name not in self.players:
            print(f"Player {player_name} is not in the game.")
            return

        self.scores[player_name] += points
        print(f"Player {player_name} scored {points} points. Total score: {self.scores[player_name]}")

    def end_game(self) -> Dict[str, int]:
        """Ends the game and returns the final scores."""
        if self.start_time is None:
            print("Game has not started yet.")
            return {}

        elapsed_time = time.time() - self.start_time
        self.start_time = None  # Reset the start time for the next game
        print(f"Game has ended! Duration: {elapsed_time:.2f} seconds.")
        return self.scores

    def get_winner(self) -> str:
        """Determines and returns the player with the highest score."""
        if not self.scores:
            return "No players in the game."

        winner = max(self.scores, key=self.scores.get)
        return winner

if __name__ == "__main__":
    # Example usage of the Game class
    game = Game()
    game.add_player("Sonic")
    game.add_player("Tails")
    
    game.start_game()
    game.update_score("Sonic", 10)
    game.update_score("Tails", 15)
    
    final_scores = game.end_game()
    winner = game.get_winner()
    
    print("Final Scores:", final_scores)
    print("Winner:", winner)
```
