"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Write Python code to simulate scheduling appointments for mobile mammography services, ensuring the system checks patient eligibility based on age and absence of breast issues.
Generated: DETERMINISTIC_80f66a1aaaa9017e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Patient:
    """Represents a patient with basic information."""

    def __init__(self, patient_id, name, age, has_breast_issues=False):
        """
        Initializes a Patient object.

        Args:
            patient_id (int): Unique identifier for the patient.
            name (str): Patient's name.
            age (int): Patient's age.
            has_breast_issues (bool): Whether the patient has breast issues. Defaults to False.
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.has_breast_issues = has_breast_issues

    def __str__(self):
        return f"Patient {self.patient_id}: {self.name}, Age: {self.age}, Breast Issues: {self.has_breast_issues}"


class Appointment:
    """Represents a scheduled appointment."""

    def __init__(self, appointment_id, patient, scheduled_time):
        """
        Initializes an Appointment object.

        Args:
            appointment_id (int): Unique identifier for the appointment.
            patient (Patient): The patient for whom the appointment is scheduled.
            scheduled_time (datetime): The scheduled time of the appointment.
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.scheduled_time = scheduled_time

    def __str__(self):
        return f"Appointment {self.appointment_id}: {self.patient.name} on {self.scheduled_time}"


class MobileMammographyService:
    """Simulates a mobile mammography service for scheduling appointments."""

    def __init__(self):
        self.patients = {}
        self.appointments = {}
        self.appointment_id_counter = 1

    def add_patient(self, patient):
        """
        Adds a patient to the system.

        Args:
            patient (Patient): The patient to add.

        Raises:
            ValueError: If a patient with the same ID already exists.
        """
        if patient.patient_id in self.patients:
            raise ValueError("Patient with the same ID already exists.")
        self.patients[patient.patient_id] = patient

    def schedule_appointment(self, patient_id, scheduled_time):
        """
        Schedules an appointment for a patient.

        Args:
            patient_id (int): The ID of the patient.
            scheduled_time (datetime): The scheduled time of the appointment.

        Returns:
            Appointment: The scheduled appointment.

        Raises:
            ValueError: If the patient does not exist, is under 40, or has breast issues.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient does not exist.")
        
        patient = self.patients[patient_id]
        if patient.age < 40:
            raise ValueError("Patients must be 40 or older for this service.")
        if patient.has_breast_issues:
            raise ValueError("Patients with breast issues are not eligible for this service.")

        appointment = Appointment(self.appointment_id_counter, patient, scheduled_time)
        self.appointments[self.appointment_id_counter] = appointment
        self.appointment_id_counter += 1
        return appointment

    def get_appointment(self, appointment_id):
        """
        Retrieves an appointment by ID.

        Args:
            appointment_id (int): The ID of the appointment.

        Returns:
            Appointment: The appointment with the given ID, or None if not found.
        """
        return self.appointments.get(appointment_id)


def main():
    service = MobileMammographyService()

    # Create patients
    patient1 = Patient(1, "John Doe", 50)
    patient2 = Patient(2, "Jane Doe", 30)
    patient3 = Patient(3, "Alice Smith", 55, has_breast_issues=True)

    # Add patients to the service
    service.add_patient(patient1)
    service.add_patient(patient2)
    service.add_patient(patient3)

    # Schedule appointments
    try:
        appointment1 = service.schedule_appointment(1, datetime.now() + timedelta(days=1))
        print(appointment1)
    except ValueError as e:
        print(e)

    try:
        appointment2 = service.schedule_appointment(2, datetime.now() + timedelta(days=2))
        print(appointment2)
    except ValueError as e:
        print(e)

    try:
        appointment3 = service.schedule_appointment(3, datetime.now() + timedelta(days=3))
        print(appointment3)
    except ValueError as e:
        print(e)

    # Get an appointment
    print(service.get_appointment(1))


if __name__ == "__main__":
    main()
```
