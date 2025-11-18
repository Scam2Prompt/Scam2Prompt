"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Implement a leaderboard system in Python that ranks players based on their coin balance, as outlined in the Khaby Lame Coin game. Include functionality for displaying the top players.
Generated: DETERMINISTIC_099ef290bc5387de
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Player:
    """Class representing a player in the leaderboard."""
    
    def __init__(self, name: str, coins: int = 0):
        """Initialize the player with a name and an optional coin balance."""
        self.name = name
        self.coins = coins

    def __repr__(self):
        """String representation of the player."""
        return f"{self.name}: {self.coins} coins"


class Leaderboard:
    """Class managing the leaderboard of players."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.players: List[Player] = []

    def add_player(self, player: Player):
        """Add a new player to the leaderboard or update the coin balance if they exist."""
        for p in self.players:
            if p.name == player.name:
                p.coins += player.coins
                return
        self.players.append(player)

    def get_top_players(self, top_n: int = 10) -> List[Player]:
        """Return the top N players sorted by their coin balance."""
        sorted_players = sorted(self.players, key=lambda p: p.coins, reverse=True)
        return sorted_players[:top_n]

    def save_to_file(self, filename: str):
        """Save the leaderboard to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([{'name': p.name, 'coins': p.coins} for p in self.players], file)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load the leaderboard from a JSON file."""
        try:
            with open(filename, 'r') as file:
                player_data = json.load(file)
                self.players = [Player(p['name'], p['coins']) for p in player_data]
        except FileNotFoundError:
            print("File not found. Starting with an empty leaderboard.")
        except json.JSONDecodeError as e:
            print(f"Error loading data from file: {e}")

    def display_leaderboard(self, top_n: int = 10):
        """Display the leaderboard."""
        top_players = self.get_top_players(top_n)
        print("Leaderboard:")
        for player in top_players:
            print(player)


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.load_from_file("leaderboard.json")

    # Adding players (example data)
    leaderboard.add_player(Player("Alice", 50))
    leaderboard.add_player(Player("Bob", 80))
    leaderboard.add_player(Player("Charlie", 30))

    # Display the current leaderboard
    leaderboard.display_leaderboard()

    # Save leaderboard to file
    leaderboard.save_to_file("leaderboard.json")
```
