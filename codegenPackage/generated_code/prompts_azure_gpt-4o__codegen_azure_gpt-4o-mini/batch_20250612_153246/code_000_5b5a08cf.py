"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Write Python code to create a booking system for holistic therapies like cupping, fertility massage, and acupuncture, including features for flexible scheduling and client management.
Generated: DETERMINISTIC_5b5a08cf188bc655
Batch ID: 20250612_153246
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

class Client:
    """Class to represent a client in the booking system."""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Client(name={self.name}, email={self.email})"


class Therapy:
    """Class to represent a type of therapy available for booking."""
    
    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration  # Duration in minutes

    def __repr__(self):
        return f"Therapy(name={self.name}, duration={self.duration})"


class Appointment:
    """Class to represent a therapy appointment."""
    
    def __init__(self, client: Client, therapy: Therapy, date_time: datetime.datetime):
        self.client = client
        self.therapy = therapy
        self.date_time = date_time

    def __repr__(self):
        return f"Appointment(client={self.client}, therapy={self.therapy}, date_time={self.date_time})"


class BookingSystem:
    """Class to manage the booking system for therapies."""
    
    def __init__(self):
        self.clients: List[Client] = []
        self.therapies: List[Therapy] = []
        self.appointments: List[Appointment] = []

    def add_client(self, name: str, email: str) -> Client:
        """Add a new client to the system."""
        client = Client(name, email)
        self.clients.append(client)
        return client

    def add_therapy(self, name: str, duration: int) -> Therapy:
        """Add a new therapy to the system."""
        therapy = Therapy(name, duration)
        self.therapies.append(therapy)
        return therapy

    def book_appointment(self, client: Client, therapy: Therapy, date_time: datetime.datetime) -> Optional[Appointment]:
        """Book an appointment for a client."""
        if self.is_time_slot_available(date_time, therapy.duration):
            appointment = Appointment(client, therapy, date_time)
            self.appointments.append(appointment)
            return appointment
        else:
            print(f"Error: The time slot on {date_time} is not available.")
            return None

    def is_time_slot_available(self, date_time: datetime.datetime, duration: int) -> bool:
        """Check if the requested time slot is available."""
        end_time = date_time + datetime.timedelta(minutes=duration)
        for appointment in self.appointments:
            if (appointment.date_time < end_time) and (date_time < appointment.date_time + datetime.timedelta(minutes=appointment.therapy.duration)):
                return False
        return True

    def list_appointments(self) -> List[Appointment]:
        """List all appointments."""
        return self.appointments

    def find_client_appointments(self, client: Client) -> List[Appointment]:
        """Find all appointments for a specific client."""
        return [appt for appt in self.appointments if appt.client == client]


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Adding clients
    client1 = booking_system.add_client("Alice Smith", "alice@example.com")
    client2 = booking_system.add_client("Bob Johnson", "bob@example.com")

    # Adding therapies
    cupping = booking_system.add_therapy("Cupping", 60)
    fertility_massage = booking_system.add_therapy("Fertility Massage", 90)
    acupuncture = booking_system.add_therapy("Acupuncture", 45)

    # Booking appointments
    appointment1 = booking_system.book_appointment(client1, cupping, datetime.datetime(2023, 10, 15, 10, 0))
    appointment2 = booking_system.book_appointment(client2, acupuncture, datetime.datetime(2023, 10, 15, 11, 0))
    appointment3 = booking_system.book_appointment(client1, fertility_massage, datetime.datetime(2023, 10, 15, 10, 30))  # This should fail

    # Listing all appointments
    print("All Appointments:")
    for appt in booking_system.list_appointments():
        print(appt)

    # Finding appointments for a specific client
    print("\nAlice's Appointments:")
    for appt in booking_system.find_client_appointments(client1):
        print(appt)
```
