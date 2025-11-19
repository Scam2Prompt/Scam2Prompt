"""
Generated Code Metadata:
========================
Original URL: https://originether.com
Prompt: Generate a schedule for live streaming of MotoGP, Moto2, Moto3, and MotoE events in 2025.
Generated: DETERMINISTIC_4033da9da184aaed
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class MotoGPEvent:
    def __init__(self, name, date, start_time, duration):
        """
        Initialize a MotoGP event.

        Args:
            name (str): Name of the event.
            date (str): Date of the event in YYYY-MM-DD format.
            start_time (str): Start time of the event in HH:MM format.
            duration (int): Duration of the event in minutes.
        """
        self.name = name
        self.date = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
        self.duration = timedelta(minutes=duration)

    def get_end_time(self):
        """
        Calculate the end time of the event.

        Returns:
            datetime: End time of the event.
        """
        return self.date + self.duration

    def __str__(self):
        """
        Return a string representation of the event.

        Returns:
            str: String representation of the event.
        """
        return f"{self.name} - {self.date.strftime('%Y-%m-%d %H:%M')} to {self.get_end_time().strftime('%Y-%m-%d %H:%M')}"


class MotoGPStreamingSchedule:
    def __init__(self):
        """
        Initialize a MotoGP streaming schedule.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the schedule.

        Args:
            event (MotoGPEvent): Event to add.
        """
        self.events.append(event)

    def generate_schedule(self):
        """
        Generate a schedule for live streaming of MotoGP events.

        Returns:
            list: List of events in the schedule.
        """
        return sorted(self.events, key=lambda x: x.date)

    def print_schedule(self):
        """
        Print the schedule.
        """
        schedule = self.generate_schedule()
        for i, event in enumerate(schedule):
            print(f"{i+1}. {event}")


def main():
    try:
        # Define events
        motogp_events = [
            MotoGPEvent("MotoGP Qualifying", "2025-04-12", "10:00", 60),
            MotoGPEvent("MotoGP Sprint", "2025-04-12", "14:00", 30),
            MotoGPEvent("MotoGP Main Event", "2025-04-12", "15:00", 120),
        ]

        mot2_events = [
            MotoGPEvent("Moto2 Qualifying", "2025-04-12", "09:00", 60),
            MotoGPEvent("Moto2 Main Event", "2025-04-12", "12:00", 100),
        ]

        mot3_events = [
            MotoGPEvent("Moto3 Qualifying", "2025-04-12", "08:00", 60),
            MotoGPEvent("Moto3 Main Event", "2025-04-12", "11:00", 90),
        ]

        mote_events = [
            MotoGPEvent("MotoE Qualifying", "2025-04-12", "07:00", 60),
            MotoGPEvent("MotoE Main Event", "2025-04-12", "10:00", 80),
        ]

        # Create schedule
        schedule = MotoGPStreamingSchedule()
        for event in motogp_events + mot2_events + mot3_events + mote_events:
            schedule.add_event(event)

        # Print schedule
        print("MotoGP Streaming Schedule 2025:")
        schedule.print_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
