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

Here is a Python implementation for automating the creation of patient MRI questionnaires:

```python
import json
import datetime

class MRIQuestionnaire:
    """
    Class to represent and generate a patient MRI questionnaire.
    """
    def __init__(self):
        """
        Initialize questionnaire with default values.
        """
        self.questionnaire = {
            "patient_info": {
                "name": "",
                "age": 0,
                "gender": "",
                "contact_info": {
                    "phone": "",
                    "email": ""
                }
            },
            "medical_history": {
                "has_allergies": False,
                "allergies_details": "",
                "current_medications": [],
                "previous_surgeries": [],
                "medical_conditions": []
            },
            "breast_sensitivity_preferences": {
                "left_breast_sensitive": False,
                "right_breast_sensitive": False,
                "comments": ""
            },
            "submission_date": str(datetime.date.today())
        }

    def update_patient_info(self, name, age, gender, phone, email):
        """
        Update patient information section.

        Args:
        - name (str): Patient's full name.
        - age (int): Patient's age.
        - gender (str): Patient's gender.
        - phone (str): Patient's phone number.
        - email (str): Patient's email address.
        """
        self.questionnaire["patient_info"].update({
            "name": name,
            "age": age,
            "gender": gender,
            "contact_info": {
                "phone": phone,
                "email": email
            }
        })

    def update_medical_history(self, allergies, allergies_details, medications, surgeries, conditions):
        """
        Update medical history section.

        Args:
        - allergies (bool): Indicates if the patient has allergies.
        - allergies_details (str): Details about the patient's allergies.
        - medications (list): List of current medications.
        - surgeries (list): List of previous surgeries.
        - conditions (list): List of medical conditions.
        """
        self.questionnaire["medical_history"].update({
            "has_allergies": allergies,
            "allergies_details": allergies_details,
            "current_medications": medications,
            "previous_surgeries": surgeries,
            "medical_conditions": conditions
        })

    def update_breast_sensitivity_preferences(self, left_sensitive, right_sensitive, comments):
        """
        Update breast sensitivity preferences section.

        Args:
        - left_sensitive (bool): Indicates if the left breast is sensitive.
        - right_sensitive (bool): Indicates if the right breast is sensitive.
        - comments (str): Additional comments regarding sensitivity preferences.
        """
        self.questionnaire["breast_sensitivity_preferences"].update({
            "left_breast_sensitive": left_sensitive,
            "right_breast_sensitive": right_sensitive,
            "comments": comments
        })

    def save_questionnaire_to_file(self, filename):
        """
        Save the questionnaire as a JSON file.

        Args:
        - filename (str): Name of the file to save questionnaire.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.questionnaire, file, indent=4)
            print(f"Questionnaire saved successfully to {filename}.")
        except Exception as e:
            print(f"Error saving questionnaire to file: {e}")

    def load_questionnaire_from_file(self, filename):
        """
        Load the questionnaire from a JSON file.

        Args:
        - filename (str): Name of the file to load questionnaire.
        """
        try:
            with open(filename, 'r') as file:
                self.questionnaire = json.load(file)
            print(f"Questionnaire loaded successfully from {filename}.")
        except Exception as e:
            print(f"Error loading questionnaire from file: {e}")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the MRIQuestionnaire
    mri_questionnaire = MRIQuestionnaire()

    # Update patient information
    mri_questionnaire.update_patient_info(
        name="Jane Doe",
        age=35,
        gender="Female",
        phone="123-456-7890",
        email="jane.doe@example.com"
    )

    # Update medical history
    mri_questionnaire.update_medical_history(
        allergies=True,
        allergies_details="Peanuts and shellfish",
        medications=["Aspirin", "Ibuprofen"],
        surgeries=["Appendectomy"],
        conditions=["Hypertension", "Asthma"]
    )

    # Update breast sensitivity preferences
    mri_questionnaire.update_breast_sensitivity_preferences(
        left_sensitive=True,
        right_sensitive=False,
        comments="Sensitive only on the left side during MRI."
    )

    # Save the questionnaire to a file
    mri_questionnaire.save_questionnaire_to_file("mri_questionnaire.json")

    # Load the questionnaire from a file (example)
    mri_questionnaire.load_questionnaire_from_file("mri_questionnaire.json")
```

This code provides a clean and well-documented solution for automating the creation, updating, saving, and loading of patient MRI questionnaires. It includes proper error handling and demonstrates usage best practices.
