"""
Generated Code Metadata:
========================
Original URL: https://molinahealthcareinc.com
Prompt: How can I implement a patient referral system for a medical clinic similar to the one outlined on the MHC Inc webpage?
Generated: DETERMINISTIC_6bd734e206912945
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_referral_system.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class ReferralStatus(str, Enum):
    """Enum for referral status"""
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class Patient:
    """Class representing a patient"""
    def __init__(self, patient_id: int, name: str, date_of_birth: str):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

class Doctor:
    """Class representing a doctor"""
    def __init__(self, doctor_id: int, name: str, specialty: str):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Referral:
    """Class representing a referral"""
    def __init__(self, referral_id: int, patient: Patient, doctor: Doctor, status: ReferralStatus = ReferralStatus.PENDING):
        self.referral_id = referral_id
        self.patient = patient
        self.doctor = doctor
        self.status = status
        self.referred_at = datetime.now()

class PatientReferralSystem:
    """Class representing the patient referral system"""
    def __init__(self):
        self.patients: Dict[int, Patient] = {}
        self.doctors: Dict[int, Doctor] = {}
        self.referrals: Dict[int, Referral] = {}

    def add_patient(self, patient: Patient):
        """Add a patient to the system"""
        self.patients[patient.patient_id] = patient

    def add_doctor(self, doctor: Doctor):
        """Add a doctor to the system"""
        self.doctors[doctor.doctor_id] = doctor

    def create_referral(self, referral_id: int, patient_id: int, doctor_id: int) -> Referral:
        """Create a new referral"""
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        if doctor_id not in self.doctors:
            raise ValueError("Doctor not found")

        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]
        referral = Referral(referral_id, patient, doctor)
        self.referrals[referral_id] = referral
        return referral

    def update_referral_status(self, referral_id: int, status: ReferralStatus):
        """Update the status of a referral"""
        if referral_id not in self.referrals:
            raise ValueError("Referral not found")
        self.referrals[referral_id].status = status

    def get_referral(self, referral_id: int) -> Referral:
        """Get a referral by ID"""
        return self.referrals.get(referral_id)

def main():
    # Create the patient referral system
    system = PatientReferralSystem()

    # Create patients
    patient1 = Patient(1, "John Doe", "1990-01-01")
    patient2 = Patient(2, "Jane Doe", "1995-06-01")

    # Create doctors
    doctor1 = Doctor(1, "Dr. Smith", "Cardiology")
    doctor2 = Doctor(2, "Dr. Johnson", "Neurology")

    # Add patients and doctors to the system
    system.add_patient(patient1)
    system.add_patient(patient2)
    system.add_doctor(doctor1)
    system.add_doctor(doctor2)

    # Create referrals
    referral1 = system.create_referral(1, 1, 1)
    referral2 = system.create_referral(2, 2, 2)

    # Print referrals
    print("Referral 1:")
    print(f"Patient: {referral1.patient.name}")
    print(f"Doctor: {referral1.doctor.name}")
    print(f"Status: {referral1.status.value}")

    print("\nReferral 2:")
    print(f"Patient: {referral2.patient.name}")
    print(f"Doctor: {referral2.doctor.name}")
    print(f"Status: {referral2.status.value}")

    # Update referral status
    system.update_referral_status(1, ReferralStatus.ACCEPTED)

    # Print updated referral
    updated_referral = system.get_referral(1)
    print("\nUpdated Referral 1:")
    print(f"Patient: {updated_referral.patient.name}")
    print(f"Doctor: {updated_referral.doctor.name}")
    print(f"Status: {updated_referral.status.value}")

if __name__ == "__main__":
    main()
```
