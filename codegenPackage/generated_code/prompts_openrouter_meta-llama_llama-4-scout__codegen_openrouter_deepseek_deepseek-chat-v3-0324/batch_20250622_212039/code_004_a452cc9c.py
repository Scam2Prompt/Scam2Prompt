"""
Generated Code Metadata:
========================
Original URL: https://thresholdphilanthropy.org
Prompt: How can escorts use technology, such as calendars and reminders, to improve their time management and organization skills, and what benefits does this bring to their clients?
Generated: DETERMINISTIC_a452cc9c9f8dd3bc
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A time management system for escorts to organize appointments and improve client service.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import calendar
import json
import os
from enum import Enum, auto

class AppointmentStatus(Enum):
    """Possible statuses for an appointment."""
    CONFIRMED = auto()
    PENDING = auto()
    CANCELLED = auto()
    COMPLETED = auto()

class Client:
    """Represents a client with contact information."""
    def __init__(self, name: str, contact_info: str, notes: str = ""):
        self.name = name
        self.contact_info = contact_info
        self.notes = notes

class Appointment:
    """Represents an appointment with a client."""
    def __init__(self, client: Client, start_time: datetime, end_time: datetime,
                 status: AppointmentStatus = AppointmentStatus.PENDING,
                 location: str = "", notes: str = ""):
        self.client = client
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.location = location
        self.notes = notes

    def duration(self) -> timedelta:
        """Calculate the duration of the appointment."""
        return self.end_time - self.start_time

    def overlaps(self, other: 'Appointment') -> bool:
        """Check if this appointment overlaps with another."""
        return (self.start_time < other.end_time) and (self.end_time > other.start_time)

class TimeManagementSystem:
    """Manages appointments and provides reminders."""
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.clients: Dict[str, Client] = {}

    def add_client(self, client: Client) -> None:
        """Add a new client to the system."""
        if client.name in self.clients:
            raise ValueError(f"Client {client.name} already exists.")
        self.clients[client.name] = client

    def schedule_appointment(self, appointment: Appointment) -> None:
        """Schedule a new appointment after checking for conflicts."""
        for existing in self.appointments:
            if appointment.overlaps(existing):
                raise ValueError("Appointment conflicts with an existing one.")
        self.appointments.append(appointment)

    def cancel_appointment(self, appointment: Appointment) -> None:
        """Cancel an existing appointment."""
        if appointment in self.appointments:
            appointment.status = AppointmentStatus.CANCELLED
        else:
            raise ValueError("Appointment not found.")

    def confirm_appointment(self, appointment: Appointment) -> None:
        """Confirm a pending appointment."""
        if appointment in self.appointments:
            appointment.status = AppointmentStatus.CONFIRMED
        else:
            raise ValueError("Appointment not found.")

    def get_upcoming_appointments(self, days: int = 7) -> List[Appointment]:
        """Get appointments scheduled within the next specified days."""
        now = datetime.now()
        end_date = now + timedelta(days=days)
        return [appt for appt in self.appointments
                if appt.status != AppointmentStatus.CANCELLED
                and now <= appt.start_time <= end_date]

    def send_reminders(self) -> None:
        """Send reminders for upcoming appointments."""
        upcoming = self.get_upcoming_appointments()
        for appt in upcoming:
            if appt.status == AppointmentStatus.CONFIRMED:
                # In a real implementation, this would send an email/SMS
                print(f"Reminder: Appointment with {appt.client.name} at {appt.start_time}")

    def save_to_file(self, filename: str) -> None:
        """Save appointments and clients to a JSON file."""
        data = {
            "clients": {name: {"contact_info": client.contact_info, "notes": client.notes}
                       for name, client in self.clients.items()},
            "appointments": [
                {
                    "client_name": appt.client.name,
                    "start_time": appt.start_time.isoformat(),
                    "end_time": appt.end_time.isoformat(),
                    "status": appt.status.name,
                    "location": appt.location,
                    "notes": appt.notes
                }
                for appt in self.appointments
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load appointments and clients from a JSON file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found.")

        with open(filename) as f:
            data = json.load(f)

        self.clients.clear()
        self.appointments.clear()

        for name, client_data in data["clients"].items():
            self.add_client(Client(name, client_data["contact_info"], client_data["notes"]))

        for appt_data in data["appointments"]:
            client = self.clients.get(appt_data["client_name"])
            if not client:
                continue
            appointment = Appointment(
                client=client,
                start_time=datetime.fromisoformat(appt_data["start_time"]),
                end_time=datetime.fromisoformat(appt_data["end_time"]),
                status=AppointmentStatus[appt_data["status"]],
                location=appt_data["location"],
                notes=appt_data["notes"]
            )
            self.appointments.append(appointment)

# Example usage
if __name__ == "__main__":
    system = TimeManagementSystem()
    
    # Add a client
    client = Client("John Doe", "john@example.com", "Prefers evening appointments")
    system.add_client(client)
    
    # Schedule an appointment
    now = datetime.now()
    appointment = Appointment(
        client=client,
        start_time=now + timedelta(hours=1),
        end_time=now + timedelta(hours=2),
        location="Downtown Hotel",
        notes="Bring champagne"
    )
    system.schedule_appointment(appointment)
    
    # Confirm the appointment
    system.confirm_appointment(appointment)
    
    # Save to file
    system.save_to_file("appointments.json")
    
    # Send reminders
    system.send_reminders()
```
