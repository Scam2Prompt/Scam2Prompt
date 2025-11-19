"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Write a Python script to manage event planning tasks such as scheduling, vendor management, and timeline creation for a corporate event.
Generated: DETERMINISTIC_a0dfe11fb5346529
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Event:
    """Class to represent an event with its details."""
    
    def __init__(self, name: str, date: datetime.date, location: str):
        self.name = name
        self.date = date
        self.location = location
        self.tasks: List[Task] = []
        self.vendors: List[Vendor] = []

    def add_task(self, task: 'Task'):
        """Add a task to the event."""
        self.tasks.append(task)

    def add_vendor(self, vendor: 'Vendor'):
        """Add a vendor to the event."""
        self.vendors.append(vendor)

    def get_event_details(self) -> Dict[str, str]:
        """Return the details of the event."""
        return {
            "name": self.name,
            "date": self.date.isoformat(),
            "location": self.location,
            "tasks": [task.get_details() for task in self.tasks],
            "vendors": [vendor.get_details() for vendor in self.vendors]
        }

class Task:
    """Class to represent a task associated with an event."""
    
    def __init__(self, description: str, due_date: datetime.date):
        self.description = description
        self.due_date = due_date

    def get_details(self) -> Dict[str, str]:
        """Return the details of the task."""
        return {
            "description": self.description,
            "due_date": self.due_date.isoformat()
        }

class Vendor:
    """Class to represent a vendor for the event."""
    
    def __init__(self, name: str, service: str, contact_info: str):
        self.name = name
        self.service = service
        self.contact_info = contact_info

    def get_details(self) -> Dict[str, str]:
        """Return the details of the vendor."""
        return {
            "name": self.name,
            "service": self.service,
            "contact_info": self.contact_info
        }

def main():
    """Main function to manage event planning tasks."""
    try:
        # Create an event
        event_name = "Corporate Annual Meeting"
        event_date = datetime.date(2023, 12, 15)
        event_location = "Downtown Conference Center"
        
        corporate_event = Event(event_name, event_date, event_location)

        # Add tasks to the event
        corporate_event.add_task(Task("Book venue", datetime.date(2023, 11, 1)))
        corporate_event.add_task(Task("Send invitations", datetime.date(2023, 11, 15)))
        corporate_event.add_task(Task("Confirm catering", datetime.date(2023, 12, 1)))

        # Add vendors to the event
        corporate_event.add_vendor(Vendor("ABC Catering", "Catering", "contact@abccatering.com"))
        corporate_event.add_vendor(Vendor("XYZ Audio", "Audio/Visual", "support@xyzaudio.com"))

        # Print event details
        event_details = corporate_event.get_event_details()
        print("Event Details:")
        print(event_details)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
