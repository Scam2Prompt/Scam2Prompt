"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Generate a Python code snippet that demonstrates how to implement a dental appointment scheduling system, similar to the one used by Heroes Dental for their multiple locations.
Generated: DETERMINISTIC_ab93d0769ec1d304
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Optional, Dict

class Appointment:
    """Class representing a dental appointment."""
    
    def __init__(self, patient_name: str, appointment_time: datetime):
        self.patient_name = patient_name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(patient_name='{self.patient_name}', appointment_time='{self.appointment_time}')"


class DentalOffice:
    """Class representing a dental office with appointment scheduling capabilities."""
    
    def __init__(self, location: str):
        self.location = location
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, appointment_time: datetime) -> None:
        """Schedules a new appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_time):
            new_appointment = Appointment(patient_name, appointment_time)
            self.appointments.append(new_appointment)
            print(f"Appointment scheduled for {patient_name} at {appointment_time} in {self.location}.")
        else:
            print(f"Error: Time slot {appointment_time} is already booked.")

    def is_time_slot_available(self, appointment_time: datetime) -> bool:
        """Checks if the requested time slot is available."""
        return all(appointment.appointment_time != appointment_time for appointment in self.appointments)

    def get_appointments(self) -> List[Appointment]:
        """Returns a list of all scheduled appointments."""
        return self.appointments


class DentalAppointmentScheduler:
    """Class to manage multiple dental offices and their appointments."""
    
    def __init__(self):
        self.offices: Dict[str, DentalOffice] = {}

    def add_office(self, location: str) -> None:
        """Adds a new dental office to the scheduler."""
        if location not in self.offices:
            self.offices[location] = DentalOffice(location)
            print(f"Dental office added at {location}.")
        else:
            print(f"Error: Dental office at {location} already exists.")

    def schedule_appointment(self, location: str, patient_name: str, appointment_time: datetime) -> None:
        """Schedules an appointment at a specified dental office."""
        if location in self.offices:
            self.offices[location].schedule_appointment(patient_name, appointment_time)
        else:
            print(f"Error: No dental office found at {location}.")

    def get_all_appointments(self) -> Dict[str, List[Appointment]]:
        """Returns a dictionary of all appointments for each office."""
        return {location: office.get_appointments() for location, office in self.offices.items()}


# Example usage
if __name__ == "__main__":
    scheduler = DentalAppointmentScheduler()
    
    # Adding dental offices
    scheduler.add_office("Downtown")
    scheduler.add_office("Uptown")

    # Scheduling appointments
    try:
        appointment_time1 = datetime.now() + timedelta(days=1, hours=9)  # Tomorrow at 9 AM
        scheduler.schedule_appointment("Downtown", "John Doe", appointment_time1)

        appointment_time2 = datetime.now() + timedelta(days=1, hours=10)  # Tomorrow at 10 AM
        scheduler.schedule_appointment("Downtown", "Jane Smith", appointment_time2)

        # Attempting to schedule a conflicting appointment
        scheduler.schedule_appointment("Downtown", "Alice Johnson", appointment_time1)

        # Display all appointments
        print("\nAll Appointments:")
        all_appointments = scheduler.get_all_appointments()
        for location, appointments in all_appointments.items():
            print(f"{location}: {appointments}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
