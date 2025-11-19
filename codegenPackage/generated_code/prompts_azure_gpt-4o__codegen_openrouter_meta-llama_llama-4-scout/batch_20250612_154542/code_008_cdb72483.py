"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Create a Python script to generate a report summarizing participation in Egatur events, such as "Feliz Día del Frappe" and "Marcha por la Salud Mental."
Generated: DETERMINISTIC_cdb7248316e44138
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# egatur_participation_report.py

import datetime
from typing import Dict, List

class Event:
    """Represents an Egatur event."""
    
    def __init__(self, name: str, date: str, participants: int, attendees: int):
        """
        Initializes an Event object.

        Args:
        - name (str): The name of the event.
        - date (str): The date of the event in YYYY-MM-DD format.
        - participants (int): The number of participants in the event.
        - attendees (int): The number of attendees in the event.
        """
        self.name = name
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        self.participants = participants
        self.attendees = attendees

    def participation_rate(self) -> float:
        """Calculates the participation rate as a percentage."""
        if self.participants == 0:
            return 0.0
        return (self.attendees / self.participants) * 100


class EgaturReport:
    """Generates a report summarizing participation in Egatur events."""

    def __init__(self):
        self.events: List[Event] = []

    def add_event(self, event: Event):
        """Adds an event to the report."""
        self.events.append(event)

    def generate_report(self) -> str:
        """Generates a report summarizing participation in Egatur events."""
        report = "Egatur Event Participation Report\n"
        report += "-----------------------------------\n"
        report += f"{'Event Name':^40} | {'Date':^10} | {'Participants':^12} | {'Attendees':^9} | {'Participation Rate':^17}\n"
        report += "-----------------------------------\n"

        for event in self.events:
            participation_rate = f"{event.participation_rate():.2f}%"
            report += f"{event.name:^40} | {event.date:^10} | {event.participants:^12} | {event.attendees:^9} | {participation_rate:^17}\n"

        report += "-----------------------------------\n"
        return report

    def save_report_to_file(self, filename: str):
        """Saves the report to a file."""
        try:
            with open(filename, "w") as file:
                file.write(self.generate_report())
            print(f"Report saved to {filename}")
        except Exception as e:
            print(f"Error saving report: {str(e)}")


def main():
    report = EgaturReport()

    # Example events
    events: List[Dict] = [
        {"name": "Feliz Día del Frappe", "date": "2024-08-10", "participants": 100, "attendees": 80},
        {"name": "Marcha por la Salud Mental", "date": "2024-09-01", "participants": 50, "attendees": 45},
    ]

    for event_data in events:
        try:
            event = Event(
                event_data["name"],
                event_data["date"],
                event_data["participants"],
                event_data["attendees"],
            )
            report.add_event(event)
        except KeyError as e:
            print(f"Error creating event: Missing key {e}")

    report.save_report_to_file("egatur_report.txt")


if __name__ == "__main__":
    main()
```
