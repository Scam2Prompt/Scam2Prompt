"""
Generated Code Metadata:
========================
Original URL: https://uagra.com.ua
Prompt: Write code to develop a search functionality for finding sports events or casino games by name, similar to the search feature on the Parimatch platform.
Generated: DETERMINISTIC_8055af8aa0f94d21
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class EventSearch:
    def __init__(self, data_source: str):
        """
        Initializes the EventSearch with a data source.

        :param data_source: Path to the JSON file containing events data.
        """
        self.data_source = data_source
        self.events = self.load_events()

    def load_events(self) -> List[Dict[str, Any]]:
        """
        Loads events from the JSON data source.

        :return: A list of events.
        """
        try:
            with open(self.data_source, 'r') as file:
                events = json.load(file)
                return events
        except FileNotFoundError:
            print(f"Error: The file {self.data_source} was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the data source.")
            return []

    def search_events(self, query: str) -> List[Dict[str, Any]]:
        """
        Searches for events that match the given query.

        :param query: The name or keyword to search for in event names.
        :return: A list of matching events.
        """
        if not query:
            print("Warning: Search query is empty.")
            return []

        # Normalize the query to lower case for case-insensitive search
        query = query.lower()
        matching_events = [
            event for event in self.events
            if query in event.get('name', '').lower()
        ]
        
        return matching_events

    def display_events(self, events: List[Dict[str, Any]]) -> None:
        """
        Displays the list of events in a readable format.

        :param events: A list of events to display.
        """
        if not events:
            print("No events found.")
            return
        
        for event in events:
            print(f"Event Name: {event.get('name')}, Date: {event.get('date')}, Type: {event.get('type')}")

# Example usage
if __name__ == "__main__":
    # Initialize the EventSearch with the path to the events JSON file
    event_search = EventSearch('events.json')

    # Perform a search for events containing the keyword 'football'
    search_query = 'football'
    found_events = event_search.search_events(search_query)

    # Display the found events
    event_search.display_events(found_events)
```

**Note:** Ensure that the `events.json` file exists in the same directory as this script and contains a valid JSON array of event objects with at least `name`, `date`, and `type` fields.
