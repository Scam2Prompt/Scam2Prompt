"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masterclicsolutions.com
Prompt: Write code to implement a feature for tracking and analyzing user engagement in gamified e-learning courses, as described by MasterClic Solutions.
Generated: DETERMINISTIC_ba25f36966071de8
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Engagement Tracker for Gamified E-Learning Courses

This script implements a feature to track and analyze user engagement in gamified e-learning courses.
It includes functionalities to log user actions, calculate engagement metrics, and generate reports.

Author: MasterClic Solutions
Date: YYYY-MM-DD
"""

import datetime
import json
import os

class EngagementTracker:
    """
    A class to track and analyze user engagement in gamified e-learning courses.
    """

    def __init__(self, data_file="engagement_data.json"):
        """
        Initialize the EngagementTracker instance.
        
        Args:
            data_file (str): Path to the file where engagement data will be stored.
        """
        self.data_file = data_file
        self.engagement_data = {}
        self._load_data()

    def _load_data(self):
        """
        Load engagement data from file (if it exists).
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    self.engagement_data = json.load(file)
            except json.JSONDecodeError:
                # Handle corrupted or invalid JSON
                print("Warning: Corrupted data file. Starting with empty data.")
                self.engagement_data = {}
        else:
            self.engagement_data = {}

    def _save_data(self):
        """
        Save engagement data to file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.engagement_data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def log_action(self, user_id, action_type, course_id):
        """
        Log a user action in the engagement data.
        
        Args:
            user_id (str): Unique identifier of the user.
            action_type (str): Type of action (e.g., "quiz_completed", "lesson_viewed").
            course_id (str): Unique identifier of the course.
        """
        timestamp = datetime.datetime.now().isoformat()
        if user_id not in self.engagement_data:
            self.engagement_data[user_id] = []
        self.engagement_data[user_id].append({
            "action_type": action_type,
            "course_id": course_id,
            "timestamp": timestamp
        })
        self._save_data()

    def calculate_engagement_score(self, user_id):
        """
        Calculate the engagement score for a given user.
        
        Args:
            user_id (str): Unique identifier of the user.
        
        Returns:
            float: Engagement score based on logged actions.
        """
        if user_id not in self.engagement_data:
            return 0.0
        
        actions = self.engagement_data[user_id]
        # Example scoring logic: 10 points for "quiz_completed", 5 points for "lesson_viewed"
        score_mapping = {
            "quiz_completed": 10,
            "lesson_viewed": 5
        }
        score = sum(score_mapping.get(action["action_type"], 0) for action in actions)

        return score

    def generate_report(self):
        """
        Generate a report of user engagement across all users.
        
        Returns:
            dict: Report containing user IDs and their respective engagement scores.
        """
        report = {user_id: self.calculate_engagement_score(user_id) for user_id in self.engagement_data}
        return report


# Example usage
if __name__ == "__main__":
    tracker = EngagementTracker()

    # Log some actions
    tracker.log_action(user_id="user123", action_type="quiz_completed", course_id="courseA")
    tracker.log_action(user_id="user123", action_type="lesson_viewed", course_id="courseA")
    tracker.log_action(user_id="user456", action_type="quiz_completed", course_id="courseB")

    # Calculate engagement score for a user
    user_score = tracker.calculate_engagement_score("user123")
    print(f"Engagement score for user123: {user_score}")

    # Generate a report of all users
    report = tracker.generate_report()
    print("Engagement Report:", report)
```
