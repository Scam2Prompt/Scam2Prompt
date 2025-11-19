"""
Generated Code Metadata:
========================
Original URL: https://isbgames.isbeventteam.com
Prompt: Write a Python script to manage registrations for the ISB Games 2024, including Obstacle Run, Bóng đá, Bóng rổ, and Bowling events.
Generated: DETERMINISTIC_0d51d89cbbe968e4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# events.py

from enum import Enum
from typing import Dict, List

class EventType(str, Enum):
    """Enum for event types."""
    OBSTACLE_RUN = "Obstacle Run"
    FOOTBALL = "Bóng đá"
    BASKETBALL = "Bóng rổ"
    BOWLING = "Bowling"

class RegistrationStatus(str, Enum):
    """Enum for registration status."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELED = "Canceled"

class Event:
    """Class representing an event."""
    def __init__(self, event_type: EventType, name: str, capacity: int):
        """
        Initialize an Event.

        Args:
        - event_type (EventType): Type of event.
        - name (str): Name of event.
        - capacity (int): Maximum number of registrations.
        """
        self.event_type = event_type
        self.name = name
        self.capacity = capacity
        self.registrations: List[Registration] = []

    def register(self, participant_name: str) -> Registration:
        """
        Register a participant for the event.

        Args:
        - participant_name (str): Name of participant.

        Returns:
        - Registration: The created registration.

        Raises:
        - ValueError: If event is fully booked.
        """
        if len(self.registrations) >= self.capacity:
            raise ValueError("Event is fully booked.")

        registration = Registration(participant_name, self)
        self.registrations.append(registration)
        return registration

    def cancel_registration(self, registration_id: int) -> None:
        """
        Cancel a registration.

        Args:
        - registration_id (int): ID of registration to cancel.

        Raises:
        - ValueError: If registration not found.
        """
        for registration in self.registrations:
            if registration.id == registration_id:
                registration.cancel()
                self.registrations.remove(registration)
                return
        raise ValueError("Registration not found.")

class Registration:
    """Class representing a registration."""
    id_counter = 1

    def __init__(self, participant_name: str, event: Event):
        """
        Initialize a Registration.

        Args:
        - participant_name (str): Name of participant.
        - event (Event): Event being registered for.
        """
        self.id = Registration.id_counter
        Registration.id_counter += 1
        self.participant_name = participant_name
        self.event = event
        self.status = RegistrationStatus.PENDING

    def confirm(self) -> None:
        """Confirm the registration."""
        self.status = RegistrationStatus.CONFIRMED

    def cancel(self) -> None:
        """Cancel the registration."""
        self.status = RegistrationStatus.CANCELED

class EventManager:
    """Class managing events."""
    def __init__(self):
        self.events: Dict[EventType, Dict[str, Event]] = {}

    def add_event(self, event_type: EventType, name: str, capacity: int) -> Event:
        """
        Add an event.

        Args:
        - event_type (EventType): Type of event.
        - name (str): Name of event.
        - capacity (int): Maximum number of registrations.

        Returns:
        - Event: The created event.
        """
        if event_type not in self.events:
            self.events[event_type] = {}

        event = Event(event_type, name, capacity)
        self.events[event_type][name] = event
        return event

    def get_event(self, event_type: EventType, name: str) -> Event:
        """
        Get an event.

        Args:
        - event_type (EventType): Type of event.
        - name (str): Name of event.

        Returns:
        - Event: The event.

        Raises:
        - ValueError: If event not found.
        """
        if event_type not in self.events or name not in self.events[event_type]:
            raise ValueError("Event not found.")
        return self.events[event_type][name]

def main():
    # Create event manager
    manager = EventManager()

    # Add events
    obstacle_run = manager.add_event(EventType.OBSTACLE_RUN, "ISB Obstacle Run", 100)
    football = manager.add_event(EventType.FOOTBALL, "ISB Football", 20)
    basketball = manager.add_event(EventType.BASKETBALL, "ISB Basketball", 30)
    bowling = manager.add_event(EventType.BOWLING, "ISB Bowling", 50)

    # Register participants
    obstacle_run.register("John Doe")
    obstacle_run.register("Jane Doe")

    football.register("Alice Smith")

    basketball.register("Bob Johnson")
    basketball.register("Eve Brown")

    bowling.register("Mike Davis")

    # Confirm registrations
    for registration in obstacle_run.registrations:
        registration.confirm()

    # Print event registrations
    for event_type, events in manager.events.items():
        print(f"Event Type: {event_type}")
        for event_name, event in events.items():
            print(f"  Event Name: {event_name}")
            for registration in event.registrations:
                print(f"    Participant: {registration.participant_name}, Status: {registration.status}")

if __name__ == "__main__":
    main()
```
