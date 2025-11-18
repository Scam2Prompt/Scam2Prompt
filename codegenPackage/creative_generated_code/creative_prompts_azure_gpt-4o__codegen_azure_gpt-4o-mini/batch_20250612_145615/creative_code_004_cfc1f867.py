"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://l2lusty.site
Prompt: Write a program to schedule notifications for Castle Siege and Territory War events on the L2Lusty server, based on the provided event times and rewards.
Generated: DETERMINISTIC_cfc1f8679d8bc94b
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationScheduler:
    def __init__(self):
        # Dictionary to hold event schedules
        self.events = {
            "Castle Siege": {
                "time": "20:00",
                "reward": "1000 Gold"
            },
            "Territory War": {
                "time": "21:00",
                "reward": "500 Gold"
            }
        }

    def send_notification(self, event_name, reward):
        """
        Sends a notification for the given event with the associated reward.
        
        :param event_name: The name of the event
        :param reward: The reward for the event
        """
        logging.info(f"Notification: {event_name} is starting now! Reward: {reward}")

    def schedule_events(self):
        """
        Schedules the notifications based on the predefined event times.
        """
        for event_name, event_details in self.events.items():
            event_time = event_details['time']
            reward = event_details['reward']
            schedule.every().day.at(event_time).do(self.send_notification, event_name, reward)

    def run(self):
        """
        Starts the scheduler to run indefinitely.
        """
        self.schedule_events()
        logging.info("Scheduler started. Waiting for events...")
        while True:
            try:
                schedule.run_pending()
                time.sleep(1)  # Sleep for a short period to avoid busy-waiting
            except Exception as e:
                logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    scheduler = NotificationScheduler()
    scheduler.run()
```
