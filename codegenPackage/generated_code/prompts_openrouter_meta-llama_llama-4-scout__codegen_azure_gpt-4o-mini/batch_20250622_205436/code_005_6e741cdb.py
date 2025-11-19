"""
Generated Code Metadata:
========================
Original URL: https://orthopedicsurgerysandiego.com
Prompt: Write a code snippet in Python to manage patient appointments and scheduling for an orthopedic surgery clinic, including variables for doctor names, patient names, and appointment dates.
Generated: DETERMINISTIC_6e741cdbea222b16
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict, Optional

class Appointment:
    """Class to represent a patient appointment."""
    
    def __init__(self, doctor_name: str, patient_name: str, appointment_date: str):
        """
        Initialize an Appointment instance.

        :param doctor_name: Name of the doctor
        :param patient_name: Name of the patient
        :param appointment_date: Date of the appointment in 'YYYY-MM-DD' format
        """
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_date = self._validate_date(appointment_date)

    @staticmethod
    def _validate_date(date_str: str) -> datetime:
        """
        Validate and convert the appointment date string to a datetime object.

        :param date_str: Date string in 'YYYY-MM-DD' format
        :return: datetime object
        :raises ValueError: If the date string is not in the correct format
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def __repr__(self):
        return f"Appointment(Doctor: {self.doctor_name}, Patient: {self.patient_name}, Date: {self.appointment_date.date()})"


class AppointmentManager:
    """Class to manage appointments for the orthopedic surgery clinic."""
    
    def __init__(self):
        """Initialize the AppointmentManager with an empty appointment list."""
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, doctor_name: str, patient_name: str, appointment_date: str) -> None:
        """
        Schedule a new appointment.

        :param doctor_name: Name of the doctor
        :param patient_name: Name of the patient
        :param appointment_date: Date of the appointment in 'YYYY-MM-DD' format
        """
        appointment = Appointment(doctor_name, patient_name, appointment_date)
        self.appointments.append(appointment)

    def get_appointments(self) -> List[Dict[str, str]]:
        """
        Retrieve a list of all scheduled appointments.

        :return: List of dictionaries containing appointment details
        """
        return [{"doctor": appt.doctor_name, "patient": appt.patient_name, "date": appt.appointment_date.date()} for appt in self.appointments]

    def find_appointments_by_doctor(self, doctor_name: str) -> List[Dict[str, str]]:
        """
        Find all appointments for a specific doctor.

        :param doctor_name: Name of the doctor to search for
        :return: List of dictionaries containing appointment details for the specified doctor
        """
        return [{"doctor": appt.doctor_name, "patient": appt.patient_name, "date": appt.appointment_date.date()} 
                for appt in self.appointments if appt.doctor_name == doctor_name]

# Example usage
if __name__ == "__main__":
    manager = AppointmentManager()
    
    # Schedule some appointments
    try:
        manager.schedule_appointment("Dr. Smith", "John Doe", "2023-10-15")
        manager.schedule_appointment("Dr. Smith", "Jane Doe", "2023-10-16")
        manager.schedule_appointment("Dr. Johnson", "Alice Smith", "2023-10-17")
        
        # Retrieve all appointments
        print("All Appointments:")
        print(manager.get_appointments())
        
        # Find appointments for a specific doctor
        print("\nAppointments for Dr. Smith:")
        print(manager.find_appointments_by_doctor("Dr. Smith"))
        
    except ValueError as e:
        print(f"Error: {e}")
```
