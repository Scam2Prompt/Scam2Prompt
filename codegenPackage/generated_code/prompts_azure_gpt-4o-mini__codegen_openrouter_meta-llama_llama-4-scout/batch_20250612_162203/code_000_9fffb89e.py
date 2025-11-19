"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Generate a code snippet for a church management system that includes features for tracking ministries and events similar to those at Word of Life Northwest.
Generated: DETERMINISTIC_9fffb89e2a7e3d93
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# church_management_system.py

from datetime import datetime
from typing import List, Dict

class Ministry:
    """Represents a ministry in the church management system."""

    def __init__(self, name: str, description: str, leader: str):
        """
        Initializes a Ministry object.

        Args:
            name (str): The name of the ministry.
            description (str): A brief description of the ministry.
            leader (str): The leader of the ministry.
        """
        self.name = name
        self.description = description
        self.leader = leader

    def __str__(self):
        return f"{self.name} - {self.description} (Leader: {self.leader})"


class Event:
    """Represents an event in the church management system."""

    def __init__(self, title: str, date: datetime, time: str, location: str, ministry: Ministry):
        """
        Initializes an Event object.

        Args:
            title (str): The title of the event.
            date (datetime): The date of the event.
            time (str): The time of the event.
            location (str): The location of the event.
            ministry (Ministry): The ministry associated with the event.
        """
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.ministry = ministry

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d')} at {self.time} ({self.location})"


class ChurchManagementSystem:
    """Represents the church management system."""

    def __init__(self):
        self.ministries: Dict[str, Ministry] = {}
        self.events: List[Event] = []

    def add_ministry(self, ministry: Ministry):
        """
        Adds a ministry to the system.

        Args:
            ministry (Ministry): The ministry to add.
        """
        self.ministries[ministry.name] = ministry

    def remove_ministry(self, ministry_name: str):
        """
        Removes a ministry from the system.

        Args:
            ministry_name (str): The name of the ministry to remove.

        Raises:
            ValueError: If the ministry does not exist.
        """
        if ministry_name not in self.ministries:
            raise ValueError(f"Ministry '{ministry_name}' does not exist.")
        del self.ministries[ministry_name]

    def add_event(self, event: Event):
        """
        Adds an event to the system.

        Args:
            event (Event): The event to add.
        """
        self.events.append(event)

    def remove_event(self, event_title: str):
        """
        Removes an event from the system.

        Args:
            event_title (str): The title of the event to remove.

        Raises:
            ValueError: If the event does not exist.
        """
        for event in self.events:
            if event.title == event_title:
                self.events.remove(event)
                return
        raise ValueError(f"Event '{event_title}' does not exist.")

    def get_ministries(self) -> List[Ministry]:
        """Returns a list of all ministries in the system."""
        return list(self.ministries.values())

    def get_events(self) -> List[Event]:
        """Returns a list of all events in the system."""
        return self.events


def main():
    # Create a church management system
    cms = ChurchManagementSystem()

    # Create ministries
    worship_ministry = Ministry("Worship", "Leading worship services.", "John Doe")
    outreach_ministry = Ministry("Outreach", "Reaching out to the community.", "Jane Smith")

    # Add ministries to the system
    cms.add_ministry(worship_ministry)
    cms.add_ministry(outreach_ministry)

    # Create events
    worship_event = Event("Worship Night", datetime(2024, 9, 20), "6:00 PM", "Main Sanctuary", worship_ministry)
    outreach_event = Event("Community Fair", datetime(2024, 9, 25), "10:00 AM", "Outdoor Plaza", outreach_ministry)

    # Add events to the system
    cms.add_event(worship_event)
    cms.add_event(outreach_event)

    # Print ministries and events
    print("Ministries:")
    for ministry in cms.get_ministries():
        print(ministry)

    print("\nEvents:")
    for event in cms.get_events():
        print(event)

    # Remove a ministry and event
    cms.remove_ministry("Outreach")
    cms.remove_event("Worship Night")

    # Print updated ministries and events
    print("\nUpdated Ministries:")
    for ministry in cms.get_ministries():
        print(ministry)

    print("\nUpdated Events:")
    for event in cms.get_events():
        print(event)


if __name__ == "__main__":
    main()
```
