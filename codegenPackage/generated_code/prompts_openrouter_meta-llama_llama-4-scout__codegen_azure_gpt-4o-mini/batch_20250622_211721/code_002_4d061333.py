"""
Generated Code Metadata:
========================
Original URL: https://smart-medicalservices.com
Prompt: Generate a code snippet to implement a simple appointment scheduling system for a medical services provider, inspired by the services offered by Smart Medical Services.
Generated: DETERMINISTIC_4d061333efb15694
Batch ID: 20250622_211721
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
    """Class representing a medical appointment."""
    
    def __init__(self, patient_name: str, appointment_time: datetime):
        self.patient_name = patient_name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(patient_name='{self.patient_name}', appointment_time='{self.appointment_time}')"


class AppointmentScheduler:
    """Class to manage appointment scheduling for a medical services provider."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, appointment_time: datetime) -> None:
        """Schedules a new appointment if the time slot is available.

        Args:
            patient_name (str): The name of the patient.
            appointment_time (datetime): The time of the appointment.

        Raises:
            ValueError: If the appointment time is in the past or already booked.
        """
        if appointment_time < datetime.now():
            raise ValueError("Cannot schedule an appointment in the past.")
        
        if self.is_time_slot_booked(appointment_time):
            raise ValueError("The selected time slot is already booked.")

        new_appointment = Appointment(patient_name, appointment_time)
        self.appointments.append(new_appointment)
        print(f"Appointment scheduled: {new_appointment}")

    def is_time_slot_booked(self, appointment_time: datetime) -> bool:
        """Checks if the given time slot is already booked.

        Args:
            appointment_time (datetime): The time to check.

        Returns:
            bool: True if the time slot is booked, False otherwise.
        """
        return any(appointment.appointment_time == appointment_time for appointment in self.appointments)

    def get_appointments(self) -> List[Appointment]:
        """Returns a list of all scheduled appointments.

        Returns:
            List[Appointment]: A list of appointments.
        """
        return self.appointments

    def cancel_appointment(self, patient_name: str, appointment_time: datetime) -> None:
        """Cancels an existing appointment.

        Args:
            patient_name (str): The name of the patient.
            appointment_time (datetime): The time of the appointment to cancel.

        Raises:
            ValueError: If the appointment does not exist.
        """
        for appointment in self.appointments:
            if appointment.patient_name == patient_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                print(f"Appointment canceled: {appointment}")
                return
        
        raise ValueError("Appointment not found.")


# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()
    
    # Schedule appointments
    try:
        scheduler.schedule_appointment("John Doe", datetime.now() + timedelta(days=1, hours=9))
        scheduler.schedule_appointment("Jane Smith", datetime.now() + timedelta(days=1, hours=10))
    except ValueError as e:
        print(f"Error scheduling appointment: {e}")

    # List all appointments
    print("Scheduled Appointments:", scheduler.get_appointments())

    # Cancel an appointment
    try:
        scheduler.cancel_appointment("John Doe", datetime.now() + timedelta(days=1, hours=9))
    except ValueError as e:
        print(f"Error canceling appointment: {e}")

    # List all appointments after cancellation
    print("Scheduled Appointments after cancellation:", scheduler.get_appointments())
```
