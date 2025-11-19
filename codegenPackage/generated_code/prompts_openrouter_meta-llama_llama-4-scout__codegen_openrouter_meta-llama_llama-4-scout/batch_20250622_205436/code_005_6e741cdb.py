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

class Doctor:
    """Represents an orthopedic surgeon."""

    def __init__(self, name):
        """
        Initializes a Doctor object.

        Args:
            name (str): The doctor's name.
        """
        self.name = name

class Patient:
    """Represents a patient."""

    def __init__(self, name):
        """
        Initializes a Patient object.

        Args:
            name (str): The patient's name.
        """
        self.name = name

class Appointment:
    """Represents a scheduled appointment."""

    def __init__(self, doctor, patient, date):
        """
        Initializes an Appointment object.

        Args:
            doctor (Doctor): The doctor for the appointment.
            patient (Patient): The patient for the appointment.
            date (str): The appointment date in YYYY-MM-DD format.

        Raises:
            ValueError: If the date is not in the correct format.
        """
        try:
            self.date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        self.doctor = doctor
        self.patient = patient

class OrthopedicClinic:
    """Manages patient appointments and scheduling."""

    def __init__(self):
        """Initializes the clinic with empty appointment schedules."""
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, name):
        """
        Adds a doctor to the clinic.

        Args:
            name (str): The doctor's name.
        """
        self.doctors.append(Doctor(name))

    def add_patient(self, name):
        """
        Adds a patient to the clinic.

        Args:
            name (str): The patient's name.
        """
        self.patients.append(Patient(name))

    def schedule_appointment(self, doctor_name, patient_name, date):
        """
        Schedules an appointment.

        Args:
            doctor_name (str): The doctor's name.
            patient_name (str): The patient's name.
            date (str): The appointment date in YYYY-MM-DD format.

        Raises:
            ValueError: If the doctor or patient is not found.
        """
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)
        patient = next((p for p in self.patients if p.name == patient_name), None)

        if not doctor:
            raise ValueError(f"Doctor '{doctor_name}' not found.")
        if not patient:
            raise ValueError(f"Patient '{patient_name}' not found.")

        appointment = Appointment(doctor, patient, date)
        self.appointments.append(appointment)

    def print_appointments(self):
        """Prints all scheduled appointments."""
        for appointment in self.appointments:
            print(f"Date: {appointment.date}")
            print(f"Doctor: {appointment.doctor.name}")
            print(f"Patient: {appointment.patient.name}")
            print("------------------------")

def main():
    clinic = OrthopedicClinic()

    while True:
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Schedule Appointment")
        print("4. Print Appointments")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter doctor's name: ")
            clinic.add_doctor(name)
        elif choice == "2":
            name = input("Enter patient's name: ")
            clinic.add_patient(name)
        elif choice == "3":
            doctor_name = input("Enter doctor's name: ")
            patient_name = input("Enter patient's name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            try:
                clinic.schedule_appointment(doctor_name, patient_name, date)
            except ValueError as e:
                print(e)
        elif choice == "4":
            clinic.print_appointments()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
