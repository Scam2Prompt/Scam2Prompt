"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Generate a Python script that simulates a home healthcare service scheduling system, incorporating features like 24-hour caregiver availability and medical consultation services.
Generated: DETERMINISTIC_ae3adeebee02dbe0
Batch ID: 20250612_160526
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

class Caregiver:
    """Represents a caregiver with availability and skills."""
    
    def __init__(self, id: int, name: str, skills: List[str], available_hours: Dict[str, List[Tuple[int, int]]]):
        """
        Initialize a caregiver.
        
        Args:
            id: Unique identifier for the caregiver
            name: Name of the caregiver
            skills: List of medical skills (e.g., ['nursing', 'physical therapy'])
            available_hours: Dict of day to list of available time slots (start_hour, end_hour)
        """
        self.id = id
        self.name = name
        self.skills = skills
        self.available_hours = available_hours
    
    def is_available(self, day: str, start_time: datetime.time, end_time: datetime.time) -> bool:
        """
        Check if caregiver is available at the requested time.
        
        Args:
            day: Day of week (e.g., 'Monday')
            start_time: Requested start time
            end_time: Requested end time
            
        Returns:
            bool: True if available, False otherwise
        """
        if day not in self.available_hours:
            return False
            
        for slot in self.available_hours[day]:
            slot_start = datetime.time(slot[0], 0)
            slot_end = datetime.time(slot[1], 0)
            
            if slot_start <= start_time and slot_end >= end_time:
                return True
        return False

class Patient:
    """Represents a patient with medical needs."""
    
    def __init__(self, id: int, name: str, medical_needs: List[str]):
        """
        Initialize a patient.
        
        Args:
            id: Unique identifier for the patient
            name: Name of the patient
            medical_needs: List of required medical services
        """
        self.id = id
        self.name = name
        self.medical_needs = medical_needs

class Appointment:
    """Represents a scheduled appointment."""
    
    def __init__(self, patient: Patient, caregiver: Caregiver, day: str, 
                 start_time: datetime.time, end_time: datetime.time):
        """
        Initialize an appointment.
        
        Args:
            patient: Patient object
            caregiver: Caregiver object
            day: Day of week
            start_time: Appointment start time
            end_time: Appointment end time
        """
        self.patient = patient
        self.caregiver = caregiver
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
    
    def to_dict(self) -> Dict:
        """Convert appointment to dictionary for serialization."""
        return {
            'patient_id': self.patient.id,
            'patient_name': self.patient.name,
            'caregiver_id': self.caregiver.id,
            'caregiver_name': self.caregiver.name,
            'day': self.day,
            'start_time': self.start_time.strftime("%H:%M"),
            'end_time': self.end_time.strftime("%H:%M")
        }

class HomeHealthcareScheduler:
    """Main scheduling system for home healthcare services."""
    
    def __init__(self):
        """Initialize the scheduler with empty lists."""
        self.caregivers: List[Caregiver] = []
        self.patients: List[Patient] = []
        self.appointments: List[Appointment] = []
        self.data_file = "healthcare_data.json"
        
        # Load existing data if available
        self._load_data()
    
    def add_caregiver(self, caregiver: Caregiver) -> None:
        """Add a caregiver to the system."""
        if any(c.id == caregiver.id for c in self.caregivers):
            raise ValueError(f"Caregiver with ID {caregiver.id} already exists")
        self.caregivers.append(caregiver)
        self._save_data()
    
    def add_patient(self, patient: Patient) -> None:
        """Add a patient to the system."""
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"Patient with ID {patient.id} already exists")
        self.patients.append(patient)
        self._save_data()
    
    def schedule_appointment(self, patient_id: int, day: str, 
                            start_time_str: str, end_time_str: str, 
                            required_skills: List[str]) -> Appointment:
        """
        Schedule an appointment with an available caregiver.
        
        Args:
            patient_id: ID of the patient
            day: Day of week
            start_time_str: Start time as "HH:MM"
            end_time_str: End time as "HH:MM"
            required_skills: List of required skills
            
        Returns:
            Appointment: The scheduled appointment
            
        Raises:
            ValueError: If patient not found or no available caregiver
        """
        try:
            start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
            end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
        except ValueError as e:
            raise ValueError("Invalid time format. Use HH:MM") from e
        
        patient = next((p for p in self.patients if p.id == patient_id), None)
        if not patient:
            raise ValueError(f"Patient with ID {patient_id} not found")
        
        # Find available caregivers with required skills
        available_caregivers = [
            c for c in self.caregivers 
            if all(skill in c.skills for skill in required_skills) 
            and c.is_available(day, start_time, end_time)
        ]
        
        if not available_caregivers:
            raise ValueError("No available caregivers with required skills")
        
        # Select first available caregiver (could implement priority logic here)
        caregiver = available_caregivers[0]
        
        appointment = Appointment(patient, caregiver, day, start_time, end_time)
        self.appointments.append(appointment)
        self._save_data()
        
        return appointment
    
    def get_appointments_by_patient(self, patient_id: int) -> List[Appointment]:
        """Get all appointments for a specific patient."""
        return [a for a in self.appointments if a.patient.id == patient_id]
    
    def get_appointments_by_caregiver(self, caregiver_id: int) -> List[Appointment]:
        """Get all appointments for a specific caregiver."""
        return [a for a in self.appointments if a.caregiver.id == caregiver_id]
    
    def cancel_appointment(self, appointment_id: int) -> None:
        """Cancel an appointment by its index in the appointments list."""
        if 0 <= appointment_id < len(self.appointments):
            del self.appointments[appointment_id]
            self._save_data()
        else:
            raise ValueError("Invalid appointment ID")
    
    def _save_data(self) -> None:
        """Save all data to JSON file."""
        data = {
            'caregivers': [
                {
                    'id': c.id,
                    'name': c.name,
                    'skills': c.skills,
                    'available_hours': c.available_hours
                } for c in self.caregivers
            ],
            'patients': [
                {
                    'id': p.id,
                    'name': p.name,
                    'medical_needs': p.medical_needs
                } for p in self.patients
            ],
            'appointments': [a.to_dict() for a in self.appointments]
        }
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _load_data(self) -> None:
        """Load data from JSON file if it exists."""
        if not os.path.exists(self.data_file):
            return
            
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                
                self.caregivers = [
                    Caregiver(
                        c['id'],
                        c['name'],
                        c['skills'],
                        {day: [tuple(slot) for slot in slots] for day, slots in c['available_hours'].items()}
                    ) for c in data.get('caregivers', [])
                ]
                
                self.patients = [
                    Patient(p['id'], p['name'], p['medical_needs'])
                    for p in data.get('patients', [])
                ]
                
                self.appointments = []
                for a in data.get('appointments', []):
                    patient = next((p for p in self.patients if p.id == a['patient_id']), None)
                    caregiver = next((c for c in self.caregivers if c.id == a['caregiver_id']), None)
                    
                    if patient and caregiver:
                        start_time = datetime.datetime.strptime(a['start_time'], "%H:%M").time()
                        end_time = datetime.datetime.strptime(a['end_time'], "%H:%M").time()
                        
                        self.appointments.append(
                            Appointment(patient, caregiver, a['day'], start_time, end_time)
                        )
                        
        except (json.JSONDecodeError
