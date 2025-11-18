"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportsbookcochilli.pages.dev
Prompt: Write code to filter and display sports events by category (e.g., Football, MMA, Boxing), as seen in the foldable menu structure of CoChilli SportsBook.
Generated: DETERMINISTIC_09a120c7e18df77f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SportsEventFilter:
    def __init__(self, events):
        """
        Initializes the SportsEventFilter with a list of sports events.
        
        :param events: List of dictionaries containing event details.
        """
        if not isinstance(events, list):
            raise ValueError("Events must be a list of dictionaries.")
        self.events = events

    def filter_by_category(self, category):
        """
        Filters sports events by the specified category.

        :param category: The category to filter events by.
        :return: A list of events in the specified category.
        """
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")
        filtered_events = [event for event in self.events if event.get('category') == category]
        return filtered_events

    def display_events(self, events):
        """
        Displays the list of events in a user-friendly format.

        :param events: List of events to be displayed.
        """
        if not events:
            print("No events found for the selected category.")
            return
        for event in events:
            print(f"Event: {event['name']}, Date: {event['date']}, Location: {event['location']}")

def main():
    # Sample data for demonstration purposes
    sample_events = [
        {"name": "Champions League", "date": "2023-05-10", "location": "Stadium A", "category": "Football"},
        {"name": "UFC 300", "date": "2023-06-20", "location": "Arena B", "category": "MMA"},
        {"name": "Boxing Match XYZ", "date": "2023-07-15", "location": "Arena C", "category": "Boxing"},
        {"name": "Premier League", "date": "2023-08-01", "location": "Stadium D", "category": "Football"}
    ]

    try:
        # Create an instance of the SportsEventFilter
        event_filter = SportsEventFilter(sample_events)

        # Example categories to filter by
        categories = ["Football", "MMA", "Boxing"]

        for category in categories:
            print(f"\nEvents in category: {category}")
            filtered_events = event_filter.filter_by_category(category)
            event_filter.display_events(filtered_events)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
