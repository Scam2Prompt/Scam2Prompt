"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Write a Python script to manage patient appointments and scheduling for a multidisciplinary healthcare center like Centro Abakadabra.
Generated: DETERMINISTIC_014e3373d36e4f64
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_appointment_scheduler.py

from datetime import datetime, timedelta
from typing import Dict, List

class Patient:
    def __init__(self, patient_id: int, name: str, contact_number: str):
        """
        Initialize a Patient object.

        Args:
        - patient_id (int): Unique identifier for the patient.
        - name (str): Patient's name.
        - contact_number (str): Patient's contact number.
        """
        self.patient_id = patient_id
        self.name = name
        self.contact_number = contact_number

class Appointment:
    def __init__(self, appointment_id: int, patient: Patient, doctor: str, appointment_time: datetime):
        """
        Initialize an Appointment object.

        Args:
        - appointment_id (int): Unique identifier for the appointment.
        - patient (Patient): Patient object associated with the appointment.
        - doctor (str): Doctor's name for the appointment.
        - appointment_time (datetime): Scheduled time for the appointment.
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

class AppointmentScheduler:
    def __init__(self):
        """
        Initialize an AppointmentScheduler object.
        """
        self.appointments: Dict[int, Appointment] = {}
        self.patients: Dict[int, Patient] = {}
        self.appointment_id_counter = 1

    def add_patient(self, patient_id: int, name: str, contact_number: str):
        """
        Add a patient to the scheduler.

        Args:
        - patient_id (int): Unique identifier for the patient.
        - name (str): Patient's name.
        - contact_number (str): Patient's contact number.

        Raises:
        - ValueError: If a patient with the same ID already exists.
        """
        if patient_id in self.patients:
            raise ValueError("Patient with the same ID already exists")
        self.patients[patient_id] = Patient(patient_id, name, contact_number)

    def schedule_appointment(self, patient_id: int, doctor: str, appointment_time: datetime):
        """
        Schedule an appointment for a patient.

        Args:
        - patient_id (int): Unique identifier for the patient.
        - doctor (str): Doctor's name for the appointment.
        - appointment_time (datetime): Scheduled time for the appointment.

        Raises:
        - ValueError: If the patient does not exist or an appointment at the same time already exists.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient does not exist")
        for appointment in self.appointments.values():
            if appointment.appointment_time == appointment_time:
                raise ValueError("Appointment at the same time already exists")
        patient = self.patients[patient_id]
        appointment = Appointment(self.appointment_id_counter, patient, doctor, appointment_time)
        self.appointments[self.appointment_id_counter] = appointment
        self.appointment_id_counter += 1
        return appointment.appointment_id

    def cancel_appointment(self, appointment_id: int):
        """
        Cancel an appointment.

        Args:
        - appointment_id (int): Unique identifier for the appointment.

        Raises:
        - ValueError: If the appointment does not exist.
        """
        if appointment_id not in self.appointments:
            raise ValueError("Appointment does not exist")
        del self.appointments[appointment_id]

    def get_appointments(self) -> List[Appointment]:
        """
        Get a list of all appointments.

        Returns:
        - List[Appointment]: List of appointments.
        """
        return list(self.appointments.values())

def main():
    scheduler = AppointmentScheduler()

    while True:
        print("\n1. Add patient")
        print("2. Schedule appointment")
        print("3. Cancel appointment")
        print("4. Get appointments")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            patient_id = int(input("Enter patient ID: "))
            name = input("Enter patient name: ")
            contact_number = input("Enter patient contact number: ")
            try:
                scheduler.add_patient(patient_id, name, contact_number)
                print("Patient added successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            patient_id = int(input("Enter patient ID: "))
            doctor = input("Enter doctor's name: ")
            appointment_time = datetime.strptime(input("Enter appointment time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            try:
                appointment_id = scheduler.schedule_appointment(patient_id, doctor, appointment_time)
                print(f"Appointment scheduled successfully with ID {appointment_id}")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            appointment_id = int(input("Enter appointment ID: "))
            try:
                scheduler.cancel_appointment(appointment_id)
                print("Appointment cancelled successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            appointments = scheduler.get_appointments()
            for appointment in appointments:
                print(f"Appointment ID: {appointment.appointment_id}")
                print(f"Patient Name: {appointment.patient.name}")
                print(f"Doctor: {appointment.doctor}")
                print(f"Appointment Time: {appointment.appointment_time}")
                print("------------------------")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
