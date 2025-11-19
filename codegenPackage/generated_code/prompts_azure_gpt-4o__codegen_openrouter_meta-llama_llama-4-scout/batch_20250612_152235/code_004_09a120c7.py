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
# sports_events.py

from enum import Enum
from typing import List, Dict

class EventCategory(str, Enum):
    """Enum for sports event categories."""
    FOOTBALL = "Football"
    MMA = "MMA"
    BOXING = "Boxing"

class SportsEvent:
    """Represents a sports event."""
    def __init__(self, id: int, name: str, category: EventCategory):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f"Event(id={self.id}, name='{self.name}', category='{self.category.value}')"

class SportsEventFilter:
    """Filters sports events by category."""
    def __init__(self, events: List[SportsEvent]):
        self.events = events

    def filter_by_category(self, category: EventCategory) -> List[SportsEvent]:
        """Filters events by the specified category."""
        return [event for event in self.events if event.category == category]

    def display_events(self, events: List[SportsEvent]):
        """Displays the specified events."""
        for event in events:
            print(f"ID: {event.id}, Name: {event.name}, Category: {event.category.value}")

def main():
    try:
        # Sample sports events
        events: List[SportsEvent] = [
            SportsEvent(1, "Super Bowl", EventCategory.FOOTBALL),
            SportsEvent(2, "UFC Fight Night", EventCategory.MMA),
            SportsEvent(3, "Boxing Match", EventCategory.BOXING),
            SportsEvent(4, "NFL Game", EventCategory.FOOTBALL),
            SportsEvent(5, "MMA Championship", EventCategory.MMA),
        ]

        filter = SportsEventFilter(events)

        print("Sports Events:")
        print("1. Football")
        print("2. MMA")
        print("3. Boxing")

        choice = input("Enter your choice (1/2/3): ")

        category_map: Dict[str, EventCategory] = {
            "1": EventCategory.FOOTBALL,
            "2": EventCategory.MMA,
            "3": EventCategory.BOXING,
        }

        if choice in category_map:
            selected_category = category_map[choice]
            filtered_events = filter.filter_by_category(selected_category)
            print(f"\n{selected_category.value} Events:")
            filter.display_events(filtered_events)
        else:
            print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
