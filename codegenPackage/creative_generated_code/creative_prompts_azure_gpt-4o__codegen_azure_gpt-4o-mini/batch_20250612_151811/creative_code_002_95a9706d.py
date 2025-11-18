"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxvillebreastcenter.com
Prompt: Generate code to automate the creation of patient MRI questionnaires, including fields for medical history and breast sensitivity preferences.
Generated: DETERMINISTIC_95a9706d6d932964
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict


class PatientMRIQuestionnaire:
    """
    A class to represent a patient's MRI questionnaire.
    """

    def __init__(self, patient_name: str, patient_id: int) -> None:
        """
        Initializes the questionnaire with basic patient information.

        :param patient_name: The name of the patient.
        :param patient_id: The unique identifier for the patient.
        """
        self.patient_name = patient_name
        self.patient_id = patient_id
        self.medical_history: List[Dict[str, str]] = []
        self.breast_sensitivity: str = ''

    def add_medical_history(self, condition: str, treatment: str) -> None:
        """
        Adds an entry to the patient's medical history.

        :param condition: The medical condition.
        :param treatment: The treatment received.
        """
        if not condition or not treatment:
            raise ValueError("Condition and treatment cannot be empty.")
        
        self.medical_history.append({
            "condition": condition,
            "treatment": treatment
        })

    def set_breast_sensitivity(self, sensitivity: str) -> None:
        """
        Sets the breast sensitivity preference for the patient.

        :param sensitivity: The patient's breast sensitivity preference (e.g., "high", "medium", "low").
        """
        valid_sensitivities = ['high', 'medium', 'low']
        if sensitivity not in valid_sensitivities:
            raise ValueError(f"Sensitivity must be one of {valid_sensitivities}.")
        
        self.breast_sensitivity = sensitivity

    def to_json(self) -> str:
        """
        Converts the questionnaire data to a JSON string.

        :return: A JSON string representing the questionnaire.
        """
        return json.dumps({
            "patient_name": self.patient_name,
            "patient_id": self.patient_id,
            "medical_history": self.medical_history,
            "breast_sensitivity": self.breast_sensitivity
        }, indent=4)

    def save_to_file(self, filename: str) -> None:
        """
        Saves the questionnaire to a file in JSON format.

        :param filename: The name of the file to save the questionnaire.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the PatientMRIQuestionnaire
        questionnaire = PatientMRIQuestionnaire(patient_name="Jane Doe", patient_id=12345)

        # Adding medical history entries
        questionnaire.add_medical_history(condition="Breast Cancer", treatment="Radiation")
        questionnaire.add_medical_history(condition="Hypertension", treatment="Medication")

        # Setting breast sensitivity preference
        questionnaire.set_breast_sensitivity(sensitivity="high")

        # Save the questionnaire to a file
        questionnaire.save_to_file("patient_questionnaire.json")
        print("Questionnaire saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
