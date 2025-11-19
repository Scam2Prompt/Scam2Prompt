"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Generate a code snippet to create a simple radio show scheduler, inspired by the radio shows listed on Radio S.
Generated: DETERMINISTIC_64085ab31083e8df
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class RadioShow:
    """Represents a radio show with its details."""

    def __init__(self, title, host, start_time, end_time, frequency):
        """
        Initializes a RadioShow object.

        Args:
            title (str): The title of the radio show.
            host (str): The host of the radio show.
            start_time (datetime): The start time of the radio show.
            end_time (datetime): The end time of the radio show.
            frequency (str): The frequency of the radio show.
        """
        self.title = title
        self.host = host
        self.start_time = start_time
        self.end_time = end_time
        self.frequency = frequency

    def __str__(self):
        return f"{self.title} with {self.host} - {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')} on {self.frequency}"


class RadioScheduler:
    """Manages a schedule of radio shows."""

    def __init__(self):
        """Initializes an empty radio scheduler."""
        self.schedule = []

    def add_show(self, show):
        """
        Adds a radio show to the schedule.

        Args:
            show (RadioShow): The radio show to add.

        Raises:
            ValueError: If the show's start time is later than its end time.
        """
        if show.start_time > show.end_time:
            raise ValueError("Start time cannot be later than end time")
        self.schedule.append(show)
        self.schedule.sort(key=lambda x: x.start_time)

    def remove_show(self, title):
        """
        Removes a radio show from the schedule by title.

        Args:
            title (str): The title of the radio show to remove.

        Raises:
            ValueError: If no show with the given title exists.
        """
        for show in self.schedule:
            if show.title == title:
                self.schedule.remove(show)
                return
        raise ValueError("No show with the given title exists")

    def get_schedule(self):
        """
        Returns the current schedule of radio shows.

        Returns:
            list[RadioShow]: The list of radio shows in the schedule.
        """
        return self.schedule

    def print_schedule(self):
        """Prints the current schedule of radio shows."""
        for show in self.schedule:
            print(show)


def main():
    scheduler = RadioScheduler()

    try:
        show1 = RadioShow(
            "Morning Drive",
            "John Doe",
            datetime.strptime("2024-09-16 06:00", "%Y-%m-%d %H:%M"),
            datetime.strptime("2024-09-16 10:00", "%Y-%m-%d %H:%M"),
            "FM 95.5"
        )
        show2 = RadioShow(
            "Afternoon Delight",
            "Jane Smith",
            datetime.strptime("2024-09-16 12:00", "%Y-%m-%d %H:%M"),
            datetime.strptime("2024-09-16 16:00", "%Y-%m-%d %H:%M"),
            "FM 95.5"
        )

        scheduler.add_show(show1)
        scheduler.add_show(show2)

        print("Radio Show Schedule:")
        scheduler.print_schedule()

        scheduler.remove_show("Morning Drive")

        print("\nUpdated Radio Show Schedule:")
        scheduler.print_schedule()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
