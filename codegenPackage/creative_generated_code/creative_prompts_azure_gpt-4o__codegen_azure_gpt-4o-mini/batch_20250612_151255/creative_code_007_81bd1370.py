"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixelverse-dashboard.pages.dev
Prompt: Write a function to track and display user activity inside a dashboard, similar to the activity-based rewards system in Pixelverse.
Generated: DETERMINISTIC_81bd137009dbfbc9
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import List, Dict

class UserActivityTracker:
    """
    A class to track user activity within a dashboard for an activity-based rewards system.
    """

    def __init__(self):
        """Initialize the activity tracker with an empty activity log."""
        self.activity_log: List[Dict] = []

    def log_activity(self, user_id: str, activity: str) -> None:
        """
        Log a user's activity with a timestamp.

        :param user_id: Unique identifier for the user.
        :param activity: Description of the activity performed by the user.
        :raises ValueError: If user_id or activity is empty.
        """
        if not user_id or not activity:
            raise ValueError("User ID and activity must not be empty.")
        
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        activity_entry = {
            'user_id': user_id,
            'activity': activity,
            'timestamp': timestamp
        }
        self.activity_log.append(activity_entry)
        print(f"Activity logged: {activity_entry}")

    def get_activity_summary(self, user_id: str) -> List[Dict]:
        """
        Retrieve a summary of activities for a specific user.

        :param user_id: Unique identifier for the user.
        :return: A list of activities performed by the user.
        :raises ValueError: If user_id is empty.
        """
        if not user_id:
            raise ValueError("User ID must not be empty.")

        user_activities = [entry for entry in self.activity_log if entry['user_id'] == user_id]
        return user_activities

    def display_activity(self, user_id: str) -> None:
        """
        Display the user's activity in a readable format.

        :param user_id: Unique identifier for the user.
        :raises ValueError: If user_id is empty.
        """
        activities = self.get_activity_summary(user_id)

        if not activities:
            print(f"No activity found for user: {user_id}")
            return

        print(f"Activity summary for user {user_id}:")
        for activity in activities:
            print(f"[{activity['timestamp']}] {activity['activity']}")

# Example usage of the UserActivityTracker class
if __name__ == "__main__":
    tracker = UserActivityTracker()
    
    # Log some activities
    tracker.log_activity("user123", "Logged in")
    tracker.log_activity("user123", "Viewed dashboard")
    tracker.log_activity("user456", "Logged out")
    
    # Display user activity
    tracker.display_activity("user123")
    tracker.display_activity("user456")
    tracker.display_activity("user789")  # No activity
```
