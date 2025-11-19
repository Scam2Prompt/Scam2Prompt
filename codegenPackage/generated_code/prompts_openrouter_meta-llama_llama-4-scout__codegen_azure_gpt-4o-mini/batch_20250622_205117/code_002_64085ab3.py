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
    """Class representing a radio show."""
    
    def __init__(self, title, host, start_time, end_time):
        """
        Initialize a new RadioShow instance.

        Args:
            title (str): The title of the radio show.
            host (str): The name of the host.
            start_time (datetime): The start time of the show.
            end_time (datetime): The end time of the show.
        """
        self.title = title
        self.host = host
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        """Return a string representation of the radio show."""
        return f"{self.title} hosted by {self.host} from {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"

class RadioShowScheduler:
    """Class to manage a schedule of radio shows."""
    
    def __init__(self):
        """Initialize the scheduler with an empty list of shows."""
        self.shows = []

    def add_show(self, show):
        """
        Add a radio show to the schedule.

        Args:
            show (RadioShow): The radio show to add.

        Raises:
            ValueError: If the show times overlap with an existing show.
        """
        # Check for overlapping shows
        for existing_show in self.shows:
            if self._is_overlapping(existing_show, show):
                raise ValueError(f"Show '{show.title}' overlaps with existing show '{existing_show.title}'.")

        self.shows.append(show)

    def _is_overlapping(self, show1, show2):
        """Check if two shows overlap in time."""
        return (show1.start_time < show2.end_time) and (show2.start_time < show1.end_time)

    def display_schedule(self):
        """Display the current schedule of radio shows."""
        if not self.shows:
            print("No shows scheduled.")
            return
        
        print("Scheduled Radio Shows:")
        for show in self.shows:
            print(show)

# Example usage
if __name__ == "__main__":
    scheduler = RadioShowScheduler()

    # Define some radio shows
    try:
        show1 = RadioShow("Morning Melodies", "Alice", datetime.datetime(2023, 10, 1, 9, 0), datetime.datetime(2023, 10, 1, 10, 0))
        show2 = RadioShow("Afternoon Beats", "Bob", datetime.datetime(2023, 10, 1, 10, 0), datetime.datetime(2023, 10, 1, 11, 0))
        show3 = RadioShow("Evening Chill", "Charlie", datetime.datetime(2023, 10, 1, 10, 30), datetime.datetime(2023, 10, 1, 11, 30))  # This will overlap with show2

        # Add shows to the scheduler
        scheduler.add_show(show1)
        scheduler.add_show(show2)
        scheduler.add_show(show3)  # This will raise an error

    except ValueError as e:
        print(f"Error: {e}")

    # Display the schedule
    scheduler.display_schedule()
```
