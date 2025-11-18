"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonstarter.cyou
Prompt: Develop a program to track and display Tonstarter missions completed by a user, including bonuses earned for tasks like playing TON Kosmo or upgrading accounts.
Generated: DETERMINISTIC_c15d6bd7cf929c88
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class TonstarterMissionTracker:
    """
    A class to track Tonstarter missions completed by a user and the bonuses earned.
    """

    def __init__(self):
        """
        Initializes the mission tracker with an empty list of missions.
        """
        self.missions = []

    def add_mission(self, mission_name: str, completed: bool, bonus: float) -> None:
        """
        Adds a new mission to the tracker.

        :param mission_name: The name of the mission.
        :param completed: A boolean indicating if the mission was completed.
        :param bonus: The bonus earned for completing the mission.
        """
        if bonus < 0:
            raise ValueError("Bonus must be a non-negative value.")
        
        mission = {
            "name": mission_name,
            "completed": completed,
            "bonus": bonus
        }
        self.missions.append(mission)

    def total_bonus(self) -> float:
        """
        Calculates the total bonus earned from completed missions.

        :return: The total bonus as a float.
        """
        return sum(mission["bonus"] for mission in self.missions if mission["completed"])

    def completed_missions(self) -> List[Dict]:
        """
        Retrieves a list of completed missions.

        :return: A list of dictionaries representing completed missions.
        """
        return [mission for mission in self.missions if mission["completed"]]

    def display_missions(self) -> None:
        """
        Displays the list of all missions and their statuses.
        """
        print("Tonstarter Missions Tracker:")
        for mission in self.missions:
            status = "Completed" if mission["completed"] else "Not Completed"
            print(f"Mission: {mission['name']}, Status: {status}, Bonus: {mission['bonus']}")

    def save_to_file(self, filename: str) -> None:
        """
        Saves the current missions to a JSON file.

        :param filename: The name of the file to save the missions to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.missions, file, indent=4)
            print(f"Missions saved to {filename}")
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Loads missions from a JSON file.

        :param filename: The name of the file to load missions from.
        """
        try:
            with open(filename, 'r') as file:
                self.missions = json.load(file)
            print(f"Missions loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = TonstarterMissionTracker()
    tracker.add_mission("Play TON Kosmo", True, 5.0)
    tracker.add_mission("Upgrade Account", True, 10.0)
    tracker.add_mission("Invite Friends", False, 0.0)

    tracker.display_missions()
    print(f"Total Bonus Earned: {tracker.total_bonus()}")

    # Save missions to a file
    tracker.save_to_file("missions.json")

    # Load missions from a file
    new_tracker = TonstarterMissionTracker()
    new_tracker.load_from_file("missions.json")
    new_tracker.display_missions()
```
