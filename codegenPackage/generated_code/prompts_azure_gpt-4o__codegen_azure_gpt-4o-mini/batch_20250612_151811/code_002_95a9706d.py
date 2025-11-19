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
import json
from typing import List, Dict

class PatientMRIQuestionnaire:
    """
    A class to represent a Patient MRI Questionnaire.
    """

    def __init__(self, patient_name: str, patient_id: str):
        """
        Initializes the PatientMRIQuestionnaire with patient details.

        :param patient_name: Name of the patient
        :param patient_id: Unique identifier for the patient
        """
        self.patient_name = patient_name
        self.patient_id = patient_id
        self.medical_history = []
        self.breast_sensitivity_preferences = None

    def add_medical_history(self, condition: str):
        """
        Adds a medical condition to the patient's medical history.

        :param condition: A string representing a medical condition
        """
        if condition:
            self.medical_history.append(condition)
        else:
            raise ValueError("Condition cannot be empty.")

    def set_breast_sensitivity_preferences(self, preferences: str):
        """
        Sets the breast sensitivity preferences for the patient.

        :param preferences: A string representing the sensitivity preferences
        """
        if preferences in ['High', 'Medium', 'Low']:
            self.breast_sensitivity_preferences = preferences
        else:
            raise ValueError("Preferences must be 'High', 'Medium', or 'Low'.")

    def to_dict(self) -> Dict:
        """
        Converts the questionnaire data to a dictionary format.

        :return: A dictionary representation of the questionnaire
        """
        return {
            "patient_name": self.patient_name,
            "patient_id": self.patient_id,
            "medical_history": self.medical_history,
            "breast_sensitivity_preferences": self.breast_sensitivity_preferences
        }

    def save_to_file(self, filename: str):
        """
        Saves the questionnaire data to a JSON file.

        :param filename: The name of the file to save the data
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving to file: {e}")

def main():
    """
    Main function to demonstrate the creation of a Patient MRI Questionnaire.
    """
    try:
        # Create a new patient MRI questionnaire
        patient_questionnaire = PatientMRIQuestionnaire("Jane Doe", "P123456")

        # Add medical history
        patient_questionnaire.add_medical_history("Asthma")
        patient_questionnaire.add_medical_history("Diabetes")

        # Set breast sensitivity preferences
        patient_questionnaire.set_breast_sensitivity_preferences("Medium")

        # Save the questionnaire to a file
        patient_questionnaire.save_to_file("patient_mri_questionnaire.json")

        print("Patient MRI Questionnaire created and saved successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
