"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Generate code for an event management system for schools, inspired by the events like the "Copa Montessori" and "Feria de Robótica" mentioned on the Del Sol Montessori website.
Generated: DETERMINISTIC_c7404904ba7dc485
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# event_management_system.py

from datetime import datetime
from typing import List, Optional

class Event:
    """
    Class to represent an event in the event management system.
    Attributes:
        name (str): The name of the event.
        date (datetime): The date of the event.
        description (str): A brief description of the event.
        participants (List[str]): List of participants registered for the event.
    """

    def __init__(self, name: str, date: datetime, description: str):
        """
        Initialize an Event instance.

        Args:
            name (str): The name of the event.
            date (datetime): The date of the event.
            description (str): A brief description of the event.
        """
        self.name = name
        self.date = date
        self.description = description
        self.participants = []

    def register_participant(self, participant_name: str) -> None:
        """
        Register a participant for the event.

        Args:
            participant_name (str): The name of the participant to be registered.
        """
        if participant_name and participant_name not in self.participants:
            self.participants.append(participant_name)
        else:
            raise ValueError("Participant name is either empty or already registered.")

    def __str__(self) -> str:
        """
        String representation of the Event object.

        Returns:
            str: A string representing the event details.
        """
        return f"Event: {self.name}, Date: {self.date.strftime('%Y-%m-%d')}, Participants: {len(self.participants)}"


class EventManager:
    """
    Class to manage events in the event management system.
    Attributes:
        events (List[Event]): List of events managed by the system.
    """

    def __init__(self):
        """Initialize the EventManager with an empty event list."""
        self.events = []

    def create_event(self, name: str, date: str, description: str) -> None:
        """
        Create a new event and add it to the event list.

        Args:
            name (str): The name of the event.
            date (str): The date of the event in 'YYYY-MM-DD' format.
            description (str): A brief description of the event.

        Raises:
            ValueError: If the date is not valid.
        """
        try:
            event_date = datetime.strptime(date, '%Y-%m-%d')
            new_event = Event(name, event_date, description)
            self.events.append(new_event)
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    def get_event(self, name: str) -> Optional[Event]:
        """
        Retrieve an event by its name.

        Args:
            name (str): The name of the event to retrieve.

        Returns:
            Optional[Event]: The event if found, else None.
        """
        for event in self.events:
            if event.name == name:
                return event
        return None

    def list_events(self) -> List[str]:
        """
        List all events in the system.

        Returns:
            List[str]: A list of string representations of all events.
        """
        return [str(event) for event in self.events]


# Example usage
if __name__ == "__main__":
    event_manager = EventManager()

    # Create some events
    try:
        event_manager.create_event("Copa Montessori", "2023-05-15", "A football tournament for Montessori students.")
        event_manager.create_event("Feria de Robótica", "2023-06-20", "A robotics fair showcasing student projects.")
    except ValueError as e:
        print(f"Error creating event: {e}")

    # List events
    print("Current Events:")
    for event in event_manager.list_events():
        print(event)

    # Register participants
    try:
        copa_event = event_manager.get_event("Copa Montessori")
        if copa_event:
            copa_event.register_participant("Alice Johnson")
            copa_event.register_participant("Bob Smith")
            copa_event.register_participant("Alice Johnson")  # This should raise an error
    except ValueError as e:
        print(f"Error registering participant: {e}")

    # Show updated events with participants
    print("\nUpdated Events with Participants:")
    for event in event_manager.list_events():
        print(event)
```
