"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Write a Python script to manage patient information for a plastic surgery practice, including storing patient testimonials and procedure details.
Generated: DETERMINISTIC_bdb725fa6947acb7
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

class PlasticSurgeryPractice:
    """
    A class to manage patient information, testimonials, and procedure details
    for a plastic surgery practice.
    """

    def __init__(self, data_file="practice_data.json"):
        """
        Initialize the practice with a data file to store information.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        """
        Load data from the JSON file. If the file doesn't exist, initialize an empty structure.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Data file is corrupted. Initializing empty data.")
                return {"patients": [], "testimonials": [], "procedures": []}
        else:
            return {"patients": [], "testimonials": [], "procedures": []}

    def _save_data(self):
        """
        Save the current data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_patient(self, name, age, contact_info):
        """
        Add a new patient to the practice.
        """
        patient = {"name": name, "age": age, "contact_info": contact_info}
        self.data["patients"].append(patient)
        self._save_data()
        print(f"Patient {name} added successfully.")

    def add_testimonial(self, patient_name, testimonial):
        """
        Add a testimonial from a patient.
        """
        testimonial_entry = {"patient_name": patient_name, "testimonial": testimonial}
        self.data["testimonials"].append(testimonial_entry)
        self._save_data()
        print(f"Testimonial from {patient_name} added successfully.")

    def add_procedure(self, procedure_name, description, cost):
        """
        Add a new procedure to the practice.
        """
        procedure = {"procedure_name": procedure_name, "description": description, "cost": cost}
        self.data["procedures"].append(procedure)
        self._save_data()
        print(f"Procedure {procedure_name} added successfully.")

    def list_patients(self):
        """
        List all patients in the practice.
        """
        print("Patients:")
        for patient in self.data["patients"]:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Contact: {patient['contact_info']}")

    def list_testimonials(self):
        """
        List all testimonials.
        """
        print("Testimonials:")
        for testimonial in self.data["testimonials"]:
            print(f"Patient: {testimonial['patient_name']}, Testimonial: {testimonial['testimonial']}")

    def list_procedures(self):
        """
        List all procedures offered by the practice.
        """
        print("Procedures:")
        for procedure in self.data["procedures"]:
            print(f"Name: {procedure['procedure_name']}, Description: {procedure['description']}, Cost: ${procedure['cost']}")

# Example usage
if __name__ == "__main__":
    practice = PlasticSurgeryPractice()

    # Adding sample data
    practice.add_patient("John Doe", 35, "john.doe@example.com")
    practice.add_testimonial("John Doe", "The procedure was life-changing!")
    practice.add_procedure("Rhinoplasty", "Reshaping of the nose", 5000)

    # Listing data
    practice.list_patients()
    practice.list_testimonials()
    practice.list_procedures()
```
