"""
Generated Code Metadata:
========================
Original URL: https://smart-medicalservices.com
Prompt: Generate a code snippet to implement a simple appointment scheduling system for a medical services provider, inspired by the services offered by Smart Medical Services.
Generated: DETERMINISTIC_4d061333efb15694
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Patient:
    """Represents a patient in the appointment scheduling system."""

    def __init__(self, patient_id: int, name: str, contact_number: str):
        """
        Initializes a Patient object.

        Args:
        patient_id (int): Unique identifier for the patient.
        name (str): Patient's name.
        contact_number (str): Patient's contact number.
        """
        self.patient_id = patient_id
        self.name = name
        self.contact_number = contact_number

class Doctor:
    """Represents a doctor in the appointment scheduling system."""

    def __init__(self, doctor_id: int, name: str, specialty: str):
        """
        Initializes a Doctor object.

        Args:
        doctor_id (int): Unique identifier for the doctor.
        name (str): Doctor's name.
        specialty (str): Doctor's specialty.
        """
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Appointment:
    """Represents an appointment in the appointment scheduling system."""

    def __init__(self, appointment_id: int, patient: Patient, doctor: Doctor, appointment_time: datetime):
        """
        Initializes an Appointment object.

        Args:
        appointment_id (int): Unique identifier for the appointment.
        patient (Patient): Patient object associated with the appointment.
        doctor (Doctor): Doctor object associated with the appointment.
        appointment_time (datetime): Scheduled time of the appointment.
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

class AppointmentSchedulingSystem:
    """Manages appointments for a medical services provider."""

    def __init__(self):
        self.appointments: Dict[int, Appointment] = {}
        self.patients: Dict[int, Patient] = {}
        self.doctors: Dict[int, Doctor] = {}
        self.appointment_id_counter = 1

    def add_patient(self, patient_id: int, name: str, contact_number: str):
        """
        Adds a patient to the system.

        Args:
        patient_id (int): Unique identifier for the patient.
        name (str): Patient's name.
        contact_number (str): Patient's contact number.

        Raises:
        ValueError: If a patient with the same ID already exists.
        """
        if patient_id in self.patients:
            raise ValueError("Patient with the same ID already exists")
        self.patients[patient_id] = Patient(patient_id, name, contact_number)

    def add_doctor(self, doctor_id: int, name: str, specialty: str):
        """
        Adds a doctor to the system.

        Args:
        doctor_id (int): Unique identifier for the doctor.
        name (str): Doctor's name.
        specialty (str): Doctor's specialty.

        Raises:
        ValueError: If a doctor with the same ID already exists.
        """
        if doctor_id in self.doctors:
            raise ValueError("Doctor with the same ID already exists")
        self.doctors[doctor_id] = Doctor(doctor_id, name, specialty)

    def schedule_appointment(self, patient_id: int, doctor_id: int, appointment_time: datetime):
        """
        Schedules an appointment.

        Args:
        patient_id (int): ID of the patient.
        doctor_id (int): ID of the doctor.
        appointment_time (datetime): Scheduled time of the appointment.

        Raises:
        ValueError: If the patient or doctor does not exist.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient does not exist")
        if doctor_id not in self.doctors:
            raise ValueError("Doctor does not exist")

        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]
        appointment = Appointment(self.appointment_id_counter, patient, doctor, appointment_time)
        self.appointments[self.appointment_id_counter] = appointment
        self.appointment_id_counter += 1
        return appointment.appointment_id

    def cancel_appointment(self, appointment_id: int):
        """
        Cancels an appointment.

        Args:
        appointment_id (int): ID of the appointment to cancel.

        Raises:
        ValueError: If the appointment does not exist.
        """
        if appointment_id not in self.appointments:
            raise ValueError("Appointment does not exist")
        del self.appointments[appointment_id]

    def get_appointments(self) -> List[Appointment]:
        """Returns a list of all appointments."""
        return list(self.appointments.values())

def main():
    scheduling_system = AppointmentSchedulingSystem()

    # Add patients
    scheduling_system.add_patient(1, "John Doe", "123-456-7890")
    scheduling_system.add_patient(2, "Jane Smith", "987-654-3210")

    # Add doctors
    scheduling_system.add_doctor(1, "Dr. Smith", "Cardiology")
    scheduling_system.add_doctor(2, "Dr. Johnson", "Neurology")

    # Schedule appointments
    appointment_time1 = datetime.now() + timedelta(days=1)
    appointment_time2 = datetime.now() + timedelta(days=3)
    appointment_id1 = scheduling_system.schedule_appointment(1, 1, appointment_time1)
    appointment_id2 = scheduling_system.schedule_appointment(2, 2, appointment_time2)

    # Print appointments
    appointments = scheduling_system.get_appointments()
    for appointment in appointments:
        print(f"Appointment ID: {appointment.appointment_id}")
        print(f"Patient: {appointment.patient.name}")
        print(f"Doctor: {appointment.doctor.name}")
        print(f"Time: {appointment.appointment_time}")
        print("------------------------")

    # Cancel an appointment
    scheduling_system.cancel_appointment(appointment_id1)

    # Print appointments after cancellation
    appointments = scheduling_system.get_appointments()
    for appointment in appointments:
        print(f"Appointment ID: {appointment.appointment_id}")
        print(f"Patient: {appointment.patient.name}")
        print(f"Doctor: {appointment.doctor.name}")
        print(f"Time: {appointment.appointment_time}")
        print("------------------------")

if __name__ == "__main__":
    main()
```
