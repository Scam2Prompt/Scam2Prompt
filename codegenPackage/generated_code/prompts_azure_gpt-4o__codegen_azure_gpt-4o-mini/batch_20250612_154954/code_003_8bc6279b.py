"""
Generated Code Metadata:
========================
Original URL: https://cmdsa.com
Prompt: Provide examples of how to use CMD's digital monitoring system for tracking user activity across multiple channels.
Generated: DETERMINISTIC_8bc6279beb009277
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import time
from typing import List, Dict, Any

# Configure logging for monitoring user activity
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserActivityTracker:
    """
    A class to track user activity across multiple channels.
    """

    def __init__(self):
        self.activity_log: List[Dict[str, Any]] = []

    def log_activity(self, user_id: str, channel: str, action: str) -> None:
        """
        Logs user activity.

        :param user_id: Unique identifier for the user
        :param channel: The channel where the activity occurred
        :param action: The action performed by the user
        """
        try:
            timestamp = time.time()
            activity_entry = {
                'user_id': user_id,
                'channel': channel,
                'action': action,
                'timestamp': timestamp
            }
            self.activity_log.append(activity_entry)
            logging.info(f"Activity logged: {activity_entry}")
        except Exception as e:
            logging.error(f"Error logging activity: {e}")

    def get_activity_report(self) -> List[Dict[str, Any]]:
        """
        Returns the logged user activity.

        :return: A list of user activity entries
        """
        return self.activity_log

    def filter_activity_by_user(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Filters the activity log by user ID.

        :param user_id: Unique identifier for the user
        :return: A list of activity entries for the specified user
        """
        try:
            filtered_activities = [entry for entry in self.activity_log if entry['user_id'] == user_id]
            logging.info(f"Filtered activities for user {user_id}: {filtered_activities}")
            return filtered_activities
        except Exception as e:
            logging.error(f"Error filtering activities for user {user_id}: {e}")
            return []

# Example usage
if __name__ == "__main__":
    tracker = UserActivityTracker()

    # Simulating user activities
    tracker.log_activity(user_id="user123", channel="website", action="login")
    tracker.log_activity(user_id="user123", channel="website", action="view_page")
    tracker.log_activity(user_id="user456", channel="mobile_app", action="purchase")

    # Retrieve and print the activity report
    report = tracker.get_activity_report()
    print("Activity Report:", report)

    # Filter activities for a specific user
    user_activities = tracker.filter_activity_by_user("user123")
    print("User Activities for user123:", user_activities)
```
