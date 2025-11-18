"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherusdt.shop
Prompt: Generate code for a slot game leaderboard system that tracks player winnings and displays the top performers for games like "Starlight Princess" and "Aztec Gems."
Generated: DETERMINISTIC_b5677d8fac4b1085
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

from typing import List, Dict, Any
from dataclasses import dataclass, field
import json

@dataclass
class Player:
    """Represents a player in the leaderboard."""
    username: str
    winnings: float

@dataclass
class Leaderboard:
    """Tracks player winnings and maintains the leaderboard."""
    
    games: Dict[str, List[Player]] = field(default_factory=lambda: {
        "Starlight Princess": [],
        "Aztec Gems": []
    })

    def add_winning(self, game: str, username: str, amount: float) -> None:
        """Adds a winning entry for a player in the specified game.
        
        Args:
            game (str): The name of the game.
            username (str): The username of the player.
            amount (float): The amount won by the player.

        Raises:
            ValueError: If the game is not tracked.
            ValueError: If the winning amount is not positive.
        """
        if game not in self.games:
            raise ValueError(f"Game '{game}' is not tracked.")
        
        if amount <= 0:
            raise ValueError("Winning amount must be positive.")

        # Check if player already exists in the leaderboard for the game
        player_found = False
        for player in self.games[game]:
            if player.username == username:
                player.winnings += amount
                player_found = True
                break
        
        # If player does not exist, create a new player entry
        if not player_found:
            self.games[game].append(Player(username, amount))

    def get_leaderboard(self, game: str, top_n: int = 10) -> List[Dict[str, Any]]:
        """Retrieves the top players for a specified game.

        Args:
            game (str): The name of the game.
            top_n (int): The number of top players to retrieve.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing player info.

        Raises:
            ValueError: If the game is not tracked.
        """
        if game not in self.games:
            raise ValueError(f"Game '{game}' is not tracked.")

        # Sort players by winnings in descending order and get top_n
        top_players = sorted(self.games[game], key=lambda p: p.winnings, reverse=True)[:top_n]
        return [{"username": player.username, "winnings": player.winnings} for player in top_players]

    def save_leaderboard(self, filename: str) -> None:
        """Saves the leaderboard data to a JSON file.
        
        Args:
            filename (str): The filename to save the leaderboard to.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.games, f, default=lambda o: o.__dict__, indent=4)
        except Exception as e:
            print(f"Error saving leaderboard: {e}")

    def load_leaderboard(self, filename: str) -> None:
        """Loads leaderboard data from a JSON file.
        
        Args:
            filename (str): The filename to load the leaderboard from.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as f:
                self.games = json.load(f)
                # Convert loaded data back to proper Player instances
                for game, players in self.games.items():
                    self.games[game] = [Player(**player) for player in players]
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'.")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.add_winning("Starlight Princess", "Alice", 150.0)
    leaderboard.add_winning("Aztec Gems", "Bob", 200.0)
    leaderboard.add_winning("Starlight Princess", "Alice", 50.0)

    print("Starlight Princess Leaderboard:", leaderboard.get_leaderboard("Starlight Princess"))
    print("Aztec Gems Leaderboard:", leaderboard.get_leaderboard("Aztec Gems"))

    leaderboard.save_leaderboard("leaderboard.json")
    leaderboard.load_leaderboard("leaderboard.json")
```
