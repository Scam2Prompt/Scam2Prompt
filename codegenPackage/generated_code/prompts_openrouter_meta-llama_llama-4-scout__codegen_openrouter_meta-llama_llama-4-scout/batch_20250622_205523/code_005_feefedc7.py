"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: "Develop a data analysis code to track patient outcomes and therapy effectiveness for a child neurology clinic, using metrics like number of cases registered and hours of free therapy provided, as mentioned in ICON Foundation's impact statistics."
Generated: DETERMINISTIC_feefedc7f4cd303a
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime

class PatientOutcomeTracker:
    """
    A class to track patient outcomes and therapy effectiveness for a child neurology clinic.

    Attributes:
    -----------
    patient_data : list
        A list of dictionaries containing patient data.
    therapy_data : list
        A list of dictionaries containing therapy data.

    Methods:
    --------
    register_patient(patient_id, age, diagnosis)
        Registers a new patient.
    log_therapy(patient_id, hours)
        Logs therapy hours for a patient.
    get_total_cases_registered()
        Returns the total number of cases registered.
    get_total_hours_free_therapy()
        Returns the total hours of free therapy provided.
    get_patient_outcomes()
        Returns a dictionary of patient outcomes.
    """

    def __init__(self):
        self.patient_data = []
        self.therapy_data = []

    def register_patient(self, patient_id, age, diagnosis):
        """
        Registers a new patient.

        Args:
        -----
        patient_id (str): Unique patient ID.
        age (int): Patient age.
        diagnosis (str): Patient diagnosis.

        Raises:
        ------
        ValueError: If patient ID already exists.
        """
        if any(patient['patient_id'] == patient_id for patient in self.patient_data):
            raise ValueError("Patient ID already exists")
        self.patient_data.append({
            'patient_id': patient_id,
            'age': age,
            'diagnosis': diagnosis,
            'therapy_hours': 0
        })

    def log_therapy(self, patient_id, hours):
        """
        Logs therapy hours for a patient.

        Args:
        -----
        patient_id (str): Unique patient ID.
        hours (float): Therapy hours.

        Raises:
        ------
        ValueError: If patient ID does not exist.
        """
        patient = next((patient for patient in self.patient_data if patient['patient_id'] == patient_id), None)
        if patient is None:
            raise ValueError("Patient ID does not exist")
        patient['therapy_hours'] += hours
        self.therapy_data.append({
            'patient_id': patient_id,
            'hours': hours,
            'timestamp': datetime.now()
        })

    def get_total_cases_registered(self):
        """
        Returns the total number of cases registered.

        Returns:
        -------
        int: Total cases registered.
        """
        return len(self.patient_data)

    def get_total_hours_free_therapy(self):
        """
        Returns the total hours of free therapy provided.

        Returns:
        -------
        float: Total hours of free therapy provided.
        """
        return sum(patient['therapy_hours'] for patient in self.patient_data)

    def get_patient_outcomes(self):
        """
        Returns a dictionary of patient outcomes.

        Returns:
        -------
        dict: Patient outcomes.
        """
        outcomes = {}
        for patient in self.patient_data:
            outcomes[patient['patient_id']] = {
                'age': patient['age'],
                'diagnosis': patient['diagnosis'],
                'therapy_hours': patient['therapy_hours']
            }
        return outcomes


def main():
    tracker = PatientOutcomeTracker()

    # Register patients
    tracker.register_patient('PAT-001', 5, 'Cerebral Palsy')
    tracker.register_patient('PAT-002', 7, 'Epilepsy')

    # Log therapy hours
    tracker.log_therapy('PAT-001', 2.5)
    tracker.log_therapy('PAT-002', 1.0)
    tracker.log_therapy('PAT-001', 3.0)

    # Get total cases registered
    total_cases = tracker.get_total_cases_registered()
    print(f"Total cases registered: {total_cases}")

    # Get total hours of free therapy provided
    total_hours = tracker.get_total_hours_free_therapy()
    print(f"Total hours of free therapy provided: {total_hours}")

    # Get patient outcomes
    patient_outcomes = tracker.get_patient_outcomes()
    print("Patient Outcomes:")
    for patient_id, outcome in patient_outcomes.items():
        print(f"Patient ID: {patient_id}")
        print(f"Age: {outcome['age']}")
        print(f"Diagnosis: {outcome['diagnosis']}")
        print(f" Therapy Hours: {outcome['therapy_hours']}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
