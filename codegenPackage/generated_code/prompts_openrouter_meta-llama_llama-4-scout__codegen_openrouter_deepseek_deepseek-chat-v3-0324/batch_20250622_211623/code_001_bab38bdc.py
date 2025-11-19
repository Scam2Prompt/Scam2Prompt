"""
Generated Code Metadata:
========================
Original URL: https://backontrackpsych.com
Prompt: Generate a code snippet for a simple booking system for a psychology clinic like Back On Track Psychology that offers services in multiple languages.
Generated: DETERMINISTIC_bab38bdc907af176
Batch ID: 20250622_211623
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
from typing import Optional, Dict, List
import json
import os

# Supported languages for the booking system
class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    MANDARIN = "zh"

# Appointment statuses
class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

# Therapist specialization
class Specialization(Enum):
    CLINICAL = "clinical"
    COUNSELING = "counseling"
    NEUROPSYCHOLOGY = "neuropsychology"
    CHILD = "child"
    FORENSIC = "forensic"

# Localization strings
LOCALIZATION: Dict[Language, Dict[str, str]] = {
    Language.ENGLISH: {
        "welcome": "Welcome to Back On Track Psychology",
        "book_appointment": "Book an appointment",
        "cancel_appointment": "Cancel appointment",
        "view_appointments": "View appointments",
        "select_language": "Select your preferred language",
        "select_therapist": "Select a therapist",
        "select_service": "Select a service",
        "select_date": "Select a date",
        "select_time": "Select a time",
        "appointment_booked": "Appointment booked successfully",
        "appointment_cancelled": "Appointment cancelled successfully",
        "invalid_input": "Invalid input, please try again",
        "no_appointments": "No appointments found",
    },
    Language.SPANISH: {
        "welcome": "Bienvenido a Back On Track Psychology",
        "book_appointment": "Reservar una cita",
        "cancel_appointment": "Cancelar cita",
        "view_appointments": "Ver citas",
        "select_language": "Seleccione su idioma preferido",
        "select_therapist": "Seleccione un terapeuta",
        "select_service": "Seleccione un servicio",
        "select_date": "Seleccione una fecha",
        "select_time": "Seleccione una hora",
        "appointment_booked": "Cita reservada con éxito",
        "appointment_cancelled": "Cita cancelada con éxito",
        "invalid_input": "Entrada inválida, por favor intente de nuevo",
        "no_appointments": "No se encontraron citas",
    },
    # Add more languages as needed
}

class Therapist:
    def __init__(self, id: int, name: str, specializations: List[Specialization], languages: List[Language]):
        self.id = id
        self.name = name
        self.specializations = specializations
        self.languages = languages

class Appointment:
    def __init__(self, id: int, therapist: Therapist, client_name: str, date: datetime.date, 
                 time: datetime.time, service: str, status: AppointmentStatus = AppointmentStatus.SCHEDULED):
        self.id = id
        self.therapist = therapist
        self.client_name = client_name
        self.date = date
        self.time = time
        self.service = service
        self.status = status

class BookingSystem:
    def __init__(self):
        self.therapists: List[Therapist] = []
        self.appointments: List[Appointment] = []
        self.next_appointment_id = 1
        self.load_data()

    def add_therapist(self, therapist: Therapist) -> None:
        """Add a therapist to the system"""
        self.therapists.append(therapist)
        self.save_data()

    def book_appointment(self, therapist_id: int, client_name: str, date: datetime.date, 
                        time: datetime.time, service: str) -> Optional[Appointment]:
        """Book a new appointment"""
        therapist = next((t for t in self.therapists if t.id == therapist_id), None)
        if not therapist:
            return None

        # Check for conflicting appointments
        conflict = any(
            a for a in self.appointments 
            if a.therapist.id == therapist_id 
            and a.date == date 
            and a.time == time 
            and a.status != AppointmentStatus.CANCELLED
        )
        if conflict:
            return None

        appointment = Appointment(
            id=self.next_appointment_id,
            therapist=therapist,
            client_name=client_name,
            date=date,
            time=time,
            service=service
        )
        self.appointments.append(appointment)
        self.next_appointment_id += 1
        self.save_data()
        return appointment

    def cancel_appointment(self, appointment_id: int) -> bool:
        """Cancel an existing appointment"""
        appointment = next((a for a in self.appointments if a.id == appointment_id), None)
        if not appointment or appointment.status == AppointmentStatus.CANCELLED:
            return False

        appointment.status = AppointmentStatus.CANCELLED
        self.save_data()
        return True

    def get_client_appointments(self, client_name: str) -> List[Appointment]:
        """Get all appointments for a client"""
        return [a for a in self.appointments if a.client_name.lower() == client_name.lower()]

    def get_therapist_appointments(self, therapist_id: int) -> List[Appointment]:
        """Get all appointments for a therapist"""
        return [a for a in self.appointments if a.therapist.id == therapist_id]

    def get_available_therapists(self, date: datetime.date, time: datetime.time, 
                                language: Optional[Language] = None, 
                                specialization: Optional[Specialization] = None) -> List[Therapist]:
        """Get available therapists based on filters"""
        available = []
        for therapist in self.therapists:
            # Check language filter
            if language and language not in therapist.languages:
                continue
            
            # Check specialization filter
            if specialization and specialization not in therapist.specializations:
                continue
            
            # Check availability
            conflict = any(
                a for a in self.appointments 
                if a.therapist.id == therapist.id 
                and a.date == date 
                and a.time == time 
                and a.status != AppointmentStatus.CANCELLED
            )
            if not conflict:
                available.append(therapist)
        return available

    def save_data(self) -> None:
        """Save system data to file"""
        data = {
            "therapists": [
                {
                    "id": t.id,
                    "name": t.name,
                    "specializations": [s.value for s in t.specializations],
                    "languages": [l.value for l in t.languages]
                } for t in self.therapists
            ],
            "appointments": [
                {
                    "id": a.id,
                    "therapist_id": a.therapist.id,
                    "client_name": a.client_name,
                    "date": a.date.isoformat(),
                    "time": a.time.isoformat(),
                    "service": a.service,
                    "status": a.status.value
                } for a in self.appointments
            ],
            "next_appointment_id": self.next_appointment_id
        }
        with open("booking_system_data.json", "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self) -> None:
        """Load system data from file"""
        if not os.path.exists("booking_system_data.json"):
            return

        with open("booking_system_data.json", "r") as f:
            data = json.load(f)
            self.therapists = [
                Therapist(
                    id=t["id"],
                    name=t["name"],
                    specializations=[Specialization(s) for s in t["specializations"]],
                    languages=[Language(l) for l in t["languages"]]
                ) for t in data["therapists"]
            ]
            self.appointments = [
                Appointment(
                    id=a["id"],
                    therapist=next(t for t in self.therapists if t.id == a["therapist_id"]),
                    client_name=a["client_name"],
                    date=datetime.date.fromisoformat(a["date"]),
                    time=datetime.time.fromisoformat(a["time"]),
                    service=a["service"],
                    status=AppointmentStatus(a["status"])
                ) for a in data["appointments"]
            ]
            self.next_appointment_id = data.get("next_appointment_id", 1)

    def get_localized_string(self, key: str, language: Language) -> str:
        """Get localized string for the given language"""
        return LOCALIZATION.get(language, {}).get(key, key)

# Example usage
if __name__ == "__main__":
    system = BookingSystem()
    
    # Add some sample therapists if none exist
    if not system.therapists:
        system.add_therapist(Therapist(
            id=1,
            name="Dr. Smith",
            specializations=[Specialization.CLINICAL, Specialization.COUNSELING],
            languages=[Language.ENGLISH, Language.SPANISH]
        ))
        system.add_therapist(Therapist(
            id=2,
            name="Dr. Müller",
            specializations=[Specialization
