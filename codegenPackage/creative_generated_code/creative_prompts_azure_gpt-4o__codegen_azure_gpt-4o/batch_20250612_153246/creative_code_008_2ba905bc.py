"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Write code to schedule and manage events like plantation drives or food distribution programs, as highlighted in Youngistaan Foundation's blog.
Generated: DETERMINISTIC_2ba905bc681e7346
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class EventManager:
    """
    EventManager class to schedule and manage events like plantation drives and food distribution programs.
    """

    def __init__(self):
        # Initialize with an empty event list
        self.events = []

    def add_event(self, name, description, date, time, location, organizer_name):
        """
        Add a new event to the schedule.

        Args:
        name (str): Name of the event.
        description (str): Description of the event.
        date (str): Date of the event in YYYY-MM-DD format.
        time (str): Time of the event in HH:MM format.
        location (str): Location of the event.
        organizer_name (str): Name of the organizer.

        Returns:
        dict: Details of the event added.
        """
        try:
            # Validate date format
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d")

            # Validate time format
            event_time = datetime.datetime.strptime(time, "%H:%M")

            # Create the event dictionary
            event = {
                "name": name,
                "description": description,
                "date": event_date.strftime("%Y-%m-%d"),
                "time": event_time.strftime("%H:%M"),
                "location": location,
                "organizer_name": organizer_name
            }

            # Add the event to the list
            self.events.append(event)
            return event
        except ValueError as e:
            # Handle invalid date or time format
            raise ValueError(f"Invalid date or time format: {e}")

    def list_events(self):
        """
        List all scheduled events.

        Returns:
        str: JSON-formatted string of all events.
        """
        return json.dumps(self.events, indent=4)

    def delete_event(self, name):
        """
        Delete an event by its name.

        Args:
        name (str): Name of the event to delete.

        Returns:
        str: Success message or error message if event not found.
        """
        for event in self.events:
            if event["name"] == name:
                self.events.remove(event)
                return f"Event '{name}' has been deleted."
        return f"Event '{name}' not found."

    def search_event(self, name):
        """
        Search for an event by its name.

        Args:
        name (str): Name of the event to search.

        Returns:
        dict|str: Event details if found, or error message if event not found.
        """
        for event in self.events:
            if event["name"] == name:
                return event
        return f"Event '{name}' not found."


# Example usage
if __name__ == "__main__":
    manager = EventManager()

    # Adding new events
    try:
        manager.add_event(
            name="Plantation Drive",
            description="A drive to plant saplings in the community park.",
            date="2023-11-15",
            time="10:30",
            location="Community Park",
            organizer_name="Youngistaan Foundation"
        )
        manager.add_event(
            name="Food Distribution Program",
            description="Distributing food packets to those in need.",
            date="2023-11-20",
            time="12:00",
            location="City Hall",
            organizer_name="Youngistaan Foundation"
        )
    except ValueError as e:
        print(e)

    # Listing all events
    print("Scheduled Events:")
    print(manager.list_events())

    # Searching for an event
    print("\nSearch Result:")
    print(manager.search_event("Plantation Drive"))

    # Deleting an event
    print("\nDelete Event:")
    print(manager.delete_event("Plantation Drive"))

    # Listing all events after deletion
    print("\nScheduled Events After Deletion:")
    print(manager.list_events())
```
