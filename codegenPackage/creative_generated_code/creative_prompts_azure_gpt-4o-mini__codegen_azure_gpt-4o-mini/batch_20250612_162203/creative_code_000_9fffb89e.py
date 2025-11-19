"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordoflifenw.com
Prompt: Generate a code snippet for a church management system that includes features for tracking ministries and events similar to those at Word of Life Northwest.
Generated: DETERMINISTIC_9fffb89e2a7e3d93
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# church_management_system.py

class Ministry:
    """
    Represents a ministry within the church.
    """
    def __init__(self, name, description):
        """
        Initializes a new Ministry instance.

        :param name: The name of the ministry.
        :param description: A brief description of the ministry.
        """
        self.name = name
        self.description = description
        self.events = []

    def add_event(self, event):
        """
        Adds an event to the ministry.

        :param event: The event to be added.
        """
        if isinstance(event, Event):
            self.events.append(event)
        else:
            raise ValueError("Invalid event. Must be an instance of Event.")

    def __str__(self):
        return f'Ministry: {self.name}, Description: {self.description}'


class Event:
    """
    Represents an event in the church.
    """
    def __init__(self, title, date, ministry):
        """
        Initializes a new Event instance.

        :param title: The title of the event.
        :param date: The date of the event (format: YYYY-MM-DD).
        :param ministry: The ministry associated with this event.
        """
        self.title = title
        self.date = date
        self.ministry = ministry

    def __str__(self):
        return f'Event: {self.title}, Date: {self.date}, Ministry: {self.ministry.name}'


class Church:
    """
    Represents the church management system.
    """
    def __init__(self):
        """
        Initializes the Church instance with an empty list of ministries.
        """
        self.ministries = []

    def add_ministry(self, ministry):
        """
        Adds a ministry to the church.

        :param ministry: The ministry to be added.
        """
        if isinstance(ministry, Ministry):
            self.ministries.append(ministry)
        else:
            raise ValueError("Invalid ministry. Must be an instance of Ministry.")

    def list_ministries(self):
        """
        Returns a list of all ministries in the church.
        """
        return [str(ministry) for ministry in self.ministries]

    def list_events(self):
        """
        Returns a list of all events for each ministry in the church.
        """
        events_list = []
        for ministry in self.ministries:
            for event in ministry.events:
                events_list.append(str(event))
        return events_list


# Example usage
if __name__ == "__main__":
    # Create church management system
    church = Church()

    # Create ministries
    youth_ministry = Ministry(name='Youth Ministry', description='Engaging youth in faith and service.')
    music_ministry = Ministry(name='Music Ministry', description='Leading worship through music.')

    # Add ministries to church
    church.add_ministry(youth_ministry)
    church.add_ministry(music_ministry)

    # Create events
    event1 = Event(title='Youth Retreat', date='2023-08-15', ministry=youth_ministry)
    event2 = Event(title='Worship Night', date='2023-09-10', ministry=music_ministry)

    # Add events to ministries
    youth_ministry.add_event(event1)
    music_ministry.add_event(event2)

    # List ministries and their events
    print("Ministries:")
    for ministry in church.list_ministries():
        print(ministry)

    print("\nEvents:")
    for event in church.list_events():
        print(event)
```
