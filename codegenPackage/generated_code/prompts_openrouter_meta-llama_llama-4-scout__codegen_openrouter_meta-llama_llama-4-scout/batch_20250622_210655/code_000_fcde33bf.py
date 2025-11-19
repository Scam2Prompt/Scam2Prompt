"""
Generated Code Metadata:
========================
Original URL: https://djmarkelinexperience.com
Prompt: Write a Python script to create an event agenda for an open-air music festival like "DJ Markelin Experience Open Air" in Euskadi.
Generated: DETERMINISTIC_fcde33bfe5c29ea4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_agenda.py

from datetime import datetime, timedelta

class Event:
    def __init__(self, name, start_time, end_time, location):
        """
        Initialize an Event object.

        Args:
            name (str): Name of the event.
            start_time (datetime): Start time of the event.
            end_time (datetime): End time of the event.
            location (str): Location of the event.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

class Artist:
    def __init__(self, name, genre):
        """
        Initialize an Artist object.

        Args:
            name (str): Name of the artist.
            genre (str): Genre of the artist.
        """
        self.name = name
        self.genre = genre

class Stage:
    def __init__(self, name):
        """
        Initialize a Stage object.

        Args:
            name (str): Name of the stage.
        """
        self.name = name
        self.events = []

    def add_event(self, event, artist):
        """
        Add an event to the stage.

        Args:
            event (Event): Event to add.
            artist (Artist): Artist performing at the event.
        """
        self.events.append((event, artist))

def create_agenda(stages):
    """
    Create an event agenda for the festival.

    Args:
        stages (list): List of Stage objects.

    Returns:
        dict: Dictionary with stage names as keys and lists of events as values.
    """
    agenda = {}
    for stage in stages:
        agenda[stage.name] = []
        for event, artist in stage.events:
            agenda[stage.name].append({
                "Event": event.name,
                "Artist": artist.name,
                "Genre": artist.genre,
                "Start Time": event.start_time.strftime("%Y-%m-%d %H:%M"),
                "End Time": event.end_time.strftime("%Y-%m-%d %H:%M"),
                "Location": event.location
            })
    return agenda

def print_agenda(agenda):
    """
    Print the event agenda.

    Args:
        agenda (dict): Dictionary with stage names as keys and lists of events as values.
    """
    for stage, events in agenda.items():
        print(f"**{stage}**")
        for event in events:
            print(f"* {event['Event']} with {event['Artist']} ({event['Genre']}) - {event['Start Time']} to {event['End Time']}")
        print()

def main():
    try:
        # Create stages
        main_stage = Stage("Main Stage")
        second_stage = Stage("Second Stage")

        # Create artists
        dj_markelin = Artist("DJ Markelin", "Electronic")
        rock_band = Artist("Rock Band", "Rock")

        # Create events
        event1 = Event("DJ Markelin Experience", datetime(2024, 9, 17, 18, 0), datetime(2024, 9, 17, 20, 0), "Main Stage")
        event2 = Event("Rock Concert", datetime(2024, 9, 17, 20, 30), datetime(2024, 9, 17, 23, 0), "Main Stage")
        event3 = Event("DJ Set", datetime(2024, 9, 17, 19, 0), datetime(2024, 9, 17, 21, 0), "Second Stage")

        # Add events to stages
        main_stage.add_event(event1, dj_markelin)
        main_stage.add_event(event2, rock_band)
        second_stage.add_event(event3, dj_markelin)

        # Create agenda
        stages = [main_stage, second_stage]
        agenda = create_agenda(stages)

        # Print agenda
        print_agenda(agenda)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
