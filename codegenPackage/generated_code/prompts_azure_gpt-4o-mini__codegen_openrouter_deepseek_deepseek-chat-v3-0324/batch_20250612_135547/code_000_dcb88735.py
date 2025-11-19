"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Generate a code snippet for a dental clinic management system that includes features for booking appointments and managing patient records, similar to the services offered by Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_dcb88735f40d7b73
Batch ID: 20250612_135547
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
from typing import Dict, List, Optional

class Patient:
    """Represents a patient in the dental clinic system."""
    
    def __init__(self, patient_id: str, name: str, dob: str, phone: str, email: str, address: str, medical_history: str = ""):
        """
        Initialize a new patient record.
        
        Args:
            patient_id: Unique identifier for the patient
            name: Full name of the patient
            dob: Date of birth in YYYY-MM-DD format
            phone: Contact phone number
            email: Contact email address
            address: Physical address
            medical_history: Optional medical history notes
        """
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.phone = phone
        self.email = email
        self.address = address
        self.medical_history = medical_history
        self.appointments = []

    def add_appointment(self, appointment_id: str):
        """Add an appointment reference to the patient's record."""
        if appointment_id not in self.appointments:
            self.appointments.append(appointment_id)

    def to_dict(self) -> Dict:
        """Convert patient data to dictionary for storage."""
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'dob': self.dob,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'medical_history': self.medical_history,
            'appointments': self.appointments
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create Patient instance from dictionary data."""
        return cls(
            data['patient_id'],
            data['name'],
            data['dob'],
            data['phone'],
            data['email'],
            data['address'],
            data.get('medical_history', '')
        )


class Appointment:
    """Represents a dental appointment."""
    
    def __init__(self, appointment_id: str, patient_id: str, dentist_id: str, date_time: str, 
                 duration: int, procedure: str, notes: str = ""):
        """
        Initialize a new appointment.
        
        Args:
            appointment_id: Unique identifier for the appointment
            patient_id: ID of the patient
            dentist_id: ID of the dentist
            date_time: Appointment date and time in ISO format
            duration: Duration in minutes
            procedure: Description of dental procedure
            notes: Optional notes about the appointment
        """
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.dentist_id = dentist_id
        self.date_time = date_time
        self.duration = duration
        self.procedure = procedure
        self.notes = notes
        self.status = "Scheduled"  # Can be: Scheduled, Completed, Cancelled, No-show

    def update_status(self, new_status: str):
        """Update the status of the appointment."""
        valid_statuses = ["Scheduled", "Completed", "Cancelled", "No-show"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")

    def to_dict(self) -> Dict:
        """Convert appointment data to dictionary for storage."""
        return {
            'appointment_id': self.appointment_id,
            'patient_id': self.patient_id,
            'dentist_id': self.dentist_id,
            'date_time': self.date_time,
            'duration': self.duration,
            'procedure': self.procedure,
            'notes': self.notes,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create Appointment instance from dictionary data."""
        appointment = cls(
            data['appointment_id'],
            data['patient_id'],
            data['dentist_id'],
            data['date_time'],
            data['duration'],
            data['procedure'],
            data.get('notes', '')
        )
        appointment.status = data.get('status', 'Scheduled')
        return appointment


class DentalClinic:
    """Main class for managing the dental clinic operations."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the dental clinic system with data storage directory."""
        self.data_dir = data_dir
        self.patients: Dict[str, Patient] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.dentists = {
            "dentist1": "Dr. Vira Palazzo",
            "dentist2": "Dr. John Smith"
        }
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        self.load_data()

    def save_data(self):
        """Save all data to JSON files."""
        try:
            # Save patients
            patients_data = {pid: patient.to_dict() for pid, patient in self.patients.items()}
            with open(os.path.join(self.data_dir, 'patients.json'), 'w') as f:
                json.dump(patients_data, f, indent=2)
            
            # Save appointments
            appointments_data = {aid: appt.to_dict() for aid, appt in self.appointments.items()}
            with open(os.path.join(self.data_dir, 'appointments.json'), 'w') as f:
                json.dump(appointments_data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        """Load data from JSON files."""
        try:
            # Load patients
            patients_path = os.path.join(self.data_dir, 'patients.json')
            if os.path.exists(patients_path):
                with open(patients_path, 'r') as f:
                    patients_data = json.load(f)
                    self.patients = {pid: Patient.from_dict(data) for pid, data in patients_data.items()}
            
            # Load appointments
            appointments_path = os.path.join(self.data_dir, 'appointments.json')
            if os.path.exists(appointments_path):
                with open(appointments_path, 'r') as f:
                    appointments_data = json.load(f)
                    self.appointments = {aid: Appointment.from_dict(data) for aid, data in appointments_data.items()}
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

    def add_patient(self, patient: Patient):
        """Add a new patient to the system."""
        if patient.patient_id in self.patients:
            raise ValueError("Patient ID already exists")
        self.patients[patient.patient_id] = patient
        self.save_data()

    def get_patient(self, patient_id: str) -> Optional[Patient]:
        """Retrieve a patient by ID."""
        return self.patients.get(patient_id)

    def update_patient(self, patient_id: str, **kwargs):
        """Update patient information."""
        patient = self.get_patient(patient_id)
        if not patient:
            raise ValueError("Patient not found")
        
        for key, value in kwargs.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        
        self.save_data()

    def schedule_appointment(self, appointment: Appointment):
        """Schedule a new appointment."""
        # Check if patient exists
        if appointment.patient_id not in self.patients:
            raise ValueError("Patient not found")
        
        # Check if dentist exists
        if appointment.dentist_id not in self.dentists:
            raise ValueError("Dentist not found")
        
        # Check for time conflicts
        appointment_time = datetime.datetime.fromisoformat(appointment.date_time)
        end_time = appointment_time + datetime.timedelta(minutes=appointment.duration)
        
        for existing_appt in self.appointments.values():
            if existing_appt.dentist_id == appointment.dentist_id:
                existing_time = datetime.datetime.fromisoformat(existing_appt.date_time)
                existing_end = existing_time + datetime.timedelta(minutes=existing_appt.duration)
                
                if (appointment_time < existing_end) and (end_time > existing_time):
                    raise ValueError("Time conflict with existing appointment")
        
        # Add appointment
        self.appointments[appointment.appointment_id] = appointment
        self.patients[appointment.patient_id].add_appointment(appointment.appointment_id)
        self.save_data()

    def cancel_appointment(self, appointment_id: str):
        """Cancel an existing appointment."""
        appointment = self.appointments.get(appointment_id)
        if not appointment:
            raise ValueError("Appointment not found")
        
        appointment.update_status("Cancelled")
        self.save_data()

    def get_appointments_by_patient(self, patient_id: str) -> List[Appointment]:
        """Get all appointments for a specific patient."""
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        
        return [appt for appt_id, appt in self.appointments.items() 
                if appt.patient_id == patient_id]

    def get_appointments_by_date(self, date: str) -> List[Appointment]:
        """Get all appointments for a specific date."""
        try:
