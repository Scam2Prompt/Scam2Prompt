"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Generate a code snippet that demonstrates how to create a leaderboard for players in SIMemes, tracking their poop collection and resource management.
Generated: DETERMINISTIC_bcc5c3af22bcf092
Batch ID: 20250612_162511
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

class Leaderboard:
    """
    A class to manage a leaderboard for players in SIMemes,
    tracking their poop collection and resource management.
    """
    def __init__(self):
        # Dictionary to hold player data in the format:
        # { "player_name": {"poop_collected": int, "resources_managed": int} }
        self.players = {}

    def add_player(self, player_name):
        """
        Adds a new player to the leaderboard.
        :param player_name: The name of the player to add.
        """
        if player_name in self.players:
            print(f"Player '{player_name}' already exists.")
            return
        self.players[player_name] = {"poop_collected": 0, "resources_managed": 0}
        print(f"Player '{player_name}' added successfully.")

    def update_player_stats(self, player_name, poop_collected=0, resources_managed=0):
        """
        Updates the stats of a player.
        :param player_name: The name of the player to update.
        :param poop_collected: The amount of poop collected to add.
        :param resources_managed: The amount of resources managed to add.
        """
        if player_name not in self.players:
            print(f"Player '{player_name}' does not exist.")
            return

        self.players[player_name]["poop_collected"] += poop_collected
        self.players[player_name]["resources_managed"] += resources_managed
        print(f"Player '{player_name}' stats updated.")

    def get_leaderboard(self):
        """
        Returns the leaderboard sorted by poop_collected
        (primary) and resources_managed (secondary).
        :return: A list of tuples in the format:
                 [("player_name", poop_collected, resources_managed), ...]
        """
        return sorted(
            [(name, stats["poop_collected"], stats["resources_managed"]) 
             for name, stats in self.players.items()],
            key=lambda x: (x[1], x[2]),  # Sort by poop_collected, then resources_managed
            reverse=True                 # Descending order
        )

    def save_leaderboard(self, file_path):
        """
        Saves the leaderboard to a JSON file.
        :param file_path: Path to the file where leaderboard will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.players, file, indent=4)
            print(f"Leaderboard saved to '{file_path}'.")
        except Exception as e:
            print(f"Error saving leaderboard: {e}")

    def load_leaderboard(self, file_path):
        """
        Loads the leaderboard from a JSON file.
        :param file_path: Path to the file from which leaderboard will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.players = json.load(file)
            print(f"Leaderboard loaded from '{file_path}'.")
        except Exception as e:
            print(f"Error loading leaderboard: {e}")


# Example usage (uncomment to run):
# leaderboard = Leaderboard()
# leaderboard.add_player("Player1")
# leaderboard.add_player("Player2")
# leaderboard.update_player_stats("Player1", poop_collected=10, resources_managed=5)
# leaderboard.update_player_stats("Player2", poop_collected=8, resources_managed=7)
# print("Leaderboard:", leaderboard.get_leaderboard())
# leaderboard.save_leaderboard("leaderboard.json")
# leaderboard.load_leaderboard("leaderboard.json")
```
