"""
Generated Code Metadata:
========================
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: Write a Python script to manage patient appointments for an orthopedic practice like Gelenkzentrum Mönchengladbach.
Generated: DETERMINISTIC_49d098cc8535fb81
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class AppointmentManager:
    """
    A class to manage patient appointments for an orthopedic practice.
    """

    def __init__(self):
        # Initialize an empty list to store appointments
        self.appointments = []

    def add_appointment(self, patient_name, appointment_date, reason):
        """
        Adds a new appointment to the system.

        Args:
            patient_name (str): Name of the patient.
            appointment_date (datetime.datetime): Date and time of the appointment.
            reason (str): Reason for the appointment.

        Returns:
            str: Confirmation message.
        """
        if not isinstance(appointment_date, datetime.datetime):
            raise ValueError("appointment_date must be a datetime object.")

        # Create an appointment dictionary
        appointment = {
            "patient_name": patient_name,
            "appointment_date": appointment_date,
            "reason": reason
        }

        # Add the appointment to the list
        self.appointments.append(appointment)
        return f"Appointment for {patient_name} on {appointment_date} has been added."

    def view_appointments(self):
        """
        Displays all scheduled appointments.

        Returns:
            list: List of all appointments.
        """
        if not self.appointments:
            return "No appointments scheduled."
        
        return self.appointments

    def cancel_appointment(self, patient_name, appointment_date):
        """
        Cancels an existing appointment.

        Args:
            patient_name (str): Name of the patient.
            appointment_date (datetime.datetime): Date and time of the appointment.

        Returns:
            str: Confirmation message or error message if appointment not found.
        """
        for appointment in self.appointments:
            if appointment["patient_name"] == patient_name and appointment["appointment_date"] == appointment_date:
                self.appointments.remove(appointment)
                return f"Appointment for {patient_name} on {appointment_date} has been canceled."
        
        return "Appointment not found."

    def find_appointments_by_patient(self, patient_name):
        """
        Finds all appointments for a specific patient.

        Args:
            patient_name (str): Name of the patient.

        Returns:
            list: List of appointments for the patient.
        """
        patient_appointments = [
            appointment for appointment in self.appointments if appointment["patient_name"] == patient_name
        ]

        if not patient_appointments:
            return f"No appointments found for {patient_name}."
        
        return patient_appointments


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the appointment manager
        manager = AppointmentManager()

        # Add appointments
        print(manager.add_appointment("John Doe", datetime.datetime(2023, 11, 15, 10, 30), "Knee pain"))
        print(manager.add_appointment("Jane Smith", datetime.datetime(2023, 11, 16, 14, 0), "Back pain"))

        # View all appointments
        print("All Appointments:")
        print(manager.view_appointments())

        # Find appointments for a specific patient
        print("Appointments for John Doe:")
        print(manager.find_appointments_by_patient("John Doe"))

        # Cancel an appointment
        print(manager.cancel_appointment("John Doe", datetime.datetime(2023, 11, 15, 10, 30)))

        # View all appointments after cancellation
        print("All Appointments After Cancellation:")
        print(manager.view_appointments())

    except Exception as e:
        print(f"An error occurred: {e}")
```
