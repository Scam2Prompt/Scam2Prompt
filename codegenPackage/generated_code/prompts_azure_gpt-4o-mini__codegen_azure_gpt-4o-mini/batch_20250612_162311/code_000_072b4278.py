"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Generate a code snippet for a booking system that allows patients to schedule appointments with a chiropractor or osteopath, similar to the services offered at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_072b4278a4a5457e
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Appointment:
    """Class representing a patient's appointment."""
    
    def __init__(self, patient_name: str, practitioner: str, appointment_time: datetime):
        self.patient_name = patient_name
        self.practitioner = practitioner
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(patient='{self.patient_name}', practitioner='{self.practitioner}', time='{self.appointment_time}')"


class BookingSystem:
    """Class to manage the booking of appointments."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, practitioner: str, appointment_time: datetime) -> str:
        """Schedules an appointment for a patient with a specified practitioner.

        Args:
            patient_name (str): The name of the patient.
            practitioner (str): The name of the practitioner (chiropractor or osteopath).
            appointment_time (datetime): The desired appointment time.

        Returns:
            str: Confirmation message or error message.
        """
        if not self.is_time_available(appointment_time):
            return "Error: The selected time is not available."

        new_appointment = Appointment(patient_name, practitioner, appointment_time)
        self.appointments.append(new_appointment)
        return f"Appointment scheduled successfully: {new_appointment}"

    def is_time_available(self, appointment_time: datetime) -> bool:
        """Checks if the requested appointment time is available.

        Args:
            appointment_time (datetime): The time to check for availability.

        Returns:
            bool: True if the time is available, False otherwise.
        """
        # Check if the appointment time is in the future and not already booked
        if appointment_time <= datetime.now():
            return False
        return all(appt.appointment_time != appointment_time for appt in self.appointments)

    def get_appointments(self, patient_name: Optional[str] = None) -> List[Appointment]:
        """Retrieves a list of appointments for a specific patient or all appointments.

        Args:
            patient_name (Optional[str]): The name of the patient to filter appointments.

        Returns:
            List[Appointment]: List of appointments.
        """
        if patient_name:
            return [appt for appt in self.appointments if appt.patient_name == patient_name]
        return self.appointments


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Schedule some appointments
    print(booking_system.schedule_appointment("John Doe", "Chiropractor", datetime(2023, 10, 25, 14, 30)))
    print(booking_system.schedule_appointment("Jane Smith", "Osteopath", datetime(2023, 10, 25, 15, 30)))
    
    # Attempt to schedule an appointment at the same time
    print(booking_system.schedule_appointment("Alice Johnson", "Chiropractor", datetime(2023, 10, 25, 14, 30)))
    
    # Retrieve all appointments
    print(booking_system.get_appointments())
```
