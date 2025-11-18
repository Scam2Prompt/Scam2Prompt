"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harpycoin.pages.dev
Prompt: Generate code for a contest leaderboard system that tracks and displays the highest buy contest results for HarpyCoin, including meme and shill contest submissions.
Generated: DETERMINISTIC_e5fe97f0ad3aba50
Batch ID: 20250612_151024
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

class Leaderboard:
    """
    A class to represent a contest leaderboard for HarpyCoin.
    It tracks and displays the highest buy contest results for meme and shill contest submissions.
    """

    def __init__(self):
        """
        Initializes the leaderboard with an empty list of scores.
        """
        self.scores: List[Dict[str, Any]] = []

    def add_submission(self, username: str, score: float, contest_type: str) -> None:
        """
        Adds a new contest submission to the leaderboard.

        Args:
            username (str): The username of the participant.
            score (float): The score submitted by the participant.
            contest_type (str): The type of contest ('meme' or 'shill').

        Raises:
            ValueError: If the score is negative or contest_type is invalid.
        """
        if score < 0:
            raise ValueError("Score cannot be negative.")
        if contest_type not in ('meme', 'shill'):
            raise ValueError("Contest type must be 'meme' or 'shill'.")

        self.scores.append({
            'username': username,
            'score': score,
            'contest_type': contest_type
        })

    def get_leaderboard(self, contest_type: str) -> List[Dict[str, Any]]:
        """
        Retrieves the leaderboard for a specific contest type sorted by score in descending order.

        Args:
            contest_type (str): The type of contest ('meme' or 'shill').

        Returns:
            List[Dict[str, Any]]: A sorted list of the leaderboard entries for the specified contest type.

        Raises:
            ValueError: If contest_type is invalid.
        """
        if contest_type not in ('meme', 'shill'):
            raise ValueError("Contest type must be 'meme' or 'shill'.")

        # Filter and sort the scores for the specified contest type
        filtered_scores = [entry for entry in self.scores if entry['contest_type'] == contest_type]
        return sorted(filtered_scores, key=lambda x: x['score'], reverse=True)

    def save_to_file(self, filename: str) -> None:
        """
        Saves the leaderboard data to a JSON file.

        Args:
            filename (str): The name of the file to save the leaderboard data.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.scores, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Loads leaderboard data from a JSON file.

        Args:
            filename (str): The name of the file to load the leaderboard data from.

        Raises:
            IOError: If the file cannot be read.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.scores = json.load(file)
        except IOError as e:
            raise IOError(f"An error occurred while reading from file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON format: {e}")

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding submissions
    leaderboard.add_submission("User1", 150.0, "meme")
    leaderboard.add_submission("User2", 200.0, "shill")
    leaderboard.add_submission("User3", 250.0, "meme")

    # Retrieve and print the meme leaderboard
    print("Meme Leaderboard:")
    print(leaderboard.get_leaderboard("meme"))

    # Save leaderboard to file
    leaderboard.save_to_file("leaderboard.json")

    # Load leaderboard from file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_from_file("leaderboard.json")
    print("Loaded Leaderboard:")
    print(new_leaderboard.get_leaderboard("meme"))
```
