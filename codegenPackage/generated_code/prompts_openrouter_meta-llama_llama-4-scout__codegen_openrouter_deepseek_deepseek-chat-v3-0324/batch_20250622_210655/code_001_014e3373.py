"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Write a Python script to manage patient appointments and scheduling for a multidisciplinary healthcare center like Centro Abakadabra.
Generated: DETERMINISTIC_014e3373d36e4f64
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple

class Patient:
    """Represents a patient with personal and contact information."""
    
    def __init__(self, patient_id: str, name: str, dob: str, phone: str, email: str = None):
        """
        Initialize a Patient object.
        
        Args:
            patient_id: Unique identifier for the patient
            name: Full name of the patient
            dob: Date of birth in YYYY-MM-DD format
            phone: Contact phone number
            email: Optional email address
        """
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.phone = phone
        self.email = email
    
    def to_dict(self) -> Dict:
        """Convert Patient object to dictionary for serialization."""
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'dob': self.dob,
            'phone': self.phone,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Patient':
        """Create Patient object from dictionary."""
        return cls(
            patient_id=data['patient_id'],
            name=data['name'],
            dob=data['dob'],
            phone=data['phone'],
            email=data.get('email')
        )

class HealthcareProvider:
    """Represents a healthcare provider with their specialization."""
    
    def __init__(self, provider_id: str, name: str, specialization: str):
        """
        Initialize a HealthcareProvider object.
        
        Args:
            provider_id: Unique identifier for the provider
            name: Full name of the provider
            specialization: Medical specialization
        """
        self.provider_id = provider_id
        self.name = name
        self.specialization = specialization
    
    def to_dict(self) -> Dict:
        """Convert HealthcareProvider object to dictionary for serialization."""
        return {
            'provider_id': self.provider_id,
            'name': self.name,
            'specialization': self.specialization
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'HealthcareProvider':
        """Create HealthcareProvider object from dictionary."""
        return cls(
            provider_id=data['provider_id'],
            name=data['name'],
            specialization=data['specialization']
        )

class Appointment:
    """Represents a scheduled appointment between a patient and provider."""
    
    def __init__(self, appointment_id: str, patient_id: str, provider_id: str, 
                 date: str, time: str, duration: int = 30, status: str = 'scheduled'):
        """
        Initialize an Appointment object.
        
        Args:
            appointment_id: Unique identifier for the appointment
            patient_id: ID of the patient
            provider_id: ID of the healthcare provider
            date: Appointment date in YYYY-MM-DD format
            time: Appointment time in HH:MM format
            duration: Duration in minutes (default: 30)
            status: Current status of the appointment (default: 'scheduled')
        """
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.provider_id = provider_id
        self.date = date
        self.time = time
        self.duration = duration
        self.status = status
    
    def to_dict(self) -> Dict:
        """Convert Appointment object to dictionary for serialization."""
        return {
            'appointment_id': self.appointment_id,
            'patient_id': self.patient_id,
            'provider_id': self.provider_id,
            'date': self.date,
            'time': self.time,
            'duration': self.duration,
            'status': self.status
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Appointment':
        """Create Appointment object from dictionary."""
        return cls(
            appointment_id=data['appointment_id'],
            patient_id=data['patient_id'],
            provider_id=data['provider_id'],
            date=data['date'],
            time=data['time'],
            duration=data.get('duration', 30),
            status=data.get('status', 'scheduled')
        )

class AppointmentScheduler:
    """Manages patient appointments and scheduling."""
    
    def __init__(self, data_dir: str = 'data'):
        """
        Initialize the AppointmentScheduler.
        
        Args:
            data_dir: Directory to store data files
        """
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        
        self.patients = self._load_data('patients.json', Patient)
        self.providers = self._load_data('providers.json', HealthcareProvider)
        self.appointments = self._load_data('appointments.json', Appointment)
    
    def _load_data(self, filename: str, cls) -> Dict[str, object]:
        """Load data from JSON file and return as dictionary of objects."""
        filepath = os.path.join(self.data_dir, filename)
        data = {}
        
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                items = json.load(f)
                for item in items.values():
                    obj = cls.from_dict(item)
                    data[obj.patient_id if isinstance(obj, Patient) else 
                         obj.provider_id if isinstance(obj, HealthcareProvider) else 
                         obj.appointment_id] = obj
        return data
    
    def _save_data(self, filename: str, data: Dict[str, object]):
        """Save dictionary of objects to JSON file."""
        filepath = os.path.join(self.data_dir, filename)
        serialized = {k: v.to_dict() for k, v in data.items()}
        
        with open(filepath, 'w') as f:
            json.dump(serialized, f, indent=2)
    
    def add_patient(self, patient_id: str, name: str, dob: str, phone: str, email: str = None) -> bool:
        """Add a new patient to the system."""
        if patient_id in self.patients:
            return False
        
        self.patients[patient_id] = Patient(patient_id, name, dob, phone, email)
        self._save_data('patients.json', self.patients)
        return True
    
    def add_provider(self, provider_id: str, name: str, specialization: str) -> bool:
        """Add a new healthcare provider to the system."""
        if provider_id in self.providers:
            return False
        
        self.providers[provider_id] = HealthcareProvider(provider_id, name, specialization)
        self._save_data('providers.json', self.providers)
        return True
    
    def schedule_appointment(self, appointment_id: str, patient_id: str, provider_id: str, 
                            date: str, time: str, duration: int = 30) -> Tuple[bool, str]:
        """Schedule a new appointment."""
        if appointment_id in self.appointments:
            return False, "Appointment ID already exists"
        
        if patient_id not in self.patients:
            return False, "Patient not found"
        
        if provider_id not in self.providers:
            return False, "Provider not found"
        
        # Check for time conflicts
        for appointment in self.appointments.values():
            if (appointment.provider_id == provider_id and 
                appointment.date == date and 
                appointment.status != 'cancelled'):
                
                # Parse times for comparison
                existing_start = datetime.datetime.strptime(f"{appointment.date} {appointment.time}", "%Y-%m-%d %H:%M")
                existing_end = existing_start + datetime.timedelta(minutes=appointment.duration)
                
                new_start = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
                new_end = new_start + datetime.timedelta(minutes=duration)
                
                if (new_start < existing_end and new_end > existing_start):
                    return False, "Time conflict with existing appointment"
        
        self.appointments[appointment_id] = Appointment(
            appointment_id, patient_id, provider_id, date, time, duration
        )
        self._save_data('appointments.json', self.appointments)
        return True, "Appointment scheduled successfully"
    
    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an existing appointment."""
        if appointment_id not in self.appointments:
            return False
        
        appointment = self.appointments[appointment_id]
        if appointment.status == 'cancelled':
            return False
        
        appointment.status = 'cancelled'
        self._save_data('appointments.json', self.appointments)
        return True
    
    def reschedule_appointment(self, appointment_id: str, new_date: str, new_time: str) -> Tuple[bool, str]:
        """Reschedule an existing appointment."""
        if appointment_id not in self.appointments:
            return False, "Appointment not found"
        
        appointment = self.appointments[appointment_id]
        if appointment.status == 'cancelled':
            return False, "Cannot reschedule cancelled appointment"
        
        # Temporarily cancel to check for conflicts
        original_status = appointment.status
        appointment.status = 'cancelled'
        
        success, message = self.schedule_appointment(
            appointment
