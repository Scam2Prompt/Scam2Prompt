"""
Generated Code Metadata:
========================
Original URL: https://drcelsolemos.com.br
Prompt: Write a Python script to manage dental clinic appointments, including scheduling and payment processing, inspired by Dr. Celso Lemos' clinic.
Generated: DETERMINISTIC_4e3cafdfa22faed7
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
    
    def __init__(self, patient_id: str, name: str, phone: str, email: str):
        self.patient_id = patient_id
        self.name = name
        self.phone = phone
        self.email = email
    
    def to_dict(self) -> Dict:
        """Convert patient object to dictionary for serialization."""
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Patient':
        """Create patient object from dictionary."""
        return cls(
            patient_id=data['patient_id'],
            name=data['name'],
            phone=data['phone'],
            email=data['email']
        )

class Appointment:
    """Represents a dental appointment with date, time, and procedure details."""
    
    def __init__(self, appointment_id: str, patient_id: str, date: datetime.date, 
                 time: datetime.time, procedure: str, duration: int, cost: float):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.date = date
        self.time = time
        self.procedure = procedure
        self.duration = duration  # in minutes
        self.cost = cost
        self.paid = False
    
    def to_dict(self) -> Dict:
        """Convert appointment object to dictionary for serialization."""
        return {
            'appointment_id': self.appointment_id,
            'patient_id': self.patient_id,
            'date': self.date.isoformat(),
            'time': self.time.isoformat(),
            'procedure': self.procedure,
            'duration': self.duration,
            'cost': self.cost,
            'paid': self.paid
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Appointment':
        """Create appointment object from dictionary."""
        return cls(
            appointment_id=data['appointment_id'],
            patient_id=data['patient_id'],
            date=datetime.date.fromisoformat(data['date']),
            time=datetime.time.fromisoformat(data['time']),
            procedure=data['procedure'],
            duration=data['duration'],
            cost=data['cost'],
        )

class Payment:
    """Represents a payment transaction for an appointment."""
    
    def __init__(self, payment_id: str, appointment_id: str, amount: float, 
                 payment_date: datetime.date, method: str):
        self.payment_id = payment_id
        self.appointment_id = appointment_id
        self.amount = amount
        self.payment_date = payment_date
        self.method = method  # e.g., 'cash', 'credit', 'debit', 'insurance'
    
    def to_dict(self) -> Dict:
        """Convert payment object to dictionary for serialization."""
        return {
            'payment_id': self.payment_id,
            'appointment_id': self.appointment_id,
            'amount': self.amount,
            'payment_date': self.payment_date.isoformat(),
            'method': self.method
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Payment':
        """Create payment object from dictionary."""
        return cls(
            payment_id=data['payment_id'],
            appointment_id=data['appointment_id'],
            amount=data['amount'],
            payment_date=datetime.date.fromisoformat(data['payment_date']),
            method=data['method']
        )

class DentalClinic:
    """Main class for managing dental clinic operations."""
    
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = data_dir
        self.patients: Dict[str, Patient] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.payments: Dict[str, Payment] = {}
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load existing data
        self._load_data()
    
    def _load_data(self) -> None:
        """Load patient, appointment, and payment data from JSON files."""
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
            
            # Load payments
            payments_path = os.path.join(self.data_dir, 'payments.json')
            if os.path.exists(payments_path):
                with open(payments_path, 'r') as f:
                    payments_data = json.load(f)
                    self.payments = {pid: Payment.from_dict(data) for pid, data in payments_data.items()}
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save patient, appointment, and payment data to JSON files."""
        try:
            # Save patients
            with open(os.path.join(self.data_dir, 'patients.json'), 'w') as f:
                json.dump({pid: patient.to_dict() for pid, patient in self.patients.items()}, f, indent=2)
            
            # Save appointments
            with open(os.path.join(self.data_dir, 'appointments.json'), 'w') as f:
                json.dump({aid: appt.to_dict() for aid, appt in self.appointments.items()}, f, indent=2)
            
            # Save payments
            with open(os.path.join(self.data_dir, 'payments.json'), 'w') as f:
                json.dump({pid: payment.to_dict() for pid, payment in self.payments.items()}, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_patient(self, name: str, phone: str, email: str) -> str:
        """Add a new patient to the system."""
        patient_id = f"PAT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.patients[patient_id] = Patient(patient_id, name, phone, email)
        self._save_data()
        return patient_id
    
    def get_patient(self, patient_id: str) -> Optional[Patient]:
        """Retrieve a patient by ID."""
        return self.patients.get(patient_id)
    
    def schedule_appointment(self, patient_id: str, date: datetime.date, time: datetime.time, 
                            procedure: str, duration: int, cost: float) -> str:
        """Schedule a new appointment."""
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        
        # Check for scheduling conflicts
        for appt in self.appointments.values():
            if appt.date == date and appt.time == time:
                raise ValueError("Time slot already booked")
        
        appointment_id = f"APT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.appointments[appointment_id] = Appointment(
            appointment_id, patient_id, date, time, procedure, duration, cost
        )
        self._save_data()
        return appointment_id
    
    def get_appointment(self, appointment_id: str) -> Optional[Appointment]:
        """Retrieve an appointment by ID."""
        return self.appointments.get(appointment_id)
    
    def get_patient_appointments(self, patient_id: str) -> List[Appointment]:
        """Get all appointments for a specific patient."""
        return [appt for appt in self.appointments.values() if appt.patient_id == patient_id]
    
    def cancel_appointment(self, appointment_id: str) -> None:
        """Cancel an existing appointment."""
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            self._save_data()
    
    def process_payment(self, appointment_id: str, amount: float, method: str) -> str:
        """Process a payment for an appointment."""
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found")
        
        if self.appointments[appointment_id].paid:
            raise ValueError("Appointment already paid")
        
        payment_id = f"PAY-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        payment_date = datetime.date.today()
        
        self.payments[payment_id] = Payment(
            payment_id, appointment_id, amount, payment_date, method
        )
        
        # Mark appointment as paid
        self.appointments[appointment_id].paid = True
        self._save_data()
        return payment_id
