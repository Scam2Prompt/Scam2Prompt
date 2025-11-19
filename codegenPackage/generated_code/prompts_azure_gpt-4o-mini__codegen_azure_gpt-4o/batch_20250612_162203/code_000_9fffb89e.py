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

import datetime

class Ministry:
    """
    Class to represent a Ministry within the church.
    """
    def __init__(self, name, description):
        """
        Initialize a Ministry object.
        :param name: Name of the ministry
        :param description: Description of the ministry
        """
        self.name = name
        self.description = description
        self.events = []  # List to store events related to the ministry

    def add_event(self, event):
        """
        Add an event to the ministry.
        :param event: Event object to be added
        """
        if isinstance(event, Event):
            self.events.append(event)
        else:
            raise TypeError("Only Event objects can be added to a ministry.")

    def list_events(self):
        """
        List all events associated with the ministry.
        :return: List of events
        """
        return self.events


class Event:
    """
    Class to represent an Event within the church.
    """
    def __init__(self, name, date, time, location, description):
        """
        Initialize an Event object.
        :param name: Name of the event
        :param date: Date of the event (YYYY-MM-DD format)
        :param time: Time of the event (HH:MM format)
        :param location: Location of the event
        :param description: Description of the event
        """
        try:
            self.name = name
            self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            self.time = datetime.datetime.strptime(time, "%H:%M").time()
            self.location = location
            self.description = description
        except ValueError as e:
            raise ValueError(f"Invalid date or time format: {e}")

    def __str__(self):
        """
        String representation of the Event object.
        :return: String describing the event
        """
        return f"Event: {self.name}, Date: {self.date}, Time: {self.time}, Location: {self.location}, Description: {self.description}"


class ChurchManagementSystem:
    """
    Class to represent the Church Management System.
    """
    def __init__(self):
        """
        Initialize the Church Management System.
        """
        self.ministries = {}  # Dictionary to store ministries by name

    def add_ministry(self, ministry):
        """
        Add a ministry to the system.
        :param ministry: Ministry object to be added
        """
        if isinstance(ministry, Ministry):
            if ministry.name not in self.ministries:
                self.ministries[ministry.name] = ministry
            else:
                raise ValueError(f"Ministry '{ministry.name}' already exists.")
        else:
            raise TypeError("Only Ministry objects can be added to the system.")

    def get_ministry(self, name):
        """
        Retrieve a ministry by name.
        :param name: Name of the ministry
        :return: Ministry object
        """
        return self.ministries.get(name, None)

    def list_ministries(self):
        """
        List all ministries in the system.
        :return: List of ministry names
        """
        return list(self.ministries.keys())


# Example usage
if __name__ == "__main__":
    try:
        # Create the church management system
        cms = ChurchManagementSystem()

        # Create ministries
        youth_ministry = Ministry("Youth Ministry", "Focuses on engaging the youth in the church.")
        worship_ministry = Ministry("Worship Ministry", "Handles music and worship services.")

        # Add ministries to the system
        cms.add_ministry(youth_ministry)
        cms.add_ministry(worship_ministry)

        # Create events
        event1 = Event("Youth Retreat", "2023-11-15", "10:00", "Campground", "A retreat for the youth.")
        event2 = Event("Worship Night", "2023-11-20", "18:00", "Main Hall", "An evening of worship and praise.")

        # Add events to ministries
        youth_ministry.add_event(event1)
        worship_ministry.add_event(event2)

        # List ministries
        print("Ministries in the system:")
        for ministry_name in cms.list_ministries():
            print(f"- {ministry_name}")

        # List events for Youth Ministry
        print("\nEvents for Youth Ministry:")
        for event in youth_ministry.list_events():
            print(event)

    except Exception as e:
        print(f"Error: {e}")
```
