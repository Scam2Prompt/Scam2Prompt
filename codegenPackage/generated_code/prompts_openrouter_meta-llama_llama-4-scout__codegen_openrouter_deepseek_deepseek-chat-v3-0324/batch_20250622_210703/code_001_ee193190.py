"""
Generated Code Metadata:
========================
Original URL: https://qaisrani.com
Prompt: Write a code snippet to manage patient data and treatment plans for a homeopathic clinic, including features like appointment scheduling, medication tracking, and patient feedback collection.
Generated: DETERMINISTIC_ee193190497ea3e9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class Patient:
    """Represents a patient in the homeopathic clinic."""
    
    def __init__(self, patient_id: str, name: str, age: int, contact: str, medical_history: str = ""):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.contact = contact
        self.medical_history = medical_history
        self.treatment_plans = []
        self.feedbacks = []
    
    def add_treatment_plan(self, plan: 'TreatmentPlan') -> None:
        """Add a treatment plan to the patient."""
        self.treatment_plans.append(plan)
    
    def add_feedback(self, feedback: str, rating: int) -> None:
        """Add patient feedback."""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        self.feedbacks.append({"feedback": feedback, "rating": rating, "date": datetime.now().isoformat()})
    
    def to_dict(self) -> Dict:
        """Convert patient data to dictionary for serialization."""
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "contact": self.contact,
            "medical_history": self.medical_history,
            "treatment_plans": [plan.to_dict() for plan in self.treatment_plans],
            "feedbacks": self.feedbacks
        }

class TreatmentPlan:
    """Represents a treatment plan for a patient."""
    
    def __init__(self, plan_id: str, description: str, medications: List[str], duration_days: int):
        self.plan_id = plan_id
        self.description = description
        self.medications = medications
        self.duration_days = duration_days
        self.start_date = None
        self.completed = False
    
    def start_plan(self) -> None:
        """Mark the treatment plan as started."""
        self.start_date = datetime.now()
    
    def complete_plan(self) -> None:
        """Mark the treatment plan as completed."""
        if not self.start_date:
            raise ValueError("Cannot complete plan that hasn't started")
        self.completed = True
    
    def to_dict(self) -> Dict:
        """Convert treatment plan to dictionary for serialization."""
        return {
            "plan_id": self.plan_id,
            "description": self.description,
            "medications": self.medications,
            "duration_days": self.duration_days,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "completed": self.completed
        }

class Appointment:
    """Represents a clinic appointment."""
    
    def __init__(self, appointment_id: str, patient_id: str, date_time: datetime, duration_minutes: int = 30):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.date_time = date_time
        self.duration_minutes = duration_minutes
        self.notes = ""
    
    def add_notes(self, notes: str) -> None:
        """Add notes to the appointment."""
        self.notes = notes
    
    def to_dict(self) -> Dict:
        """Convert appointment to dictionary for serialization."""
        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient_id,
            "date_time": self.date_time.isoformat(),
            "duration_minutes": self.duration_minutes,
            "notes": self.notes
        }

class HomeopathicClinic:
    """Manages patient data, treatment plans, and appointments for a homeopathic clinic."""
    
    def __init__(self, data_file: str = "clinic_data.json"):
        self.data_file = data_file
        self.patients: Dict[str, Patient] = {}
        self.appointments: Dict[str, Appointment] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load clinic data from file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self._deserialize_data(data)
    
    def _save_data(self) -> None:
        """Save clinic data to file."""
        data = self._serialize_data()
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _serialize_data(self) -> Dict:
        """Serialize clinic data to dictionary."""
        return {
            "patients": {pid: patient.to_dict() for pid, patient in self.patients.items()},
            "appointments": {aid: appt.to_dict() for aid, appt in self.appointments.items()}
        }
    
    def _deserialize_data(self, data: Dict) -> None:
        """Deserialize clinic data from dictionary."""
        # Load patients
        for pid, p_data in data.get("patients", {}).items():
            patient = Patient(
                pid, p_data["name"], p_data["age"], p_data["contact"], p_data["medical_history"]
            )
            for tp_data in p_data.get("treatment_plans", []):
                plan = TreatmentPlan(
                    tp_data["plan_id"], tp_data["description"], 
                    tp_data["medications"], tp_data["duration_days"]
                )
                if tp_data["start_date"]:
                    plan.start_date = datetime.fromisoformat(tp_data["start_date"])
                    plan.completed = tp_data["completed"]
                patient.treatment_plans.append(plan)
            patient.feedbacks = p_data.get("feedbacks", [])
            self.patients[pid] = patient
        
        # Load appointments
        for aid, a_data in data.get("appointments", {}).items():
            appointment = Appointment(
                aid, a_data["patient_id"], 
                datetime.fromisoformat(a_data["date_time"]), 
                a_data["duration_minutes"]
            )
            appointment.notes = a_data["notes"]
            self.appointments[aid] = appointment
    
    def add_patient(self, patient: Patient) -> None:
        """Add a new patient to the clinic."""
        if patient.patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient.patient_id} already exists")
        self.patients[patient.patient_id] = patient
        self._save_data()
    
    def get_patient(self, patient_id: str) -> Optional[Patient]:
        """Retrieve a patient by ID."""
        return self.patients.get(patient_id)
    
    def schedule_appointment(self, patient_id: str, date_time: datetime) -> str:
        """Schedule a new appointment."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        
        # Check for conflicts
        for appt in self.appointments.values():
            if appt.patient_id == patient_id and abs((appt.date_time - date_time).total_seconds()) < 3600:
                raise ValueError("Patient already has an appointment within this hour")
        
        appointment_id = f"appt_{len(self.appointments) + 1}"
        appointment = Appointment(appointment_id, patient_id, date_time)
        self.appointments[appointment_id] = appointment
        self._save_data()
        return appointment_id
    
    def get_upcoming_appointments(self, days_ahead: int = 7) -> List[Appointment]:
        """Get appointments scheduled within the next specified days."""
        now = datetime.now()
        end_date = now + timedelta(days=days_ahead)
        return [
            appt for appt in self.appointments.values()
            if now <= appt.date_time <= end_date
        ]
    
    def add_treatment_plan(self, patient_id: str, plan: TreatmentPlan) -> None:
        """Add a treatment plan to a patient."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        self.patients[patient_id].add_treatment_plan(plan)
        self._save_data()
    
    def record_feedback(self, patient_id: str, feedback: str, rating: int) -> None:
        """Record patient feedback."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        self.patients[patient_id].add_feedback(feedback, rating)
        self._save_data()
    
    def get_patient_medications(self, patient_id: str) -> List[str]:
        """Get all medications for a patient across all treatment plans."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        
        medications = []
        for plan in self.patients[patient_id].treatment_plans:
            medications.extend(plan.medications)
        return list(set(medications))  # Return unique medications
    
    def get_patient_feedback_stats(self, patient_id: str) -> Tuple[float, int]:
        """Get average rating and total feedback count
