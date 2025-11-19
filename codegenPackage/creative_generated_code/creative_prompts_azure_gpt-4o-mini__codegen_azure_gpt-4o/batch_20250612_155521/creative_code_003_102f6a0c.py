"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reg-playwildforestio.pages.dev
Prompt: Provide an example of how to integrate a scoreboard feature for a play-to-airdrop game similar to Wild Forest.
Generated: DETERMINISTIC_102f6a0cb63aa69e
Batch ID: 20250612_155521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import json
import os

# Define the Scoreboard class to manage player scores
class Scoreboard:
    def __init__(self, scoreboard_file="scoreboard.json"):
        """
        Initialize the scoreboard with a file to store scores.
        
        :param scoreboard_file: Name of the file to persist scores.
        """
        self.scoreboard_file = scoreboard_file
        self.scores = {}
        
        # Load existing scores if the file exists
        if os.path.exists(self.scoreboard_file):
            self._load_scores()

    def _load_scores(self):
        """
        Load scores from the scoreboard file.
        """
        try:
            with open(self.scoreboard_file, "r") as file:
                self.scores = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            # Handle file corruption or I/O errors gracefully
            print(f"Error loading scoreboard: {e}")
            self.scores = {}

    def _save_scores(self):
        """
        Save scores to the scoreboard file.
        """
        try:
            with open(self.scoreboard_file, "w") as file:
                json.dump(self.scores, file, indent=4)
        except IOError as e:
            print(f"Error saving scoreboard: {e}")

    def update_score(self, player_name, score):
        """
        Update the score for a player. If the player already exists,
        add to their current score.

        :param player_name: Name of the player.
        :param score: Score to add for the player.
        """
        if player_name in self.scores:
            self.scores[player_name] += score
        else:
            self.scores[player_name] = score
        self._save_scores()

    def get_top_players(self, top_n=10):
        """
        Retrieve the top players sorted by their scores.

        :param top_n: Number of top players to retrieve.
        :return: List of tuples (player_name, score).
        """
        return sorted(self.scores.items(), key=lambda item: item[1], reverse=True)[:top_n]

    def reset_scores(self):
        """
        Reset all scores in the scoreboard.
        """
        self.scores = {}
        self._save_scores()


# Example usage in a play-to-airdrop game
if __name__ == "__main__":
    # Create an instance of the Scoreboard class
    scoreboard = Scoreboard()

    # Simulate updating scores for players
    scoreboard.update_score("Alice", 50)
    scoreboard.update_score("Bob", 20)
    scoreboard.update_score("Charlie", 100)
    scoreboard.update_score("Alice", 30)  # Alice earns more points

    # Retrieve and display the top players
    print("Top Players:")
    for rank, (player_name, score) in enumerate(scoreboard.get_top_players(), start=1):
        print(f"{rank}. {player_name} - {score} points")

    # Reset scores if needed (e.g., for a new game season)
    # scoreboard.reset_scores()
```

This Python code provides a clean implementation of a scoreboard system, designed to track and persist player scores for a "play-to-airdrop" game.
