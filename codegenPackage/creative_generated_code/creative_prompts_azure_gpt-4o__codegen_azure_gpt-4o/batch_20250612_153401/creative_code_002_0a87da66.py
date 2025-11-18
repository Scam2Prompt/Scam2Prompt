"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Generate a script for automating event management and registration workflows in a CMS system tailored for cooperatives.
Generated: DETERMINISTIC_0a87da666661d58d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
from typing import List, Dict, Optional

# Constants for the script
EVENTS_FILE = "events.json"
REGISTRATIONS_FILE = "registrations.json"

# Helper functions to handle loading and saving JSON data
def load_json(filename: str) -> Dict:
    """Load JSON data from a file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON from {filename}")

def save_json(filename: str, data: Dict) -> None:
    """Save JSON data to a file."""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise IOError(f"Error saving JSON to {filename}: {e}")

# Event Management Class
class EventManager:
    def __init__(self, events_file: str, registrations_file: str):
        self.events_file = events_file
        self.registrations_file = registrations_file
        self.events = load_json(events_file)
        self.registrations = load_json(registrations_file)

    def create_event(self, event_id: str, name: str, date: str, capacity: int) -> None:
        """
        Create a new event.
        :param event_id: Unique identifier for the event.
        :param name: Name of the event.
        :param date: Date of the event (YYYY-MM-DD).
        :param capacity: Maximum capacity for the event.
        """
        if event_id in self.events:
            raise ValueError(f"Event with ID '{event_id}' already exists.")
        
        try:
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date}. Use YYYY-MM-DD format.")

        self.events[event_id] = {
            "name": name,
            "date": str(event_date),
            "capacity": capacity,
            "registrations": 0
        }
        save_json(self.events_file, self.events)

    def register_user(self, event_id: str, user_id: str) -> None:
        """
        Register a user for an event.
        :param event_id: Unique identifier for the event.
        :param user_id: Unique identifier for the user.
        """
        if event_id not in self.events:
            raise ValueError(f"Event with ID '{event_id}' does not exist.")
        
        event = self.events[event_id]
        
        if event["registrations"] >= event["capacity"]:
            raise ValueError(f"Event '{event_id}' is at full capacity.")

        if event_id not in self.registrations:
            self.registrations[event_id] = []
        
        if user_id in self.registrations[event_id]:
            raise ValueError(f"User '{user_id}' is already registered for event '{event_id}'.")
        
        self.registrations[event_id].append(user_id)
        self.events[event_id]["registrations"] += 1

        save_json(self.registrations_file, self.registrations)
        save_json(self.events_file, self.events)

    def list_events(self) -> List[Dict]:
        """
        List all events.
        :return: A list of dictionaries containing event information.
        """
        return list(self.events.values())

    def list_event_registrations(self, event_id: str) -> List[str]:
        """
        List all registrations for an event.
        :param event_id: Unique identifier for the event.
        :return: A list of user IDs registered for the event.
        """
        if event_id not in self.events:
            raise ValueError(f"Event with ID '{event_id}' does not exist.")
        
        return self.registrations.get(event_id, [])

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Event Manager
        manager = EventManager(EVENTS_FILE, REGISTRATIONS_FILE)

        # Create a new event
        manager.create_event("event001", "Cooperative Annual Meeting", "2023-12-01", 100)

        # Register users for the event
        manager.register_user("event001", "user001")
        manager.register_user("event001", "user002")

        # List all events
        print("Events:")
        for event in manager.list_events():
            print(event)

        # List registrations for a specific event
        print("\nRegistrations for 'event001':")
        for user in manager.list_event_registrations("event001"):
            print(user)

    except Exception as e:
        print(f"Error: {e}")
```
