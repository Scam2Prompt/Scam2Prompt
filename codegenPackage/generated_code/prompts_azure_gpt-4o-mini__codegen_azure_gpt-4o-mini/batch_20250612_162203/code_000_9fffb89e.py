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

class Ministry:
    """
    A class to represent a ministry within the church.
    """

    def __init__(self, name, description):
        """
        Initializes a new Ministry instance.

        :param name: Name of the ministry
        :param description: Description of the ministry
        """
        self.name = name
        self.description = description
        self.events = []

    def add_event(self, event):
        """
        Adds an event to the ministry.

        :param event: Event instance to be added
        """
        if not isinstance(event, Event):
            raise ValueError("Only Event instances can be added.")
        self.events.append(event)

    def __str__(self):
        return f"Ministry: {self.name}, Description: {self.description}, Events: {len(self.events)}"


class Event:
    """
    A class to represent an event within a ministry.
    """

    def __init__(self, title, date, location):
        """
        Initializes a new Event instance.

        :param title: Title of the event
        :param date: Date of the event (YYYY-MM-DD format)
        :param location: Location of the event
        """
        self.title = title
        self.date = date
        self.location = location

    def __str__(self):
        return f"Event: {self.title}, Date: {self.date}, Location: {self.location}"


class ChurchManagementSystem:
    """
    A class to manage ministries and events in the church.
    """

    def __init__(self):
        """
        Initializes the Church Management System with an empty list of ministries.
        """
        self.ministries = []

    def add_ministry(self, ministry):
        """
        Adds a ministry to the church management system.

        :param ministry: Ministry instance to be added
        """
        if not isinstance(ministry, Ministry):
            raise ValueError("Only Ministry instances can be added.")
        self.ministries.append(ministry)

    def list_ministries(self):
        """
        Lists all ministries in the church management system.
        """
        for ministry in self.ministries:
            print(ministry)

    def find_ministry(self, name):
        """
        Finds a ministry by name.

        :param name: Name of the ministry to find
        :return: Ministry instance if found, else None
        """
        for ministry in self.ministries:
            if ministry.name == name:
                return ministry
        return None


# Example usage
if __name__ == "__main__":
    try:
        cms = ChurchManagementSystem()

        # Create ministries
        youth_ministry = Ministry("Youth Ministry", "Engaging youth in faith and community.")
        adult_ministry = Ministry("Adult Ministry", "Fostering spiritual growth among adults.")

        # Add ministries to the system
        cms.add_ministry(youth_ministry)
        cms.add_ministry(adult_ministry)

        # Create events
        event1 = Event("Youth Retreat", "2023-09-15", "Camp Pinewood")
        event2 = Event("Adult Bible Study", "2023-09-20", "Church Hall")

        # Add events to ministries
        youth_ministry.add_event(event1)
        adult_ministry.add_event(event2)

        # List all ministries
        cms.list_ministries()

    except Exception as e:
        print(f"An error occurred: {e}")
```
