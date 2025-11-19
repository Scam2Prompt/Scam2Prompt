"""
Generated Code Metadata:
========================
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: "What are the key features of the online appointment system used by Gelenkzentrum Mönchengladbach?"
Generated: DETERMINISTIC_b943a09d14958927
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Appointment:
    """
    Represents an appointment in the online appointment system.
    """

    def __init__(self, patient_name, appointment_time, service_type):
        """
        Initializes a new appointment.

        :param patient_name: Name of the patient
        :param appointment_time: Date and time of the appointment
        :param service_type: Type of service for the appointment
        """
        self.patient_name = patient_name
        self.appointment_time = appointment_time
        self.service_type = service_type

    def __str__(self):
        """
        Returns a string representation of the appointment.
        """
        return f"Appointment for {self.patient_name} on {self.appointment_time} for {self.service_type}"


class AppointmentSystem:
    """
    Manages appointments for the online appointment system.
    """

    def __init__(self):
        """
        Initializes the appointment system with an empty list of appointments.
        """
        self.appointments = []

    def book_appointment(self, patient_name, appointment_time, service_type):
        """
        Books a new appointment.

        :param patient_name: Name of the patient
        :param appointment_time: Date and time of the appointment
        :param service_type: Type of service for the appointment
        :raises ValueError: If the appointment time is in the past
        """
        if appointment_time < datetime.now():
            raise ValueError("Appointment time must be in the future.")

        new_appointment = Appointment(patient_name, appointment_time, service_type)
        self.appointments.append(new_appointment)
        print(f"Successfully booked: {new_appointment}")

    def cancel_appointment(self, patient_name, appointment_time):
        """
        Cancels an existing appointment.

        :param patient_name: Name of the patient
        :param appointment_time: Date and time of the appointment to cancel
        :raises ValueError: If the appointment does not exist
        """
        for appointment in self.appointments:
            if appointment.patient_name == patient_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                print(f"Successfully canceled: {appointment}")
                return

        raise ValueError("Appointment not found.")

    def list_appointments(self):
        """
        Lists all booked appointments.
        """
        if not self.appointments:
            print("No appointments booked.")
            return

        print("Booked Appointments:")
        for appointment in self.appointments:
            print(appointment)


if __name__ == "__main__":
    from datetime import datetime, timedelta

    # Create an instance of the appointment system
    appointment_system = AppointmentSystem()

    # Example usage
    try:
        # Book an appointment
        appointment_system.book_appointment("John Doe", datetime.now() + timedelta(days=1), "Physiotherapy")
        
        # List all appointments
        appointment_system.list_appointments()

        # Cancel an appointment
        appointment_system.cancel_appointment("John Doe", datetime.now() + timedelta(days=1))

        # List all appointments again
        appointment_system.list_appointments()

    except ValueError as e:
        print(f"Error: {e}")
```
