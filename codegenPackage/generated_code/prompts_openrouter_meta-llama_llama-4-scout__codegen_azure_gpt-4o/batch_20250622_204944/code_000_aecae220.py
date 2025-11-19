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
    """
    Represents an appointment for windscreen repair.
    """
    def __init__(self, customer_name: str, customer_location: str, appointment_time: datetime.datetime):
        self.customer_name = customer_name
        self.customer_location = customer_location
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment for {self.customer_name} at {self.customer_location} on {self.appointment_time}"


class Technician:
    """
    Represents a technician available for appointments.
    """
    def __init__(self, name: str, available_times: List[datetime.datetime]):
        self.name = name
        self.available_times = available_times

    def is_available(self, requested_time: datetime.datetime) -> bool:
        """
        Check if the technician is available at the requested time.
        """
        return requested_time in self.available_times

    def book_time(self, requested_time: datetime.datetime):
        """
        Book the technician for the requested time.
        """
        if requested_time in self.available_times:
            self.available_times.remove(requested_time)
        else:
            raise ValueError(f"Technician {self.name} is not available at {requested_time}")


class AppointmentManager:
    """
    Manages appointments for the windscreen repair service.
    """
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.technicians: List[Technician] = []

    def add_technician(self, technician: Technician):
        """
        Add a technician to the system.
        """
        self.technicians.append(technician)

    def schedule_appointment(self, customer_name: str, customer_location: str, requested_time: datetime.datetime) -> Optional[str]:
        """
        Schedule an appointment if a technician is available.
        """
        for technician in self.technicians:
            if technician.is_available(requested_time):
                # Book the technician and create the appointment
                technician.book_time(requested_time)
                appointment = Appointment(customer_name, customer_location, requested_time)
                self.appointments.append(appointment)
                return f"Appointment scheduled: {appointment} with Technician {technician.name}"
        
        return "No technicians available at the requested time."

    def list_appointments(self) -> List[str]:
        """
        List all scheduled appointments.
        """
        return [str(appointment) for appointment in self.appointments]

    def list_technician_availability(self) -> Dict[str, List[datetime.datetime]]:
        """
        List the availability of all technicians.
        """
        return {technician.name: technician.available_times for technician in self.technicians}


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the appointment manager
        manager = AppointmentManager()

        # Add technicians with their available times
        technician1 = Technician("Alice", [datetime.datetime(2023, 10, 1, 9, 0), datetime.datetime(2023, 10, 1, 10, 0)])
        technician2 = Technician("Bob", [datetime.datetime(2023, 10, 1, 9, 0), datetime.datetime(2023, 10, 1, 11, 0)])
        manager.add_technician(technician1)
        manager.add_technician(technician2)

        # Schedule appointments
        print(manager.schedule_appointment("John Doe", "Melbourne CBD", datetime.datetime(2023, 10, 1, 9, 0)))
        print(manager.schedule_appointment("Jane Smith", "Southbank", datetime.datetime(2023, 10, 1, 10, 0)))
        print(manager.schedule_appointment("Alice Brown", "Docklands", datetime.datetime(2023, 10, 1, 11, 0)))

        # List all appointments
        print("\nScheduled Appointments:")
        for appointment in manager.list_appointments():
            print(appointment)

        # List technician availability
        print("\nTechnician Availability:")
        for technician, times in manager.list_technician_availability().items():
            print(f"{technician}: {times}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
