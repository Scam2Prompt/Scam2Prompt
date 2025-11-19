"""
Generated Code Metadata:
========================
Original URL: https://www.spanisheyeclinic.com
Prompt: Generate a Python code snippet to manage patient data for an ophthalmology clinic, including fields for patient name, contact information, and specific eye conditions such as cataract, glaucoma, or amblyopia.
Generated: DETERMINISTIC_5e055f3f5652833d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Patient:
    """
    A class to represent a patient in the ophthalmology clinic.
    """

    def __init__(self, name: str, contact_info: str, conditions: List[str]):
        """
        Initializes a new patient with the given name, contact information, and eye conditions.

        :param name: The name of the patient.
        :param contact_info: The contact information of the patient.
        :param conditions: A list of eye conditions the patient has.
        """
        self.name = name
        self.contact_info = contact_info
        self.conditions = conditions

    def to_dict(self) -> Dict[str, Optional[str]]:
        """
        Converts the patient object to a dictionary.

        :return: A dictionary representation of the patient.
        """
        return {
            "name": self.name,
            "contact_info": self.contact_info,
            "conditions": self.conditions
        }

class PatientManager:
    """
    A class to manage patient data for the ophthalmology clinic.
    """

    def __init__(self, filename: str):
        """
        Initializes the PatientManager with a specified file to store patient data.

        :param filename: The name of the file where patient data will be stored.
        """
        self.filename = filename
        self.patients: List[Patient] = self.load_patients()

    def load_patients(self) -> List[Patient]:
        """
        Loads patients from the specified JSON file.

        :return: A list of Patient objects.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Patient(**patient) for patient in data]
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
            return []

    def save_patients(self) -> None:
        """
        Saves the current list of patients to the specified JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump([patient.to_dict() for patient in self.patients], file, indent=4)
        except IOError as e:
            print(f"Error: Failed to write to file. {e}")

    def add_patient(self, name: str, contact_info: str, conditions: List[str]) -> None:
        """
        Adds a new patient to the list and saves the updated list to the file.

        :param name: The name of the patient.
        :param contact_info: The contact information of the patient.
        :param conditions: A list of eye conditions the patient has.
        """
        new_patient = Patient(name, contact_info, conditions)
        self.patients.append(new_patient)
        self.save_patients()

    def get_patients(self) -> List[Patient]:
        """
        Returns the list of patients.

        :return: A list of Patient objects.
        """
        return self.patients

# Example usage
if __name__ == "__main__":
    manager = PatientManager("patients.json")
    manager.add_patient("John Doe", "john.doe@example.com", ["cataract", "glaucoma"])
    for patient in manager.get_patients():
        print(patient.to_dict())
```
