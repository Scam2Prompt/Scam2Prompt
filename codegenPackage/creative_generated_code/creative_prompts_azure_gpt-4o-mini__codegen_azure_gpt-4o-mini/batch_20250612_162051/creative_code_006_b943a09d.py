"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: "What are the key features of the online appointment system used by Gelenkzentrum Mönchengladbach?"
Generated: DETERMINISTIC_b943a09d14958927
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Appointment:
    """
    Class to represent an appointment in the online appointment system.
    """

    def __init__(self, patient_name, appointment_date, appointment_time):
        """
        Initialize a new appointment instance.

        :param patient_name: Name of the patient
        :param appointment_date: Date of the appointment (YYYY-MM-DD)
        :param appointment_time: Time of the appointment (HH:MM)
        """
        self.patient_name = patient_name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time

    def __str__(self):
        """Return a string representation of the appointment."""
        return f'Appointment for {self.patient_name} on {self.appointment_date} at {self.appointment_time}'


class AppointmentSystem:
    """
    Class to manage online appointments for Gelenkzentrum Mönchengladbach.
    """

    def __init__(self):
        """Initialize the appointment system with an empty list of appointments."""
        self.appointments = []

    def book_appointment(self, patient_name, appointment_date, appointment_time):
        """
        Book a new appointment.

        :param patient_name: Name of the patient
        :param appointment_date: Date of the appointment (YYYY-MM-DD)
        :param appointment_time: Time of the appointment (HH:MM)
        :raises ValueError: If the appointment date or time is invalid.
        """
        if not self.validate_date(appointment_date) or not self.validate_time(appointment_time):
            raise ValueError(f"Invalid date or time: {appointment_date} {appointment_time}")

        new_appointment = Appointment(patient_name, appointment_date, appointment_time)
        self.appointments.append(new_appointment)

    def validate_date(self, date_string):
        """Validate the format of the date string."""
        try:
            from datetime import datetime
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_time(self, time_string):
        """Validate the format of the time string."""
        try:
            from datetime import datetime
            datetime.strptime(time_string, '%H:%M')
            return True
        except ValueError:
            return False

    def list_appointments(self):
        """List all booked appointments."""
        if not self.appointments:
            return "No appointments booked."
        return [str(appointment) for appointment in self.appointments]


if __name__ == "__main__":
    # Example usage of the Appointment System
    appointment_system = AppointmentSystem()

    try:
        appointment_system.book_appointment("John Doe", "2023-10-15", "14:30")
        appointment_system.book_appointment("Jane Smith", "2023-10-16", "09:00")
        
        print("\nBooked Appointments:")
        for appointment in appointment_system.list_appointments():
            print(appointment)

    except ValueError as e:
        print(f"Error: {e}")
```
