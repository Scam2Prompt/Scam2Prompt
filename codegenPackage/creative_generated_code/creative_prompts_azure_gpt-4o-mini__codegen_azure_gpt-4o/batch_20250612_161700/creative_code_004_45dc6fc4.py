"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Provide an example of how to implement a leaderboard feature in a game that tracks user earnings and ranks players based on their trading performance in Meme Moguls.
Generated: DETERMINISTIC_45dc6fc44d83e218
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

import json
from typing import List, Dict


class Leaderboard:
    """
    A class to manage the leaderboard for Meme Moguls trading performance.
    Tracks user earnings and ranks players based on their trading performance.
    """

    def __init__(self):
        """
        Initializes an empty leaderboard.
        """
        self.leaderboard: List[Dict[str, float]] = []

    def add_player(self, username: str, earnings: float):
        """
        Adds a player to the leaderboard or updates their earnings if they already exist.

        Args:
            username (str): The username of the player.
            earnings (float): The earnings of the player.
        """
        if not isinstance(username, str) or not isinstance(earnings, (int, float)):
            raise ValueError("Invalid data types. 'username' must be a string and 'earnings' a number.")

        # Check if the player already exists
        player_found = False
        for player in self.leaderboard:
            if player["username"] == username:
                player["earnings"] = earnings
                player_found = True
                break

        # Add the player if they do not exist
        if not player_found:
            self.leaderboard.append({"username": username, "earnings": earnings})

        # Sort the leaderboard after the update
        self.sort_leaderboard()

    def sort_leaderboard(self):
        """
        Sorts the leaderboard in descending order based on earnings.
        """
        self.leaderboard.sort(key=lambda player: player["earnings"], reverse=True)

    def get_leaderboard(self, top_n: int = None) -> List[Dict[str, float]]:
        """
        Retrieves the leaderboard, optionally limited to top N players.

        Args:
            top_n (int, optional): The number of top players to retrieve. Defaults to None (all players).

        Returns:
            List[Dict[str, float]]: The sorted leaderboard.
        """
        if top_n is not None:
            if not isinstance(top_n, int) or top_n <= 0:
                raise ValueError("Invalid value for 'top_n'. It must be a positive integer.")
            return self.leaderboard[:top_n]
        return self.leaderboard

    def save_to_file(self, filename: str):
        """
        Saves the leaderboard to a JSON file.

        Args:
            filename (str): The name of the file to save the leaderboard to.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.leaderboard, file)
        except Exception as e:
            raise RuntimeError(f"Failed to save leaderboard to file: {e}")

    def load_from_file(self, filename: str):
        """
        Loads the leaderboard from a JSON file.

        Args:
            filename (str): The name of the file to load the leaderboard from.
        """
        try:
            with open(filename, "r") as file:
                self.leaderboard = json.load(file)
                self.sort_leaderboard()  # Ensure the leaderboard remains sorted
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Failed to decode JSON from file '{filename}'.")
        except Exception as e:
            raise RuntimeError(f"Failed to load leaderboard from file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the leaderboard
    leaderboard = Leaderboard()

    # Add players
    leaderboard.add_player("Player1", 1500.5)
    leaderboard.add_player("Player2", 2000.0)
    leaderboard.add_player("Player3", 1800.0)

    # Update a player's earnings
    leaderboard.add_player("Player1", 2500.0)

    # Display the full leaderboard
    print("Full Leaderboard:")
    print(leaderboard.get_leaderboard())

    # Display the top 2 players
    print("\nTop 2 Players:")
    print(leaderboard.get_leaderboard(top_n=2))

    # Save the leaderboard to a file
    leaderboard.save_to_file("leaderboard.json")

    # Load the leaderboard from a file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_from_file("leaderboard.json")
    print("\nLoaded Leaderboard:")
    print(new_leaderboard.get_leaderboard())
```
