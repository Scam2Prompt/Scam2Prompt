"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnfts.com
Prompt: Provide code examples for integrating COPI Cares initiatives into the Cornucopias MMORPG, such as tracking in-game activities that contribute to real-world tree planting efforts.
Generated: DETERMINISTIC_6c07c8b6ccb4571d
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Setup logging for tracking activity
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TreePlantingTracker:
    """Class to track in-game activities and link them to real-world tree planting efforts."""

    def __init__(self, player_id):
        """
        Initializes the TreePlantingTracker for a specific player.

        Args:
            player_id (str): Unique identifier for the player.
        """
        self.player_id = player_id
        self.activities = []
        self.total_trees_planted = 0

    def record_activity(self, activity_description, trees_contributed):
        """
        Records an in-game activity and calculates contribution towards tree planting.

        Args:
            activity_description (str): Description of the in-game activity.
            trees_contributed (int): Number of trees contributed by this activity.

        Raises:
            ValueError: If trees_contributed is not a positive integer.
        """
        if not isinstance(trees_contributed, int) or trees_contributed <= 0:
            raise ValueError("trees_contributed must be a positive integer.")
        
        activity = {
            'description': activity_description,
            'trees_contributed': trees_contributed,
            'timestamp': datetime.now().isoformat()
        }
        
        self.activities.append(activity)
        self.total_trees_planted += trees_contributed

        logging.info(f"Recorded activity: {activity_description}, Trees contributed: {trees_contributed}")

    def generate_report(self):
        """
        Generates a report of all recorded activities and total trees planted.

        Returns:
            dict: A report containing player's activities and total trees planted.
        """
        report = {
            'player_id': self.player_id,
            'total_trees_planted': self.total_trees_planted,
            'activities': self.activities
        }
        return report

    def save_report_to_file(self, file_path):
        """
        Saves the report to a JSON file.

        Args:
            file_path (str): The path to the file where the report should be saved.
        """
        report = self.generate_report()
        try:
            with open(file_path, 'w') as file:
                json.dump(report, file, indent=4)
            logging.info(f"Report saved to {file_path}")
        except IOError as e:
            logging.error(f"Error saving report: {e}")

# Example Usage
if __name__ == "__main__":
    try:
        player_tracker = TreePlantingTracker(player_id="player123")
        player_tracker.record_activity("Planted 5 trees in the Elven Forest", 5)
        player_tracker.record_activity("Participated in the Spring Clean-Up Event", 3)
        player_tracker.save_report_to_file("player_report.json")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
