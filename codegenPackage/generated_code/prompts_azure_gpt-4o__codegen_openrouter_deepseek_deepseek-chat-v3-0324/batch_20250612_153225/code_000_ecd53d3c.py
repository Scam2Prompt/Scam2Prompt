"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Write Python code to implement a teleconsultation scheduling system for a speech-language pathology clinic, incorporating features like user authentication and appointment management, inspired by the services offered by Open Minds Instituto.
Generated: DETERMINISTIC_ecd53d3c428f9cea
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
import uuid
from typing import Optional, List, Dict
from enum import Enum
import hashlib
import secrets
import json
import os

# Database simulation using JSON files
DB_FILE = "database.json"

class UserType(Enum):
    ADMIN = "admin"
    THERAPIST = "therapist"
    PATIENT = "patient"

class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class User:
    def __init__(self, username: str, password_hash: str, salt: str, user_type: UserType, full_name: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.password_hash = password_hash
        self.salt = salt
        self.user_type = user_type
        self.full_name = full_name
        self.email = email

    def to_dict(self) -> Dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password_hash": self.password_hash,
            "salt": self.salt,
            "user_type": self.user_type.value,
            "full_name": self.full_name,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        return cls(
            username=data["username"],
            password_hash=data["password_hash"],
            salt=data["salt"],
            user_type=UserType(data["user_type"]),
            full_name=data["full_name"],
            email=data["email"]
        )

class Appointment:
    def __init__(self, patient_id: str, therapist_id: str, date_time: datetime.datetime, duration_minutes: int, status: AppointmentStatus):
        self.appointment_id = str(uuid.uuid4())
        self.patient_id = patient_id
        self.therapist_id = therapist_id
        self.date_time = date_time
        self.duration_minutes = duration_minutes
        self.status = status

    def to_dict(self) -> Dict:
        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient_id,
            "therapist_id": self.therapist_id,
            "date_time": self.date_time.isoformat(),
            "duration_minutes": self.duration_minutes,
            "status": self.status.value
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Appointment':
        return cls(
            patient_id=data["patient_id"],
            therapist_id=data["therapist_id"],
            date_time=datetime.datetime.fromisoformat(data["date_time"]),
            duration_minutes=data["duration_minutes"],
            status=AppointmentStatus(data["status"])
        )

class Database:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r") as f:
                data = json.load(f)
                self.users = {user_id: User.from_dict(user_data) for user_id, user_data in data.get("users", {}).items()}
                self.appointments = {appt_id: Appointment.from_dict(appt_data) for appt_id, appt_data in data.get("appointments", {}).items()}

    def save_data(self):
        data = {
            "users": {user_id: user.to_dict() for user_id, user in self.users.items()},
            "appointments": {appt_id: appt.to_dict() for appt_id, appt in self.appointments.items()}
        }
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def add_user(self, user: User) -> None:
        self.users[user.user_id] = user
        self.save_data()

    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        for user in self.users.values():
            if user.username == username:
                return user
        return None

    def add_appointment(self, appointment: Appointment) -> None:
        self.appointments[appointment.appointment_id] = appointment
        self.save_data()

    def get_appointment(self, appointment_id: str) -> Optional[Appointment]:
        return self.appointments.get(appointment_id)

    def get_appointments_for_user(self, user_id: str, user_type: UserType) -> List[Appointment]:
        if user_type == UserType.PATIENT:
            return [appt for appt in self.appointments.values() if appt.patient_id == user_id]
        elif user_type == UserType.THERAPIST:
            return [appt for appt in self.appointments.values() if appt.therapist_id == user_id]
        return []

    def update_appointment_status(self, appointment_id: str, status: AppointmentStatus) -> bool:
        if appointment_id in self.appointments:
            self.appointments[appointment_id].status = status
            self.save_data()
            return True
        return False

class AuthService:
    def __init__(self, db: Database):
        self.db = db

    @staticmethod
    def hash_password(password: str, salt: str) -> str:
        return hashlib.sha256((password + salt).encode()).hexdigest()

    def register_user(self, username: str, password: str, user_type: UserType, full_name: str, email: str) -> Optional[User]:
        if self.db.get_user_by_username(username):
            return None
        
        salt = secrets.token_hex(16)
        password_hash = self.hash_password(password, salt)
        user = User(username, password_hash, salt, user_type, full_name, email)
        self.db.add_user(user)
        return user

    def login(self, username: str, password: str) -> Optional[User]:
        user = self.db.get_user_by_username(username)
        if user and user.password_hash == self.hash_password(password, user.salt):
            return user
        return None

class AppointmentService:
    def __init__(self, db: Database):
        self.db = db

    def schedule_appointment(self, patient_id: str, therapist_id: str, date_time: datetime.datetime, duration_minutes: int) -> Optional[Appointment]:
        # Check if therapist exists
        therapist = self.db.get_user(therapist_id)
        if not therapist or therapist.user_type != UserType.THERAPIST:
            return None
        
        # Check if patient exists
        patient = self.db.get_user(patient_id)
        if not patient or patient.user_type != UserType.PATIENT:
            return None
        
        # Check for scheduling conflicts
        therapist_appointments = self.db.get_appointments_for_user(therapist_id, UserType.THERAPIST)
        end_time = date_time + datetime.timedelta(minutes=duration_minutes)
        
        for appt in therapist_appointments:
            appt_end = appt.date_time + datetime.timedelta(minutes=appt.duration_minutes)
            if (date_time < appt_end) and (end_time > appt.date_time):
                return None
        
        appointment = Appointment(patient_id, therapist_id, date_time, duration_minutes, AppointmentStatus.SCHEDULED)
        self.db.add_appointment(appointment)
        return appointment

    def cancel_appointment(self, appointment_id: str, user_id: str) -> bool:
        appointment = self.db.get_appointment(appointment_id)
        if not appointment:
            return False
        
        if appointment.patient_id !=
