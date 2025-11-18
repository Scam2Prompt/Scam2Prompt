"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimplena.vercel.app
Prompt: Create a function to track leaderboard rankings for participants in the $PLENA Quest using data provided by Galxe and Plena Finance.
Generated: DETERMINISTIC_5e5934c05fb728c3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Tuple

class Leaderboard:
    """
    A class to represent the leaderboard for $PLENA Quest participants.
    It tracks rankings based on data provided by Galxe and Plena Finance.
    """

    def __init__(self):
        """
        Initialize an empty leaderboard.
        """
        self.leaderboard = {}  # Stores participant data as {user_id: score}

    def update_score(self, user_id: str, score: float) -> None:
        """
        Updates the score for a participant. If the user does not exist, adds them to the leaderboard.

        :param user_id: Unique identifier for the participant.
        :param score: A numeric score to be added to the participant's total.
        """
        if not user_id or not isinstance(score, (int, float)) or score < 0:
            raise ValueError("Invalid user_id or score. Ensure user_id is non-empty and score is a positive number.")

        # Update existing score or add new participant
        self.leaderboard[user_id] = self.leaderboard.get(user_id, 0) + score

    def get_rankings(self) -> List[Tuple[str, float]]:
        """
        Returns the leaderboard rankings sorted by score in descending order.

        :return: A list of tuples in the format [(user_id, score), ...] sorted by score (highest to lowest).
        """
        return sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)

    def to_json(self) -> str:
        """
        Converts the leaderboard data to a JSON string for export.

        :return: A JSON string representation of the leaderboard.
        """
        return json.dumps(self.leaderboard, indent=4)

    def load_from_json(self, json_data: str) -> None:
        """
        Loads leaderboard data from a JSON string.

        :param json_data: A JSON string containing leaderboard data.
        """
        try:
            data = json.loads(json_data)
            if not isinstance(data, dict):
                raise ValueError("Invalid JSON format. Expected a dictionary.")
            self.leaderboard = {k: float(v) for k, v in data.items()}
        except (json.JSONDecodeError, ValueError) as e:
            raise ValueError(f"Failed to load leaderboard data: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the leaderboard
        lb = Leaderboard()

        # Update scores for participants
        lb.update_score("user_1", 150.5)
        lb.update_score("user_2", 99.9)
        lb.update_score("user_3", 200)
        lb.update_score("user_1", 50)  # Increment existing user's score

        # Print current rankings
        print("Current Rankings:")
        for rank, (user_id, score) in enumerate(lb.get_rankings(), start=1):
            print(f"{rank}. {user_id}: {score}")

        # Export leaderboard to JSON
        json_data = lb.to_json()
        print("\nLeaderboard JSON:")
        print(json_data)

        # Load data from JSON (simulation)
        new_lb = Leaderboard()
        new_lb.load_from_json(json_data)
        print("\nLoaded Rankings from JSON:")
        for rank, (user_id, score) in enumerate(new_lb.get_rankings(), start=1):
            print(f"{rank}. {user_id}: {score}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
