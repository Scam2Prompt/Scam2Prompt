"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Create a simulation in Python to model the workflow of a Unidade Básica de Saúde (Basic Health Unit), including patient intake, problem-solving for simple cases, and referrals to specialty clinics or hospitals.
Generated: DETERMINISTIC_c67fef0e9ce0bfcf
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import queue
from random import choice, randint


class Patient:
    """
    Represents a patient in the health unit.
    """

    def __init__(self, name):
        self.name = name
        self.symptoms = self.generate_symptoms()
        self.is_simple_case = self.determine_case()

    def generate_symptoms(self):
        """
        Generate random symptoms for the patient.
        """
        symptom_list = ["fever", "cough", "headache", "rash", "stomach pain"]
        return choice(symptom_list)

    def determine_case(self):
        """
        Randomly determine if the patient's case is simple (True) or complex (False).
        """
        return randint(0, 1) == 0


class BasicHealthUnit:
    """
    Simulates the workflow of a Unidade Básica de Saúde (Basic Health Unit).
    """

    def __init__(self):
        self.intake_queue = queue.Queue()
        self.referral_queue = []
        self.simple_cases_resolved = 0
        self.total_patients = 0

    def intake_patient(self, patient):
        """
        Add a patient to the intake queue.
        """
        self.intake_queue.put(patient)
        self.total_patients += 1

    def handle_patients(self):
        """
        Process patients from the intake queue.
        Resolve simple cases and refer complex cases.
        """
        while not self.intake_queue.empty():
            patient = self.intake_queue.get()

            if patient.is_simple_case:
                # Handle simple case
                self.resolve_simple_case(patient)
            else:
                # Refer complex case
                self.refer_to_specialty_clinic(patient)

    def resolve_simple_case(self, patient):
        """
        Resolve a simple case for the patient.
        """
        print(f"Resolving simple case for patient: {patient.name} (Symptoms: {patient.symptoms}).")
        self.simple_cases_resolved += 1

    def refer_to_specialty_clinic(self, patient):
        """
        Refer a patient with a complex case to a specialty clinic or hospital.
        """
        print(f"Referring patient: {patient.name} (Symptoms: {patient.symptoms}) to specialty clinic or hospital.")
        self.referral_queue.append(patient)

    def generate_report(self):
        """
        Generate a summary report of the basic health unit workflow.
        """
        print("\n--- Unidade Básica de Saúde Workflow Report ---")
        print(f"Total patients processed: {self.total_patients}")
        print(f"Simple cases resolved: {self.simple_cases_resolved}")
        print(f"Patients referred to specialty clinics/hospitals: {len(self.referral_queue)}")
        print("-------------------------------------------------")


# Simulation
if __name__ == "__main__":
    # Initialize the health unit
    health_unit = BasicHealthUnit()

    # Create a list of sample patients
    sample_patients = [Patient(name=f"Patient_{i}") for i in range(1, 11)]

    # Intake patients into the health unit
    for patient in sample_patients:
        health_unit.intake_patient(patient)

    # Handle patients
    health_unit.handle_patients()

    # Generate a report
    health_unit.generate_report()
```
