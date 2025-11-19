"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiffany-holz.de
Prompt: Write a script to manage event scheduling for a personal hobby website like tiffany-holz.de.
Generated: DETERMINISTIC_833bedb350606789
Batch ID: 20250612_135417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class EventManager:
    """
    A class to manage event scheduling for a personal hobby website.
    """

    def __init__(self, data_file="events.json"):
        """
        Initialize the EventManager with a file to store event data.

        :param data_file: Path to the JSON file for saving events.
        """
        self.data_file = data_file
        self.events = self.load_events()

    def load_events(self):
        """
        Load events from the JSON file.

        :return: List of events loaded from the file.
        """
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Return an empty list if the file does not exist
            return []
        except json.JSONDecodeError:
            # Handle corrupted file gracefully
            print("Error: Failed to decode events file. Starting fresh.")
            return []

    def save_events(self):
        """
        Save current events to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.events, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save events. {e}")

    def add_event(self, title, date, description=""):
        """
        Add a new event.

        :param title: Title of the event.
        :param date: Date of the event in YYYY-MM-DD format.
        :param description: Optional description of the event.
        """
        try:
            event_date = datetime.strptime(date, "%Y-%m-%d")
            new_event = {
                "title": title,
                "date": date,
                "description": description,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.events.append(new_event)
            self.events.sort(key=lambda x: x["date"])  # Keep events sorted by date
            self.save_events()
            print("Event added successfully!")
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")

    def delete_event(self, title):
        """
        Delete an event by its title.

        :param title: Title of the event to delete.
        """
        original_count = len(self.events)
        self.events = [event for event in self.events if event["title"] != title]
        if len(self.events) < original_count:
            self.save_events()
            print("Event deleted successfully!")
        else:
            print("Error: Event not found.")

    def list_events(self):
        """
        List all scheduled events.
        """
        if not self.events:
            print("No events scheduled.")
        else:
            print("Scheduled Events:")
            for event in self.events:
                print(f" - {event['title']} on {event['date']}: {event['description']}")

    def search_event(self, keyword):
        """
        Search for events by keyword.

        :param keyword: Keyword to search in event titles or descriptions.
        """
        matching_events = [
            event for event in self.events
            if keyword.lower() in event["title"].lower() or keyword.lower() in event["description"].lower()
        ]
        if matching_events:
            print("Matching Events:")
            for event in matching_events:
                print(f" - {event['title']} on {event['date']}: {event['description']}")
        else:
            print("No matching events found.")

# Example usage
if __name__ == "__main__":
    manager = EventManager()

    print("\nAdding sample events...")
    manager.add_event("Painting Workshop", "2023-10-15", "Learn the basics of watercolor painting.")
    manager.add_event("Photography Walk", "2023-11-01", "Explore nature and capture beautiful moments.")
    manager.add_event("DIY Craft Night", "2023-12-05", "Build your own creative crafts.")

    print("\nListing all events...")
    manager.list_events()

    print("\nSearching for events with 'Craft'...")
    manager.search_event("Craft")

    print("\nDeleting an event...")
    manager.delete_event("DIY Craft Night")

    print("\nListing all events after deletion...")
    manager.list_events()
```

This script creates an `EventManager` class for managing events, including functionality to add, delete, search, and list events. All data is stored in a JSON file (`events.json`) for persistence.
