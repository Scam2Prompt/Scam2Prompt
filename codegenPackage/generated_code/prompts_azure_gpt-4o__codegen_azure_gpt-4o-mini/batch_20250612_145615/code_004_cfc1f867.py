"""
Generated Code Metadata:
========================
Original URL: https://l2lusty.site
Prompt: Write a program to schedule notifications for Castle Siege and Territory War events on the L2Lusty server, based on the provided event times and rewards.
Generated: DETERMINISTIC_cfc1f8679d8bc94b
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import schedule
import time
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EventScheduler:
    def __init__(self):
        self.events = []

    def add_event(self, event_time, event_name, reward):
        """
        Add an event to the scheduler.

        :param event_time: The time of the event (datetime object)
        :param event_name: The name of the event (str)
        :param reward: The reward for the event (str)
        """
        self.events.append({
            'time': event_time,
            'name': event_name,
            'reward': reward
        })
        logging.info(f"Event '{event_name}' scheduled for {event_time} with reward: {reward}")

    def notify_event(self, event):
        """
        Notify about the scheduled event.

        :param event: The event dictionary containing event details
        """
        logging.info(f"Notification: Event '{event['name']}' is starting now! Reward: {event['reward']}")

    def schedule_notifications(self):
        """
        Schedule notifications for all events.
        """
        for event in self.events:
            schedule_time = event['time'] - timedelta(minutes=10)  # Notify 10 minutes before the event
            schedule.every().day.at(schedule_time.strftime("%H:%M")).do(self.notify_event, event)

    def run(self):
        """
        Run the scheduler to check for events.
        """
        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep to prevent busy waiting

def main():
    # Create an instance of EventScheduler
    scheduler = EventScheduler()

    # Define event times and rewards
    events = [
        (datetime.now().replace(hour=20, minute=0, second=0, microsecond=0), "Castle Siege", "1000 Gold"),
        (datetime.now().replace(hour=21, minute=0, second=0, microsecond=0), "Territory War", "500 Gold")
    ]

    # Add events to the scheduler
    for event_time, event_name, reward in events:
        scheduler.add_event(event_time, event_name, reward)

    # Schedule notifications for the events
    scheduler.schedule_notifications()

    # Start the scheduler
    try:
        logging.info("Starting the event scheduler...")
        scheduler.run()
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
