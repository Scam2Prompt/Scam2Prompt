"""
Generated Code Metadata:
========================
Original URL: https://vipmoov.com
Prompt: Write a Python function that utilizes an event planning library to manage events globally, inspired by the services provided by VIP MOOV.
Generated: DETERMINISTIC_7d8bc75b541973ef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel, ValidationError

# Event model using Pydantic for data validation
class Event(BaseModel):
    name: str
    location: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    description: Optional[str] = None

# Global event storage
event_storage: List[Event] = []

def add_event(event_data: Dict) -> str:
    """
    Adds a new event to the global event storage.

    Args:
        event_data (Dict): A dictionary containing event details.

    Returns:
        str: Success message or error message.
    """
    try:
        # Validate and create an Event object
        event = Event(**event_data)
        
        # Check for overlapping events
        for existing_event in event_storage:
            if (event.start_time < existing_event.end_time and 
                event.end_time > existing_event.start_time):
                return f"Error: Event '{event.name}' overlaps with '{existing_event.name}'."
        
        # Add the event to storage
        event_storage.append(event)
        return f"Event '{event.name}' added successfully."
    except ValidationError as e:
        return f"Error: Invalid event data. {e}"

def list_events() -> List[Dict]:
    """
    Lists all events in the global event storage.

    Returns:
        List[Dict]: A list of dictionaries representing all events.
    """
    return [event.dict() for event in event_storage]

def remove_event(event_name: str) -> str:
    """
    Removes an event by name from the global event storage.

    Args:
        event_name (str): The name of the event to remove.

    Returns:
        str: Success message or error message.
    """
    global event_storage
    for event in event_storage:
        if event.name == event_name:
            event_storage.remove(event)
            return f"Event '{event_name}' removed successfully."
    return f"Error: Event '{event_name}' not found."

# Example usage
if __name__ == "__main__":
    # Adding events
    print(add_event({
        "name": "VIP Gala",
        "location": "New York",
        "start_time": datetime.datetime(2023, 12, 1, 18, 0),
        "end_time": datetime.datetime(2023, 12, 1, 22, 0),
        "description": "An exclusive gala for VIPs."
    }))
    
    print(add_event({
        "name": "Tech Conference",
        "location": "San Francisco",
        "start_time": datetime.datetime(2023, 12, 2, 9, 0),
        "end_time": datetime.datetime(2023, 12, 2, 17, 0),
        "description": "A conference for tech enthusiasts."
    }))
    
    # Listing events
    print("Current Events:", list_events())
    
    # Removing an event
    print(remove_event("VIP Gala"))
    
    # Listing events after removal
    print("Current Events:", list_events())
```
