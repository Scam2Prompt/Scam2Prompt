"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Create a simple Python program to manage dental patient records similar to what might be used by Heroes Dental.
Generated: DETERMINISTIC_e8c7fff38ebec22d
Batch ID: 20250622_210243
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

class DentalPatientManager:
    """
    A class to manage dental patient records.
    """

    def __init__(self, data_file="patient_records.json"):
        """
        Initialize the manager with a file to store patient records.
        :param data_file: Path to the JSON file where records are stored.
        """
        self.data_file = data_file
        self.records = self._load_records()

    def _load_records(self):
        """
        Load patient records from the JSON file.
        :return: A dictionary of patient records.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading records. Starting with an empty database.")
                return {}
        return {}

    def _save_records(self):
        """
        Save patient records to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.records, file, indent=4)
        except IOError as e:
            print(f"Error saving records: {e}")

    def add_patient(self, patient_id, name, age, contact, medical_history):
        """
        Add a new patient record.
        :param patient_id: Unique identifier for the patient.
        :param name: Name of the patient.
        :param age: Age of the patient.
        :param contact: Contact information of the patient.
        :param medical_history: Medical history of the patient.
        """
        if patient_id in self.records:
            print(f"Patient ID {patient_id} already exists.")
            return

        self.records[patient_id] = {
            "name": name,
            "age": age,
            "contact": contact,
            "medical_history": medical_history
        }
        self._save_records()
        print(f"Patient {name} added successfully.")

    def update_patient(self, patient_id, **kwargs):
        """
        Update an existing patient record.
        :param patient_id: Unique identifier for the patient.
        :param kwargs: Fields to update (e.g., name, age, contact, medical_history).
        """
        if patient_id not in self.records:
            print(f"Patient ID {patient_id} not found.")
            return

        self.records[patient_id].update(kwargs)
        self._save_records()
        print(f"Patient ID {patient_id} updated successfully.")

    def delete_patient(self, patient_id):
        """
        Delete a patient record.
        :param patient_id: Unique identifier for the patient.
        """
        if patient_id not in self.records:
            print(f"Patient ID {patient_id} not found.")
            return

        del self.records[patient_id]
        self._save_records()
        print(f"Patient ID {patient_id} deleted successfully.")

    def view_patient(self, patient_id):
        """
        View a patient record.
        :param patient_id: Unique identifier for the patient.
        :return: The patient record if found, otherwise None.
        """
        return self.records.get(patient_id, f"Patient ID {patient_id} not found.")

    def list_patients(self):
        """
        List all patient records.
        :return: A dictionary of all patient records.
        """
        return self.records


# Example usage
if __name__ == "__main__":
    manager = DentalPatientManager()

    # Add patients
    manager.add_patient("001", "John Doe", 30, "555-1234", "No allergies")
    manager.add_patient("002", "Jane Smith", 25, "555-5678", "Braces installed")

    # Update a patient
    manager.update_patient("001", age=31, contact="555-4321")

    # View a patient
    print(manager.view_patient("001"))

    # List all patients
    print(manager.list_patients())

    # Delete a patient
    manager.delete_patient("002")

    # List all patients after deletion
    print(manager.list_patients())
```
