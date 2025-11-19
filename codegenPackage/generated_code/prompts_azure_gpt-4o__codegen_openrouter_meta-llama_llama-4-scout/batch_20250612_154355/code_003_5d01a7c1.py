"""
Generated Code Metadata:
========================
Original URL: https://molinahealthcareinc.com
Prompt: Provide an example of code to create a referral system for doctors to admit patients to a medical center, as mentioned in the "Refer a patient" section of the Molina Healthcare Inc. website.
Generated: DETERMINISTIC_5d01a7c11dd81b4e
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

from datetime import datetime
from typing import Dict, List

class Patient:
    """Represents a patient in the referral system."""

    def __init__(self, patient_id: int, name: str, date_of_birth: str):
        """
        Initializes a Patient object.

        Args:
        - patient_id (int): Unique identifier for the patient.
        - name (str): Patient's name.
        - date_of_birth (str): Patient's date of birth in YYYY-MM-DD format.
        """
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

class Doctor:
    """Represents a doctor in the referral system."""

    def __init__(self, doctor_id: int, name: str, specialty: str):
        """
        Initializes a Doctor object.

        Args:
        - doctor_id (int): Unique identifier for the doctor.
        - name (str): Doctor's name.
        - specialty (str): Doctor's specialty.
        """
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Referral:
    """Represents a referral in the system."""

    def __init__(self, referral_id: int, patient: Patient, referring_doctor: Doctor, admitted_doctor: Doctor, referral_date: str):
        """
        Initializes a Referral object.

        Args:
        - referral_id (int): Unique identifier for the referral.
        - patient (Patient): Patient being referred.
        - referring_doctor (Doctor): Doctor referring the patient.
        - admitted_doctor (Doctor): Doctor admitting the patient.
        - referral_date (str): Date of referral in YYYY-MM-DD format.
        """
        self.referral_id = referral_id
        self.patient = patient
        self.referring_doctor = referring_doctor
        self.admitted_doctor = admitted_doctor
        self.referral_date = datetime.strptime(referral_date, "%Y-%m-%d")

class ReferralSystem:
    """Manages referrals between doctors and patients."""

    def __init__(self):
        self.patients: Dict[int, Patient] = {}
        self.doctors: Dict[int, Doctor] = {}
        self.referrals: Dict[int, Referral] = {}

    def add_patient(self, patient: Patient):
        """Adds a patient to the system."""
        self.patients[patient.patient_id] = patient

    def add_doctor(self, doctor: Doctor):
        """Adds a doctor to the system."""
        self.doctors[doctor.doctor_id] = doctor

    def create_referral(self, referral: Referral):
        """Creates a new referral in the system."""
        self.referrals[referral.referral_id] = referral

    def get_referral(self, referral_id: int) -> Referral:
        """
        Retrieves a referral by ID.

        Args:
        - referral_id (int): ID of the referral to retrieve.

        Returns:
        - Referral: The referral object, or None if not found.
        """
        return self.referrals.get(referral_id)

def main():
    # Create a referral system
    system = ReferralSystem()

    # Create patients
    patient1 = Patient(1, "John Doe", "1990-01-01")
    patient2 = Patient(2, "Jane Smith", "1995-06-01")

    # Add patients to the system
    system.add_patient(patient1)
    system.add_patient(patient2)

    # Create doctors
    doctor1 = Doctor(1, "Dr. Bob Johnson", "Cardiology")
    doctor2 = Doctor(2, "Dr. Alice Brown", "Oncology")

    # Add doctors to the system
    system.add_doctor(doctor1)
    system.add_doctor(doctor2)

    # Create referrals
    referral1 = Referral(1, patient1, doctor1, doctor2, "2022-01-01")
    referral2 = Referral(2, patient2, doctor2, doctor1, "2022-06-01")

    # Add referrals to the system
    system.create_referral(referral1)
    system.create_referral(referral2)

    # Retrieve and print referrals
    print("Referral 1:")
    referral = system.get_referral(1)
    if referral:
        print(f"Patient: {referral.patient.name}")
        print(f"Referring Doctor: {referral.referring_doctor.name}")
        print(f"Admitted Doctor: {referral.admitted_doctor.name}")
        print(f"Referral Date: {referral.referral_date.date()}")
    else:
        print("Not found")

    print("\nReferral 2:")
    referral = system.get_referral(2)
    if referral:
        print(f"Patient: {referral.patient.name}")
        print(f"Referring Doctor: {referral.referring_doctor.name}")
        print(f"Admitted Doctor: {referral.admitted_doctor.name}")
        print(f"Referral Date: {referral.referral_date.date()}")
    else:
        print("Not found")

if __name__ == "__main__":
    main()
```
