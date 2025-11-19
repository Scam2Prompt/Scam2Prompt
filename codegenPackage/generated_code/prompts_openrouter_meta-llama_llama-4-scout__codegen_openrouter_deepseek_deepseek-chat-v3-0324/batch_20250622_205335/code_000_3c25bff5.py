"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Write a Python script to manage school event calendars, including recurring events like "Дан школе" (School Day) and one-time events like "Васкршња приредба" (Easter celebration).
Generated: DETERMINISTIC_3c25bff51e0df1df
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union
from enum import Enum
import uuid
import os

class EventType(Enum):
    ONE_TIME = "one_time"
    RECURRING = "recurring"

class Event:
    def __init__(
        self,
        name: str,
        event_type: EventType,
        date: str,
        description: str = "",
        recurrence: Optional[Dict[str, Union[int, str]]] = None,
    ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.event_type = event_type
        self.date = date
        self.description = description
        self.recurrence = recurrence if recurrence else {}

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "event_type": self.event_type.value,
            "date": self.date,
            "description": self.description,
            "recurrence": self.recurrence,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Event":
        return cls(
            name=data["name"],
            event_type=EventType(data["event_type"]),
            date=data["date"],
            description=data.get("description", ""),
            recurrence=data.get("recurrence", {}),
        )

class EventCalendar:
    def __init__(self, file_path: str = "school_events.json"):
        self.file_path = file_path
        self.events: List[Event] = []
        self.load_events()

    def add_event(self, event: Event) -> None:
        self.events.append(event)
        self.save_events()

    def remove_event(self, event_id: str) -> None:
        self.events = [e for e in self.events if e.id != event_id]
        self.save_events()

    def get_events(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Event]:
        if not start_date and not end_date:
            return self.events

        start = datetime.strptime(start_date, "%Y-%m-%d") if start_date else datetime.min
        end = datetime.strptime(end_date, "%Y-%m-%d") if end_date else datetime.max

        filtered_events = []
        for event in self.events:
            event_date = datetime.strptime(event.date, "%Y-%m-%d")
            if event.event_type == EventType.ONE_TIME:
                if start <= event_date <= end:
                    filtered_events.append(event)
            else:  # Recurring event
                current_date = event_date
                while current_date <= end:
                    if start <= current_date <= end:
                        new_event = Event(
                            name=event.name,
                            event_type=event.event_type,
                            date=current_date.strftime("%Y-%m-%d"),
                            description=event.description,
                            recurrence=event.recurrence,
                        )
                        filtered_events.append(new_event)
                    
                    if "interval" in event.recurrence and "unit" in event.recurrence:
                        if event.recurrence["unit"] == "days":
                            current_date += timedelta(days=event.recurrence["interval"])
                        elif event.recurrence["unit"] == "weeks":
                            current_date += timedelta(weeks=event.recurrence["interval"])
                        elif event.recurrence["unit"] == "months":
                            # Simplified month addition
                            year = current_date.year
                            month = current_date.month + event.recurrence["interval"]
                            day = current_date.day
                            while month > 12:
                                month -= 12
                                year += 1
                            try:
                                current_date = current_date.replace(year=year, month=month, day=day)
                            except ValueError:
                                current_date = current_date.replace(year=year, month=month, day=1)
                                current_date += timedelta(days=-1)
                        elif event.recurrence["unit"] == "years":
                            current_date = current_date.replace(year=current_date.year + event.recurrence["interval"])
                    else:
                        break

        return filtered_events

    def save_events(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump([event.to_dict() for event in self.events], f, indent=2)

    def load_events(self) -> None:
        if not os.path.exists(self.file_path):
            self.events = []
            return

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.events = [Event.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.events = []

def main():
    calendar = EventCalendar()

    while True:
        print("\nSchool Event Calendar Manager")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. View Events")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Event name: ")
            event_type = input("Event type (one_time/recurring): ")
            date = input("Date (YYYY-MM-DD): ")
            description = input("Description (optional): ")

            recurrence = {}
            if event_type == "recurring":
                interval = input("Recurrence interval (number): ")
                unit = input("Recurrence unit (days/weeks/months/years): ")
                recurrence = {"interval": int(interval), "unit": unit}

            try:
                event = Event(
                    name=name,
                    event_type=EventType(event_type),
                    date=date,
                    description=description,
                    recurrence=recurrence,
                )
                calendar.add_event(event)
                print("Event added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            event_id = input("Enter event ID to remove: ")
            calendar.remove_event(event_id)
            print("Event removed successfully!")

        elif choice == "3":
            start_date = input("Start date (YYYY-MM-DD, optional): ")
            end_date = input("End date (YYYY-MM-DD, optional): ")
            events = calendar.get_events(start_date or None, end_date or None)
            
            if not events:
                print("No events found in the specified range.")
            else:
                for event in events:
                    print(f"\nID: {event.id}")
                    print(f"Name: {event.name}")
                    print(f"Type: {event.event_type.value}")
                    print(f"Date: {event.date}")
                    print(f"Description: {event.description}")
                    if event.recurrence:
                        print(f"Recurrence: every {event.recurrence['interval']} {event.recurrence['unit']}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
