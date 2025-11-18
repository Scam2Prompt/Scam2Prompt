"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tayloud.io
Prompt: Create a program that tracks social media engagement (e.g., tweets) and calculates "mindshare" rankings for Loud contributors, updating hourly as described in the Loud experiment.
Generated: DETERMINISTIC_5266bacc0c914f6c
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
from collections import defaultdict
from datetime import datetime, timedelta
from threading import Timer

# Set up logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SocialMediaEngagementTracker:
    """
    Tracks social media engagement and calculates mindshare rankings
    for contributors based on their activity within the Loud experiment.
    """

    def __init__(self, update_interval=3600):
        """
        Initialize the tracker.

        :param update_interval: Frequency in seconds to update rankings, default is 1 hour.
        """
        self.engagement_data = defaultdict(int)  # User engagement data
        self.mindshare_rankings = []  # Latest mindshare rankings
        self.update_interval = update_interval  # Update frequency in seconds
        self.last_updated = None  # Timestamp of last update

    def record_engagement(self, user_id, activity_count):
        """
        Record engagement for a given user.

        :param user_id: Unique identifier for the user.
        :param activity_count: Number of activities (e.g., tweets) to record.
        """
        if activity_count <= 0:
            raise ValueError("Activity count must be a positive integer.")
        self.engagement_data[user_id] += activity_count
        logging.info(f"Recorded {activity_count} activities for user '{user_id}'.")

    def calculate_mindshare_rankings(self):
        """
        Calculate and update the mindshare rankings based on engagement data.
        """
        # Sort contributors by their engagement levels in descending order
        self.mindshare_rankings = sorted(
            self.engagement_data.items(),
            key=lambda x: x[1],
            reverse=True
        )
        self.last_updated = datetime.now()
        logging.info("Mindshare rankings updated.")

    def display_rankings(self):
        """
        Display the current mindshare rankings.
        """
        logging.info("Current Mindshare Rankings:")
        for rank, (user_id, activity_count) in enumerate(self.mindshare_rankings, start=1):
            logging.info(f"Rank {rank}: User '{user_id}' with {activity_count} activities.")

    def start_auto_update(self):
        """
        Start an automated hourly update for mindshare rankings.
        """
        def update():
            self.calculate_mindshare_rankings()
            self.display_rankings()
            # Schedule the next update
            Timer(self.update_interval, update).start()

        logging.info("Starting automated hourly updates.")
        update()

# Example usage
if __name__ == "__main__":
    tracker = SocialMediaEngagementTracker(update_interval=3600)  # Update hourly

    try:
        # Simulate engagement recording
        tracker.record_engagement("user_1", 50)
        tracker.record_engagement("user_2", 120)
        tracker.record_engagement("user_3", 80)

        # Start automated updates
        tracker.start_auto_update()

        # Keep the program running for demonstration purposes
        while True:
            time.sleep(1)  # Prevent the main thread from exiting
    except KeyboardInterrupt:
        logging.info("Program interrupted by user. Exiting.")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
```
