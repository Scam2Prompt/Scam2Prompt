"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: Can you provide a code example for tracking user earnings and activity statistics for a platform like AUTOBUX?
Generated: DETERMINISTIC_15b50c745d0bfe31
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class UserActivityTracker:
    """
    A class to track user earnings and activity statistics for a platform like AUTOBUX.
    """

    def __init__(self, user_id):
        """
        Initializes the activity tracker for a specific user.
        Args:
            user_id (str): Unique identifier for the user.
        """
        self.user_id = user_id
        self.earnings = 0.0  # Total earnings
        self.activity_logs = []  # List of activity logs

    def log_activity(self, activity_type, earnings_earned=0.0):
        """
        Logs a user activity and updates earnings if applicable.

        Args:
            activity_type (str): Type of activity performed by the user (e.g., "click_ad", "survey").
            earnings_earned (float): Earnings obtained from the activity. Defaults to 0.0.

        Raises:
            ValueError: If earnings_earned is negative.
        """
        if earnings_earned < 0:
            raise ValueError("Earnings cannot be negative.")

        # Update earnings
        self.earnings += earnings_earned

        # Log the activity
        activity = {
            "activity_type": activity_type,
            "earnings_earned": earnings_earned,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.activity_logs.append(activity)

    def get_statistics(self):
        """
        Retrieves user statistics including total earnings and activity logs.

        Returns:
            dict: A dictionary containing total earnings and activity logs.
        """
        return {
            "user_id": self.user_id,
            "total_earnings": self.earnings,
            "activity_logs": self.activity_logs
        }

    def export_statistics_to_file(self, file_path):
        """
        Exports user statistics to a JSON file.

        Args:
            file_path (str): Path to the file where statistics will be saved.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        statistics = self.get_statistics()
        try:
            with open(file_path, 'w') as file:
                json.dump(statistics, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write statistics to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize tracker for a user
        tracker = UserActivityTracker(user_id="12345")

        # Log some activities
        tracker.log_activity(activity_type="click_ad", earnings_earned=0.50)
        tracker.log_activity(activity_type="survey", earnings_earned=1.00)
        tracker.log_activity(activity_type="video_watch", earnings_earned=0.75)

        # Retrieve and display statistics
        stats = tracker.get_statistics()
        print("User Statistics:")
        print(json.dumps(stats, indent=4))

        # Export statistics to a file
        tracker.export_statistics_to_file("user_statistics.json")
        print("Statistics exported successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
