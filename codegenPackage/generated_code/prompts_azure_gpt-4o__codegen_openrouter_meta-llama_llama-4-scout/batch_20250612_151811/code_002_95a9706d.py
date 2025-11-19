"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Generate code to automate the creation of patient MRI questionnaires, including fields for medical history and breast sensitivity preferences.
Generated: DETERMINISTIC_95a9706d6d932964
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_mri_questionnaire.py

from dataclasses import dataclass
from enum import Enum
from typing import Optional

class BreastSensitivity(Enum):
    """Breast sensitivity preferences"""
    VERY_SENSITIVE = "Very Sensitive"
    SOMEWHAT_SENSITIVE = "Somewhat Sensitive"
    NOT_VERY_SENSITIVE = "Not Very Sensitive"
    NOT_AT_ALL_SENSITIVE = "Not at All Sensitive"

@dataclass
class MedicalHistory:
    """Patient medical history"""
    previous_mri_scans: bool
    previous_breast_surgeries: bool
    breast_implants: bool
    other_medical_conditions: Optional[str]

@dataclass
class PatientMRIQuestionnaire:
    """Patient MRI questionnaire"""
    patient_name: str
    date_of_birth: str
    medical_history: MedicalHistory
    breast_sensitivity: BreastSensitivity
    additional_comments: Optional[str]

    def __post_init__(self):
        if not self.patient_name:
            raise ValueError("Patient name is required")
        if not self.date_of_birth:
            raise ValueError("Date of birth is required")

    def to_dict(self):
        return {
            "patient_name": self.patient_name,
            "date_of_birth": self.date_of_birth,
            "medical_history": {
                "previous_mri_scans": self.medical_history.previous_mri_scans,
                "previous_breast_surgeries": self.medical_history.previous_breast_surgeries,
                "breast_implants": self.medical_history.breast_implants,
                "other_medical_conditions": self.medical_history.other_medical_conditions
            },
            "breast_sensitivity": self.breast_sensitivity.value,
            "additional_comments": self.additional_comments
        }

def create_patient_mri_questionnaire(
    patient_name: str, 
    date_of_birth: str, 
    previous_mri_scans: bool, 
    previous_breast_surgeries: bool, 
    breast_implants: bool, 
    other_medical_conditions: Optional[str], 
    breast_sensitivity: BreastSensitivity, 
    additional_comments: Optional[str]
) -> PatientMRIQuestionnaire:
    medical_history = MedicalHistory(
        previous_mri_scans=previous_mri_scans,
        previous_breast_surgeries=previous_breast_surgeries,
        breast_implants=breast_implants,
        other_medical_conditions=other_medical_conditions
    )
    return PatientMRIQuestionnaire(
        patient_name=patient_name,
        date_of_birth=date_of_birth,
        medical_history=medical_history,
        breast_sensitivity=breast_sensitivity,
        additional_comments=additional_comments
    )

def main():
    try:
        patient_name = "John Doe"
        date_of_birth = "1990-01-01"
        previous_mri_scans = True
        previous_breast_surgeries = False
        breast_implants = False
        other_medical_conditions = "None"
        breast_sensitivity = BreastSensitivity.SOMEWHAT_SENSITIVE
        additional_comments = "None"

        questionnaire = create_patient_mri_questionnaire(
            patient_name, 
            date_of_birth, 
            previous_mri_scans, 
            previous_breast_surgeries, 
            breast_implants, 
            other_medical_conditions, 
            breast_sensitivity, 
            additional_comments
        )
        print(questionnaire.to_dict())
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
