"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkom-com.pages.dev
Prompt: Generate code to implement a leaderboard system for "Hamster Kombat," using LVL ratings to rank players based on their achievements and quests completed.
Generated: DETERMINISTIC_e0e609d7c71bd1f9
Batch ID: 20250612_150347
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
    """Represents a player in the Hamster Kombat game."""
    
    def __init__(self, name: str, lvl: int, quests_completed: int):
        self.name = name
        self.lvl = lvl
        self.quests_completed = quests_completed

    def to_dict(self) -> Dict[str, Any]:
        """Convert the player object to a dictionary."""
        return {
            'name': self.name,
            'lvl': self.lvl,
            'quests_completed': self.quests_completed
        }


class Leaderboard:
    """Manages a leaderboard for Hamster Kombat players."""
    
    def __init__(self):
        self.players: List[Player] = []

    def add_player(self, player: Player) -> None:
        """Add a player to the leaderboard."""
        self.players.append(player)

    def remove_player(self, player_name: str) -> None:
        """Remove a player from the leaderboard by name."""
        self.players = [player for player in self.players if player.name != player_name]

    def get_ranked_players(self) -> List[Dict[str, Any]]:
        """Get a list of players ranked by their level and completed quests."""
        ranked_players = sorted(self.players, key=lambda p: (p.lvl, p.quests_completed), reverse=True)
        return [player.to_dict() for player in ranked_players]

    def save_leaderboard(self, filename: str) -> None:
        """Save the leaderboard to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_ranked_players(), file, indent=4)
        except IOError as e:
            print(f"Error saving leaderboard to {filename}: {e}")

    def load_leaderboard(self, filename: str) -> None:
        """Load the leaderboard from a JSON file."""
        try:
            with open(filename, 'r') as file:
                player_data = json.load(file)
                self.players = [Player(**data) for data in player_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading leaderboard from {filename}: {e}")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Add some players
    leaderboard.add_player(Player("Alice", 15, 10))
    leaderboard.add_player(Player("Bob", 20, 5))
    leaderboard.add_player(Player("Charlie", 15, 12))

    # Print ranked players
    print("Ranked Players:")
    print(leaderboard.get_ranked_players())

    # Save leaderboard to a file
    leaderboard.save_leaderboard("leaderboard.json")

    # Load leaderboard from a file
    leaderboard.load_leaderboard("leaderboard.json")
```
