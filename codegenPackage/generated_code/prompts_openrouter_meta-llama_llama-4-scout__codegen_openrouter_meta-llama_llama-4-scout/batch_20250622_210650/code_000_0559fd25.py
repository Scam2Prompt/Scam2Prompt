"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Write a Python script to create a simple puppetry show schedule using the Corporación El Cristal's event data.
Generated: DETERMINISTIC_0559fd2580287a9d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# puppetry_show_schedule.py

from datetime import datetime
import json

class Event:
    """Represents an event in the Corporación El Cristal's event data."""

    def __init__(self, title, start_time, end_time, description):
        """
        Initializes an Event object.

        Args:
            title (str): The title of the event.
            start_time (str): The start time of the event in 'YYYY-MM-DD HH:MM' format.
            end_time (str): The end time of the event in 'YYYY-MM-DD HH:MM' format.
            description (str): A brief description of the event.
        """
        self.title = title
        self.start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M')
        self.end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M')
        self.description = description

class PuppetryShowSchedule:
    """Represents a simple puppetry show schedule."""

    def __init__(self):
        """Initializes an empty schedule."""
        self.events = []

    def add_event(self, event):
        """
        Adds an event to the schedule.

        Args:
            event (Event): The event to add.
        """
        self.events.append(event)
        self.events.sort(key=lambda x: x.start_time)

    def print_schedule(self):
        """Prints the schedule."""
        for event in self.events:
            print(f"Title: {event.title}")
            print(f"Time: {event.start_time.strftime('%Y-%m-%d %H:%M')} - {event.end_time.strftime('%Y-%m-%d %H:%M')}")
            print(f"Description: {event.description}")
            print("------------------------")

def load_event_data(file_path):
    """
    Loads event data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list[Event]: A list of Event objects.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            events = []
            for event_data in data:
                event = Event(
                    title=event_data['title'],
                    start_time=event_data['start_time'],
                    end_time=event_data['end_time'],
                    description=event_data['description']
                )
                events.append(event)
            return events
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{file_path}': {e}")
        return []

def main():
    file_path = 'event_data.json'  # replace with your file path
    events = load_event_data(file_path)
    schedule = PuppetryShowSchedule()
    for event in events:
        schedule.add_event(event)
    schedule.print_schedule()

if __name__ == "__main__":
    main()
```

```json
// event_data.json

[
    {
        "title": "Puppetry Show 1",
        "start_time": "2024-09-17 10:00",
        "end_time": "2024-09-17 11:00",
        "description": "A fun puppetry show for kids."
    },
    {
        "title": "Puppetry Show 2",
        "start_time": "2024-09-17 11:30",
        "end_time": "2024-09-17 12:30",
        "description": "Another entertaining puppetry show."
    }
]
```
