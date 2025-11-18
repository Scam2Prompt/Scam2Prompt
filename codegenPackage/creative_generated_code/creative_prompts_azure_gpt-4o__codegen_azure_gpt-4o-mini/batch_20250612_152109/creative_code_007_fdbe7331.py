"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub-claim.pages.dev
Prompt: Generate code for a leaderboard system that tracks social influence and PvP Duel Race outcomes in the Bitcoin Dogs Club game.
Generated: DETERMINISTIC_fdbe73319c95f52e
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Any

class Leaderboard:
    def __init__(self, file_path: str):
        """
        Initializes the Leaderboard with a given file path for storing leaderboard data.
        
        :param file_path: The path to the JSON file that stores leaderboard data.
        """
        self.file_path = file_path
        self.leaderboard_data = self.load_leaderboard()

    def load_leaderboard(self) -> Dict[str, Any]:
        """
        Loads leaderboard data from a JSON file. If the file does not exist, initializes an empty leaderboard.
        
        :return: A dictionary containing the leaderboard data.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return {}

    def save_leaderboard(self):
        """
        Saves the current leaderboard data to a JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.leaderboard_data, file, indent=4)

    def update_score(self, user_id: str, influence: int, duel_wins: int):
        """
        Updates the score for a user based on their social influence and duel race outcomes.
        
        :param user_id: Unique identifier for the user.
        :param influence: The social influence score of the user.
        :param duel_wins: The number of PvP duel races won by the user.
        """
        if user_id not in self.leaderboard_data:
            self.leaderboard_data[user_id] = {
                'influence': 0,
                'duel_wins': 0
            }

        self.leaderboard_data[user_id]['influence'] += influence
        self.leaderboard_data[user_id]['duel_wins'] += duel_wins
        self.save_leaderboard()

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        """
        Retrieves the leaderboard sorted by influence and duel wins.
        
        :return: A list of users sorted by their scores.
        """
        sorted_leaderboard = sorted(
            self.leaderboard_data.items(),
            key=lambda item: (item[1]['influence'], item[1]['duel_wins']),
            reverse=True
        )
        return [{"user_id": user_id, **data} for user_id, data in sorted_leaderboard]

    def display_leaderboard(self):
        """
        Displays the leaderboard in a formatted manner.
        """
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        print("{:<20} | {:<10} | {:<10}".format("User ID", "Influence", "Duel Wins"))
        print("-" * 50)
        for entry in leaderboard:
            print("{:<20} | {:<10} | {:<10}".format(entry['user_id'], entry['influence'], entry['duel_wins']))

# Example usage of the Leaderboard class
if __name__ == "__main__":
    leaderboard = Leaderboard("leaderboard.json")

    # Update scores for demonstration
    leaderboard.update_score("user123", 50, 3)
    leaderboard.update_score("user456", 70, 1)
    leaderboard.update_score("user123", 30, 2)

    # Display the leaderboard
    leaderboard.display_leaderboard()
```
