"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Write a Python script that lists activities and seminars for a wine festival, similar to those offered at FestiVin Caraquet.
Generated: DETERMINISTIC_fd075a65a7e0c46f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wine_festival.py

class Event:
    """Base class for events."""

    def __init__(self, name, description, time):
        """
        Initialize an event.

        Args:
            name (str): Event name.
            description (str): Event description.
            time (str): Event time.
        """
        self.name = name
        self.description = description
        self.time = time

    def __str__(self):
        return f"{self.name} - {self.time}: {self.description}"


class Activity(Event):
    """Class for activities."""

    def __init__(self, name, description, time, location):
        """
        Initialize an activity.

        Args:
            name (str): Activity name.
            description (str): Activity description.
            time (str): Activity time.
            location (str): Activity location.
        """
        super().__init__(name, description, time)
        self.location = location

    def __str__(self):
        return f"{super().__str__()} at {self.location}"


class Seminar(Event):
    """Class for seminars."""

    def __init__(self, name, description, time, speaker):
        """
        Initialize a seminar.

        Args:
            name (str): Seminar name.
            description (str): Seminar description.
            time (str): Seminar time.
            speaker (str): Seminar speaker.
        """
        super().__init__(name, description, time)
        self.speaker = speaker

    def __str__(self):
        return f"{super().__str__()} with {self.speaker}"


class WineFestival:
    """Class for wine festival."""

    def __init__(self, name):
        """
        Initialize a wine festival.

        Args:
            name (str): Festival name.
        """
        self.name = name
        self.activities = []
        self.seminars = []

    def add_activity(self, activity):
        """
        Add an activity to the festival.

        Args:
            activity (Activity): Activity to add.
        """
        self.activities.append(activity)

    def add_seminar(self, seminar):
        """
        Add a seminar to the festival.

        Args:
            seminar (Seminar): Seminar to add.
        """
        self.seminars.append(seminar)

    def list_events(self):
        """
        List all events at the festival.
        """
        print(f"Events at {self.name}:")
        print("Activities:")
        for i, activity in enumerate(self.activities, start=1):
            print(f"{i}. {activity}")
        print("\nSeminars:")
        for i, seminar in enumerate(self.seminars, start=1):
            print(f"{i}. {seminar}")


def main():
    try:
        festival = WineFestival("FestiVin Caraquet")

        # Add activities
        festival.add_activity(Activity("Wine Tasting", "Taste different wines from around the world.", "10:00 AM", "Main Stage"))
        festival.add_activity(Activity("Grape Stomping", "Experience traditional grape stomping.", "2:00 PM", "Winery"))
        festival.add_activity(Activity("Wine and Cheese Pairing", "Learn about pairing wine and cheese.", "4:00 PM", "Food Court"))

        # Add seminars
        festival.add_seminar(Seminar("The Art of Winemaking", "Learn about the winemaking process.", "11:00 AM", "John Doe"))
        festival.add_seminar(Seminar("Wine and Food Pairing", "Discover the perfect wine and food pairings.", "3:00 PM", "Jane Smith"))

        # List events
        festival.list_events()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
