"""
Generated Code Metadata:
========================
Original URL: https://sportsbookcochilli.pages.dev
Prompt: Write code to filter and display sports events by category (e.g., Football, MMA, Boxing), as seen in the foldable menu structure of CoChilli SportsBook.
Generated: DETERMINISTIC_09a120c7e18df77f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class SportsEvent:
    """
    Represents a sports event with its details.
    """
    def __init__(self, event_id: str, name: str, category: str, start_time: str, participants: List[str]):
        self.event_id = event_id
        self.name = name
        self.category = category
        self.start_time = start_time
        self.participants = participants

    def to_dict(self) -> Dict:
        """Convert the event to a dictionary for easy serialization."""
        return {
            'event_id': self.event_id,
            'name': self.name,
            'category': self.category,
            'start_time': self.start_time,
            'participants': self.participants
        }

class SportsEventManager:
    """
    Manages sports events and provides filtering by category.
    """
    def __init__(self):
        self.events: List[SportsEvent] = []

    def add_event(self, event: SportsEvent) -> None:
        """Add a new sports event to the manager."""
        self.events.append(event)

    def get_events_by_category(self, category: str) -> List[SportsEvent]:
        """
        Retrieve all events in a specific category.
        
        Args:
            category: The category to filter by (e.g., 'Football', 'MMA').
        
        Returns:
            List of events in the specified category.
        """
        return [event for event in self.events if event.category.lower() == category.lower()]

    def get_all_categories(self) -> List[str]:
        """Get a list of all unique event categories."""
        return list(set(event.category for event in self.events))

    def load_events_from_json(self, file_path: str) -> None:
        """
        Load events from a JSON file.
        
        Args:
            file_path: Path to the JSON file containing events data.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for event_data in data.get('events', []):
                    event = SportsEvent(
                        event_id=event_data['event_id'],
                        name=event_data['name'],
                        category=event_data['category'],
                        start_time=event_data['start_time'],
                        participants=event_data['participants']
                    )
                    self.add_event(event)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("The file is not valid JSON.", file_path, 0)

class SportsEventDisplay:
    """
    Handles the display of sports events in a foldable menu structure.
    """
    @staticmethod
    def display_events_by_category(manager: SportsEventManager) -> None:
        """Display all events grouped by category in a foldable menu structure."""
        categories = manager.get_all_categories()
        for category in sorted(categories):
            print(f"\n=== {category.upper()} ===")
            events = manager.get_events_by_category(category)
            for event in events:
                print(f"  - {event.name} (ID: {event.event_id})")
                print(f"    Start Time: {event.start_time}")
                print(f"    Participants: {', '.join(event.participants)}")

# Example usage
if __name__ == "__main__":
    # Initialize the event manager
    event_manager = SportsEventManager()
    
    # Load events from a JSON file (example file path)
    try:
        event_manager.load_events_from_json('sports_events.json')
    except Exception as e:
        print(f"Error loading events: {e}")
        exit(1)
    
    # Display events by category
    SportsEventDisplay.display_events_by_category(event_manager)
```
