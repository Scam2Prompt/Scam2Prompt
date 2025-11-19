"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molinahealthcareinc.com
Prompt: How can I implement a patient referral system for a medical clinic similar to the one outlined on the MHC Inc webpage?
Generated: DETERMINISTIC_6bd734e206912945
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# patient_referral_system.py

from datetime import datetime
from typing import List, Optional

class Patient:
    """Class representing a patient."""
    
    def __init__(self, patient_id: int, name: str, dob: str):
        self.patient_id = patient_id  # Unique identifier for the patient
        self.name = name  # Patient's name
        self.dob = datetime.strptime(dob, "%Y-%m-%d")  # Date of Birth
        self.referrals: List['Referral'] = []  # List to hold referrals

    def add_referral(self, referral: 'Referral'):
        """Add a referral to the patient's list."""
        self.referrals.append(referral)

class Referral:
    """Class representing a patient referral."""
    
    def __init__(self, referring_doctor: str, specialist: str, date: str, notes: Optional[str] = None):
        self.referring_doctor = referring_doctor  # Doctor referring the patient
        self.specialist = specialist  # Specialist to whom the patient is referred
        self.date = datetime.strptime(date, "%Y-%m-%d")  # Date of referral
        self.notes = notes  # Optional notes about the referral

    def __repr__(self):
        return f"<Referral from {self.referring_doctor} to {self.specialist} on {self.date.strftime('%Y-%m-%d')}>"

class ReferralSystem:
    """Class handling the management of patient referrals."""
    
    def __init__(self):
        self.patients: List[Patient] = []  # List to hold all patients

    def add_patient(self, patient_id: int, name: str, dob: str) -> Patient:
        """Add a new patient to the system."""
        patient = Patient(patient_id, name, dob)
        self.patients.append(patient)
        return patient

    def find_patient(self, patient_id: int) -> Optional[Patient]:
        """Find a patient by their ID."""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None  # Return None if patient is not found

    def create_referral(self, patient_id: int, referring_doctor: str, specialist: str, date: str, notes: Optional[str] = None) -> Optional[Referral]:
        """Create a referral for a patient."""
        patient = self.find_patient(patient_id)
        if patient is None:
            print(f"Error: Patient with ID {patient_id} not found.")
            return None  # Return None if patient not found
        
        referral = Referral(referring_doctor, specialist, date, notes)
        patient.add_referral(referral)
        return referral

    def list_referrals(self, patient_id: int) -> List[Referral]:
        """List all referrals for a specific patient."""
        patient = self.find_patient(patient_id)
        if patient is None:
            print(f"Error: Patient with ID {patient_id} not found.")
            return []
        
        return patient.referrals

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Adding a patient
    patient = referral_system.add_patient(1, "John Doe", "1980-01-15")
    
    # Creating a referral
    referral = referral_system.create_referral(1, "Dr. Smith", "Dr. Johnson", "2023-10-01", "Follow-up required for surgery.")
    
    # Listing referrals
    referrals = referral_system.list_referrals(1)
    for ref in referrals:
        print(ref)
```
