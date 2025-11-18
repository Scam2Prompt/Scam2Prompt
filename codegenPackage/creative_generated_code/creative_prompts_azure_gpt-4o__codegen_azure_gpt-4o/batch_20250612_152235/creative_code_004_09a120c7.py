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

# Sample data representing sports events
sports_data = [
    {"id": 1, "name": "Champions League Final", "category": "Football"},
    {"id": 2, "name": "UFC 280", "category": "MMA"},
    {"id": 3, "name": "WBO Heavyweight Championship", "category": "Boxing"},
    {"id": 4, "name": "Premier League Match", "category": "Football"},
    {"id": 5, "name": "Bellator 300", "category": "MMA"},
]

def filter_events_by_category(events, category):
    """
    Filters sports events by the given category.

    Args:
        events (list): List of sports events, where each event is a dictionary.
        category (str): Category to filter events by (e.g., 'Football', 'MMA').

    Returns:
        list: List of filtered events belonging to the specified category.
    """
    try:
        # Validate input
        if not isinstance(events, list):
            raise ValueError("Events should be a list of dictionaries.")
        if not isinstance(category, str):
            raise ValueError("Category should be a string.")

        # Filter events
        filtered_events = [event for event in events if event.get("category") == category]
        return filtered_events
    except Exception as e:
        print(f"Error filtering events: {e}")
        return []

def display_events(events):
    """
    Displays sports events in a readable format.

    Args:
        events (list): List of sports events, where each event is a dictionary.
    """
    if not events:  # Handle case when there are no events to display
        print("No events available.")
        return

    print("Sports Events:")
    for event in events:
        print(f"- {event['name']} (Category: {event['category']})")

def main():
    """
    Main function to demonstrate filtering and displaying sports events by category.
    """
    print("Available Categories: Football, MMA, Boxing")
    selected_category = input("Enter category to filter events: ").strip()

    # Filter events based on user input
    filtered_events = filter_events_by_category(sports_data, selected_category)

    # Display filtered events
    display_events(filtered_events)

if __name__ == "__main__":
    main()
```
