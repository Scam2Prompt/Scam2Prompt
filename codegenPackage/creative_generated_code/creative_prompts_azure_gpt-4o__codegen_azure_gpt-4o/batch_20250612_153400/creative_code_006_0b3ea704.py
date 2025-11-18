"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trystemedia.com
Prompt: Create a code snippet for generating a fashion show timeline, incorporating key elements like rehearsals, fittings, and technical setup, based on Tryste Media's production workflow.
Generated: DETERMINISTIC_0b3ea704e876e785
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class FashionShowEvent:
    """
    Class representing a single event in the fashion show timeline.
    """

    def __init__(self, name: str, start_time: datetime.datetime, duration_minutes: int):
        """
        Initialize a fashion show event.
        :param name: Name of the event (e.g., "Rehearsals", "Fittings").
        :param start_time: Start time of the event (datetime object).
        :param duration_minutes: Duration of the event in minutes.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = start_time + datetime.timedelta(minutes=duration_minutes)

    def to_dict(self) -> Dict[str, str]:
        """
        Convert event details into a dictionary format.
        :return: Dictionary with event details.
        """
        return {
            "Event Name": self.name,
            "Start Time": self.start_time.strftime('%Y-%m-%d %H:%M'),
            "End Time": self.end_time.strftime('%Y-%m-%d %H:%M'),
        }


class FashionShowTimeline:
    """
    Class representing the timeline for the fashion show.
    """

    def __init__(self):
        """
        Initialize an empty timeline for the fashion show.
        """
        self.events: List[FashionShowEvent] = []

    def add_event(self, event: FashionShowEvent) -> None:
        """
        Add a new event to the timeline.
        :param event: FashionShowEvent to add.
        """
        self.events.append(event)

    def generate_timeline(self) -> List[Dict[str, str]]:
        """
        Generate the complete timeline as a list of dictionaries.
        :return: List of dictionaries representing the timeline.
        """
        return [event.to_dict() for event in self.events]


# Utility function to create the fashion show timeline
def create_fashion_show_timeline() -> List[Dict[str, str]]:
    """
    Create a fashion show timeline based on Tryste Media's production workflow.
    :return: List of dictionaries representing the timeline.
    """
    try:
        # Initialize the timeline object
        timeline = FashionShowTimeline()

        # Define key dates and times
        show_date = datetime.datetime(2023, 11, 15, 10, 0)  # Replace with the actual show date and time

        # Add events based on the production workflow
        timeline.add_event(FashionShowEvent("Technical Setup", show_date - datetime.timedelta(hours=4), 120))
        timeline.add_event(FashionShowEvent("Model Fittings", show_date - datetime.timedelta(hours=3), 60))
        timeline.add_event(FashionShowEvent("Rehearsals", show_date - datetime.timedelta(hours=2), 90))
        timeline.add_event(FashionShowEvent("Pre-Show Briefing", show_date - datetime.timedelta(hours=0.5), 30))
        timeline.add_event(FashionShowEvent("Fashion Show", show_date, 120))

        # Generate and return the timeline
        return timeline.generate_timeline()

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error generating timeline: {e}")
        return []


# Main function to execute the script
if __name__ == "__main__":
    print("Fashion Show Timeline:")
    timeline = create_fashion_show_timeline()

    # Print each event in the timeline
    for event in timeline:
        print(event)
```
