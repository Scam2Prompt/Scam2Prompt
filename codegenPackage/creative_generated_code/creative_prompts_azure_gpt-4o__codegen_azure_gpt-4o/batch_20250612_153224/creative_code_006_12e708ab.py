"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lalitarora.in
Prompt: Create a Python script to track weekly progress in a coaching program, similar to the features in Dr. Lalit Arora's Gold Plus Membership.
Generated: DETERMINISTIC_12e708ab22ae6758
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime, timedelta

class CoachingProgressTracker:
    def __init__(self, data_file="progress_data.json"):
        """
        Initialize the progress tracker with a file for storing progress data.
        
        :param data_file: The path to the JSON file where progress data will be saved.
        """
        self.data_file = data_file
        self.progress_data = self._load_data()

    def _load_data(self):
        """
        Load progress data from a JSON file. If the file doesn't exist, initialize it.
        
        :return: A dictionary containing the progress data.
        """
        if not os.path.exists(self.data_file):
            return {}
        
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {}

    def _save_data(self):
        """
        Save progress data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.progress_data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_weekly_progress(self, user_id, week_number, progress_details):
        """
        Add or update weekly progress for a specific user.

        :param user_id: A unique identifier for the user.
        :param week_number: The week number in the coaching program (e.g., 1, 2, 3, ...).
        :param progress_details: A dictionary containing progress details (e.g., tasks completed, comments, etc.).
        """
        if user_id not in self.progress_data:
            self.progress_data[user_id] = {}
        
        self.progress_data[user_id][week_number] = {
            "progress_details": progress_details,
            "updated_at": datetime.now().isoformat()
        }
        self._save_data()

    def get_progress(self, user_id, week_number=None):
        """
        Retrieve progress for a specific user. Optionally retrieve progress for a specific week.

        :param user_id: A unique identifier for the user.
        :param week_number: (Optional) The week number to retrieve progress for. If None, return all progress.
        :return: Progress data for the user.
        """
        user_progress = self.progress_data.get(user_id, None)
        if user_progress is None:
            return f"No progress found for user ID {user_id}."
        
        if week_number:
            return user_progress.get(week_number, f"No progress found for week {week_number}.")
        
        return user_progress

    def delete_progress(self, user_id, week_number=None):
        """
        Delete progress for a specific user. Optionally delete progress for a specific week.

        :param user_id: A unique identifier for the user.
        :param week_number: (Optional) The week number to delete progress for. If None, delete all progress for the user.
        """
        if user_id not in self.progress_data:
            print(f"No progress found for user ID {user_id}.")
            return
        
        if week_number:
            if week_number in self.progress_data[user_id]:
                del self.progress_data[user_id][week_number]
                print(f"Progress for week {week_number} deleted for user ID {user_id}.")
            else:
                print(f"No progress found for week {week_number} for user ID {user_id}.")
        else:
            del self.progress_data[user_id]
            print(f"All progress deleted for user ID {user_id}.")
        
        self._save_data()

# Example Usage
if __name__ == "__main__":
    tracker = CoachingProgressTracker()

    # Add weekly progress
    tracker.add_weekly_progress(
        user_id="user123", 
        week_number=1, 
        progress_details={"tasks_completed": 5, "comments": "Great start!"}
    )

    # Retrieve progress
    print(tracker.get_progress("user123"))  # Get all progress for user
    print(tracker.get_progress("user123", week_number=1))  # Get progress for week 1

    # Delete progress for a specific week
    tracker.delete_progress("user123", week_number=1)

    # Delete all progress for a user
    tracker.delete_progress("user123")
```
