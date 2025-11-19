"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a Python script to manage appointments for a mobile windscreen repair service in Melbourne, considering factors like customer location and technician availability.
Generated: DETERMINISTIC_aecae2205a047dfe
Batch ID: 20250622_204944
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

class Appointment:
    """Class to represent an appointment for windscreen repair."""
    
    def __init__(self, customer_name: str, location: str, appointment_time: datetime.datetime):
        self.customer_name = customer_name
        self.location = location
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(customer_name={self.customer_name}, location={self.location}, appointment_time={self.appointment_time})"


class Technician:
    """Class to represent a technician."""
    
    def __init__(self, name: str):
        self.name = name
        self.availability: List[datetime.datetime] = []

    def add_availability(self, time: datetime.datetime):
        """Add an available time slot for the technician."""
        self.availability.append(time)

    def is_available(self, time: datetime.datetime) -> bool:
        """Check if the technician is available at the given time."""
        return time in self.availability


class AppointmentManager:
    """Class to manage appointments for the windscreen repair service."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.technicians: Dict[str, Technician] = {}

    def add_technician(self, technician: Technician):
        """Add a technician to the manager."""
        self.technicians[technician.name] = technician

    def schedule_appointment(self, customer_name: str, location: str, appointment_time: datetime.datetime, technician_name: str) -> Optional[Appointment]:
        """Schedule an appointment if the technician is available."""
        technician = self.technicians.get(technician_name)
        
        if technician is None:
            raise ValueError(f"Technician {technician_name} not found.")
        
        if not technician.is_available(appointment_time):
            raise ValueError(f"Technician {technician_name} is not available at {appointment_time}.")
        
        appointment = Appointment(customer_name, location, appointment_time)
        self.appointments.append(appointment)
        return appointment

    def get_appointments(self) -> List[Appointment]:
        """Return a list of all scheduled appointments."""
        return self.appointments


# Example usage
if __name__ == "__main__":
    # Create an instance of AppointmentManager
    manager = AppointmentManager()

    # Create technicians and add their availability
    tech1 = Technician("John Doe")
    tech1.add_availability(datetime.datetime(2023, 10, 15, 9, 0))
    tech1.add_availability(datetime.datetime(2023, 10, 15, 10, 0))
    
    tech2 = Technician("Jane Smith")
    tech2.add_availability(datetime.datetime(2023, 10, 15, 11, 0))
    tech2.add_availability(datetime.datetime(2023, 10, 15, 12, 0))

    # Add technicians to the manager
    manager.add_technician(tech1)
    manager.add_technician(tech2)

    # Schedule appointments
    try:
        appointment1 = manager.schedule_appointment("Alice Johnson", "123 Main St, Melbourne", datetime.datetime(2023, 10, 15, 9, 0), "John Doe")
        print(f"Scheduled: {appointment1}")
        
        appointment2 = manager.schedule_appointment("Bob Brown", "456 Elm St, Melbourne", datetime.datetime(2023, 10, 15, 11, 0), "Jane Smith")
        print(f"Scheduled: {appointment2}")

        # Attempt to schedule an appointment with an unavailable technician
        appointment3 = manager.schedule_appointment("Charlie Green", "789 Oak St, Melbourne", datetime.datetime(2023, 10, 15, 9, 0), "Jane Smith")
    except ValueError as e:
        print(f"Error scheduling appointment: {e}")

    # List all appointments
    print("All scheduled appointments:")
    for appointment in manager.get_appointments():
        print(appointment)
```
