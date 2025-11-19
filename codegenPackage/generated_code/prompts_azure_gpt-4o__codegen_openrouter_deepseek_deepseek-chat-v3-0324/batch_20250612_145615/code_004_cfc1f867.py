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
import datetime
import time
import logging
from typing import Dict, List, Optional
import platform
import os
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('l2lusty_notifications.log'),
        logging.StreamHandler()
    ]
)

class Event:
    """Represents a game event with its schedule and rewards."""
    def __init__(self, name: str, schedule: Dict[str, List[str]], rewards: List[str]):
        self.name = name
        self.schedule = schedule
        self.rewards = rewards
        self.next_event_time: Optional[datetime.datetime] = None

    def calculate_next_event(self) -> None:
        """Calculate the next occurrence of this event based on current time."""
        now = datetime.datetime.now()
        current_weekday = now.strftime("%A")  # e.g., "Monday"
        current_time = now.time()

        # Get today's event times
        today_times = self.schedule.get(current_weekday, [])
        
        # Find the next event time today
        for event_time_str in today_times:
            event_time = datetime.datetime.strptime(event_time_str, "%H:%M").time()
            if event_time > current_time:
                self.next_event_time = datetime.datetime.combine(now.date(), event_time)
                return

        # If no more events today, find the next day with events
        days = list(self.schedule.keys())
        current_day_index = days.index(current_weekday) if current_weekday in days else -1
        
        for i in range(1, 8):  # Check next 7 days
            next_day_index = (current_day_index + i) % 7
            next_day = days[next_day_index]
            if next_day in self.schedule and self.schedule[next_day]:
                # Take the first event of the next day
                event_time_str = self.schedule[next_day][0]
                event_time = datetime.datetime.strptime(event_time_str, "%H:%M").time()
                next_date = now.date() + datetime.timedelta(days=i)
                self.next_event_time = datetime.datetime.combine(next_date, event_time)
                return

class NotificationScheduler:
    """Manages scheduling and sending notifications for game events."""
    def __init__(self):
        # Define event schedules and rewards
        self.events = [
            Event(
                name="Castle Siege",
                schedule={
                    "Sunday": ["20:00"],
                },
                rewards=[
                    "Control of Aden Castle",
                    "Tax revenue from territories",
                    "Prestige and glory"
                ]
            ),
            Event(
                name="Territory War",
                schedule={
                    "Tuesday": ["20:00"],
                    "Thursday": ["20:00"],
                    "Saturday": ["20:00"],
                },
                rewards=[
                    "Control of territories",
                    "Tax revenue",
                    "Special bonuses"
                ]
            )
        ]
        
        # Platform-specific notification function
        if platform.system() == "Windows":
            self.notify_func = self._notify_windows
        elif platform.system() == "Darwin":
            self.notify_func = self._notify_mac
        else:  # Linux and others
            self.notify_func = self._notify_linux

    def _notify_windows(self, title: str, message: str) -> None:
        """Send notification on Windows."""
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=10)
        except ImportError:
            logging.warning("win10toast not installed. Falling back to print.")
            print(f"{title}: {message}")

    def _notify_mac(self, title: str, message: str) -> None:
        """Send notification on macOS."""
        try:
            os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")
        except Exception as e:
            logging.warning(f"Failed to send macOS notification: {e}")
            print(f"{title}: {message}")

    def _notify_linux(self, title: str, message: str) -> None:
        """Send notification on Linux."""
        try:
            os.system(f'notify-send "{title}" "{message}"')
        except Exception as e:
            logging.warning(f"Failed to send Linux notification: {e}")
            print(f"{title}: {message}")

    def send_notification(self, event: Event) -> None:
        """Send a notification for an upcoming event."""
        time_str = event.next_event_time.strftime("%Y-%m-%d %H:%M")
        rewards_str = "\n- " + "\n- ".join(event.rewards)
        message = f"{event.name} starts at {time_str}\nRewards:{rewards_str}"
        
        logging.info(f"Sending notification: {message}")
        self.notify_func("L2Lusty Event Reminder", message)

    def calculate_all_events(self) -> None:
        """Calculate next occurrence for all events."""
        for event in self.events:
            event.calculate_next_event()
            if event.next_event_time:
                logging.info(f"Next {event.name}: {event.next_event_time}")

    def run(self) -> None:
        """Main scheduling loop."""
        logging.info("Starting L2Lusty Event Notification Scheduler")
        self.calculate_all_events()

        while True:
            now = datetime.datetime.now()
            
            for event in self.events:
                if event.next_event_time and now >= event.next_event_time:
                    self.send_notification(event)
                    # Recalculate next event time after current one has passed
                    event.calculate_next_event()
                    if event.next_event_time:
                        logging.info(f"Next {event.name} rescheduled to {event.next_event_time}")

            # Sleep for 1 minute to avoid busy waiting
            time.sleep(60)

def main() -> None:
    """Entry point for the application."""
    try:
        scheduler = NotificationScheduler()
        scheduler.run()
    except KeyboardInterrupt:
        logging.info("Shutting down notification scheduler...")
        sys.exit(0)
    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
