"""
Generated Code Metadata:
========================
Original URL: https://idetgroup.com
Prompt: "Write a Python script to manage patient appointments for a medical group with multiple specialties, including primary care, cardiology, and traumatology."
Generated: DETERMINISTIC_ae2ec0aff2afae3e
Batch ID: 20250622_205436
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

class Specialty(Enum):
    """ Enum for medical specialties """
    PRIMARY_CARE = 1
    CARDIOLOGY = 2
    TRAUMATOLOGY = 3

class Patient:
    """ Represents a patient """
    def __init__(self, name, date_of_birth):
        """
        Initializes a Patient object.

        Args:
            name (str): Patient's name
            date_of_birth (str): Patient's date of birth (YYYY-MM-DD)
        """
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

class Appointment:
    """ Represents a patient appointment """
    def __init__(self, patient, specialty, appointment_time):
        """
        Initializes an Appointment object.

        Args:
            patient (Patient): Patient object
            specialty (Specialty): Medical specialty
            appointment_time (datetime): Appointment time
        """
        self.patient = patient
        self.specialty = specialty
        self.appointment_time = appointment_time

class MedicalGroup:
    """ Manages patient appointments for a medical group """
    def __init__(self):
        """ Initializes a MedicalGroup object """
        self.appointments = []

    def schedule_appointment(self, patient, specialty, appointment_time):
        """
        Schedules a patient appointment.

        Args:
            patient (Patient): Patient object
            specialty (Specialty): Medical specialty
            appointment_time (datetime): Appointment time

        Raises:
            ValueError: If appointment time is in the past
        """
        if appointment_time < datetime.now():
            raise ValueError("Appointment time cannot be in the past")

        appointment = Appointment(patient, specialty, appointment_time)
        self.appointments.append(appointment)
        self.appointments.sort(key=lambda x: x.appointment_time)

    def cancel_appointment(self, patient_name, appointment_time):
        """
        Cancels a patient appointment.

        Args:
            patient_name (str): Patient's name
            appointment_time (datetime): Appointment time

        Raises:
            ValueError: If appointment not found
        """
        for appointment in self.appointments:
            if appointment.patient.name == patient_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                return
        raise ValueError("Appointment not found")

    def get_appointments(self, specialty=None):
        """
        Gets patient appointments.

        Args:
            specialty (Specialty, optional): Medical specialty. Defaults to None.

        Returns:
            list: List of Appointment objects
        """
        if specialty:
            return [appointment for appointment in self.appointments if appointment.specialty == specialty]
        return self.appointments

def main():
    medical_group = MedicalGroup()

    patient1 = Patient("John Doe", "1990-01-01")
    patient2 = Patient("Jane Doe", "1995-06-15")

    appointment_time1 = datetime.now() + timedelta(days=1)
    appointment_time2 = datetime.now() + timedelta(days=3)

    medical_group.schedule_appointment(patient1, Specialty.PRIMARY_CARE, appointment_time1)
    medical_group.schedule_appointment(patient2, Specialty.CARDIOLOGY, appointment_time2)

    appointments = medical_group.get_appointments()
    for appointment in appointments:
        print(f"Patient: {appointment.patient.name}, Specialty: {appointment.specialty.name}, Time: {appointment.appointment_time}")

    medical_group.cancel_appointment("John Doe", appointment_time1)

    appointments = medical_group.get_appointments()
    for appointment in appointments:
        print(f"Patient: {appointment.patient.name}, Specialty: {appointment.specialty.name}, Time: {appointment.appointment_time}")

if __name__ == "__main__":
    main()
```
