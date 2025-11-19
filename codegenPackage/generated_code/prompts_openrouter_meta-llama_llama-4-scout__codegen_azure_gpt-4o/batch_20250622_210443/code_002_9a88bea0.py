"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: "Generate a code for scheduling water tests and consultations for residential areas."
Generated: DETERMINISTIC_9a88bea0d78d6d5d
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Appointment:
    """
    Represents an appointment for water testing or consultation.
    """
    def __init__(self, appointment_type: str, date: datetime.date, time: datetime.time, location: str):
        self.appointment_type = appointment_type  # Type of appointment: 'Water Test' or 'Consultation'
        self.date = date  # Date of the appointment
        self.time = time  # Time of the appointment
        self.location = location  # Location of the appointment

    def __str__(self):
        return f"{self.appointment_type} on {self.date} at {self.time} in {self.location}"


class Scheduler:
    """
    Scheduler for managing water tests and consultations.
    """
    def __init__(self):
        self.appointments: List[Appointment] = []  # List to store all scheduled appointments

    def schedule_appointment(self, appointment_type: str, date: str, time: str, location: str) -> Optional[str]:
        """
        Schedules a new appointment.
        
        :param appointment_type: Type of appointment ('Water Test' or 'Consultation')
        :param date: Date of the appointment in 'YYYY-MM-DD' format
        :param time: Time of the appointment in 'HH:MM' format
        :param location: Location of the appointment
        :return: Success message or error message
        """
        try:
            # Validate and parse date and time
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            appointment_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Create and add the appointment
            new_appointment = Appointment(appointment_type, appointment_date, appointment_time, location)
            self.appointments.append(new_appointment)
            return f"Appointment successfully scheduled: {new_appointment}"
        except ValueError as e:
            # Handle invalid date/time format
            return f"Error scheduling appointment: {e}"

    def view_appointments(self) -> List[str]:
        """
        Returns a list of all scheduled appointments.
        
        :return: List of appointment details
        """
        if not self.appointments:
            return ["No appointments scheduled."]
        return [str(appointment) for appointment in self.appointments]

    def cancel_appointment(self, appointment_type: str, date: str, time: str, location: str) -> Optional[str]:
        """
        Cancels an existing appointment.
        
        :param appointment_type: Type of appointment ('Water Test' or 'Consultation')
        :param date: Date of the appointment in 'YYYY-MM-DD' format
        :param time: Time of the appointment in 'HH:MM' format
        :param location: Location of the appointment
        :return: Success message or error message
        """
        try:
            # Validate and parse date and time
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            appointment_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Find and remove the appointment
            for appointment in self.appointments:
                if (appointment.appointment_type == appointment_type and
                        appointment.date == appointment_date and
                        appointment.time == appointment_time and
                        appointment.location == location):
                    self.appointments.remove(appointment)
                    return f"Appointment successfully canceled: {appointment}"
            return "Error: Appointment not found."
        except ValueError as e:
            # Handle invalid date/time format
            return f"Error canceling appointment: {e}"


# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()

    # Schedule appointments
    print(scheduler.schedule_appointment("Water Test", "2023-10-15", "10:00", "123 Main St"))
    print(scheduler.schedule_appointment("Consultation", "2023-10-16", "14:00", "456 Elm St"))

    # View appointments
    print("\nScheduled Appointments:")
    for appointment in scheduler.view_appointments():
        print(appointment)

    # Cancel an appointment
    print("\nCanceling Appointment:")
    print(scheduler.cancel_appointment("Water Test", "2023-10-15", "10:00", "123 Main St"))

    # View appointments after cancellation
    print("\nScheduled Appointments After Cancellation:")
    for appointment in scheduler.view_appointments():
        print(appointment)
```
