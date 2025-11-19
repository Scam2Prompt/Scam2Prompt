"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Illustrate how to implement a project management tool for organizing museum events, based on the organizational strategies shared by Mêtis.
Generated: DETERMINISTIC_c04c0cd77548f3cd
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Management Tool for Organizing Museum Events
This tool helps manage museum events based on organizational strategies inspired by Mêtis, an approach to organizing resources and tasks efficiently.
"""

# Import necessary modules
import datetime
import json


class Event:
    """
    Class representing an individual event.
    """
    def __init__(self, title, description, date, time, location):
        """
        Initialize an event with necessary details.
        
        :param title: Title of the event (str)
        :param description: Description of the event (str)
        :param date: Date of the event (YYYY-MM-DD format) (str)
        :param time: Time of the event (HH:MM format) (str)
        :param location: Location of the event (str)
        """
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.location = location

    def __str__(self):
        """
        Return a string representation of the event.
        """
        return f"{self.title} - {self.description} on {self.date} at {self.time}, Location: {self.location}"

    def serialize(self):
        """
        Serialize event details into a dictionary.
        
        :return: Dictionary representation of the event
        """
        return {
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "time": self.time,
            "location": self.location
        }


class ProjectManagementTool:
    """
    Class for managing museum events.
    """
    def __init__(self):
        """
        Initialize the project management tool with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add a new event to the management system.
        
        :param event: An instance of the Event class
        """
        self.events.append(event)

    def list_events(self):
        """
        List all events, sorted by date and time.
        """
        sorted_events = sorted(
            self.events, key=lambda e: (e.date, e.time)
        )
        for event in sorted_events:
            print(event)

    def save_events_to_file(self, filename):
        """
        Save all events to a file in JSON format.
        
        :param filename: Name of the file to save events to (str)
        """
        try:
            with open(filename, 'w') as file:
                json.dump([event.serialize() for event in self.events], file)
            print(f"Events successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving events to file: {e}")

    def load_events_from_file(self, filename):
        """
        Load events from a file in JSON format.
        
        :param filename: Name of the file to load events from (str)
        """
        try:
            with open(filename, 'r') as file:
                events_data = json.load(file)
                self.events = [
                    Event(
                        event['title'],
                        event['description'],
                        event['date'],
                        event['time'],
                        event['location']
                    )
                    for event in events_data
                ]
            print(f"Events successfully loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading events from file: {e}")


# Main program for demonstration
if __name__ == "__main__":
    pm_tool = ProjectManagementTool()

    # Add sample events
    pm_tool.add_event(Event("Art Exhibition", "An exhibition of modern art", "2023-11-15", "18:00", "Main Gallery"))
    pm_tool.add_event(Event("History Talk", "Lecture on ancient civilizations", "2023-11-20", "15:00", "Auditorium"))

    # Display events
    print("Current Events:")
    pm_tool.list_events()

    # Save events to file
    pm_tool.save_events_to_file("events.json")

    # Load events from file
    pm_tool.load_events_from_file("events.json")
    print("Events After Loading:")
    pm_tool.list_events()
```
