"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://movilabtorremedica2.com
Prompt: Generate a code snippet for an appointment scheduling system that integrates with a medical service provider like Movilab Torre Médica.
Generated: DETERMINISTIC_57baffd917f50e6b
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class Appointment:
    """
    A class representing an appointment in the scheduling system.
    """
    def __init__(self, patient_name, provider_name, appointment_date):
        """
        Initialize the appointment details.

        :param patient_name: Name of the patient
        :param provider_name: Name of the medical service provider
        :param appointment_date: Date and time of the appointment
        """
        self.patient_name = patient_name
        self.provider_name = provider_name
        self.appointment_date = appointment_date

    def to_json(self):
        """
        Convert appointment details to a JSON string for storage or API requests.

        :return: JSON representation of the appointment
        """
        return json.dumps({
            'patient_name': self.patient_name,
            'provider_name': self.provider_name,
            'appointment_date': self.appointment_date.isoformat(),
        })


class AppointmentScheduler:
    """
    A class to manage appointment scheduling operations.
    """
    def __init__(self):
        """
        Initialize the scheduler with an empty list of appointments.
        """
        self.appointments = []  # List to store scheduled appointments.

    def schedule_appointment(self, patient_name, provider_name, appointment_date):
        """
        Schedule a new appointment.

        :param patient_name: Name of the patient
        :param provider_name: Name of the medical service provider
        :param appointment_date: Date and time of the appointment
        :raises ValueError: If the appointment date is in the past
        """
        if appointment_date < datetime.datetime.now():
            raise ValueError("Appointment date cannot be in the past.")

        appointment = Appointment(patient_name, provider_name, appointment_date)
        self.appointments.append(appointment)
        print(f"Appointment successfully scheduled for {patient_name} with {provider_name} on {appointment_date}.")

    def list_appointments(self):
        """
        List all scheduled appointments.

        :return: List of appointments as JSON strings
        """
        return [appointment.to_json() for appointment in self.appointments]

    def cancel_appointment(self, patient_name, provider_name, appointment_date):
        """
        Cancel an existing appointment.

        :param patient_name: Name of the patient
        :param provider_name: Name of the medical service provider
        :param appointment_date: Date and time of the appointment
        :raises ValueError: If the appointment is not found
        """
        for appointment in self.appointments:
            if (appointment.patient_name == patient_name and
                appointment.provider_name == provider_name and
                appointment.appointment_date == appointment_date):
                self.appointments.remove(appointment)
                print(f"Appointment for {patient_name} with {provider_name} on {appointment_date} has been canceled.")
                return
        
        raise ValueError("Appointment not found.")

# Example usage of the AppointmentScheduler
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    try:
        # Scheduling an appointment
        scheduler.schedule_appointment(
            patient_name="John Doe",
            provider_name="Movilab Torre Médica",
            appointment_date=datetime.datetime(2023, 12, 10, 14, 30)
        )

        # Listing all appointments
        print("Scheduled appointments:")
        for appointment_json in scheduler.list_appointments():
            print(appointment_json)

        # Canceling an appointment
        scheduler.cancel_appointment(
            patient_name="John Doe",
            provider_name="Movilab Torre Médica",
            appointment_date=datetime.datetime(2023, 12, 10, 14, 30)
        )

    except ValueError as e:
        print(f"Error: {e}")
```
