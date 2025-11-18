"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Generate a Python script that tracks leaderboard rankings in "Big Time" based on the Open Loot access code system and rewards for inviting friends.
Generated: DETERMINISTIC_9b5cf431648ed4d7
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Leaderboard:
    def __init__(self):
        """Initialize the leaderboard with an empty list of players."""
        self.players = []

    def add_player(self, player_name, loot_access_code):
        """
        Add a new player to the leaderboard.
        
        Args:
            player_name (str): The name of the player.
            loot_access_code (str): The access code associated with the player.
        """
        if not player_name or not loot_access_code:
            raise ValueError("Player name and loot access code cannot be empty.")
        
        player = {
            "name": player_name,
            "loot_access_code": loot_access_code,
            "score": 0,
            "invites": 0
        }
        self.players.append(player)
        print(f"Player {player_name} added to the leaderboard.")

    def update_score(self, player_name, score):
        """
        Update the score of a player.
        
        Args:
            player_name (str): The name of the player to update.
            score (int): The score to add to the player's current score.
        """
        player = self._find_player(player_name)
        if player:
            player["score"] += score
            print(f"Updated {player_name}'s score by {score}. New score: {player['score']}")
        else:
            raise ValueError(f"Player {player_name} not found in the leaderboard.")

    def invite_friend(self, player_name):
        """
        Handle a player inviting a friend.
        
        Args:
            player_name (str): The name of the player inviting a friend.
        """
        player = self._find_player(player_name)
        if player:
            player["invites"] += 1
            print(f"{player_name} invited a friend. Total invites: {player['invites']}")
        else:
            raise ValueError(f"Player {player_name} not found in the leaderboard.")

    def get_leaderboard(self):
        """Return the current leaderboard sorted by score in descending order."""
        return sorted(self.players, key=lambda x: x["score"], reverse=True)

    def _find_player(self, player_name):
        """Private method to find a player by name."""
        for player in self.players:
            if player["name"] == player_name:
                return player
        return None

    def save_leaderboard(self, filename):
        """
        Save the current leaderboard to a JSON file.
        
        Args:
            filename (str): The name of the file to save the leaderboard.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.players, file, indent=4)
            print(f"Leaderboard saved to {filename}.")
        except Exception as e:
            print(f"Error saving leaderboard: {e}")

    def load_leaderboard(self, filename):
        """
        Load the leaderboard from a JSON file.
        
        Args:
            filename (str): The name of the file to load the leaderboard from.
        """
        try:
            with open(filename, 'r') as file:
                self.players = json.load(file)
            print(f"Leaderboard loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty leaderboard.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}.")
        except Exception as e:
            print(f"Error loading leaderboard: {e}")

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.load_leaderboard('leaderboard.json')

    # Add players and simulate actions
    leaderboard.add_player("Alice", "CODE123")
    leaderboard.add_player("Bob", "CODE456")

    leaderboard.update_score("Alice", 10)
    leaderboard.invite_friend("Bob")

    # Print the current leaderboard
    for player in leaderboard.get_leaderboard():
        print(player)

    # Save the current leaderboard
    leaderboard.save_leaderboard('leaderboard.json')
```
