"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Develop a scheduling system in Python that allows for appointment confirmations and changes, similar to ProSync's appointment scheduling feature.
Generated: DETERMINISTIC_72f99b754a873b1a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Appointment:
    """
    Class representing an appointment in the scheduling system.
    """
    def __init__(self, appointment_id: int, client_name: str, appointment_time: datetime.datetime):
        self.appointment_id = appointment_id
        self.client_name = client_name
        self.appointment_time = appointment_time
        self.confirmed = False

    def confirm(self):
        """Confirms the appointment."""
        self.confirmed = True

    def reschedule(self, new_time: datetime.datetime):
        """Reschedules the appointment to a new time."""
        self.appointment_time = new_time

class AppointmentScheduler:
    """
    Class to manage appointments and scheduling.
    """
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.next_id = 1

    def _find_appointment(self, appointment_id: int) -> Optional[Appointment]:
        """Private method to find an appointment by ID."""
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        return None

    def schedule_appointment(self, client_name: str, appointment_time: datetime.datetime) -> int:
        """
        Schedule a new appointment.

        Args:
            client_name (str): Name of the client.
            appointment_time (datetime): Time of the appointment.

        Returns:
            int: The appointment ID of the newly created appointment.
        """
        if appointment_time < datetime.datetime.now():
            raise ValueError("Appointment time must be in the future.")
        
        appointment = Appointment(self.next_id, client_name, appointment_time)
        self.appointments.append(appointment)
        self.next_id += 1
        return appointment.appointment_id

    def confirm_appointment(self, appointment_id: int):
        """
        Confirm an existing appointment.

        Args:
            appointment_id (int): The ID of the appointment to confirm.
        """
        appointment = self._find_appointment(appointment_id)
        if appointment is None:
            raise ValueError("Appointment not found.")
        appointment.confirm()

    def reschedule_appointment(self, appointment_id: int, new_time: datetime.datetime):
        """
        Reschedule an existing appointment.

        Args:
            appointment_id (int): The ID of the appointment to reschedule.
            new_time (datetime): The new time for the appointment.
        """
        if new_time < datetime.datetime.now():
            raise ValueError("New appointment time must be in the future.")

        appointment = self._find_appointment(appointment_id)
        if appointment is None:
            raise ValueError("Appointment not found.")
        appointment.reschedule(new_time)

    def get_appointments(self) -> List[Appointment]:
        """Return a list of all scheduled appointments."""
        return self.appointments

# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    try:
        # Schedule a new appointment
        appointment_id = scheduler.schedule_appointment("John Doe", datetime.datetime(2023, 10, 25, 15, 30))
        print(f"Scheduled appointment ID: {appointment_id}")

        # Confirm the appointment
        scheduler.confirm_appointment(appointment_id)
        print(f"Appointment {appointment_id} confirmed.")

        # Reschedule the appointment
        new_time = datetime.datetime(2023, 10, 26, 15, 30)
        scheduler.reschedule_appointment(appointment_id, new_time)
        print(f"Appointment {appointment_id} rescheduled to {new_time}.")

        # List all appointments
        for appointment in scheduler.get_appointments():
            status = "Confirmed" if appointment.confirmed else "Not Confirmed"
            print(f"Appointment ID: {appointment.appointment_id}, Client: {appointment.client_name}, "
                  f"Time: {appointment.appointment_time}, Status: {status}")

    except Exception as e:
        print(f"Error: {e}")
```
