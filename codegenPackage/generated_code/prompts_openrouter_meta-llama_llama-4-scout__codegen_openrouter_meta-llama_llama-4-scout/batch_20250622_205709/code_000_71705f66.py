"""
Generated Code Metadata:
========================
Original URL: https://institutovidaesportiva.com.br
Prompt: Write a Python script to manage patient information for a sports medicine institute like Instituto Vida Esportiva, including fields for patient name, age, and medical conditions.
Generated: DETERMINISTIC_71705f6630accf47
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_manager.py

class MedicalCondition:
    """Represents a medical condition."""

    def __init__(self, name, description):
        """
        Initializes a MedicalCondition.

        Args:
            name (str): The name of the condition.
            description (str): A brief description of the condition.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Patient:
    """Represents a patient."""

    def __init__(self, name, age):
        """
        Initializes a Patient.

        Args:
            name (str): The patient's name.
            age (int): The patient's age.

        Raises:
            ValueError: If age is not a positive integer.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")

        self.name = name
        self.age = age
        self.medical_conditions = []

    def add_medical_condition(self, condition):
        """
        Adds a medical condition to the patient's record.

        Args:
            condition (MedicalCondition): The condition to add.

        Raises:
            TypeError: If condition is not a MedicalCondition.
        """
        if not isinstance(condition, MedicalCondition):
            raise TypeError("Condition must be a MedicalCondition.")

        self.medical_conditions.append(condition)

    def __str__(self):
        patient_info = f"Name: {self.name}, Age: {self.age}\n"
        conditions_info = "\n".join(["  - " + str(condition) for condition in self.medical_conditions])
        return f"{patient_info}Medical Conditions:\n{conditions_info}"


class PatientManager:
    """Manages patient information."""

    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        """
        Adds a patient to the manager.

        Args:
            patient (Patient): The patient to add.

        Raises:
            TypeError: If patient is not a Patient.
            ValueError: If a patient with the same name already exists.
        """
        if not isinstance(patient, Patient):
            raise TypeError("Patient must be a Patient.")

        if patient.name in self.patients:
            raise ValueError("Patient with the same name already exists.")

        self.patients[patient.name] = patient

    def get_patient(self, name):
        """
        Retrieves a patient by name.

        Args:
            name (str): The patient's name.

        Returns:
            Patient: The patient with the given name, or None if not found.
        """
        return self.patients.get(name)

    def __str__(self):
        patients_info = "\n\n".join([str(patient) for patient in self.patients.values()])
        return patients_info


def main():
    try:
        manager = PatientManager()

        # Create medical conditions
        injury = MedicalCondition("Injury", "Knee injury")
        asthma = MedicalCondition("Asthma", "Chronic respiratory disease")

        # Create patients
        patient1 = Patient("John Doe", 30)
        patient1.add_medical_condition(injury)

        patient2 = Patient("Jane Doe", 25)
        patient2.add_medical_condition(asthma)

        # Add patients to manager
        manager.add_patient(patient1)
        manager.add_patient(patient2)

        # Print patients
        print(manager)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
