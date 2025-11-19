"""
Generated Code Metadata:
========================
Original URL: https://idetgroup.com
Prompt: Illustrate how to implement a patient management system that includes features for telemedicine and home visits, drawing from the services provided by Grupo Clínico IDET.
Generated: DETERMINISTIC_1c312dae4b1991e8
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Patient Management System with Telemedicine and Home Visit Features
Inspired by Grupo Clínico IDET services
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import uuid
import json
from enum import Enum, auto


class AppointmentType(Enum):
    IN_PERSON = auto()
    TELEMEDICINE = auto()
    HOME_VISIT = auto()


class PatientStatus(Enum):
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()


class VisitStatus(Enum):
    SCHEDULED = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    IN_PROGRESS = auto()


class Patient:
    def __init__(
        self,
        patient_id: str,
        first_name: str,
        last_name: str,
        dob: str,
        phone: str,
        email: str,
        address: str,
        status: PatientStatus = PatientStatus.PENDING,
    ):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.phone = phone
        self.email = email
        self.address = address
        self.status = status
        self.medical_history = []
        self.appointments = []

    def add_medical_record(self, record: Dict):
        """Add a medical record to patient's history"""
        self.medical_history.append(record)

    def schedule_appointment(self, appointment: "Appointment"):
        """Schedule an appointment for the patient"""
        self.appointments.append(appointment)

    def update_status(self, new_status: PatientStatus):
        """Update patient status"""
        self.status = new_status

    def to_dict(self):
        """Convert patient data to dictionary"""
        return {
            "patient_id": self.patient_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "status": self.status.name,
            "medical_history": self.medical_history,
            "appointments": [appt.to_dict() for appt in self.appointments],
        }


class Doctor:
    def __init__(self, doctor_id: str, name: str, specialty: str, license_number: str):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.license_number = license_number
        self.availability = []

    def add_availability(self, start_time: datetime, end_time: datetime):
        """Add availability slot for the doctor"""
        self.availability.append({"start": start_time, "end": end_time})

    def is_available(self, start_time: datetime, end_time: datetime) -> bool:
        """Check if doctor is available during specified time"""
        for slot in self.availability:
            if slot["start"] <= start_time and slot["end"] >= end_time:
                return True
        return False

    def to_dict(self):
        """Convert doctor data to dictionary"""
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialty": self.specialty,
            "license_number": self.license_number,
            "availability": [
                {"start": slot["start"].isoformat(), "end": slot["end"].isoformat()}
                for slot in self.availability
            ],
        }


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        doctor: Doctor,
        appointment_type: AppointmentType,
        scheduled_time: datetime,
        duration: int = 30,
        status: VisitStatus = VisitStatus.SCHEDULED,
        notes: str = "",
    ):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_type = appointment_type
        self.scheduled_time = scheduled_time
        self.duration = duration
        self.end_time = scheduled_time + timedelta(minutes=duration)
        self.status = status
        self.notes = notes

    def update_status(self, new_status: VisitStatus):
        """Update appointment status"""
        self.status = new_status

    def add_notes(self, notes: str):
        """Add notes to the appointment"""
        self.notes = notes

    def to_dict(self):
        """Convert appointment data to dictionary"""
        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient.patient_id,
            "doctor_id": self.doctor.doctor_id,
            "appointment_type": self.appointment_type.name,
            "scheduled_time": self.scheduled_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "duration": self.duration,
            "status": self.status.name,
            "notes": self.notes,
        }


class TelemedicineSession:
    def __init__(
        self,
        session_id: str,
        appointment: Appointment,
        video_url: str,
        start_time: datetime,
    ):
        self.session_id = session_id
        self.appointment = appointment
        self.video_url = video_url
        self.start_time = start_time
        self.end_time = None
        self.recording_url = None

    def end_session(self, end_time: datetime, recording_url: str = None):
        """End the telemedicine session"""
        self.end_time = end_time
        self.recording_url = recording_url
        self.appointment.update_status(VisitStatus.COMPLETED)

    def to_dict(self):
        """Convert telemedicine session data to dictionary"""
        return {
            "session_id": self.session_id,
            "appointment_id": self.appointment.appointment_id,
            "video_url": self.video_url,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "recording_url": self.recording_url,
        }


class HomeVisit:
    def __init__(
        self,
        visit_id: str,
        appointment: Appointment,
        assigned_nurse: str,
        estimated_arrival: datetime,
    ):
        self.visit_id = visit_id
        self.appointment = appointment
        self.assigned_nurse = assigned_nurse
        self.estimated_arrival = estimated_arrival
        self.actual_arrival = None
        self.departure = None
        self.visit_notes = ""

    def record_arrival(self, arrival_time: datetime):
        """Record actual arrival time"""
        self.actual_arrival = arrival_time
        self.appointment.update_status(VisitStatus.IN_PROGRESS)

    def record_departure(self, departure_time: datetime, notes: str):
        """Record departure time and visit notes"""
        self.departure = departure_time
        self.visit_notes = notes
        self.appointment.update_status(VisitStatus.COMPLETED)

    def to_dict(self):
        """Convert home visit data to dictionary"""
        return {
            "visit_id": self.visit_id,
            "appointment_id": self.appointment.appointment_id,
            "assigned_nurse": self.assigned_nurse,
            "estimated_arrival": self.estimated_arrival.isoformat(),
            "actual_arrival": self.actual_arrival.isoformat()
            if self.actual_arrival
            else None,
            "departure": self.departure.isoformat() if self.departure else None,
            "visit_notes": self.visit_notes,
        }


class PatientManagementSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        self.telemedicine_sessions = {}
        self.home_visits = {}

    def add_patient(self, patient: Patient):
        """Add a new patient to the system"""
        if patient.patient_id in self.patients:
            raise ValueError("Patient ID already exists")
        self.patients[patient.patient_id] = patient

    def add_doctor(self, doctor: Doctor):
        """Add a new doctor to the system"""
        if doctor.doctor_id in self.doctors:
            raise ValueError("Doctor ID already exists")
        self.doctors[doctor.doctor_id] = doctor

    def schedule_appointment(
        self,
        patient_id: str,
        doctor_id: str,
        appointment_type: AppointmentType,
        scheduled_time: datetime,
        duration: int = 30,
    ) -> Appointment:
        """Schedule a new appointment"""
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        if doctor_id not in self.doctors:
            raise ValueError("Doctor not found")

        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]

        if not doctor.is_available(
            scheduled_time, scheduled_time + timedelta(minutes=duration)
        ):
            raise ValueError("Doctor not available at requested time")

        appointment_id = str(uuid.uuid4())
        appointment = Appointment(
            appointment_id=appointment_id,
            patient=patient,
            doctor=doctor,
            appointment_type=appointment
