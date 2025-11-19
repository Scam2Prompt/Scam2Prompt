"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playemberssssssssssssss.pages.dev
Prompt: Create a function that tracks user downloads and active users for a mobile game, using metrics similar to those highlighted by Playember.
Generated: DETERMINISTIC_d8ba5a2982f13b08
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from collections import defaultdict
import json

class GameMetricsTracker:
    def __init__(self):
        """
        Initialize the GameMetricsTracker with default dictionaries
        to track downloads and active users.
        """
        self.downloads = 0
        self.active_users = set()
        self.user_activity = defaultdict(list)

    def record_download(self, user_id):
        """
        Record a new download for a user.

        Args:
            user_id (str): Unique identifier for the user.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        
        self.downloads += 1
        self.active_users.add(user_id)
        self.user_activity[user_id].append({
            "event": "download",
            "timestamp": datetime.datetime.now().isoformat()
        })

    def record_activity(self, user_id):
        """
        Record user activity for an active user.

        Args:
            user_id (str): Unique identifier for the user.
        """
        if user_id not in self.active_users:
            raise ValueError("User is not active. Please record a download first.")
        
        self.user_activity[user_id].append({
            "event": "activity",
            "timestamp": datetime.datetime.now().isoformat()
        })

    def get_metrics(self):
        """
        Get the current metrics for downloads and active users.

        Returns:
            dict: A dictionary containing the number of downloads 
                  and the list of active users.
        """
        return {
            "downloads": self.downloads,
            "active_users": list(self.active_users),
            "user_activity": self.user_activity
        }

    def save_metrics_to_file(self, file_path):
        """
        Save the current metrics to a JSON file.

        Args:
            file_path (str): The path to the file where metrics will be saved.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.get_metrics(), f, indent=4)
        except IOError as e:
            raise Exception(f"Failed to write metrics to file: {e}")

# Example Usage
if __name__ == "__main__":
    tracker = GameMetricsTracker()
    
    # Simulating user downloads and activity
    try:
        tracker.record_download("user123")
        tracker.record_activity("user123")
        
        tracker.record_download("user456")
        
        # Save metrics to file
        tracker.save_metrics_to_file("game_metrics.json")
        
        print("Metrics tracked successfully.")
    except Exception as e:
        print(f"Error tracking metrics: {e}")
```
