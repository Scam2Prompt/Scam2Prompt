"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://private-gomble.pages.dev
Prompt: Write code for a leaderboard system that ranks players based on their balloon height achievements, as described in GOMBLE's competitive gameplay.
Generated: DETERMINISTIC_5ec01c0f63ce87cb
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

# Import required modules
import json

class Leaderboard:
    """
    A class to manage the leaderboard for players based
    on their balloon height achievements.
    """
    def __init__(self):
        # Initialize the leaderboard as an empty dictionary
        # Keys will be player names, values will be their balloon heights
        self.leaderboard = {}

    def update_score(self, player_name, balloon_height):
        """
        Update the leaderboard with the new score for a player.
        If the player already exists, keep the highest score.

        :param player_name: str - The name of the player
        :param balloon_height: int - The height achieved by the player
        """
        if not isinstance(player_name, str) or not isinstance(balloon_height, (int, float)):
            raise ValueError("Invalid player_name or balloon_height. Make sure player_name is a string and balloon_height is a number.")

        # Update the leaderboard
        if player_name in self.leaderboard:
            # Keep the highest score
            self.leaderboard[player_name] = max(self.leaderboard[player_name], balloon_height)
        else:
            # Add the new player to the leaderboard
            self.leaderboard[player_name] = balloon_height

    def get_top_players(self, n=10):
        """
        Get the top N players sorted by their balloon height in descending order.

        :param n: int - The number of top players to return (default is 10)
        :return: list - A list of tuples (player_name, balloon_height)
        """
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Parameter 'n' must be a positive integer.")

        # Sort the leaderboard based on balloon height (descending)
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)

        # Return the top N players
        return sorted_leaderboard[:n]

    def save_to_file(self, file_path):
        """
        Save the current leaderboard to a file in JSON format.

        :param file_path: str - The path of the file to save the leaderboard
        """
        if not isinstance(file_path, str):
            raise ValueError("file_path must be a string.")

        try:
            with open(file_path, 'w') as file:
                json.dump(self.leaderboard, file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save leaderboard to file: {str(e)}")

    def load_from_file(self, file_path):
        """
        Load the leaderboard from a file in JSON format.

        :param file_path: str - The path of the file to load the leaderboard
        """
        if not isinstance(file_path, str):
            raise ValueError("file_path must be a string.")

        try:
            with open(file_path, 'r') as file:
                self.leaderboard = json.load(file)
        except Exception as e:
            raise IOError(f"Failed to load leaderboard from file: {str(e)}")


# Example usage:
if __name__ == "__main__":
    # Instantiate the leaderboard
    leaderboard = Leaderboard()

    # Update scores
    leaderboard.update_score("Player1", 150)
    leaderboard.update_score("Player2", 200)
    leaderboard.update_score("Player1", 180)
    leaderboard.update_score("Player3", 120)

    # Get top players
    top_players = leaderboard.get_top_players(n=3)
    print("Top Players:", top_players)

    # Save leaderboard to file
    leaderboard.save_to_file("leaderboard.json")

    # Load leaderboard from file
    leaderboard.load_from_file("leaderboard.json")
    print("Loaded Leaderboard:", leaderboard.leaderboard)
```
