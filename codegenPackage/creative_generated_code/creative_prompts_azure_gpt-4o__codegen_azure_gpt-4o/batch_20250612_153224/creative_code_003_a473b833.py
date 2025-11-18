"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.al-aanqua.com
Prompt: Create a script to organize and categorize cultural events listed on "العنقاء للثقافة," including مهرجان المسرح العربي and مهرجان وهران الدولي للفيلم العربي.
Generated: DETERMINISTIC_a473b833a6d2f08c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Define a class for managing cultural events
class CulturalEventManager:
    def __init__(self, data_file='events_data.json'):
        """
        Initialize the manager with a data file.
        :param data_file: Path to the JSON file storing event data.
        """
        self.data_file = data_file
        self.events = []

        # Load events from file if it exists
        if os.path.exists(self.data_file):
            self._load_events()

    def _load_events(self):
        """
        Load events from the JSON file.
        """
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                self.events = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading events: {e}")
            self.events = []

    def _save_events(self):
        """
        Save events to the JSON file.
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(self.events, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error saving events: {e}")

    def add_event(self, name, category, location, date):
        """
        Add a new cultural event.
        :param name: Name of the event.
        :param category: Category of the event (e.g., Theater, Film).
        :param location: Location of the event.
        :param date: Date of the event in YYYY-MM-DD format.
        """
        self.events.append({
            'name': name,
            'category': category,
            'location': location,
            'date': date
        })
        self._save_events()

    def list_events_by_category(self, category):
        """
        List all events under a specific category.
        :param category: Category to filter events by.
        :return: List of events matching the category.
        """
        return [event for event in self.events if event['category'].lower() == category.lower()]

    def list_all_events(self):
        """
        List all events.
        :return: List of all events.
        """
        return self.events

# Instantiate the CulturalEventManager
event_manager = CulturalEventManager()

# Add initial cultural events
event_manager.add_event(
    name="مهرجان المسرح العربي",
    category="Theater",
    location="Various Locations",
    date="2023-11-15"
)

event_manager.add_event(
    name="مهرجان وهران الدولي للفيلم العربي",
    category="Film",
    location="وهران، الجزائر",
    date="2023-12-10"
)

# Example usage
print("All Events:")
print(event_manager.list_all_events())

print("\nTheater Events:")
print(event_manager.list_events_by_category("Theater"))

print("\nFilm Events:")
print(event_manager.list_events_by_category("Film"))
```
