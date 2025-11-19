"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://japkasai.net
Prompt: Generate a code snippet for a booking system that allows clients to schedule appointments at a men's grooming salon, incorporating features like service selection and time slots based on the hours of operation (10:00 to 23:00).
Generated: DETERMINISTIC_f757960d2a1d6965
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Service:
    """Represents a grooming service offered by the salon."""
    
    def __init__(self, name: str, duration: int, price: float):
        self.name = name             # Name of the service
        self.duration = duration     # Duration of the service in minutes
        self.price = price           # Price of the service

class Appointment:
    """Represents a scheduled appointment."""
    
    def __init__(self, service: Service, start_time: datetime):
        self.service = service                             # Service for the appointment
        self.start_time = start_time                       # Start time of the appointment
        self.end_time = start_time + timedelta(minutes=service.duration)  # End time of the appointment

class BookingSystem:
    """Handles scheduling of appointments for the salon."""
    
    def __init__(self):
        self.services: List[Service] = []
        self.appointments: List[Appointment] = []
        self.opening_hour = 10  # Salon opens at 10:00 AM
        self.closing_hour = 23  # Salon closes at 11:00 PM

    def add_service(self, name: str, duration: int, price: float):
        """Adds a new service to the salon menu."""
        service = Service(name, duration, price)
        self.services.append(service)

    def get_available_slots(self, date: datetime) -> List[datetime]:
        """Returns available time slots for the given date."""
        available_slots = []
        for hour in range(self.opening_hour, self.closing_hour):
            for minute in [0, 30]:  # Check half-hour increments
                slot_time = datetime(date.year, date.month, date.day, hour, minute)
                if self.is_slot_available(slot_time):
                    available_slots.append(slot_time)
        return available_slots

    def is_slot_available(self, slot_time: datetime) -> bool:
        """Checks if the given time slot is available for booking."""
        for appointment in self.appointments:
            if appointment.start_time <= slot_time < appointment.end_time:
                return False
        return True

    def book_appointment(self, service_name: str, slot_time: datetime) -> Optional[Appointment]:
        """Books an appointment if the service exists and the time slot is available."""
        service = next((s for s in self.services if s.name == service_name), None)
        if not service:
            raise ValueError(f"Service '{service_name}' not found.")
        if not self.is_slot_available(slot_time):
            raise ValueError(f"Time slot {slot_time.strftime('%Y-%m-%d %H:%M')} is not available.")
        
        appointment = Appointment(service, slot_time)
        self.appointments.append(appointment)
        return appointment

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    booking_system.add_service("Haircut", 30, 25.0)
    booking_system.add_service("Shave", 15, 15.0)
    
    # Schedule an appointment for a haircut on a specified date
    try:
        appointment_date = datetime(2023, 10, 15)  # Example date
        available_slots = booking_system.get_available_slots(appointment_date)
        if available_slots:
            appointment = booking_system.book_appointment("Haircut", available_slots[0])
            print(f"Appointment booked for {appointment.service.name} at {appointment.start_time.strftime('%Y-%m-%d %H:%M')}.")
        else:
            print("No available slots for the selected date.")
    except ValueError as e:
        print(f"Error: {e}")
```
