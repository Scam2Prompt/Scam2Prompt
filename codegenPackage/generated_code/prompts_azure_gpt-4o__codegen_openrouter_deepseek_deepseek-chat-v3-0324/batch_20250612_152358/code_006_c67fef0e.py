"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Create a simulation in Python to model the workflow of a Unidade Básica de Saúde (Basic Health Unit), including patient intake, problem-solving for simple cases, and referrals to specialty clinics or hospitals.
Generated: DETERMINISTIC_c67fef0e9ce0bfcf
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta

class PatientStatus(Enum):
    WAITING = "Waiting"
    IN_TRIAGE = "In Triage"
    IN_CONSULTATION = "In Consultation"
    REFERRED = "Referred"
    DISCHARGED = "Discharged"

class HealthProblemSeverity(Enum):
    MINOR = "Minor"
    MODERATE = "Moderate"
    SEVERE = "Severe"

class Specialty(Enum):
    CARDIOLOGY = "Cardiology"
    DERMATOLOGY = "Dermatology"
    PEDIATRICS = "Pediatrics"
    ORTHOPEDICS = "Orthopedics"
    GENERAL_PRACTICE = "General Practice"

@dataclass
class Patient:
    id: int
    name: str
    age: int
    arrival_time: datetime
    status: PatientStatus
    problem_description: str
    problem_severity: HealthProblemSeverity
    assigned_doctor: Optional[str] = None
    referred_to: Optional[Specialty] = None
    discharge_time: Optional[datetime] = None

@dataclass
class Doctor:
    id: int
    name: str
    specialty: Specialty
    is_available: bool = True

class BasicHealthUnit:
    def __init__(self):
        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []
        self.waiting_room_capacity = 20
        self.current_day = datetime.now().date()
        self.initialize_doctors()
    
    def initialize_doctors(self):
        """Initialize the doctors available in the health unit."""
        self.doctors = [
            Doctor(1, "Dr. Silva", Specialty.GENERAL_PRACTICE),
            Doctor(2, "Dr. Oliveira", Specialty.GENERAL_PRACTICE),
            Doctor(3, "Dr. Santos", Specialty.PEDIATRICS),
            Doctor(4, "Dr. Costa", Specialty.CARDIOLOGY),
            Doctor(5, "Dr. Pereira", Specialty.DERMATOLOGY)
        ]
    
    def add_patient(self, name: str, age: int, problem_description: str) -> bool:
        """Add a new patient to the system if there's capacity."""
        if len([p for p in self.patients if p.status == PatientStatus.WAITING]) >= self.waiting_room_capacity:
            return False
        
        severity = random.choice(list(HealthProblemSeverity))
        patient = Patient(
            id=len(self.patients) + 1,
            name=name,
            age=age,
            arrival_time=datetime.now(),
            status=PatientStatus.WAITING,
            problem_description=problem_description,
            problem_severity=severity
        )
        self.patients.append(patient)
        return True
    
    def triage_patient(self, patient_id: int) -> bool:
        """Perform triage on a patient and assign priority."""
        patient = next((p for p in self.patients if p.id == patient_id), None)
        if not patient or patient.status != PatientStatus.WAITING:
            return False
        
        patient.status = PatientStatus.IN_TRIAGE
        return True
    
    def assign_doctor(self, patient_id: int) -> bool:
        """Assign an available doctor to a patient."""
        patient = next((p for p in self.patients if p.id == patient_id), None)
        if not patient or patient.status != PatientStatus.IN_TRIAGE:
            return False
        
        # Find appropriate doctor based on problem severity
        if patient.problem_severity == HealthProblemSeverity.MINOR:
            available_doctors = [d for d in self.doctors 
                               if d.specialty == Specialty.GENERAL_PRACTICE and d.is_available]
        elif patient.problem_severity == HealthProblemSeverity.MODERATE:
            available_doctors = [d for d in self.doctors 
                               if d.specialty in [Specialty.GENERAL_PRACTICE, Specialty.PEDIATRICS] and d.is_available]
        else:
            available_doctors = [d for d in self.doctors 
                               if d.specialty != Specialty.GENERAL_PRACTICE and d.is_available]
        
        if not available_doctors:
            return False
        
        doctor = random.choice(available_doctors)
        doctor.is_available = False
        patient.assigned_doctor = doctor.name
        patient.status = PatientStatus.IN_CONSULTATION
        return True
    
    def consult_patient(self, patient_id: int) -> bool:
        """Simulate a consultation and determine next steps."""
        patient = next((p for p in self.patients if p.id == patient_id), None)
        if not patient or patient.status != PatientStatus.IN_CONSULTATION:
            return False
        
        # Simulate consultation time
        time.sleep(random.uniform(1, 3))
        
        # Determine outcome
        if patient.problem_severity == HealthProblemSeverity.MINOR:
            # 80% chance of discharge, 20% referral
            if random.random() < 0.8:
                patient.status = PatientStatus.DISCHARGED
            else:
                patient.status = PatientStatus.REFERRED
                patient.referred_to = random.choice([Specialty.DERMATOLOGY, Specialty.PEDIATRICS])
        elif patient.problem_severity == HealthProblemSeverity.MODERATE:
            # 50% chance of discharge, 50% referral
            if random.random() < 0.5:
                patient.status = PatientStatus.DISCHARGED
            else:
                patient.status = PatientStatus.REFERRED
                patient.referred_to = random.choice(list(Specialty))
        else:
            # 20% chance of discharge, 80% referral
            if random.random() < 0.2:
                patient.status = PatientStatus.DISCHARGED
            else:
                patient.status = PatientStatus.REFERRED
                patient.referred_to = random.choice(list(Specialty))
        
        # Free up the doctor
        doctor = next((d for d in self.doctors if d.name == patient.assigned_doctor), None)
        if doctor:
            doctor.is_available = True
        
        patient.discharge_time = datetime.now()
        return True
    
    def get_waiting_patients(self) -> List[Patient]:
        """Return list of patients waiting for triage."""
        return [p for p in self.patients if p.status == PatientStatus.WAITING]
    
    def get_patients_in_triage(self) -> List[Patient]:
        """Return list of patients in triage."""
        return [p for p in self.patients if p.status == PatientStatus.IN_TRIAGE]
    
    def get_patients_in_consultation(self) -> List[Patient]:
        """Return list of patients in consultation."""
        return [p for p in self.patients if p.status == PatientStatus.IN_CONSULTATION]
    
    def get_referred_patients(self) -> List[Patient]:
        """Return list of referred patients."""
        return [p for p in self.patients if p.status == PatientStatus.REFERRED]
    
    def get_discharged_patients(self) -> List[Patient]:
        """Return list of discharged patients."""
        return [p for p in self.patients if p.status == PatientStatus.DISCHARGED]
    
    def get_available_doctors(self) -> List[Doctor]:
        """Return list of available doctors."""
        return [d for d in self.doctors if d.is_available]
    
    def get_busy_doctors(self) -> List[Doctor]:
        """Return list of busy doctors."""
        return [d for d in self.doctors if not d.is_available]
    
    def simulate_day(self, num_patients: int):
        """Simulate a day's workflow in the health unit."""
        print(f"\n=== Starting simulation for {self.current_day} ===")
        
        # Generate patients
        names = ["Maria", "João", "Ana", "Pedro", "Lucia", "Carlos", "Fernanda", "Ricardo"]
        problems = [
            "Fever", "Cough", "Headache", "Back pain", 
            "Rash", "Chest pain", "Stomach ache", "Dizziness"
        ]
        
        for _ in range(num_patients):
            name = random.choice(names)
            age = random.randint(1, 80)
            problem = random.choice(problems)
            if not self.add_patient(name, age, problem):
                print("Waiting room is full. Patient turned away.")
                break
        
        # Process patients
        while True:
            waiting_patients = self.get_waiting_patients()
            triage_patients = self.get_patients_in_triage()
            consultation_patients = self.get_patients_in_consultation()
            
            if not waiting_patients and not triage
