"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Write code to implement a role-based access control system for healthcare professionals in a SUS-inspired system, ensuring that general practitioners, nurses, and community health agents have access to relevant patient data.
Generated: DETERMINISTIC_88181a014dd5f0a6
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

# Define roles for healthcare professionals
class Role(Enum):
    GENERAL_PRACTITIONER = 1
    NURSE = 2
    COMMUNITY_HEALTH_AGENT = 3

# Define patient data structure
class Patient:
    def __init__(self, patient_id: int, name: str, data: Dict):
        self.patient_id = patient_id
        self.name = name
        self.data = data

# Define access control class
class AccessControl:
    def __init__(self):
        # Initialize role-based access control rules
        self.access_rules = {
            Role.GENERAL_PRACTITIONER: ["medical_history", "diagnosis", "treatment"],
            Role.NURSE: ["medical_history", "vital_signs", "medication"],
            Role.COMMUNITY_HEALTH_AGENT: ["medical_history", "vaccination_history"]
        }

    # Method to check access for a specific role
    def check_access(self, role: Role, patient_data: Dict, requested_fields: List[str]):
        allowed_fields = self.access_rules.get(role, [])
        for field in requested_fields:
            if field not in allowed_fields:
                raise PermissionError(f"Role {role.name} does not have access to field: {field}")
        return {field: patient_data.get(field) for field in requested_fields}

# Define healthcare professional class
class HealthcareProfessional:
    def __init__(self, professional_id: int, name: str, role: Role):
        self.professional_id = professional_id
        self.name = name
        self.role = role

    # Method to access patient data
    def access_patient_data(self, patient: Patient, requested_fields: List[str], access_control: AccessControl):
        try:
            accessed_data = access_control.check_access(self.role, patient.data, requested_fields)
            return accessed_data
        except PermissionError as e:
            print(f"Error: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create patients
    patient1 = Patient(1, "John Doe", {
        "medical_history": "Hypertension",
        "diagnosis": "High Blood Pressure",
        "treatment": "Medication",
        "vital_signs": "BP 140/90",
        "medication": "Lisinopril",
        "vaccination_history": "COVID-19 vaccinated"
    })

    # Create healthcare professionals
    gp = HealthcareProfessional(1, "Dr. Smith", Role.GENERAL_PRACTITIONER)
    nurse = HealthcareProfessional(2, "Nurse Johnson", Role.NURSE)
    cha = HealthcareProfessional(3, "CHA Davis", Role.COMMUNITY_HEALTH_AGENT)

    # Create access control instance
    access_control = AccessControl()

    # Access patient data
    gp_data = gp.access_patient_data(patient1, ["medical_history", "diagnosis", "treatment"], access_control)
    nurse_data = nurse.access_patient_data(patient1, ["medical_history", "vital_signs", "medication"], access_control)
    cha_data = cha.access_patient_data(patient1, ["medical_history", "vaccination_history"], access_control)

    # Print accessed data
    print("GP Data:", gp_data)
    print("Nurse Data:", nurse_data)
    print("CHA Data:", cha_data)

    # Test unauthorized access
    try:
        gp.access_patient_data(patient1, ["vital_signs"], access_control)
    except PermissionError as e:
        print(f"Error: {e}")
```
