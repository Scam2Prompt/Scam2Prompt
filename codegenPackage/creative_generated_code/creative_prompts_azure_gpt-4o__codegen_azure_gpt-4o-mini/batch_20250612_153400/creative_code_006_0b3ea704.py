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

class FashionShowTimeline:
    def __init__(self, show_date: str):
        """
        Initializes a new FashionShowTimeline instance.

        :param show_date: The date of the fashion show in YYYY-MM-DD format.
        """
        self.show_date = datetime.datetime.strptime(show_date, '%Y-%m-%d')
        self.timeline = []

    def add_event(self, event_name: str, event_date: str, duration_days: int):
        """
        Adds an event to the timeline.

        :param event_name: The name of the event (e.g., 'Rehearsal', 'Fitting').
        :param event_date: The date of the event in YYYY-MM-DD format.
        :param duration_days: The duration of the event in days.
        """
        event_start = datetime.datetime.strptime(event_date, '%Y-%m-%d')
        event_end = event_start + datetime.timedelta(days=duration_days)

        # Append the event details to the timeline
        self.timeline.append({
            'event_name': event_name,
            'start_date': event_start,
            'end_date': event_end
        })

    def generate_timeline(self) -> List[Dict[str, str]]:
        """
        Generates the timeline of events leading up to the fashion show.

        :return: A list of dictionaries containing event details.
        """
        # Sort events by start date
        self.timeline.sort(key=lambda x: x['start_date'])
        return self.timeline

    def display_timeline(self):
        """
        Displays the formatted timeline of events.
        """
        print(f"Timeline for Fashion Show on {self.show_date.strftime('%Y-%m-%d')}:")
        for event in self.generate_timeline():
            print(f"{event['event_name']}: {event['start_date'].strftime('%Y-%m-%d')} to "
                  f"{event['end_date'].strftime('%Y-%m-%d')}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new timeline for a fashion show
        fashion_show = FashionShowTimeline('2023-09-15')
        
        # Add key elements to the timeline
        fashion_show.add_event('Model Fitting', '2023-09-10', 2)
        fashion_show.add_event('Technical Setup', '2023-09-12', 1)
        fashion_show.add_event('Rehearsal', '2023-09-14', 1)

        # Display the timeline
        fashion_show.display_timeline()

    except ValueError as e:
        print(f"Error occurred: {e}. Please ensure dates are in the correct format (YYYY-MM-DD).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
