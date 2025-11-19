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
import datetime
from typing import List, Dict, Optional


class Appointment:
    """
    Represents a dental appointment.
    """
    def __init__(self, patient_name: str, date: datetime.date, time: datetime.time, location: str):
        self.patient_name = patient_name
        self.date = date
        self.time = time
        self.location = location

    def __str__(self):
        return f"Appointment for {self.patient_name} on {self.date} at {self.time} in {self.location}"


class DentalOffice:
    """
    Represents a dental office location.
    """
    def __init__(self, location_name: str):
        self.location_name = location_name
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, date: datetime.date, time: datetime.time) -> Optional[str]:
        """
        Schedules an appointment if the time slot is available.
        """
        # Check for conflicts
        for appointment in self.appointments:
            if appointment.date == date and appointment.time == time:
                return f"Time slot {time} on {date} is already booked."

        # Add the appointment
        new_appointment = Appointment(patient_name, date, time, self.location_name)
        self.appointments.append(new_appointment)
        return f"Appointment successfully scheduled: {new_appointment}"

    def list_appointments(self) -> List[str]:
        """
        Lists all appointments for the location.
        """
        if not self.appointments:
            return ["No appointments scheduled."]
        return [str(appointment) for appointment in self.appointments]


class DentalAppointmentSystem:
    """
    Manages dental appointments across multiple locations.
    """
    def __init__(self):
        self.locations: Dict[str, DentalOffice] = {}

    def add_location(self, location_name: str):
        """
        Adds a new dental office location.
        """
        if location_name in self.locations:
            raise ValueError(f"Location '{location_name}' already exists.")
        self.locations[location_name] = DentalOffice(location_name)

    def schedule_appointment(self, location_name: str, patient_name: str, date: datetime.date, time: datetime.time) -> str:
        """
        Schedules an appointment at a specific location.
        """
        if location_name not in self.locations:
            return f"Location '{location_name}' does not exist."
        return self.locations[location_name].schedule_appointment(patient_name, date, time)

    def list_appointments(self, location_name: str) -> List[str]:
        """
        Lists all appointments for a specific location.
        """
        if location_name not in self.locations:
            return [f"Location '{location_name}' does not exist."]
        return self.locations[location_name].list_appointments()


# Example usage
if __name__ == "__main__":
    system = DentalAppointmentSystem()

    # Add locations
    system.add_location("Downtown Clinic")
    system.add_location("Uptown Clinic")

    # Schedule appointments
    print(system.schedule_appointment("Downtown Clinic", "John Doe", datetime.date(2023, 11, 15), datetime.time(10, 0)))
    print(system.schedule_appointment("Downtown Clinic", "Jane Smith", datetime.date(2023, 11, 15), datetime.time(10, 0)))  # Conflict
    print(system.schedule_appointment("Uptown Clinic", "Alice Brown", datetime.date(2023, 11, 16), datetime.time(14, 30)))

    # List appointments
    print("\nDowntown Clinic Appointments:")
    print("\n".join(system.list_appointments("Downtown Clinic")))

    print("\nUptown Clinic Appointments:")
    print("\n".join(system.list_appointments("Uptown Clinic")))
```
