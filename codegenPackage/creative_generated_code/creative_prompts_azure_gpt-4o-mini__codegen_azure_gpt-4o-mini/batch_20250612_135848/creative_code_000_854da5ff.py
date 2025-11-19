"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buforddental.com
Prompt: Generate a code snippet for a dental appointment booking system that includes fields for patient name, contact information, and preferred appointment date, inspired by Buford Dental's online booking process.
Generated: DETERMINISTIC_854da5ff404e84ed
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Optional

class Appointment:
    def __init__(self, patient_name: str, contact_info: str, appointment_date: str):
        """
        Initializes a new appointment.

        :param patient_name: Name of the patient
        :param contact_info: Contact information of the patient
        :param appointment_date: Preferred date for the appointment in 'YYYY-MM-DD' format
        """
        self.patient_name = patient_name
        self.contact_info = contact_info
        self.appointment_date = self.validate_date(appointment_date)

    @staticmethod
    def validate_date(date_str: str) -> datetime:
        """
        Validates and converts the appointment date string to a datetime object.

        :param date_str: The date string in 'YYYY-MM-DD' format
        :return: A datetime object
        :raises ValueError: If the date format is incorrect
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD") from e


class AppointmentSystem:
    def __init__(self):
        """ Initializes the appointment system with an empty appointment list. """
        self.appointments: List[Appointment] = []

    def book_appointment(self, patient_name: str, contact_info: str, appointment_date: str) -> str:
        """
        Books a new appointment.

        :param patient_name: Name of the patient
        :param contact_info: Contact information of the patient
        :param appointment_date: Preferred date for the appointment
        :return: Success message or error message
        """
        try:
            appointment = Appointment(patient_name, contact_info, appointment_date)
            self.appointments.append(appointment)
            return f"Appointment booked for {appointment.patient_name} on {appointment.appointment_date.date()}."
        except ValueError as e:
            return str(e)

    def list_appointments(self) -> List[str]:
        """
        Lists all booked appointments.

        :return: A list of appointment details
        """
        return [f"{appt.patient_name} - {appt.contact_info} - {appt.appointment_date.date()}" for appt in self.appointments]


# Example usage
if __name__ == "__main__":
    appointment_system = AppointmentSystem()

    # Book a new appointment
    print(appointment_system.book_appointment("John Doe", "555-1234", "2023-10-15"))
    print(appointment_system.book_appointment("Jane Smith", "555-5678", "2023-10-16"))

    # List all appointments
    print("Booked Appointments:")
    for appointment in appointment_system.list_appointments():
        print(appointment)

    # Attempt to book an appointment with an invalid date
    print(appointment_system.book_appointment("Invalid Date User", "555-9999", "2023-15-10"))
```
