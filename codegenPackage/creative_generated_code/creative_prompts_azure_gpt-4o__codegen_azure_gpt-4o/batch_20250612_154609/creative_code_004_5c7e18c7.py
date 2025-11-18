"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Write a script to manage and display upcoming events for an organization, including filtering by industry or membership type.
Generated: DETERMINISTIC_5c7e18c7f086f1e9
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python script that implements a system to manage and display upcoming events for an organization, with filtering options by industry or membership type:

```python
import datetime


class Event:
    """
    Represents an event with details such as name, date, industry, and membership type.
    """

    def __init__(self, name, date, industry, membership_type):
        """
        Initialize an event object.
        
        :param name: Event name
        :param date: Event date (datetime object)
        :param industry: Industry associated with the event
        :param membership_type: Membership type associated with the event
        """
        self.name = name
        self.date = date
        self.industry = industry
        self.membership_type = membership_type


class EventManager:
    """
    Manages a collection of events and provides filtering and display functionality.
    """

    def __init__(self):
        """
        Initialize the event manager with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the manager.
        
        :param event: An instance of the Event class
        """
        if not isinstance(event, Event):
            raise TypeError("Invalid event type. Expected an instance of Event.")
        self.events.append(event)

    def filter_events(self, industry=None, membership_type=None):
        """
        Filter events based on industry and/or membership type.
        
        :param industry: Filter by industry (string, optional)
        :param membership_type: Filter by membership type (string, optional)
        :return: List of filtered events
        """
        filtered_events = self.events
        if industry:
            filtered_events = [event for event in filtered_events if event.industry == industry]
        if membership_type:
            filtered_events = [event for event in filtered_events if event.membership_type == membership_type]

        return filtered_events

    def get_upcoming_events(self):
        """
        Get upcoming events (events with dates in the future).
        
        :return: List of upcoming events
        """
        today = datetime.datetime.now()
        return [event for event in self.events if event.date > today]

    def display_events(self, events):
        """
        Display a list of events with details.
        
        :param events: List of Event objects to display
        """
        if not events:
            print("No events found.")
            return
        print(f"{'Event Name':<20} {'Date':<15} {'Industry':<15} {'Membership Type':<15}")
        print("=" * 65)
        for event in events:
            print(f"{event.name:<20} {event.date.strftime('%Y-%m-%d'):<15} {event.industry:<15} {event.membership_type:<15}")


# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the event manager
        manager = EventManager()

        # Add some events
        manager.add_event(Event("Tech Conference", datetime.datetime(2023, 11, 10), "Technology", "Premium"))
        manager.add_event(Event("Finance Summit", datetime.datetime(2023, 12, 5), "Finance", "Regular"))
        manager.add_event(Event("Health Expo", datetime.datetime(2023, 12, 15), "Healthcare", "Premium"))
        manager.add_event(Event("Tech Workshop", datetime.datetime(2023, 11, 20), "Technology", "Regular"))

        # Display all upcoming events
        print("\nUpcoming Events:")
        upcoming_events = manager.get_upcoming_events()
        manager.display_events(upcoming_events)

        # Filter events by industry
        print("\nFiltered Events (Industry: Technology):")
        tech_events = manager.filter_events(industry="Technology")
        manager.display_events(tech_events)

        # Filter events by membership type
        print("\nFiltered Events (Membership Type: Premium):")
        premium_events = manager.filter_events(membership_type="Premium")
        manager.display_events(premium_events)

    except Exception as e:
        print(f"An error occurred: {e}")
```

This script follows best practices for readability, maintainability, and error handling, and should work as expected in a production environment.
