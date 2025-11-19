"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Write a Python script to manage event registrations for a corporate event in Bogotá, including social event planning and RSVP tracking.
Generated: DETERMINISTIC_384e5a92c35e8753
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
from typing import Dict, List, Optional

class EventRegistrationManager:
    """Manages event registrations, social event planning, and RSVP tracking."""

    def __init__(self, data_file: str = "event_registrations.csv"):
        """Initialize the registration manager with a data file."""
        self.data_file = data_file
        self.registrations: List[Dict[str, str]] = []
        self._load_registrations()

    def _load_registrations(self) -> None:
        """Load existing registrations from the data file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    self.registrations = list(reader)
        except Exception as e:
            print(f"Error loading registrations: {e}")
            self.registrations = []

    def _save_registrations(self) -> None:
        """Save current registrations to the data file."""
        try:
            fieldnames = ["id", "name", "email", "company", "position", 
                         "event_date", "rsvp_status", "social_event", "timestamp"]
            
            with open(self.data_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.registrations)
        except Exception as e:
            print(f"Error saving registrations: {e}")

    def register_attendee(self, name: str, email: str, company: str, position: str, 
                         event_date: str, social_event: str = "No") -> str:
        """Register a new attendee for the event."""
        try:
            attendee_id = str(len(self.registrations) + 1)
            timestamp = datetime.datetime.now().isoformat()
            
            registration = {
                "id": attendee_id,
                "name": name,
                "email": email,
                "company": company,
                "position": position,
                "event_date": event_date,
                "rsvp_status": "Pending",
                "social_event": social_event,
                "timestamp": timestamp
            }
            
            self.registrations.append(registration)
            self._save_registrations()
            return attendee_id
        except Exception as e:
            print(f"Error registering attendee: {e}")
            return ""

    def update_rsvp(self, attendee_id: str, status: str) -> bool:
        """Update the RSVP status of an attendee."""
        try:
            for registration in self.registrations:
                if registration["id"] == attendee_id:
                    registration["rsvp_status"] = status
                    self._save_registrations()
                    return True
            return False
        except Exception as e:
            print(f"Error updating RSVP: {e}")
            return False

    def get_attendee(self, attendee_id: str) -> Optional[Dict[str, str]]:
        """Retrieve attendee details by ID."""
        try:
            for registration in self.registrations:
                if registration["id"] == attendee_id:
                    return registration
            return None
        except Exception as e:
            print(f"Error retrieving attendee: {e}")
            return None

    def list_attendees(self, rsvp_status: Optional[str] = None) -> List[Dict[str, str]]:
        """List all attendees, optionally filtered by RSVP status."""
        try:
            if rsvp_status:
                return [reg for reg in self.registrations if reg["rsvp_status"] == rsvp_status]
            return self.registrations.copy()
        except Exception as e:
            print(f"Error listing attendees: {e}")
            return []

    def get_social_event_attendees(self) -> List[Dict[str, str]]:
        """List all attendees who opted for the social event."""
        try:
            return [reg for reg in self.registrations if reg["social_event"].lower() == "yes"]
        except Exception as e:
            print(f"Error retrieving social event attendees: {e}")
            return []

    def count_attendees(self) -> Dict[str, int]:
        """Count attendees by RSVP status."""
        try:
            counts = {"Total": len(self.registrations)}
            statuses = set(reg["rsvp_status"] for reg in self.registrations)
            
            for status in statuses:
                counts[status] = sum(1 for reg in self.registrations if reg["rsvp_status"] == status)
            
            return counts
        except Exception as e:
            print(f"Error counting attendees: {e}")
            return {"Total": 0}

# Example usage
if __name__ == "__main__":
    manager = EventRegistrationManager()
    
    # Register a new attendee
    attendee_id = manager.register_attendee(
        name="Juan Perez",
        email="juan@example.com",
        company="Tech Corp",
        position="Developer",
        event_date="2023-12-15",
        social_event="Yes"
    )
    
    # Update RSVP status
    manager.update_rsvp(attendee_id, "Confirmed")
    
    # Get attendee details
    attendee = manager.get_attendee(attendee_id)
    print(f"Attendee details: {attendee}")
    
    # List all confirmed attendees
    confirmed = manager.list_attendees(rsvp_status="Confirmed")
    print(f"Confirmed attendees: {len(confirmed)}")
    
    # Count attendees by status
    counts = manager.count_attendees()
    print(f"Attendee counts: {counts}")
    
    # List social event attendees
    social_attendees = manager.get_social_event_attendees()
    print(f"Social event attendees: {len(social_attendees)}")
```
