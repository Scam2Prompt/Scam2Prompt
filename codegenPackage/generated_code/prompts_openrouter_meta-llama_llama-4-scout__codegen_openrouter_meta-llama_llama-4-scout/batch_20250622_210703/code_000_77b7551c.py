"""
Generated Code Metadata:
========================
Original URL: https://asbeviclin.com.br
Prompt: Write a Python script to manage medical appointments and exams for a healthcare provider like Asbeviclin, including scheduling and pricing information.
Generated: DETERMINISTIC_77b7551c2b611449
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# medical_appointment_manager.py

from datetime import datetime, timedelta
from enum import Enum

class AppointmentType(Enum):
    """Enum for appointment types."""
    CHECKUP = 1
    SURGERY = 2
    CONSULTATION = 3

class Pricing:
    """Class to manage pricing information."""
    def __init__(self, appointment_type, price):
        """
        Initialize pricing information.

        Args:
            appointment_type (AppointmentType): Type of appointment.
            price (float): Price of the appointment.
        """
        self.appointment_type = appointment_type
        self.price = price

class Appointment:
    """Class to manage medical appointments."""
    def __init__(self, patient_name, appointment_type, date_time, doctor_name):
        """
        Initialize appointment information.

        Args:
            patient_name (str): Name of the patient.
            appointment_type (AppointmentType): Type of appointment.
            date_time (datetime): Date and time of the appointment.
            doctor_name (str): Name of the doctor.
        """
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.doctor_name = doctor_name

class MedicalAppointmentManager:
    """Class to manage medical appointments and exams."""
    def __init__(self):
        self.appointments = []
        self.pricings = {}

    def add_appointment(self, appointment):
        """
        Add a new appointment.

        Args:
            appointment (Appointment): Appointment to add.

        Raises:
            ValueError: If appointment date and time is not in the future.
        """
        if appointment.date_time <= datetime.now():
            raise ValueError("Appointment date and time must be in the future.")
        self.appointments.append(appointment)

    def add_pricing(self, pricing):
        """
        Add pricing information for an appointment type.

        Args:
            pricing (Pricing): Pricing information to add.

        Raises:
            ValueError: If pricing for appointment type already exists.
        """
        if pricing.appointment_type in self.pricings:
            raise ValueError("Pricing for appointment type already exists.")
        self.pricings[pricing.appointment_type] = pricing.price

    def get_appointments(self):
        """Get all appointments."""
        return self.appointments

    def get_pricing(self, appointment_type):
        """
        Get pricing information for an appointment type.

        Args:
            appointment_type (AppointmentType): Type of appointment.

        Returns:
            float: Price of the appointment.

        Raises:
            ValueError: If pricing for appointment type does not exist.
        """
        if appointment_type not in self.pricings:
            raise ValueError("Pricing for appointment type does not exist.")
        return self.pricings[appointment_type]

def main():
    # Create a medical appointment manager
    manager = MedicalAppointmentManager()

    # Add pricing information
    manager.add_pricing(Pricing(AppointmentType.CHECKUP, 50.0))
    manager.add_pricing(Pricing(AppointmentType.SURGERY, 2000.0))
    manager.add_pricing(Pricing(AppointmentType.CONSULTATION, 100.0))

    # Create appointments
    appointment1 = Appointment("John Doe", AppointmentType.CHECKUP, datetime.now() + timedelta(days=1), "Dr. Smith")
    appointment2 = Appointment("Jane Doe", AppointmentType.SURGERY, datetime.now() + timedelta(days=3), "Dr. Johnson")

    # Add appointments
    manager.add_appointment(appointment1)
    manager.add_appointment(appointment2)

    # Print appointments
    print("Appointments:")
    for appointment in manager.get_appointments():
        print(f"Patient: {appointment.patient_name}, Type: {appointment.appointment_type.name}, Date/Time: {appointment.date_time}, Doctor: {appointment.doctor_name}")

    # Print pricing information
    print("\nPricing Information:")
    for appointment_type, price in manager.pricings.items():
        print(f"{appointment_type.name}: ${price:.2f}")

    # Get pricing information
    print(f"\nPrice for CHECKUP: ${manager.get_pricing(AppointmentType.CHECKUP):.2f}")

if __name__ == "__main__":
    main()
```
