"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Write a Python script to manage patient data for a hospice care service, including fields for patient name, diagnosis, and care team members, inspired by Amalfi Hospice Care's comprehensive approach.
Generated: DETERMINISTIC_6f35dfc6b3bd2c85
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
import os

class HospiceCareManager:
    """
    A class to manage patient data for a hospice care service.
    """

    def __init__(self, data_file="patients_data.json"):
        """
        Initialize the HospiceCareManager with a data file.
        :param data_file: Path to the JSON file where patient data is stored.
        """
        self.data_file = data_file
        self.patients = self._load_data()

    def _load_data(self):
        """
        Load patient data from the JSON file.
        :return: A dictionary containing patient data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Data file is corrupted. Starting with an empty dataset.")
                return {}
        return {}

    def _save_data(self):
        """
        Save patient data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.patients, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save data to file. {e}")

    def add_patient(self, patient_id, name, diagnosis, care_team):
        """
        Add a new patient to the system.
        :param patient_id: Unique identifier for the patient.
        :param name: Name of the patient.
        :param diagnosis: Diagnosis of the patient.
        :param care_team: List of care team members assigned to the patient.
        """
        if patient_id in self.patients:
            print(f"Error: Patient ID {patient_id} already exists.")
            return

        self.patients[patient_id] = {
            "name": name,
            "diagnosis": diagnosis,
            "care_team": care_team
        }
        self._save_data()
        print(f"Patient {name} added successfully.")

    def update_patient(self, patient_id, name=None, diagnosis=None, care_team=None):
        """
        Update an existing patient's information.
        :param patient_id: Unique identifier for the patient.
        :param name: Updated name of the patient (optional).
        :param diagnosis: Updated diagnosis of the patient (optional).
        :param care_team: Updated list of care team members (optional).
        """
        if patient_id not in self.patients:
            print(f"Error: Patient ID {patient_id} does not exist.")
            return

        if name:
            self.patients[patient_id]["name"] = name
        if diagnosis:
            self.patients[patient_id]["diagnosis"] = diagnosis
        if care_team:
            self.patients[patient_id]["care_team"] = care_team

        self._save_data()
        print(f"Patient ID {patient_id} updated successfully.")

    def delete_patient(self, patient_id):
        """
        Delete a patient from the system.
        :param patient_id: Unique identifier for the patient.
        """
        if patient_id not in self.patients:
            print(f"Error: Patient ID {patient_id} does not exist.")
            return

        del self.patients[patient_id]
        self._save_data()
        print(f"Patient ID {patient_id} deleted successfully.")

    def view_patient(self, patient_id):
        """
        View details of a specific patient.
        :param patient_id: Unique identifier for the patient.
        :return: Dictionary containing patient details.
        """
        if patient_id not in self.patients:
            print(f"Error: Patient ID {patient_id} does not exist.")
            return None

        return self.patients[patient_id]

    def list_patients(self):
        """
        List all patients in the system.
        :return: Dictionary containing all patient data.
        """
        return self.patients


# Example usage
if __name__ == "__main__":
    manager = HospiceCareManager()

    # Add patients
    manager.add_patient("001", "John Doe", "Cancer", ["Dr. Smith", "Nurse Jane"])
    manager.add_patient("002", "Jane Roe", "Heart Disease", ["Dr. Brown", "Nurse Alice"])

    # Update a patient
    manager.update_patient("001", diagnosis="Lung Cancer")

    # View a patient
    patient = manager.view_patient("001")
    if patient:
        print("Patient Details:", patient)

    # List all patients
    print("All Patients:", manager.list_patients())

    # Delete a patient
    manager.delete_patient("002")
    print("All Patients after deletion:", manager.list_patients())
```
