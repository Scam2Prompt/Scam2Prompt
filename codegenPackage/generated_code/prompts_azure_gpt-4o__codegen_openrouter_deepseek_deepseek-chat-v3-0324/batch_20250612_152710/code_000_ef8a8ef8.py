"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Write Python code to create an appointment scheduling system for a dental clinic with multiple locations, incorporating features like patient details, preferred dates, and services (e.g., pediatric dentistry, orthodontics, cosmetic dentistry).
Generated: DETERMINISTIC_ef8a8ef8906e5cc7
Batch ID: 20250612_152710
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
import uuid
import json
import os


class ServiceType(Enum):
    """Enum representing different dental services."""
    GENERAL = "General Dentistry"
    PEDIATRIC = "Pediatric Dentistry"
    ORTHODONTICS = "Orthodontics"
    COSMETIC = "Cosmetic Dentistry"
    PERIODONTICS = "Periodontics"
    ENDODONTICS = "Endodontics"


class Location:
    """Class representing a dental clinic location."""
    
    def __init__(self, name: str, address: str, phone: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.phone = phone
    
    def to_dict(self) -> Dict:
        """Convert location data to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Location':
        """Create Location instance from dictionary."""
        location = cls(data["name"], data["address"], data["phone"])
        location.id = data["id"]
        return location


class Patient:
    """Class representing a patient."""
    
    def __init__(self, first_name: str, last_name: str, email: str, phone: str, dob: str):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.dob = dob
        self.medical_history: List[str] = []
    
    def to_dict(self) -> Dict:
        """Convert patient data to dictionary."""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "dob": self.dob,
            "medical_history": self.medical_history
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Patient':
        """Create Patient instance from dictionary."""
        patient = cls(
            data["first_name"],
            data["last_name"],
            data["email"],
            data["phone"],
            data["dob"]
        )
        patient.id = data["id"]
        patient.medical_history = data.get("medical_history", [])
        return patient


class Appointment:
    """Class representing an appointment."""
    
    def __init__(
        self,
        patient_id: str,
        location_id: str,
        service_type: ServiceType,
        preferred_date: datetime.datetime,
        duration: int = 30
    ):
        self.id = str(uuid.uuid4())
        self.patient_id = patient_id
        self.location_id = location_id
        self.service_type = service_type
        self.preferred_date = preferred_date
        self.confirmed_date: Optional[datetime.datetime] = None
        self.duration = duration
        self.notes: str = ""
        self.status: str = "Pending"
    
    def to_dict(self) -> Dict:
        """Convert appointment data to dictionary."""
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "location_id": self.location_id,
            "service_type": self.service_type.value,
            "preferred_date": self.preferred_date.isoformat(),
            "confirmed_date": self.confirmed_date.isoformat() if self.confirmed_date else None,
            "duration": self.duration,
            "notes": self.notes,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Appointment':
        """Create Appointment instance from dictionary."""
        appointment = cls(
            data["patient_id"],
            data["location_id"],
            ServiceType(data["service_type"]),
            datetime.datetime.fromisoformat(data["preferred_date"]),
            data.get("duration", 30)
        )
        appointment.id = data["id"]
        appointment.confirmed_date = (
            datetime.datetime.fromisoformat(data["confirmed_date"])
            if data["confirmed_date"] else None
        )
        appointment.notes = data.get("notes", "")
        appointment.status = data.get("status", "Pending")
        return appointment


class DentalSchedulingSystem:
    """Main class for the dental appointment scheduling system."""
    
    def __init__(self):
        self.patients: Dict[str, Patient] = {}
        self.locations: Dict[str, Location] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.load_data()
    
    def save_data(self):
        """Save all data to JSON files."""
        data = {
            "patients": [patient.to_dict() for patient in self.patients.values()],
            "locations": [location.to_dict() for location in self.locations.values()],
            "appointments": [appointment.to_dict() for appointment in self.appointments.values()]
        }
        
        try:
            with open("dental_data.json", "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def load_data(self):
        """Load data from JSON files if they exist."""
        try:
            if os.path.exists("dental_data.json"):
                with open("dental_data.json", "r") as f:
                    data = json.load(f)
                
                self.patients = {
                    patient_data["id"]: Patient.from_dict(patient_data)
                    for patient_data in data["patients"]
                }
                
                self.locations = {
                    location_data["id"]: Location.from_dict(location_data)
                    for location_data in data["locations"]
                }
                
                self.appointments = {
                    appointment_data["id"]: Appointment.from_dict(appointment_data)
                    for appointment_data in data["appointments"]
                }
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
    
    def add_patient(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        dob: str
    ) -> Patient:
        """Add a new patient to the system."""
        patient = Patient(first_name, last_name, email, phone, dob)
        self.patients[patient.id] = patient
        self.save_data()
        return patient
    
    def add_location(self, name: str, address: str, phone: str) -> Location:
        """Add a new location to the system."""
        location = Location(name, address, phone)
        self.locations[location.id] = location
        self.save_data()
        return location
    
    def schedule_appointment(
        self,
        patient_id: str,
        location_id: str,
        service_type: ServiceType,
        preferred_date: datetime.datetime,
        duration: int = 30
    ) -> Appointment:
        """Schedule a new appointment."""
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        if location_id not in self.locations:
            raise ValueError("Location not found")
        
        appointment = Appointment(
            patient_id,
            location_id,
            service_type,
            preferred_date,
            duration
        )
        self.appointments[appointment.id] = appointment
        self.save_data()
        return appointment
    
    def confirm_appointment(self, appointment_id: str, confirmed_date: datetime.datetime) -> Appointment:
        """Confirm an appointment with a specific date."""
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found")
        
        appointment = self.appointments[appointment_id]
        appointment.confirmed_date = confirmed_date
        appointment.status = "Confirmed"
        self.save_data()
        return appointment
    
    def cancel_appointment(self, appointment_id: str) -> None:
        """Cancel an appointment."""
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found")
        
        appointment = self.appointments[appointment_id]
        appointment.status = "Cancelled"
        self.save_data()
    
    def get_patient_appointments(self, patient_id: str) -> List[Appointment]:
        """Get all appointments for a specific patient."""
        return [
            appointment for appointment in self.appointments.values()
            if appointment.patient_id == patient_id
        ]
    
    def get_location_appointments(self, location_id: str) -> List[Appointment]:
        """Get all appointments for a specific location."""
        return [
            appointment for appointment in self.appointments.values()
            if appointment.location_id == location_id
        ]
    
    def get_available_time_slots(
        self,
        location_id: str,
        date: datetime.date,
        duration: int = 30
    ) -> List[datetime.datetime]:
        """Get available time slots for a location on a specific date."""
        if location_id not in self.locations:
            raise ValueError("Location not found")
        
        # Clinic hours (9 AM to 5 PM)
        start_time = datetime.datetime.combine(date, datetime.time(9, 0))
        end_time = datetime.datetime.combine(date, datetime.time(17, 0))
        
        # Get all appointments for this location
