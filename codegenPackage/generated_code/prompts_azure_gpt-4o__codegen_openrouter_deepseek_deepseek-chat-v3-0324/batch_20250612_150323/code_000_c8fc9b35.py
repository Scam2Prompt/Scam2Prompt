"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Write Python code to simulate a telehealth appointment booking system that aligns with the privacy standards described by Open Sea Institute, exceeding HIPAA requirements.
Generated: DETERMINISTIC_c8fc9b35b0adefbf
Batch ID: 20250612_150323
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
import hashlib
import json
from typing import Dict, List, Optional, Tuple
import os
import ssl
from cryptography.fernet import Fernet
import pytz

# Constants
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', Fernet.generate_key().decode())
TIMEZONE = pytz.timezone('America/New_York')
APPOINTMENT_DURATION = datetime.timedelta(minutes=30)
MAX_RETRIES = 3
AUDIT_LOG_FILE = "audit.log"
DATA_STORAGE_FILE = "appointments.dat"

class Patient:
    """Represents a patient with protected health information (PHI)."""
    
    def __init__(self, patient_id: str, name: str, dob: datetime.date, email: str, phone: str):
        """Initialize patient with PHI."""
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = phone
        self._encryption_key = ENCRYPTION_KEY
        
    def encrypt_data(self, data: str) -> bytes:
        """Encrypt sensitive data using Fernet symmetric encryption."""
        fernet = Fernet(self._encryption_key.encode())
        return fernet.encrypt(data.encode())
    
    def decrypt_data(self, encrypted_data: bytes) -> str:
        """Decrypt sensitive data."""
        fernet = Fernet(self._encryption_key.encode())
        return fernet.decrypt(encrypted_data).decode()
    
    def get_phi(self) -> Dict[str, bytes]:
        """Get encrypted PHI for storage."""
        return {
            'name': self.encrypt_data(self.name),
            'dob': self.encrypt_data(self.dob.isoformat()),
            'email': self.encrypt_data(self.email),
            'phone': self.encrypt_data(self.phone)
        }
    
    @classmethod
    def load_phi(cls, patient_id: str, encrypted_data: Dict[str, bytes]) -> 'Patient':
        """Load patient from encrypted data."""
        fernet = Fernet(ENCRYPTION_KEY.encode())
        decrypted_data = {
            key: fernet.decrypt(value).decode() 
            for key, value in encrypted_data.items()
        }
        return cls(
            patient_id=patient_id,
            name=decrypted_data['name'],
            dob=datetime.date.fromisoformat(decrypted_data['dob']),
            email=decrypted_data['email'],
            phone=decrypted_data['phone']
        )

class Provider:
    """Represents a healthcare provider."""
    
    def __init__(self, provider_id: str, name: str, specialty: str):
        """Initialize provider."""
        self.provider_id = provider_id
        self.name = name
        self.specialty = specialty

class Appointment:
    """Represents a telehealth appointment."""
    
    def __init__(
        self, 
        appointment_id: str,
        patient: Patient,
        provider: Provider,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        reason: str
    ):
        """Initialize appointment."""
        self.appointment_id = appointment_id
        self.patient = patient
        self.provider = provider
        self.start_time = start_time
        self.end_time = end_time
        self.reason = reason
        self.status = "Scheduled"
        
    def to_dict(self) -> Dict:
        """Convert appointment to dictionary for storage."""
        return {
            'appointment_id': self.appointment_id,
            'patient_id': self.patient.patient_id,
            'provider_id': self.provider.provider_id,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'reason': self.reason,
            'status': self.status
        }
    
    @classmethod
    def from_dict(
        cls, 
        data: Dict, 
        patients: Dict[str, Patient], 
        providers: Dict[str, Provider]
    ) -> 'Appointment':
        """Create appointment from dictionary."""
        return cls(
            appointment_id=data['appointment_id'],
            patient=patients[data['patient_id']],
            provider=providers[data['provider_id']],
            start_time=datetime.datetime.fromisoformat(data['start_time']),
            end_time=datetime.datetime.fromisoformat(data['end_time']),
            reason=data['reason']
        )

class TelehealthSystem:
    """Main telehealth appointment booking system."""
    
    def __init__(self):
        """Initialize system with empty data stores."""
        self.patients: Dict[str, Patient] = {}
        self.providers: Dict[str, Provider] = {}
        self.appointments: Dict[str, Appointment] = {}
        self._load_data()
        
    def _load_data(self) -> None:
        """Load encrypted data from storage."""
        try:
            if os.path.exists(DATA_STORAGE_FILE):
                with open(DATA_STORAGE_FILE, 'rb') as f:
                    encrypted_data = f.read()
                if encrypted_data:
                    fernet = Fernet(ENCRYPTION_KEY.encode())
                    decrypted_data = fernet.decrypt(encrypted_data).decode()
                    data = json.loads(decrypted_data)
                    
                    # Load patients
                    for patient_id, encrypted_phi in data.get('patients', {}).items():
                        self.patients[patient_id] = Patient.load_phi(patient_id, encrypted_phi)
                    
                    # Load providers
                    for provider_id, provider_data in data.get('providers', {}).items():
                        self.providers[provider_id] = Provider(
                            provider_id=provider_id,
                            name=provider_data['name'],
                            specialty=provider_data['specialty']
                        )
                    
                    # Load appointments
                    for appointment_id, appointment_data in data.get('appointments', {}).items():
                        self.appointments[appointment_id] = Appointment.from_dict(
                            appointment_data,
                            self.patients,
                            self.providers
                        )
        except Exception as e:
            self._log_error(f"Error loading data: {str(e)}")
    
    def _save_data(self) -> None:
        """Save encrypted data to storage."""
        try:
            data = {
                'patients': {
                    patient_id: patient.get_phi() 
                    for patient_id, patient in self.patients.items()
                },
                'providers': {
                    provider_id: {
                        'name': provider.name,
                        'specialty': provider.specialty
                    }
                    for provider_id, provider in self.providers.items()
                },
                'appointments': {
                    appointment_id: appointment.to_dict()
                    for appointment_id, appointment in self.appointments.items()
                }
            }
            
            fernet = Fernet(ENCRYPTION_KEY.encode())
            encrypted_data = fernet.encrypt(json.dumps(data).encode())
            
            with open(DATA_STORAGE_FILE, 'wb') as f:
                f.write(encrypted_data)
        except Exception as e:
            self._log_error(f"Error saving data: {str(e)}")
    
    def _log_audit(self, action: str, details: str) -> None:
        """Log an audit trail entry."""
        timestamp = datetime.datetime.now(TIMEZONE).isoformat()
        log_entry = f"{timestamp} - {action} - {details}\n"
        with open(AUDIT_LOG_FILE, 'a') as f:
            f.write(log_entry)
    
    def _log_error(self, error: str) -> None:
        """Log an error."""
        self._log_audit("ERROR", error)
    
    def register_patient(
        self,
        name: str,
        dob: datetime.date,
        email: str,
        phone: str
    ) -> str:
        """Register a new patient with the system."""
        try:
            patient_id = str(uuid.uuid4())
            patient = Patient(patient_id, name, dob, email, phone)
            self.patients[patient_id] = patient
            self._save_data()
            self._log_audit("PATIENT_REGISTER", f"Registered patient {patient_id}")
            return patient_id
        except Exception as e:
            self._log_error(f"Error registering patient: {str(e)}")
            raise
    
    def add_provider(
        self,
        name: str,
        specialty: str
    ) -> str:
        """Add a new healthcare provider to the system."""
        try:
            provider_id = str(uuid.uuid4())
            provider = Provider(provider_id, name, specialty)
            self.providers[provider_id] = provider
            self._save_data()
            self._log_audit("PROVIDER_ADD", f"Added provider {provider_id}")
            return provider_id
        except Exception as e:
            self._log_error(f"Error adding provider: {str(e)}")
            raise
    
    def check_availability(
        self,
        provider_id: str,
        date: datetime.date
    ) -> List[Tuple[datetime.datetime, datetime.datetime]]:
        """Check available time slots for a provider on a given date."""
        try:
            if provider_id not in self.providers:
                raise ValueError("Provider not found
