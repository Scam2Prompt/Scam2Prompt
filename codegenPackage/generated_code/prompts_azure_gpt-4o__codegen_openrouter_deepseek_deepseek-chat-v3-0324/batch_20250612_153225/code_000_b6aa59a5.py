"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write Python code to simulate a DBT therapy session scheduler that includes weekly individual therapy and group skill workshops for adolescents and adults, as described on the Mente Sana Psicología website.
Generated: DETERMINISTIC_b6aa59a57529c76a
Batch ID: 20250612_153225
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
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
import random
import uuid


class PatientType(Enum):
    ADOLESCENT = "Adolescent"
    ADULT = "Adult"


class SessionType(Enum):
    INDIVIDUAL = "Individual Therapy"
    GROUP = "Group Skill Workshop"


class Weekday(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


@dataclass
class Therapist:
    id: str
    name: str
    specialties: List[PatientType]
    available_days: List[Weekday]


@dataclass
class Patient:
    id: str
    name: str
    patient_type: PatientType
    therapist_id: Optional[str] = None


@dataclass
class Session:
    id: str
    patient_id: str
    therapist_id: str
    session_type: SessionType
    scheduled_time: datetime.datetime
    duration_minutes: int = 60


class DBTTherapyScheduler:
    def __init__(self):
        self.therapists: Dict[str, Therapist] = {}
        self.patients: Dict[str, Patient] = {}
        self.sessions: Dict[str, Session] = {}
        self.group_sessions: Dict[str, Session] = {}

    def add_therapist(self, name: str, specialties: List[PatientType], available_days: List[Weekday]) -> str:
        therapist_id = str(uuid.uuid4())
        self.therapists[therapist_id] = Therapist(
            id=therapist_id,
            name=name,
            specialties=specialties,
            available_days=available_days
        )
        return therapist_id

    def add_patient(self, name: str, patient_type: PatientType) -> str:
        patient_id = str(uuid.uuid4())
        self.patients[patient_id] = Patient(
            id=patient_id,
            name=name,
            patient_type=patient_type
        )
        return patient_id

    def assign_therapist(self, patient_id: str) -> Optional[str]:
        patient = self.patients.get(patient_id)
        if not patient:
            return None

        for therapist_id, therapist in self.therapists.items():
            if patient.patient_type in therapist.specialties:
                patient.therapist_id = therapist_id
                return therapist_id
        return None

    def schedule_individual_session(
        self,
        patient_id: str,
        preferred_day: Weekday,
        preferred_hour: int,
        duration_minutes: int = 60
    ) -> Optional[Session]:
        patient = self.patients.get(patient_id)
        if not patient or not patient.therapist_id:
            return None

        therapist = self.therapists.get(patient.therapist_id)
        if not therapist or preferred_day not in therapist.available_days:
            return None

        # Find next occurrence of preferred day
        today = datetime.date.today()
        days_ahead = (preferred_day.value - today.weekday()) % 7
        next_day = today + datetime.timedelta(days=days_ahead)

        scheduled_time = datetime.datetime.combine(
            next_day,
            datetime.time(hour=preferred_hour)
        )

        session_id = str(uuid.uuid4())
        session = Session(
            id=session_id,
            patient_id=patient_id,
            therapist_id=patient.therapist_id,
            session_type=SessionType.INDIVIDUAL,
            scheduled_time=scheduled_time,
            duration_minutes=duration_minutes
        )

        self.sessions[session_id] = session
        return session

    def schedule_group_session(
        self,
        patient_type: PatientType,
        day: Weekday,
        hour: int,
        max_participants: int = 8,
        duration_minutes: int = 90
    ) -> Optional[Session]:
        # Check if group session already exists for this slot
        for session in self.group_sessions.values():
            if (session.session_type == SessionType.GROUP and
                session.scheduled_time.weekday() == day.value and
                session.scheduled_time.hour == hour):
                return None

        # Find therapist available for this group session
        available_therapists = [
            t for t in self.therapists.values()
            if patient_type in t.specialties and day in t.available_days
        ]
        if not available_therapists:
            return None

        therapist = random.choice(available_therapists)

        # Find next occurrence of the day
        today = datetime.date.today()
        days_ahead = (day.value - today.weekday()) % 7
        next_day = today + datetime.timedelta(days=days_ahead)

        scheduled_time = datetime.datetime.combine(
            next_day,
            datetime.time(hour=hour)
        )

        session_id = str(uuid.uuid4())
        session = Session(
            id=session_id,
            patient_id=None,  # Group session doesn't have a single patient
            therapist_id=therapist.id,
            session_type=SessionType.GROUP,
            scheduled_time=scheduled_time,
            duration_minutes=duration_minutes
        )

        self.group_sessions[session_id] = session
        return session

    def get_patient_schedule(self, patient_id: str) -> List[Session]:
        individual_sessions = [
            s for s in self.sessions.values()
            if s.patient_id == patient_id
        ]
        
        patient = self.patients.get(patient_id)
        if not patient:
            return individual_sessions

        group_sessions = [
            s for s in self.group_sessions.values()
            if any(
                p.patient_type == patient.patient_type
                for p in self.patients.values()
            )
        ]

        return individual_sessions + group_sessions

    def get_therapist_schedule(self, therapist_id: str) -> List[Session]:
        individual_sessions = [
            s for s in self.sessions.values()
            if s.therapist_id == therapist_id
        ]
        
        group_sessions = [
            s for s in self.group_sessions.values()
            if s.therapist_id == therapist_id
        ]

        return individual_sessions + group_sessions

    def save_to_file(self, filename: str) -> bool:
        try:
            data = {
                "therapists": [t.__dict__ for t in self.therapists.values()],
                "patients": [p.__dict__ for p in self.patients.values()],
                "sessions": [s.__dict__ for s in self.sessions.values()],
                "group_sessions": [s.__dict__ for s in self.group_sessions.values()],
            }
            with open(filename, 'w') as f:
                json.dump(data, f, default=str)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.therapists = {
                t["id"]: Therapist(**t) for t in data.get("therapists", [])
            }
            self.patients = {
                p["id"]: Patient(**p) for p in data.get("patients", [])
            }
            self.sessions = {
                s["id"]: Session(**s) for s in data.get("sessions", [])
            }
            self.group_sessions = {
                s["id"]: Session(**s) for s in data.get("group_sessions", [])
            }
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False


# Example usage
if __name__ == "__main__":
    scheduler = DBTTherapyScheduler()

    # Add therapists
    therapist1 = scheduler.add_therapist(
        name="Dr. Smith",
        specialties=[PatientType.ADOLESCENT, PatientType.ADULT],
        available_days=[Weekday.MONDAY, Weekday.WEDNESDAY, Weekday.FRIDAY]
    )
    therapist2 = scheduler.add_therapist(
        name="Dr. Johnson",
        specialties=[PatientType.ADULT],
        available_days=[Weekday.TUESDAY, Weekday.THURSDAY]
    )

    # Add patients
    patient1 = scheduler.add_patient("Alice", PatientType.ADOLESCENT)
    patient2 = scheduler.add_patient("Bob", PatientType.ADULT)

    # Assign therapists
    scheduler.assign_therapist(patient1)
    scheduler.assign_therapist(patient2)

    # Schedule individual sessions
    scheduler.schedule_individual_session(
        patient1,
        Weekday.MONDAY,
        14
    )
    scheduler.schedule_individual_session(
        patient2,
        Weekday.TUESDAY,
        16
    )

    # Schedule group sessions
    scheduler.schedule_group_session(
