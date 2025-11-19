"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Write Python code to simulate a scheduling system for medical exams like colonoscopy, endoscopy, and elastography, including options for selecting dates, times, and specialties such as gastroenterology and hepatology.
Generated: DETERMINISTIC_8cb1cd011b51504b
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple


class ExamType(Enum):
    COLONOSCOPY = "Colonoscopy"
    ENDOSCOPY = "Endoscopy"
    ELASTOGRAPHY = "Elastography"


class Specialty(Enum):
    GASTROENTEROLOGY = "Gastroenterology"
    HEPATOLOGY = "Hepatology"


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Doctor:
    def __init__(self, id: int, name: str, specialty: Specialty):
        self.id = id
        self.name = name
        self.specialty = specialty


class Patient:
    def __init__(self, id: int, name: str, date_of_birth: datetime.date):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth


class Appointment:
    def __init__(
        self,
        id: int,
        patient: Patient,
        doctor: Doctor,
        exam_type: ExamType,
        scheduled_time: datetime.datetime,
        status: AppointmentStatus = AppointmentStatus.SCHEDULED,
    ):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.exam_type = exam_type
        self.scheduled_time = scheduled_time
        self.status = status

    def cancel(self):
        self.status = AppointmentStatus.CANCELLED

    def complete(self):
        self.status = AppointmentStatus.COMPLETED


class MedicalExamScheduler:
    def __init__(self):
        self.doctors: List[Doctor] = []
        self.patients: List[Patient] = []
        self.appointments: List[Appointment] = []
        self.available_slots: Dict[Tuple[datetime.date, Specialty], List[datetime.time]] = {}

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def _validate_specialty(self, specialty: Specialty, exam_type: ExamType) -> bool:
        if specialty == Specialty.GASTROENTEROLOGY:
            return exam_type in [ExamType.COLONOSCOPY, ExamType.ENDOSCOPY]
        elif specialty == Specialty.HEPATOLOGY:
            return exam_type == ExamType.ELASTOGRAPHY
        return False

    def add_available_slot(
        self, date: datetime.date, time: datetime.time, specialty: Specialty
    ):
        key = (date, specialty)
        if key not in self.available_slots:
            self.available_slots[key] = []
        if time not in self.available_slots[key]:
            self.available_slots[key].append(time)

    def get_available_slots(
        self, date: datetime.date, specialty: Specialty
    ) -> List[datetime.time]:
        return self.available_slots.get((date, specialty), [])

    def schedule_appointment(
        self,
        patient_id: int,
        doctor_id: int,
        exam_type: ExamType,
        date: datetime.date,
        time: datetime.time,
    ) -> Optional[Appointment]:
        try:
            patient = next(p for p in self.patients if p.id == patient_id)
            doctor = next(d for d in self.doctors if d.id == doctor_id)

            if not self._validate_specialty(doctor.specialty, exam_type):
                raise ValueError("Doctor specialty does not match exam type")

            available_slots = self.get_available_slots(date, doctor.specialty)
            if time not in available_slots:
                raise ValueError("Requested time slot is not available")

            scheduled_time = datetime.datetime.combine(date, time)
            appointment_id = len(self.appointments) + 1
            appointment = Appointment(
                appointment_id, patient, doctor, exam_type, scheduled_time
            )

            self.appointments.append(appointment)
            self.available_slots[(date, doctor.specialty)].remove(time)

            return appointment
        except StopIteration:
            print("Patient or doctor not found")
            return None
        except ValueError as e:
            print(f"Error scheduling appointment: {e}")
            return None

    def cancel_appointment(self, appointment_id: int) -> bool:
        try:
            appointment = next(a for a in self.appointments if a.id == appointment_id)
            appointment.cancel()

            date = appointment.scheduled_time.date()
            time = appointment.scheduled_time.time()
            specialty = appointment.doctor.specialty

            self.add_available_slot(date, time, specialty)
            return True
        except StopIteration:
            print("Appointment not found")
            return False

    def complete_appointment(self, appointment_id: int) -> bool:
        try:
            appointment = next(a for a in self.appointments if a.id == appointment_id)
            appointment.complete()
            return True
        except StopIteration:
            print("Appointment not found")
            return False

    def get_appointments_by_patient(self, patient_id: int) -> List[Appointment]:
        return [a for a in self.appointments if a.patient.id == patient_id]

    def get_appointments_by_doctor(self, doctor_id: int) -> List[Appointment]:
        return [a for a in self.appointments if a.doctor.id == doctor_id]


# Example usage
if __name__ == "__main__":
    scheduler = MedicalExamScheduler()

    # Add doctors
    doc1 = Doctor(1, "Dr. Smith", Specialty.GASTROENTEROLOGY)
    doc2 = Doctor(2, "Dr. Johnson", Specialty.HEPATOLOGY)
    scheduler.add_doctor(doc1)
    scheduler.add_doctor(doc2)

    # Add patients
    patient1 = Patient(1, "John Doe", datetime.date(1980, 5, 15))
    patient2 = Patient(2, "Jane Smith", datetime.date(1975, 8, 22))
    scheduler.add_patient(patient1)
    scheduler.add_patient(patient2)

    # Add available slots
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    scheduler.add_available_slot(today, datetime.time(9, 0), Specialty.GASTROENTEROLOGY)
    scheduler.add_available_slot(today, datetime.time(10, 0), Specialty.GASTROENTEROLOGY)
    scheduler.add_available_slot(tomorrow, datetime.time(11, 0), Specialty.HEPATOLOGY)

    # Schedule appointments
    appointment1 = scheduler.schedule_appointment(
        1, 1, ExamType.COLONOSCOPY, today, datetime.time(9, 0)
    )
    appointment2 = scheduler.schedule_appointment(
        2, 2, ExamType.ELASTOGRAPHY, tomorrow, datetime.time(11, 0)
    )

    # Print appointments
    print(f"Patient 1 appointments: {[a.id for a in scheduler.get_appointments_by_patient(1)]}")
    print(f"Doctor 1 appointments: {[a.id for a in scheduler.get_appointments_by_doctor(1)]}")

    # Cancel an appointment
    if appointment1:
        scheduler.cancel_appointment(appointment1.id)
        print(f"Appointment {appointment1.id} cancelled")

    # Complete an appointment
    if appointment2:
        scheduler.complete_appointment(appointment2.id)
        print(f"Appointment {appointment2.id} completed")
```
