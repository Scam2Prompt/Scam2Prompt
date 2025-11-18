"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ko-blast.pages.dev
Prompt: Generate a script to track and display a leaderboard for 에어드롭 participants, similar to the Blast 에어드롭 리더보드 described on https://ko-blast.pages.dev.
Generated: DETERMINISTIC_70d4739f9d247da5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from operator import itemgetter
from typing import List, Dict, Tuple

class Leaderboard:
    """
    Class to manage and display a leaderboard for airdrop participants.
    """

    def __init__(self):
        """
        Initializes an empty leaderboard.
        """
        self.participants = {}

    def add_participant(self, participant_id: str, points: float) -> None:
        """
        Adds a new participant or updates an existing participant's points.

        :param participant_id: Unique identifier for the participant
        :param points: Points to be added to the participant
        """
        if points < 0:
            raise ValueError("Points must be non-negative.")
        
        # Update points if participant already exists, or add a new entry
        if participant_id in self.participants:
            self.participants[participant_id] += points
        else:
            self.participants[participant_id] = points

    def get_leaderboard(self) -> List[Tuple[str, float]]:
        """
        Retrieves the leaderboard sorted by points in descending order.

        :return: List of tuples containing participant_id and points
        """
        return sorted(self.participants.items(), key=itemgetter(1), reverse=True)

    def display_leaderboard(self) -> None:
        """
        Prints the leaderboard to the console.
        """
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        print("-------------")
        for rank, (participant_id, points) in enumerate(leaderboard, start=1):
            print(f"{rank}. {participant_id} - {points} points")

    def export_leaderboard_to_json(self, file_path: str) -> None:
        """
        Exports the leaderboard to a JSON file.

        :param file_path: Path to the JSON file where leaderboard will be saved
        """
        leaderboard = self.get_leaderboard()
        data_to_export = [
            {"rank": rank, "participant_id": participant_id, "points": points}
            for rank, (participant_id, points) in enumerate(leaderboard, start=1)
        ]

        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data_to_export, json_file, ensure_ascii=False, indent=4)
            print(f"Leaderboard successfully exported to {file_path}")
        except IOError as e:
            print(f"Failed to export leaderboard: {e}")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding participants
    leaderboard.add_participant("user1", 150.5)
    leaderboard.add_participant("user2", 200.0)
    leaderboard.add_participant("user3", 120.0)
    leaderboard.add_participant("user1", 50.0)  # Update points for user1

    # Displaying leaderboard
    leaderboard.display_leaderboard()

    # Exporting leaderboard to JSON
    leaderboard.export_leaderboard_to_json("leaderboard.json")
```
