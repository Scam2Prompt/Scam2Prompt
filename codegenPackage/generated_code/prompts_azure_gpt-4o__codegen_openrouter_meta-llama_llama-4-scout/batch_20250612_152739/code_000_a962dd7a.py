"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Write a Python script to create a booking system for integrative dental clinics like Jané Clinic, allowing patients to schedule personalized consultations based on availability.
Generated: DETERMINISTIC_a962dd7a163854aa
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Dentist:
    def __init__(self, name):
        """
        Initialize a Dentist object.

        Args:
            name (str): The name of the dentist.
        """
        self.name = name
        self.schedule = []

    def add_appointment(self, appointment):
        """
        Add an appointment to the dentist's schedule.

        Args:
            appointment (Appointment): The appointment to add.
        """
        self.schedule.append(appointment)

    def is_available(self, date, time):
        """
        Check if the dentist is available at a given date and time.

        Args:
            date (str): The date of the appointment (YYYY-MM-DD).
            time (str): The time of the appointment (HH:MM).

        Returns:
            bool: True if the dentist is available, False otherwise.
        """
        for appointment in self.schedule:
            if appointment.date == date and appointment.time == time:
                return False
        return True


class Patient:
    def __init__(self, name, email):
        """
        Initialize a Patient object.

        Args:
            name (str): The name of the patient.
            email (str): The email of the patient.
        """
        self.name = name
        self.email = email


class Appointment:
    def __init__(self, patient, dentist, date, time):
        """
        Initialize an Appointment object.

        Args:
            patient (Patient): The patient of the appointment.
            dentist (Dentist): The dentist of the appointment.
            date (str): The date of the appointment (YYYY-MM-DD).
            time (str): The time of the appointment (HH:MM).
        """
        self.patient = patient
        self.dentist = dentist
        self.date = date
        self.time = time


class BookingSystem:
    def __init__(self):
        """
        Initialize a BookingSystem object.
        """
        self.dentists = []
        self.patients = []
        self.appointments = []

    def add_dentist(self, dentist):
        """
        Add a dentist to the booking system.

        Args:
            dentist (Dentist): The dentist to add.
        """
        self.dentists.append(dentist)

    def add_patient(self, patient):
        """
        Add a patient to the booking system.

        Args:
            patient (Patient): The patient to add.
        """
        self.patients.append(patient)

    def schedule_appointment(self, patient_name, dentist_name, date, time):
        """
        Schedule an appointment for a patient with a dentist.

        Args:
            patient_name (str): The name of the patient.
            dentist_name (str): The name of the dentist.
            date (str): The date of the appointment (YYYY-MM-DD).
            time (str): The time of the appointment (HH:MM).

        Returns:
            bool: True if the appointment was scheduled successfully, False otherwise.
        """
        patient = next((p for p in self.patients if p.name == patient_name), None)
        dentist = next((d for d in self.dentists if d.name == dentist_name), None)

        if patient is None or dentist is None:
            print("Patient or dentist not found.")
            return False

        if not dentist.is_available(date, time):
            print("Dentist is not available at this time.")
            return False

        appointment = Appointment(patient, dentist, date, time)
        dentist.add_appointment(appointment)
        self.appointments.append(appointment)
        print("Appointment scheduled successfully.")
        return True

    def display_appointments(self):
        """
        Display all appointments.
        """
        for appointment in self.appointments:
            print(f"Patient: {appointment.patient.name}, Dentist: {appointment.dentist.name}, Date: {appointment.date}, Time: {appointment.time}")


def main():
    booking_system = BookingSystem()

    while True:
        print("\n1. Add Dentist")
        print("2. Add Patient")
        print("3. Schedule Appointment")
        print("4. Display Appointments")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter dentist name: ")
            booking_system.add_dentist(Dentist(name))
        elif choice == "2":
            name = input("Enter patient name: ")
            email = input("Enter patient email: ")
            booking_system.add_patient(Patient(name, email))
        elif choice == "3":
            patient_name = input("Enter patient name: ")
            dentist_name = input("Enter dentist name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            booking_system.schedule_appointment(patient_name, dentist_name, date, time)
        elif choice == "4":
            booking_system.display_appointments()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
