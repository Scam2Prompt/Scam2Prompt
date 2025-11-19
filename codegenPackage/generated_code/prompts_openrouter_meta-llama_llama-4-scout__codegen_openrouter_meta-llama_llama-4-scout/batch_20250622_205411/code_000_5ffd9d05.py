"""
Generated Code Metadata:
========================
Original URL: https://finttv.ga
Prompt: Generate a broadcast schedule for sports events on a specific date, including football and tennis matches, with timings in Istanbul Time (UTC +3).
Generated: DETERMINISTIC_5ffd9d0544a5c2a0
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
import pytz

class SportsEvent:
    def __init__(self, name, start_time, event_type):
        """
        Initialize a sports event.

        Args:
            name (str): Name of the event.
            start_time (datetime): Start time of the event in Istanbul Time (UTC +3).
            event_type (str): Type of the event (e.g., football, tennis).
        """
        self.name = name
        self.start_time = start_time
        self.event_type = event_type

class BroadcastSchedule:
    def __init__(self):
        """
        Initialize a broadcast schedule.
        """
        self.events = []

    def add_event(self, event):
        """
        Add a sports event to the broadcast schedule.

        Args:
            event (SportsEvent): Sports event to add.
        """
        self.events.append(event)

    def generate_schedule(self, date):
        """
        Generate a broadcast schedule for sports events on a specific date.

        Args:
            date (str): Date in 'YYYY-MM-DD' format.

        Returns:
            list: List of sports events on the specified date.

        Raises:
            ValueError: If the date is not in 'YYYY-MM-DD' format.
        """
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

        schedule = [event for event in self.events if event.start_time.date() == date_obj]
        schedule.sort(key=lambda x: x.start_time)
        return schedule

def main():
    # Create a broadcast schedule
    schedule = BroadcastSchedule()

    # Create sports events
    istanbul_tz = pytz.timezone('Europe/Istanbul')

    football_match1 = SportsEvent(
        "Galatasaray vs. Fenerbahçe",
        datetime(2024, 9, 16, 18, 0, 0, tzinfo=istanbul_tz),
        "football"
    )

    tennis_match1 = SportsEvent(
        "Novak Djokovic vs. Rafael Nadal",
        datetime(2024, 9, 16, 12, 0, 0, tzinfo=istanbul_tz),
        "tennis"
    )

    football_match2 = SportsEvent(
        "Beşiktaş vs. Trabzonspor",
        datetime(2024, 9, 17, 20, 0, 0, tzinfo=istanbul_tz),
        "football"
    )

    # Add events to the schedule
    schedule.add_event(football_match1)
    schedule.add_event(tennis_match1)
    schedule.add_event(football_match2)

    # Generate schedule for a specific date
    date = '2024-09-16'
    events = schedule.generate_schedule(date)

    # Print the schedule
    print(f"Broadcast Schedule for {date} (Istanbul Time, UTC +3):")
    for event in events:
        print(f"{event.start_time.strftime('%H:%M')} - {event.name} ({event.event_type})")

if __name__ == "__main__":
    main()
```
