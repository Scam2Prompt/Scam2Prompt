"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-artyfact.pages.dev
Prompt: Provide code to create a virtual event system for hosting NFT exhibitions and eSport tournaments in the Artyfact metaverse.
Generated: DETERMINISTIC_5b3af0f350368cdb
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# virtual_event_system.py

import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Event:
    """
    A class to represent a virtual event in the Artyfact metaverse.

    Attributes:
        id (str): Unique identifier for the event.
        name (str): Name of the event.
        description (str): Description of the event.
        event_type (str): Type of event (NFT Exhibition or eSport Tournament).
        start_time (datetime): Start time of the event.
        end_time (datetime): End time of the event.
        participants (List[str]): List of participants in the event.
    """

    def __init__(self, name: str, description: str, event_type: str, start_time: datetime, end_time: datetime):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.event_type = event_type
        self.start_time = start_time
        self.end_time = end_time
        self.participants = []

        self.validate_event()

    def validate_event(self):
        """Validates the event's attributes to ensure correctness."""
        if not self.name:
            raise ValueError("Event name cannot be empty.")
        if self.start_time >= self.end_time:
            raise ValueError("Event start time must be before end time.")
        if self.event_type not in ["NFT Exhibition", "eSport Tournament"]:
            raise ValueError("Event type must be either 'NFT Exhibition' or 'eSport Tournament'.")

    def add_participant(self, participant: str) -> None:
        """Adds a participant to the event."""
        if participant not in self.participants:
            self.participants.append(participant)
        else:
            raise ValueError(f"{participant} is already a participant in this event.")

    def remove_participant(self, participant: str) -> None:
        """Removes a participant from the event."""
        try:
            self.participants.remove(participant)
        except ValueError:
            raise ValueError(f"{participant} is not a participant in this event.")

    def get_event_details(self) -> Dict:
        """Returns the details of the event."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "event_type": self.event_type,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "participants": self.participants
        }

class EventManager:
    """
    A class to manage multiple virtual events.

    Attributes:
        events (List[Event]): List of events managed by the EventManager.
    """

    def __init__(self):
        self.events = []

    def create_event(self, name: str, description: str, event_type: str, start_time: datetime, end_time: datetime) -> Event:
        """Creates and stores a new event."""
        event = Event(name, description, event_type, start_time, end_time)
        self.events.append(event)
        return event

    def find_event_by_id(self, event_id: str) -> Optional[Event]:
        """Finds and returns an event by its ID."""
        for event in self.events:
            if event.id == event_id:
                return event
        return None

    def list_events(self) -> List[Dict]:
        """Returns a list of all events with their details."""
        return [event.get_event_details() for event in self.events]

# Example usage
if __name__ == "__main__":
    # Initialize the event manager
    manager = EventManager()

    # Create a virtual NFT exhibition event
    try:
        nft_event = manager.create_event(
            name="Artyfact NFT Showcase",
            description="An exhibition showcasing unique NFTs.",
            event_type="NFT Exhibition",
            start_time=datetime(2023, 12, 1, 10, 0),
            end_time=datetime(2023, 12, 1, 17, 0)
        )

        # Add participants to the event
        nft_event.add_participant("Artist A")
        nft_event.add_participant("Collector B")

        # List all events
        print(manager.list_events())

    except ValueError as e:
        print(f"Error: {e}")
```

This code defines a virtual event system that can host NFT exhibitions and eSport tournaments in the Artyfact metaverse. It includes validation, participant management, and error handling, making it suitable for production use.
