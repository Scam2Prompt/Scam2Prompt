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
from datetime import datetime, timedelta
import time
import threading


class EventScheduler:
    """
    A class to schedule and send notifications for Castle Siege and Territory War
    events on the L2Lusty server.
    """

    def __init__(self):
        self.events = []

    def add_event(self, event_name, event_time, reward, notification_time_before=30):
        """
        Add an event to the scheduler.

        :param event_name: Name of the event (e.g., "Castle Siege").
        :param event_time: Datetime object representing when the event starts.
        :param reward: Description of the reward for the event.
        :param notification_time_before: Minutes before the event to send a notification.
        """
        notification_time = event_time - timedelta(minutes=notification_time_before)
        self.events.append({
            "event_name": event_name,
            "event_time": event_time,
            "reward": reward,
            "notification_time": notification_time
        })
        print(f"Event '{event_name}' scheduled for {event_time}. Notification will be sent at {notification_time}.")

    def send_notification(self, event):
        """
        Send a notification for an event.

        :param event: Dictionary containing event details.
        """
        print(f"Notification: The {event['event_name']} is starting soon at {event['event_time']}! Reward: {event['reward']}")

    def start_scheduler(self):
        """
        Start the scheduler to send notifications at the appropriate times.
        """
        def scheduler_loop():
            while True:
                now = datetime.now()
                for event in self.events[:]:  # Iterate over a copy of the event list
                    if now >= event["notification_time"]:
                        try:
                            self.send_notification(event)
                        except Exception as e:
                            print(f"Error sending notification for event '{event['event_name']}': {e}")
                        self.events.remove(event)  # Remove the event after notification
                time.sleep(1)  # Check every second

        print("Event scheduler started.")
        threading.Thread(target=scheduler_loop, daemon=True).start()


# Usage example
if __name__ == "__main__":
    # Initialize the scheduler
    scheduler = EventScheduler()

    # Define event details
    castle_siege_time = datetime.now() + timedelta(minutes=5)  # Event starts in 5 minutes
    territory_war_time = datetime.now() + timedelta(hours=1)   # Event starts in 1 hour

    # Add events to the scheduler
    scheduler.add_event("Castle Siege", castle_siege_time, "Epic Loot", notification_time_before=30)
    scheduler.add_event("Territory War", territory_war_time, "Rare Items", notification_time_before=60)

    # Start the scheduler
    scheduler.start_scheduler()

    # Prevent the script from exiting immediately
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped.")
```
