"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Write a Python script to manage home healthcare services, including patient tracking and appointment scheduling, inspired by the services offered by Payidar Evde Sağlık Hizmetleri.
Generated: DETERMINISTIC_30fc1383eacd7e53
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Patient:
    """
    Class to represent a patient in the home healthcare system.
    """
    def __init__(self, patient_id, name, age, address, phone_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Address: {self.address}, Phone: {self.phone_number}"


class Appointment:
    """
    Class to represent an appointment in the home healthcare system.
    """
    def __init__(self, appointment_id, patient, date, time, service_type):
        self.appointment_id = appointment_id
        self.patient = patient
        self.date = date
        self.time = time
        self.service_type = service_type

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Date: {self.date}, Time: {self.time}, Service: {self.service_type}"


class HomeHealthcareService:
    """
    Class to manage home healthcare services, including patient tracking and appointment scheduling.
    """
    def __init__(self):
        self.patients = {}
        self.appointments = {}

    def add_patient(self, patient_id, name, age, address, phone_number):
        """
        Add a new patient to the system.
        """
        if patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient_id} already exists.")
        self.patients[patient_id] = Patient(patient_id, name, age, address, phone_number)
        print(f"Patient {name} added successfully.")

    def schedule_appointment(self, appointment_id, patient_id, date, time, service_type):
        """
        Schedule a new appointment for a patient.
        """
        if appointment_id in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} already exists.")
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        
        # Validate date and time format
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            datetime.datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.")
        
        patient = self.patients[patient_id]
        self.appointments[appointment_id] = Appointment(appointment_id, patient, date, time, service_type)
        print(f"Appointment for {patient.name} scheduled successfully.")

    def view_patients(self):
        """
        View all patients in the system.
        """
        if not self.patients:
            print("No patients found.")
        else:
            for patient in self.patients.values():
                print(patient)

    def view_appointments(self):
        """
        View all appointments in the system.
        """
        if not self.appointments:
            print("No appointments found.")
        else:
            for appointment in self.appointments.values():
                print(appointment)

    def cancel_appointment(self, appointment_id):
        """
        Cancel an existing appointment.
        """
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} does not exist.")
        del self.appointments[appointment_id]
        print(f"Appointment ID {appointment_id} canceled successfully.")


# Example usage
if __name__ == "__main__":
    service = HomeHealthcareService()

    # Adding patients
    service.add_patient(1, "John Doe", 45, "123 Main St", "555-1234")
    service.add_patient(2, "Jane Smith", 30, "456 Elm St", "555-5678")

    # Viewing patients
    print("\nPatients:")
    service.view_patients()

    # Scheduling appointments
    service.schedule_appointment(101, 1, "2023-10-15", "14:00", "Physical Therapy")
    service.schedule_appointment(102, 2, "2023-10-16", "10:00", "Nursing Care")

    # Viewing appointments
    print("\nAppointments:")
    service.view_appointments()

    # Canceling an appointment
    service.cancel_appointment(101)

    # Viewing appointments after cancellation
    print("\nAppointments after cancellation:")
    service.view_appointments()
```
