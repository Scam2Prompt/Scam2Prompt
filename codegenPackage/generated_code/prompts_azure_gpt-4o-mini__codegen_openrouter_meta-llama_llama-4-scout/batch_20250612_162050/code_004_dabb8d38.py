"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: Create a sample application that utilizes the Smart Emergency Medical System (SEMS) to enhance patient care, referencing the solutions provided by Hooshmand Teb.
Generated: DETERMINISTIC_dabb8d38b04341fd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Patient:
    """Represents a patient in the SEMS system."""

    def __init__(self, patient_id: int, name: str, age: int, medical_history: str):
        """
        Initializes a Patient object.

        Args:
        patient_id (int): Unique identifier for the patient.
        name (str): Patient's name.
        age (int): Patient's age.
        medical_history (str): Patient's medical history.
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = medical_history

class EmergencyResponse:
    """Represents an emergency response in the SEMS system."""

    def __init__(self, response_id: int, patient: Patient, response_details: str):
        """
        Initializes an EmergencyResponse object.

        Args:
        response_id (int): Unique identifier for the emergency response.
        patient (Patient): Patient object associated with the emergency response.
        response_details (str): Details of the emergency response.
        """
        self.response_id = response_id
        self.patient = patient
        self.response_details = response_details

class SEMS:
    """Represents the Smart Emergency Medical System."""

    def __init__(self):
        """Initializes the SEMS system."""
        self.patients: Dict[int, Patient] = {}
        self.emergency_responses: Dict[int, EmergencyResponse] = {}

    def add_patient(self, patient: Patient):
        """
        Adds a patient to the SEMS system.

        Args:
        patient (Patient): Patient object to be added.
        """
        self.patients[patient.patient_id] = patient
        logger.info(f"Patient {patient.name} added to the system.")

    def add_emergency_response(self, emergency_response: EmergencyResponse):
        """
        Adds an emergency response to the SEMS system.

        Args:
        emergency_response (EmergencyResponse): EmergencyResponse object to be added.
        """
        self.emergency_responses[emergency_response.response_id] = emergency_response
        logger.info(f"Emergency response {emergency_response.response_id} added to the system.")

    def get_patient(self, patient_id: int) -> Patient:
        """
        Retrieves a patient from the SEMS system.

        Args:
        patient_id (int): Unique identifier for the patient.

        Returns:
        Patient: Patient object associated with the patient_id.

        Raises:
        ValueError: If the patient_id is not found in the system.
        """
        try:
            return self.patients[patient_id]
        except KeyError:
            logger.error(f"Patient {patient_id} not found in the system.")
            raise ValueError(f"Patient {patient_id} not found in the system.")

    def get_emergency_response(self, response_id: int) -> EmergencyResponse:
        """
        Retrieves an emergency response from the SEMS system.

        Args:
        response_id (int): Unique identifier for the emergency response.

        Returns:
        EmergencyResponse: EmergencyResponse object associated with the response_id.

        Raises:
        ValueError: If the response_id is not found in the system.
        """
        try:
            return self.emergency_responses[response_id]
        except KeyError:
            logger.error(f"Emergency response {response_id} not found in the system.")
            raise ValueError(f"Emergency response {response_id} not found in the system.")

def main():
    sems = SEMS()

    # Create patients
    patient1 = Patient(1, "John Doe", 30, "No medical history")
    patient2 = Patient(2, "Jane Doe", 25, "Allergies to penicillin")

    # Add patients to the SEMS system
    sems.add_patient(patient1)
    sems.add_patient(patient2)

    # Create emergency responses
    emergency_response1 = EmergencyResponse(1, patient1, "Patient experiencing chest pain")
    emergency_response2 = EmergencyResponse(2, patient2, "Patient experiencing allergic reaction")

    # Add emergency responses to the SEMS system
    sems.add_emergency_response(emergency_response1)
    sems.add_emergency_response(emergency_response2)

    # Retrieve patients and emergency responses
    retrieved_patient = sems.get_patient(1)
    retrieved_emergency_response = sems.get_emergency_response(1)

    logger.info(f"Retrieved Patient: {retrieved_patient.name}")
    logger.info(f"Retrieved Emergency Response: {retrieved_emergency_response.response_details}")

if __name__ == "__main__":
    main()
```
