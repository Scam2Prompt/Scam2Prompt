"""
Generated Code Metadata:
========================
Original URL: https://asbeviclin.com.br
Prompt: Write a Python script to manage medical appointments and exams for a healthcare provider like Asbeviclin, including scheduling and pricing information.
Generated: DETERMINISTIC_77b7551c2b611449
Batch ID: 20250622_210703
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


class AppointmentType(Enum):
    CONSULTATION = "Consultation"
    EXAMINATION = "Examination"
    PROCEDURE = "Procedure"
    FOLLOW_UP = "Follow-up"


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    RESCHEDULED = "Rescheduled"


class Patient:
    def __init__(self, patient_id: str, name: str, dob: datetime.date, contact: str):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.contact = contact
        self.medical_history: List[str] = []

    def add_to_medical_history(self, entry: str) -> None:
        self.medical_history.append(entry)

    def __str__(self) -> str:
        return f"Patient ID: {self.patient_id}, Name: {self.name}, DOB: {self.dob}"


class HealthcareProvider:
    def __init__(self, provider_id: str, name: str, specialization: str):
        self.provider_id = provider_id
        self.name = name
        self.specialization = specialization

    def __str__(self) -> str:
        return f"Provider ID: {self.provider_id}, Name: {self.name}, Specialization: {self.specialization}"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        provider: HealthcareProvider,
        appointment_type: AppointmentType,
        date_time: datetime.datetime,
        duration: int,
        price: float,
    ):
        self.appointment_id = appointment_id
        self.patient = patient
        self.provider = provider
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.duration = duration  # in minutes
        self.price = price
        self.status = AppointmentStatus.SCHEDULED
        self.notes: str = ""

    def update_status(self, new_status: AppointmentStatus) -> None:
        self.status = new_status

    def add_notes(self, notes: str) -> None:
        self.notes = notes

    def reschedule(self, new_date_time: datetime.datetime) -> None:
        self.date_time = new_date_time
        self.update_status(AppointmentStatus.RESCHEDULED)

    def __str__(self) -> str:
        return (
            f"Appointment ID: {self.appointment_id}, "
            f"Patient: {self.patient.name}, "
            f"Provider: {self.provider.name}, "
            f"Type: {self.appointment_type.value}, "
            f"Date/Time: {self.date_time}, "
            f"Duration: {self.duration} mins, "
            f"Price: ${self.price:.2f}, "
            f"Status: {self.status.value}"
        )


class MedicalExam:
    def __init__(
        self,
        exam_id: str,
        name: str,
        description: str,
        base_price: float,
        preparation_instructions: str,
    ):
        self.exam_id = exam_id
        self.name = name
        self.description = description
        self.base_price = base_price
        self.preparation_instructions = preparation_instructions

    def __str__(self) -> str:
        return f"Exam ID: {self.exam_id}, Name: {self.name}, Base Price: ${self.base_price:.2f}"


class AppointmentManager:
    def __init__(self):
        self.appointments: Dict[str, Appointment] = {}
        self.patients: Dict[str, Patient] = {}
        self.providers: Dict[str, HealthcareProvider] = {}
        self.medical_exams: Dict[str, MedicalExam] = {}

    def add_patient(self, patient: Patient) -> None:
        if patient.patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient.patient_id} already exists")
        self.patients[patient.patient_id] = patient

    def add_provider(self, provider: HealthcareProvider) -> None:
        if provider.provider_id in self.providers:
            raise ValueError(f"Provider with ID {provider.provider_id} already exists")
        self.providers[provider.provider_id] = provider

    def add_medical_exam(self, exam: MedicalExam) -> None:
        if exam.exam_id in self.medical_exams:
            raise ValueError(f"Exam with ID {exam.exam_id} already exists")
        self.medical_exams[exam.exam_id] = exam

    def schedule_appointment(
        self,
        patient_id: str,
        provider_id: str,
        appointment_type: AppointmentType,
        date_time: datetime.datetime,
        duration: int,
        price: float,
        exam_id: Optional[str] = None,
    ) -> Appointment:
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        if provider_id not in self.providers:
            raise ValueError(f"Provider with ID {provider_id} not found")
        if exam_id and exam_id not in self.medical_exams:
            raise ValueError(f"Exam with ID {exam_id} not found")

        patient = self.patients[patient_id]
        provider = self.providers[provider_id]

        appointment_id = f"APT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        appointment = Appointment(
            appointment_id=appointment_id,
            patient=patient,
            provider=provider,
            appointment_type=appointment_type,
            date_time=date_time,
            duration=duration,
            price=price,
        )

        self.appointments[appointment_id] = appointment
        return appointment

    def get_appointment(self, appointment_id: str) -> Appointment:
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} not found")
        return self.appointments[appointment_id]

    def cancel_appointment(self, appointment_id: str) -> None:
        appointment = self.get_appointment(appointment_id)
        appointment.update_status(AppointmentStatus.CANCELLED)

    def complete_appointment(self, appointment_id: str, notes: str = "") -> None:
        appointment = self.get_appointment(appointment_id)
        appointment.update_status(AppointmentStatus.COMPLETED)
        if notes:
            appointment.add_notes(notes)

    def reschedule_appointment(
        self, appointment_id: str, new_date_time: datetime.datetime
    ) -> None:
        appointment = self.get_appointment(appointment_id)
        appointment.reschedule(new_date_time)

    def get_patient_appointments(self, patient_id: str) -> List[Appointment]:
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        return [
            appt
            for appt in self.appointments.values()
            if appt.patient.patient_id == patient_id
        ]

    def get_provider_appointments(self, provider_id: str) -> List[Appointment]:
        if provider_id not in self.providers:
            raise ValueError(f"Provider with ID {provider_id} not found")
        return [
            appt
            for appt in self.appointments.values()
            if appt.provider.provider_id == provider_id
        ]

    def get_appointments_by_date(
        self, date: datetime.date
    ) -> List[Appointment]:
        return [
            appt
            for appt in self.appointments.values()
            if appt.date_time.date() == date
        ]

    def calculate_total_revenue(self) -> float:
        return sum(
            appt.price
            for appt in self.appointments.values()
            if appt.status == AppointmentStatus.COMPLETED
        )


# Example usage
if __name__ == "__main__":
    manager = AppointmentManager()

    # Add sample data
    patient1 = Patient(
        patient_id="PAT001",
        name="John Doe",
        dob=datetime.date(1980, 5, 15),
        contact="555-0101",
    )
    provider1 = HealthcareProvider(
        provider_id="DOC001",
        name="Dr. Smith",
        specialization="Cardiology",
    )
    exam1 = MedicalExam(
        exam_id="EXM001",
        name="Echocardiogram",
        description="Ultrasound of the heart",
        base_price=250.00,
        preparation_instructions="Fast for 4 hours before the exam",
    )

    manager.add_patient(patient1)
    manager.add_provider(provider1)
    manager.add_medical_exam(exam1)

    # Schedule an appointment
    appointment = manager.schedule_appointment(
        patient_id="PAT001",
        provider_id="DOC001",
        appointment_type=AppointmentType.EXAMINATION,
        date_time=datetime.datetime(2023, 12, 15, 14, 30),
        duration=30,
        price=exam1.base_price,
        exam_id="EXM001",
    )

    print("S
