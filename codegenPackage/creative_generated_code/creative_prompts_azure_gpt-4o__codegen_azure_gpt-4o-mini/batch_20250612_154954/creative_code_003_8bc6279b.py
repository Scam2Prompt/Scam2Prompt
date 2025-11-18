"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmdsa.com
Prompt: Provide examples of how to use CMD's digital monitoring system for tracking user activity across multiple channels.
Generated: DETERMINISTIC_8bc6279beb009277
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserActivityMonitor:
    def __init__(self, user_id):
        """
        Initializes the UserActivityMonitor with a specific user ID.
        
        :param user_id: str - Unique identifier for the user
        """
        self.user_id = user_id
        self.activity_log = []

    def log_activity(self, channel, activity):
        """
        Logs user activity to the activity log.

        :param channel: str - The communication channel where the activity took place
        :param activity: str - Description of the user activity
        """
        timestamp = datetime.now()
        entry = {
            'timestamp': timestamp,
            'channel': channel,
            'activity': activity
        }
        self.activity_log.append(entry)
        logging.info(f"Activity logged: {entry}")

    def get_activity_history(self, start_time=None, end_time=None):
        """
        Retrieves the user's activity history within the specified time range.
        
        :param start_time: datetime - Start of the time range (inclusive)
        :param end_time: datetime - End of the time range (exclusive)
        :return: list - List of activities within the specified time range
        """
        if start_time is None:
            start_time = datetime.now() - timedelta(days=7)  # Default to last 7 days
        if end_time is None:
            end_time = datetime.now()

        filtered_activity = [
            entry for entry in self.activity_log
            if start_time <= entry['timestamp'] < end_time
        ]
        
        return filtered_activity

    def clear_activity_log(self):
        """
        Clears the activity log for the user.
        """
        self.activity_log.clear()
        logging.info("Activity log cleared.")

# Example usage of UserActivityMonitor
if __name__ == "__main__":
    try:
        # Create an instance of UserActivityMonitor for a specific user
        user_monitor = UserActivityMonitor(user_id="user123")

        # Simulate logging user activities
        user_monitor.log_activity(channel="email", activity="Opened promotional email.")
        user_monitor.log_activity(channel="social_media", activity="Liked a post.")
        user_monitor.log_activity(channel="website", activity="Browsed products.")

        # Retrieve user's activity history in the last 7 days
        history = user_monitor.get_activity_history()
        logging.info(f"User activity history: {history}")

        # Clear the activity log if needed
        user_monitor.clear_activity_log()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
