"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Create a Python program to schedule and manage consultations for immigration law services, including support for Skype, phone, and in-person appointments.
Generated: DETERMINISTIC_042f32ce49be3dcf
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict


class Appointment:
    """
    Class representing an appointment for immigration law services.
    Supports Skype, phone, and in-person consultations.
    """
    def __init__(self, appointment_type: str, date: str, time: str, client_name: str):
        """
        Initialize an Appointment instance.

        :param appointment_type: Type of consultation - 'Skype', 'Phone', or 'In-Person'.
        :param date: Date of the appointment in YYYY-MM-DD format.
        :param time: Time of the appointment in HH:MM format.
        :param client_name: Name of the client.
        """
        if appointment_type not in ['Skype', 'Phone', 'In-Person']:
            raise ValueError("Invalid appointment type. Choose 'Skype', 'Phone', or 'In-Person'.")
        
        try:
            self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self.time = datetime.datetime.strptime(time, '%H:%M').time()
        except ValueError:
            raise ValueError("Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.")

        self.appointment_type = appointment_type
        self.client_name = client_name

    def __str__(self):
        """
        String representation of an Appointment instance.

        :return: A string describing the appointment.
        """
        return f"{self.client_name} - {self.appointment_type} Consultation on {self.date} at {self.time}"


class AppointmentScheduler:
    """
    Class to manage the scheduling and management of consultations.
    """
    def __init__(self):
        """
        Initialize an AppointmentScheduler instance.
        """
        self.appointments: List[Appointment] = []

    def add_appointment(self, appointment: Appointment) -> None:
        """
        Add a new appointment to the scheduler.

        :param appointment: Appointment instance to add.
        """
        if any(existing.date == appointment.date and existing.time == appointment.time for existing in self.appointments):
            raise ValueError("Conflict detected: Another appointment is already scheduled at this time.")
        self.appointments.append(appointment)

    def cancel_appointment(self, client_name: str, date: str, time: str) -> None:
        """
        Cancel an appointment based on client name, date, and time.

        :param client_name: Name of the client.
        :param date: Date of the appointment in YYYY-MM-DD format.
        :param time: Time of the appointment in HH:MM format.
        """
        try:
            appointment_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            appointment_time = datetime.datetime.strptime(time, '%H:%M').time()
        except ValueError:
            raise ValueError("Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.")

        for appointment in self.appointments:
            if appointment.client_name == client_name and appointment.date == appointment_date and appointment.time == appointment_time:
                self.appointments.remove(appointment)
                return
        
        raise ValueError("No matching appointment found to cancel.")

    def view_appointments(self) -> List[Dict[str, str]]:
        """
        View all scheduled appointments.

        :return: A list of dictionaries containing appointment details.
        """
        return [
            {
                "Client Name": appointment.client_name,
                "Type": appointment.appointment_type,
                "Date": appointment.date.strftime('%Y-%m-%d'),
                "Time": appointment.time.strftime('%H:%M')
            }
            for appointment in self.appointments
        ]


# Main function to demonstrate handling of the AppointmentScheduler
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    # Example usage
    try:
        appointment1 = Appointment("Skype", "2023-10-15", "10:30", "John Doe")
        appointment2 = Appointment("Phone", "2023-10-16", "14:00", "Jane Smith")
        appointment3 = Appointment("In-Person", "2023-10-17", "09:00", "Emily Johnson")

        scheduler.add_appointment(appointment1)
        scheduler.add_appointment(appointment2)
        scheduler.add_appointment(appointment3)

        print("Scheduled Appointments:")
        for appt in scheduler.view_appointments():
            print(appt)

        # Cancel an appointment
        scheduler.cancel_appointment("Jane Smith", "2023-10-16", "14:00")
        print("\nUpdated Appointments After Cancellation:")
        for appt in scheduler.view_appointments():
            print(appt)
    except ValueError as e:
        print(f"Error: {e}")
```
