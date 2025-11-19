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

class Patient:
    """
    A class to represent a patient in the ophthalmology clinic.
    """
    def __init__(self, name, contact_info, eye_conditions):
        """
        Initialize a Patient object.

        :param name: str - Full name of the patient
        :param contact_info: dict - Contact information (e.g., phone, email)
        :param eye_conditions: list - List of diagnosed eye conditions
        """
        self.name = name
        self.contact_info = contact_info
        self.eye_conditions = eye_conditions

    def to_dict(self):
        """
        Convert the Patient object to a dictionary.

        :return: dict - Dictionary representation of the patient
        """
        return {
            "name": self.name,
            "contact_info": self.contact_info,
            "eye_conditions": self.eye_conditions
        }


class OphthalmologyClinic:
    """
    A class to manage patient data for an ophthalmology clinic.
    """
    def __init__(self):
        """
        Initialize the clinic with an empty patient database.
        """
        self.patients = []

    def add_patient(self, patient):
        """
        Add a new patient to the clinic.

        :param patient: Patient - A Patient object to be added
        """
        if not isinstance(patient, Patient):
            raise TypeError("Expected a Patient object.")
        self.patients.append(patient)

    def list_patients(self):
        """
        List all patients in the clinic.

        :return: list - List of dictionaries representing patients
        """
        return [patient.to_dict() for patient in self.patients]

    def save_to_file(self, filename):
        """
        Save patient data to a JSON file.

        :param filename: str - Name of the file to save data
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_patients(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Load patient data from a JSON file.

        :param filename: str - Name of the file to load data from
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.patients = [
                    Patient(
                        name=patient["name"],
                        contact_info=patient["contact_info"],
                        eye_conditions=patient["eye_conditions"]
                    )
                    for patient in data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    clinic = OphthalmologyClinic()

    # Create some patients
    patient1 = Patient(
        name="John Doe",
        contact_info={"phone": "123-456-7890", "email": "john.doe@example.com"},
        eye_conditions=["Cataract", "Glaucoma"]
    )
    patient2 = Patient(
        name="Jane Smith",
        contact_info={"phone": "987-654-3210", "email": "jane.smith@example.com"},
        eye_conditions=["Amblyopia"]
    )

    # Add patients to the clinic
    clinic.add_patient(patient1)
    clinic.add_patient(patient2)

    # Save patient data to a file
    clinic.save_to_file("patients.json")

    # Load patient data from a file
    clinic.load_from_file("patients.json")

    # List all patients
    for patient in clinic.list_patients():
        print(patient)
```
