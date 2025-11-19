"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Write a Python script to manage school event calendars for events like "Дан школе" and "Васкршња приредба".
Generated: DETERMINISTIC_e1280ecf30dd9a31
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class SchoolEventCalendar:
    """
    A class to manage school event calendars.
    """

    def __init__(self, file_name="school_events.json"):
        """
        Initialize the calendar with a file to store events.
        :param file_name: Name of the file to store events.
        """
        self.file_name = file_name
        self.events = self._load_events()

    def _load_events(self):
        """
        Load events from the file. If the file doesn't exist, return an empty list.
        :return: List of events.
        """
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON. Starting with an empty event list.")
            return []

    def _save_events(self):
        """
        Save events to the file.
        """
        try:
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(self.events, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error: Failed to save events to file. {e}")

    def add_event(self, name, date, description=""):
        """
        Add a new event to the calendar.
        :param name: Name of the event.
        :param date: Date of the event in YYYY-MM-DD format.
        :param description: Optional description of the event.
        """
        try:
            # Validate date format
            event_date = datetime.strptime(date, "%Y-%m-%d")
            self.events.append({
                "name": name,
                "date": event_date.strftime("%Y-%m-%d"),
                "description": description
            })
            self._save_events()
            print(f"Event '{name}' added successfully.")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")

    def remove_event(self, name):
        """
        Remove an event by name.
        :param name: Name of the event to remove.
        """
        original_count = len(self.events)
        self.events = [event for event in self.events if event["name"] != name]
        if len(self.events) < original_count:
            self._save_events()
            print(f"Event '{name}' removed successfully.")
        else:
            print(f"Error: Event '{name}' not found.")

    def list_events(self):
        """
        List all events in the calendar.
        """
        if not self.events:
            print("No events found.")
        else:
            print("School Events:")
            for event in self.events:
                print(f"- {event['name']} (Date: {event['date']}) - {event['description']}")

    def find_event(self, name):
        """
        Find an event by name.
        :param name: Name of the event to find.
        """
        for event in self.events:
            if event["name"] == name:
                print(f"Event Found: {event['name']} (Date: {event['date']}) - {event['description']}")
                return
        print(f"Error: Event '{name}' not found.")


# Example usage
if __name__ == "__main__":
    calendar = SchoolEventCalendar()

    # Add events
    calendar.add_event("Дан школе", "2023-11-15", "Прослава дана школе.")
    calendar.add_event("Васкршња приредба", "2024-04-20", "Приредба поводом Васкрса.")

    # List events
    calendar.list_events()

    # Find an event
    calendar.find_event("Дан школе")

    # Remove an event
    calendar.remove_event("Васкршња приредба")

    # List events after removal
    calendar.list_events()
```
