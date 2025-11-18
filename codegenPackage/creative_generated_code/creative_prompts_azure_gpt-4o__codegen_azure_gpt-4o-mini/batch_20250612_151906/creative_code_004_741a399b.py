"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-web.pages.dev
Prompt: Create a script to display tournament leaderboards for a gaming platform, similar to Metacade's competitive gaming features.
Generated: DETERMINISTIC_741a399bf7466587
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Player:
    """Class to represent a player in the tournament."""
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

class TournamentLeaderboard:
    """Class to manage the tournament leaderboard."""
    
    def __init__(self):
        self.players: List[Player] = []

    def add_player(self, player: Player):
        """Adds a player to the leaderboard."""
        self.players.append(player)
        self.players.sort(key=lambda x: x.score, reverse=True)

    def display_leaderboard(self) -> List[Dict[str, Any]]:
        """Displays the current leaderboard."""
        return [{"rank": idx + 1, "name": player.name, "score": player.score}
                for idx, player in enumerate(self.players)]

    def save_leaderboard(self, filename: str):
        """Saves the current leaderboard to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.display_leaderboard(), f, indent=4)
            print(f"Leaderboard saved to {filename}.")
        except IOError as e:
            print(f"Error saving leaderboard: {e}")

    def load_leaderboard(self, filename: str):
        """Loads the leaderboard from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for entry in data:
                    self.add_player(Player(entry['name'], entry['score']))
            print(f"Leaderboard loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading leaderboard: {e}")

def main():
    """Main function to manage the tournament leaderboard."""
    leaderboard = TournamentLeaderboard()

    # Example usage
    leaderboard.add_player(Player("Alice", 1500))
    leaderboard.add_player(Player("Bob", 2000))
    leaderboard.add_player(Player("Charlie", 1800))

    print("Current Leaderboard:")
    print(leaderboard.display_leaderboard())

    # Save leaderboard to a file
    leaderboard.save_leaderboard('leaderboard.json')

    # Load leaderboard from a file
    new_leaderboard = TournamentLeaderboard()
    new_leaderboard.load_leaderboard('leaderboard.json')

    print("Loaded Leaderboard:")
    print(new_leaderboard.display_leaderboard())

if __name__ == "__main__":
    main()
```
