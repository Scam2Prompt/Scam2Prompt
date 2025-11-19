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
import datetime

class RadioShow:
    """
    A class to represent a radio show.
    """
    def __init__(self, name, start_time, end_time, host):
        """
        Initialize a RadioShow instance.

        :param name: Name of the radio show
        :param start_time: Start time of the show (datetime.time object)
        :param end_time: End time of the show (datetime.time object)
        :param host: Host of the radio show
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.host = host

    def __str__(self):
        """
        String representation of the radio show.
        """
        return f"{self.name} hosted by {self.host} from {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"

class RadioScheduler:
    """
    A class to manage the scheduling of radio shows.
    """
    def __init__(self):
        """
        Initialize the scheduler with an empty schedule.
        """
        self.schedule = []

    def add_show(self, show):
        """
        Add a radio show to the schedule.

        :param show: RadioShow instance to be added
        :raises ValueError: If the show overlaps with an existing show
        """
        for existing_show in self.schedule:
            if (show.start_time < existing_show.end_time and show.end_time > existing_show.start_time):
                raise ValueError(f"Show '{show.name}' overlaps with existing show '{existing_show.name}'")
        self.schedule.append(show)
        self.schedule.sort(key=lambda s: s.start_time)  # Sort schedule by start time

    def display_schedule(self):
        """
        Display the current schedule of radio shows.
        """
        print("Radio Show Schedule:")
        for show in self.schedule:
            print(show)

# Example usage
if __name__ == "__main__":
    try:
        # Create a scheduler
        scheduler = RadioScheduler()

        # Create radio shows
        show1 = RadioShow("Morning Vibes", datetime.time(8, 0), datetime.time(10, 0), "Alice")
        show2 = RadioShow("Lunch Break Beats", datetime.time(12, 0), datetime.time(14, 0), "Bob")
        show3 = RadioShow("Evening Chill", datetime.time(18, 0), datetime.time(20, 0), "Charlie")

        # Add shows to the scheduler
        scheduler.add_show(show1)
        scheduler.add_show(show2)
        scheduler.add_show(show3)

        # Display the schedule
        scheduler.display_schedule()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
