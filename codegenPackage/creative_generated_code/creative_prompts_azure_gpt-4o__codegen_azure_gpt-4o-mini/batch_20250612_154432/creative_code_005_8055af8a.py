"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Write code to develop a search functionality for finding sports events or casino games by name, similar to the search feature on the Parimatch platform.
Generated: DETERMINISTIC_8055af8aa0f94d21
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Union, Optional

class EventSearch:
    def __init__(self, data_source: str):
        """
        Initialize the EventSearch with a JSON data source.

        :param data_source: Path to the JSON file containing sports events and casino games.
        """
        self.data_source = data_source
        self.events = self.load_data()

    def load_data(self) -> List[Dict[str, Union[str, int]]]:
        """
        Load event data from the JSON file.

        :return: A list of event dictionaries.
        """
        try:
            with open(self.data_source, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data source {self.data_source} not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON. Please check the file format.")

    def search_events(self, query: str) -> List[Dict[str, Union[str, int]]]:
        """
        Search for events containing the query in their name.

        :param query: The search term to look for in event names.
        :return: A list of events that match the search query.
        """
        if not query:
            raise ValueError("Search query cannot be empty.")
        
        # Normalize query to lowercase for case-insensitive searching
        query = query.lower()
        matched_events = [
            event for event in self.events 
            if query in event['name'].lower()
        ]
        
        return matched_events

    def display_results(self, results: List[Dict[str, Union[str, int]]]) -> None:
        """
        Display the search results in a readable format.

        :param results: List of events to display.
        """
        if not results:
            print("No matching events found.")
            return
        
        for event in results:
            print(f"Event Name: {event['name']}, Type: {event['type']}, ID: {event['id']}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the EventSearch with a JSON data source
        searcher = EventSearch('events.json')

        # Search for events with a specific query
        search_query = input("Enter the name of the event or game to search: ")
        results = searcher.search_events(search_query)

        # Display the search results
        searcher.display_results(results)

    except Exception as e:
        print(f"An error occurred: {e}")
```
