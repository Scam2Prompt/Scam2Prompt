"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molinahealthcareinc.com
Prompt: Provide an example of code to create a referral system for doctors to admit patients to a medical center, as mentioned in the "Refer a patient" section of the Molina Healthcare Inc. website.
Generated: DETERMINISTIC_5d01a7c11dd81b4e
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

from datetime import datetime
from typing import List, Optional

class Patient:
    """Class representing a patient."""

    def __init__(self, name: str, dob: str):
        """
        Initialize a Patient instance.

        Args:
            name (str): Name of the patient.
            dob (str): Date of birth of the patient in 'YYYY-MM-DD' format.
        """
        self.name = name
        self.dob = datetime.strptime(dob, '%Y-%m-%d')
        self.referral_records: List[Referral] = []

class Doctor:
    """Class representing a doctor."""

    def __init__(self, name: str, specialty: str):
        """
        Initialize a Doctor instance.

        Args:
            name (str): Name of the doctor.
            specialty (str): Specialty of the doctor.
        """
        self.name = name
        self.specialty = specialty

class Referral:
    """Class representing a referral from one doctor to another."""

    def __init__(self, referring_doctor: Doctor, patient: Patient, referred_doctor: Doctor, reason: str):
        """
        Initialize a Referral instance.

        Args:
            referring_doctor (Doctor): The doctor making the referral.
            patient (Patient): The patient being referred.
            referred_doctor (Doctor): The doctor receiving the referral.
            reason (str): Reason for the referral.
        """
        self.referring_doctor = referring_doctor
        self.patient = patient
        self.referred_doctor = referred_doctor
        self.reason = reason
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Referral from Dr. {self.referring_doctor.name} to Dr. {self.referred_doctor.name} for {self.patient.name} ({self.reason}) on {self.timestamp}"

class ReferralSystem:
    """Class to manage the referral system."""

    def __init__(self):
        self.referrals: List[Referral] = []

    def create_referral(self, referring_doctor: Doctor, patient: Patient, referred_doctor: Doctor, reason: str) -> Optional[Referral]:
        """
        Create a new referral.

        Args:
            referring_doctor (Doctor): The doctor making the referral.
            patient (Patient): The patient being referred.
            referred_doctor (Doctor): The doctor receiving the referral.
            reason (str): Reason for the referral.

        Returns:
            Referral: The created referral instance or None if an error occurs.
        """
        try:
            referral = Referral(referring_doctor, patient, referred_doctor, reason)
            self.referrals.append(referral)
            patient.referral_records.append(referral)
            return referral
        except Exception as e:
            print(f"Error creating referral: {e}")
            return None

    def get_referrals_for_patient(self, patient: Patient) -> List[Referral]:
        """
        Retrieve all referrals for a specific patient.

        Args:
            patient (Patient): The patient whose referrals should be retrieved.

        Returns:
            List[Referral]: A list of referrals for the patient.
        """
        return patient.referral_records

# Example Usage
if __name__ == "__main__":
    # Create doctors
    dr_smith = Doctor("John Smith", "Cardiology")
    dr_adams = Doctor("Jane Adams", "Neurology")

    # Create a patient
    patient_jones = Patient("Emily Jones", "1985-05-15")

    # Initialize the referral system
    referral_system = ReferralSystem()

    # Create a referral
    referral = referral_system.create_referral(dr_smith, patient_jones, dr_adams, "Consult for migraines")

    # Output the referral
    if referral:
        print(referral)

    # Get referrals for a patient
    referrals_for_jones = referral_system.get_referrals_for_patient(patient_jones)
    print(f"Referrals for {patient_jones.name}:")
    for r in referrals_for_jones:
        print(r)
```
