"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Write a Python code snippet to manage patient data for a foot and ankle surgery clinic, including fields for patient name, date of birth, and surgery type.
Generated: DETERMINISTIC_3729c798049b200a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class Patient:
    """Class to represent a patient in the clinic."""
    
    def __init__(self, name: str, dob: str, surgery_type: str):
        """
        Initialize a new patient instance.

        Args:
            name (str): The name of the patient.
            dob (str): The date of birth of the patient in 'YYYY-MM-DD' format.
            surgery_type (str): The type of surgery the patient will undergo.
        """
        self.name = name
        self.dob = self.validate_dob(dob)
        self.surgery_type = surgery_type

    @staticmethod
    def validate_dob(dob: str) -> str:
        """Validate the date of birth format and return it.

        Args:
            dob (str): The date of birth to validate.

        Returns:
            str: The validated date of birth.

        Raises:
            ValueError: If the date of birth is not in the correct format.
        """
        try:
            datetime.strptime(dob, '%Y-%m-%d')
            return dob
        except ValueError:
            raise ValueError("Date of birth must be in 'YYYY-MM-DD' format.")

    def to_dict(self) -> dict:
        """Convert the patient instance to a dictionary.

        Returns:
            dict: A dictionary representation of the patient.
        """
        return {
            'name': self.name,
            'dob': self.dob,
            'surgery_type': self.surgery_type
        }

class PatientManager:
    """Class to manage patient data for the clinic."""
    
    def __init__(self, filename: str):
        """
        Initialize the patient manager with a file to store patient data.

        Args:
            filename (str): The name of the file to store patient data.
        """
        self.filename = filename
        self.patients = self.load_patients()

    def load_patients(self) -> list:
        """Load patients from the JSON file.

        Returns:
            list: A list of patient dictionaries.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the patient data file.")

    def save_patients(self):
        """Save the current list of patients to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.patients, file, indent=4)

    def add_patient(self, patient: Patient):
        """Add a new patient to the list and save to file.

        Args:
            patient (Patient): The patient instance to add.
        """
        self.patients.append(patient.to_dict())
        self.save_patients()

    def get_patients(self) -> list:
        """Get the list of all patients.

        Returns:
            list: A list of patient dictionaries.
        """
        return self.patients

# Example usage
if __name__ == "__main__":
    manager = PatientManager('patients.json')
    
    # Create a new patient
    try:
        new_patient = Patient(name="John Doe", dob="1985-06-15", surgery_type="Ankle Reconstruction")
        manager.add_patient(new_patient)
        print("Patient added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Retrieve and print all patients
    patients = manager.get_patients()
    print("Current patients:", patients)
```
