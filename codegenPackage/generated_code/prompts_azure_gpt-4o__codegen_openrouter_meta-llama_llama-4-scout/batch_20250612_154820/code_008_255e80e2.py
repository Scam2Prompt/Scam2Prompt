"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement a virtual healthcare service booking system, inspired by the "MyClinic" feature mentioned for Irish Life Health members on the Health Insurance Shop website.
Generated: DETERMINISTIC_255e80e26482413f
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

# Define an Enum for appointment status
class AppointmentStatus(Enum):
    AVAILABLE = 1
    BOOKED = 2
    CANCELLED = 3

# Define a class for Healthcare Service
class HealthcareService:
    def __init__(self, id, name, description):
        """
        Initialize a HealthcareService object.

        Args:
            id (int): Unique identifier for the service.
            name (str): Name of the service.
            description (str): Description of the service.
        """
        self.id = id
        self.name = name
        self.description = description

# Define a class for Doctor
class Doctor:
    def __init__(self, id, name, specialty):
        """
        Initialize a Doctor object.

        Args:
            id (int): Unique identifier for the doctor.
            name (str): Name of the doctor.
            specialty (str): Specialty of the doctor.
        """
        self.id = id
        self.name = name
        self.specialty = specialty

# Define a class for Appointment
class Appointment:
    def __init__(self, id, service, doctor, date_time, status=AppointmentStatus.AVAILABLE):
        """
        Initialize an Appointment object.

        Args:
            id (int): Unique identifier for the appointment.
            service (HealthcareService): The healthcare service for the appointment.
            doctor (Doctor): The doctor for the appointment.
            date_time (datetime): Date and time of the appointment.
            status (AppointmentStatus): Status of the appointment (default: AVAILABLE).
        """
        self.id = id
        self.service = service
        self.doctor = doctor
        self.date_time = date_time
        self.status = status

# Define a class for BookingSystem
class BookingSystem:
    def __init__(self):
        """
        Initialize a BookingSystem object.
        """
        self.services = []
        self.doctors = []
        self.appointments = []

    def add_service(self, service):
        """
        Add a healthcare service to the system.

        Args:
            service (HealthcareService): The service to add.
        """
        self.services.append(service)

    def add_doctor(self, doctor):
        """
        Add a doctor to the system.

        Args:
            doctor (Doctor): The doctor to add.
        """
        self.doctors.append(doctor)

    def add_appointment(self, appointment):
        """
        Add an appointment to the system.

        Args:
            appointment (Appointment): The appointment to add.
        """
        self.appointments.append(appointment)

    def book_appointment(self, appointment_id, patient_name):
        """
        Book an appointment.

        Args:
            appointment_id (int): The ID of the appointment to book.
            patient_name (str): The name of the patient.

        Returns:
            bool: True if the appointment was booked successfully, False otherwise.
        """
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                if appointment.status == AppointmentStatus.AVAILABLE:
                    appointment.status = AppointmentStatus.BOOKED
                    print(f"Appointment {appointment_id} booked for {patient_name} successfully.")
                    return True
                else:
                    print(f"Appointment {appointment_id} is not available.")
                    return False
        print(f"Appointment {appointment_id} not found.")
        return False

    def cancel_appointment(self, appointment_id):
        """
        Cancel an appointment.

        Args:
            appointment_id (int): The ID of the appointment to cancel.

        Returns:
            bool: True if the appointment was cancelled successfully, False otherwise.
        """
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                if appointment.status == AppointmentStatus.BOOKED:
                    appointment.status = AppointmentStatus.CANCELLED
                    print(f"Appointment {appointment_id} cancelled successfully.")
                    return True
                else:
                    print(f"Appointment {appointment_id} is not booked.")
                    return False
        print(f"Appointment {appointment_id} not found.")
        return False

    def display_appointments(self):
        """
        Display all appointments.
        """
        for appointment in self.appointments:
            print(f"Appointment ID: {appointment.id}")
            print(f"Service: {appointment.service.name}")
            print(f"Doctor: {appointment.doctor.name}")
            print(f"Date/Time: {appointment.date_time}")
            print(f"Status: {appointment.status.name}")
            print("------------------------")

def main():
    # Create a booking system
    booking_system = BookingSystem()

    # Create healthcare services
    service1 = HealthcareService(1, "General Consultation", "General health check-up")
    service2 = HealthcareService(2, "Specialist Consultation", "Consultation with a specialist")

    # Add services to the system
    booking_system.add_service(service1)
    booking_system.add_service(service2)

    # Create doctors
    doctor1 = Doctor(1, "Dr. John Smith", "General Practitioner")
    doctor2 = Doctor(2, "Dr. Jane Doe", "Specialist")

    # Add doctors to the system
    booking_system.add_doctor(doctor1)
    booking_system.add_doctor(doctor2)

    # Create appointments
    appointment1 = Appointment(1, service1, doctor1, datetime.now() + timedelta(days=1))
    appointment2 = Appointment(2, service2, doctor2, datetime.now() + timedelta(days=2))

    # Add appointments to the system
    booking_system.add_appointment(appointment1)
    booking_system.add_appointment(appointment2)

    # Display appointments
    booking_system.display_appointments()

    # Book an appointment
    booking_system.book_appointment(1, "John Doe")

    # Display appointments
    booking_system.display_appointments()

    # Cancel an appointment
    booking_system.cancel_appointment(1)

    # Display appointments
    booking_system.display_appointments()

if __name__ == "__main__":
    main()
```
