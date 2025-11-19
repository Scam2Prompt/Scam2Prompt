"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Generate a code snippet for a booking system that allows patients to schedule appointments with a chiropractor or osteopath, similar to the services offered at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_072b4278a4a5457e
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum

class PractitionerType(Enum):
    CHIROPRACTOR = "Chiropractor"
    OSTEOPATH = "Osteopath"

class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

class Patient:
    def __init__(self, patient_id: str, name: str, email: str, phone: str):
        self.patient_id = patient_id
        self.name = name
        self.email = email
        self.phone = phone

class Practitioner:
    def __init__(self, practitioner_id: str, name: str, practitioner_type: PractitionerType):
        self.practitioner_id = practitioner_id
        self.name = name
        self.type = practitioner_type

class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        status: AppointmentStatus = AppointmentStatus.SCHEDULED
    ):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def cancel(self) -> None:
        if self.status == AppointmentStatus.SCHEDULED:
            self.status = AppointmentStatus.CANCELLED
        else:
            raise ValueError("Only scheduled appointments can be cancelled.")

    def complete(self) -> None:
        if self.status == AppointmentStatus.SCHEDULED:
            self.status = AppointmentStatus.COMPLETED
        else:
            raise ValueError("Only scheduled appointments can be completed.")

class BookingSystem:
    def __init__(self):
        self.patients: Dict[str, Patient] = {}
        self.practitioners: Dict[str, Practitioner] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.available_slots: Dict[PractitionerType, List[datetime.datetime]] = {}

    def register_patient(self, patient_id: str, name: str, email: str, phone: str) -> Patient:
        if patient_id in self.patients:
            raise ValueError("Patient ID already exists.")
        patient = Patient(patient_id, name, email, phone)
        self.patients[patient_id] = patient
        return patient

    def register_practitioner(self, practitioner_id: str, name: str, practitioner_type: PractitionerType) -> Practitioner:
        if practitioner_id in self.practitioners:
            raise ValueError("Practitioner ID already exists.")
        practitioner = Practitioner(practitioner_id, name, practitioner_type)
        self.practitioners[practitioner_id] = practitioner
        return practitioner

    def add_available_slot(self, practitioner_type: PractitionerType, slot: datetime.datetime) -> None:
        if practitioner_type not in self.available_slots:
            self.available_slots[practitioner_type] = []
        if slot not in self.available_slots[practitioner_type]:
            self.available_slots[practitioner_type].append(slot)

    def get_available_slots(self, practitioner_type: PractitionerType) -> List[datetime.datetime]:
        return sorted(self.available_slots.get(practitioner_type, []))

    def book_appointment(
        self,
        patient_id: str,
        practitioner_id: str,
        start_time: datetime.datetime,
        duration_minutes: int = 30
    ) -> Appointment:
        if patient_id not in self.patients:
            raise ValueError("Patient not found.")
        if practitioner_id not in self.practitioners:
            raise ValueError("Practitioner not found.")

        practitioner = self.practitioners[practitioner_id]
        end_time = start_time + datetime.timedelta(minutes=duration_minutes)

        # Check if slot is available
        if practitioner.type not in self.available_slots or start_time not in self.available_slots[practitioner.type]:
            raise ValueError("Requested time slot is not available.")

        # Check for overlapping appointments
        for appointment in self.appointments.values():
            if appointment.practitioner.practitioner_id == practitioner_id and not (
                end_time <= appointment.start_time or start_time >= appointment.end_time
            ):
                raise ValueError("Practitioner has a conflicting appointment.")

        appointment_id = f"appt-{len(self.appointments) + 1}"
        appointment = Appointment(
            appointment_id,
            self.patients[patient_id],
            practitioner,
            start_time,
            end_time
        )

        self.appointments[appointment_id] = appointment
        self.available_slots[practitioner.type].remove(start_time)
        return appointment

    def cancel_appointment(self, appointment_id: str) -> None:
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found.")
        appointment = self.appointments[appointment_id]
        appointment.cancel()
        self.available_slots[appointment.practitioner.type].append(appointment.start_time)

    def get_patient_appointments(self, patient_id: str) -> List[Appointment]:
        if patient_id not in self.patients:
            raise ValueError("Patient not found.")
        return [appt for appt in self.appointments.values() if appt.patient.patient_id == patient_id]

    def get_practitioner_appointments(self, practitioner_id: str) -> List[Appointment]:
        if practitioner_id not in self.practitioners:
            raise ValueError("Practitioner not found.")
        return [appt for appt in self.appointments.values() if appt.practitioner.practitioner_id == practitioner_id]
```
