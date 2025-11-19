"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Create a simulation in Python to model the workflow of a Unidade Básica de Saúde (Basic Health Unit), including patient intake, problem-solving for simple cases, and referrals to specialty clinics or hospitals.
Generated: DETERMINISTIC_c67fef0e9ce0bfcf
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List

class PatientStatus(Enum):
    """Enum for patient status"""
    INTAKE = 1
    TREATED = 2
    REFERRED = 3

class Patient:
    """Class representing a patient"""
    def __init__(self, name: str, age: int, symptoms: str):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.status = PatientStatus.INTAKE

class HealthUnit:
    """Class representing a Basic Health Unit"""
    def __init__(self):
        self.patients: List[Patient] = []
        self.specialty_clinics = ["Cardiology", "Neurology", "Oncology"]
        self.hospitals = ["Hospital Geral", "Hospital Especializado"]

    def admit_patient(self, patient: Patient):
        """Admit a patient to the health unit"""
        self.patients.append(patient)
        print(f"Patient {patient.name} admitted.")

    def treat_patient(self, patient: Patient):
        """Treat a patient with simple care"""
        if patient.status == PatientStatus.INTAKE:
            patient.status = PatientStatus.TREATED
            print(f"Patient {patient.name} treated.")
        else:
            print(f"Patient {patient.name} is not in intake status.")

    def refer_patient(self, patient: Patient, destination: str):
        """Refer a patient to a specialty clinic or hospital"""
        if patient.status == PatientStatus.INTAKE or patient.status == PatientStatus.TREATED:
            patient.status = PatientStatus.REFERRED
            print(f"Patient {patient.name} referred to {destination}.")
        else:
            print(f"Patient {patient.name} is not in intake or treated status.")

    def display_patients(self):
        """Display all patients in the health unit"""
        for patient in self.patients:
            print(f"Name: {patient.name}, Age: {patient.age}, Symptoms: {patient.symptoms}, Status: {patient.status.name}")


def main():
    health_unit = HealthUnit()

    while True:
        print("\n1. Admit Patient")
        print("2. Treat Patient")
        print("3. Refer Patient")
        print("4. Display Patients")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            symptoms = input("Enter patient symptoms: ")
            patient = Patient(name, age, symptoms)
            health_unit.admit_patient(patient)
        elif choice == "2":
            name = input("Enter patient name: ")
            for patient in health_unit.patients:
                if patient.name == name:
                    health_unit.treat_patient(patient)
                    break
            else:
                print("Patient not found.")
        elif choice == "3":
            name = input("Enter patient name: ")
            destination_type = input("Enter destination type (clinic/hospital): ")
            destination = ""
            if destination_type.lower() == "clinic":
                print("Available clinics: ")
                for i, clinic in enumerate(health_unit.specialty_clinics):
                    print(f"{i+1}. {clinic}")
                choice = int(input("Choose a clinic: ")) - 1
                destination = health_unit.specialty_clinics[choice]
            elif destination_type.lower() == "hospital":
                print("Available hospitals: ")
                for i, hospital in enumerate(health_unit.hospitals):
                    print(f"{i+1}. {hospital}")
                choice = int(input("Choose a hospital: ")) - 1
                destination = health_unit.hospitals[choice]
            for patient in health_unit.patients:
                if patient.name == name:
                    health_unit.refer_patient(patient, destination)
                    break
            else:
                print("Patient not found.")
        elif choice == "4":
            health_unit.display_patients()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
