"""
Generated Code Metadata:
========================
Original URL: https://tizianotestori.com
Prompt: Write a Python script for managing dental patient records, including fields for patient name, contact information, and treatment history, inspired by Tiziano Testori's dental practice.
Generated: DETERMINISTIC_b13fb02b1e6839f2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dental_patient_record.py

class Patient:
    """Represents a dental patient with their details and treatment history."""

    def __init__(self, patient_id, name, phone_number, email):
        """
        Initializes a Patient object.

        Args:
            patient_id (int): Unique identifier for the patient.
            name (str): Patient's full name.
            phone_number (str): Patient's phone number.
            email (str): Patient's email address.
        """
        self.patient_id = patient_id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.treatment_history = []

    def add_treatment(self, treatment_date, description):
        """
        Adds a treatment to the patient's treatment history.

        Args:
            treatment_date (str): Date of the treatment in YYYY-MM-DD format.
            description (str): Description of the treatment.

        Raises:
            ValueError: If treatment_date is not in YYYY-MM-DD format.
        """
        try:
            # Attempt to parse the date to ensure it's in the correct format
            year, month, day = map(int, treatment_date.split('-'))
            self.treatment_history.append({
                'treatment_date': treatment_date,
                'description': description
            })
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def __str__(self):
        return f"Patient ID: {self.patient_id}\nName: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}"


class DentalPractice:
    """Manages a collection of dental patient records."""

    def __init__(self):
        self.patients = {}
        self.patient_id_counter = 1

    def add_patient(self, name, phone_number, email):
        """
        Adds a new patient to the dental practice.

        Args:
            name (str): Patient's full name.
            phone_number (str): Patient's phone number.
            email (str): Patient's email address.

        Returns:
            Patient: The newly added patient object.
        """
        new_patient = Patient(self.patient_id_counter, name, phone_number, email)
        self.patients[self.patient_id_counter] = new_patient
        self.patient_id_counter += 1
        return new_patient

    def get_patient(self, patient_id):
        """
        Retrieves a patient by their ID.

        Args:
            patient_id (int): ID of the patient to retrieve.

        Returns:
            Patient: The patient object if found, otherwise None.
        """
        return self.patients.get(patient_id)

    def update_patient(self, patient_id, name=None, phone_number=None, email=None):
        """
        Updates a patient's details.

        Args:
            patient_id (int): ID of the patient to update.
            name (str, optional): New patient name. Defaults to None.
            phone_number (str, optional): New patient phone number. Defaults to None.
            email (str, optional): New patient email. Defaults to None.

        Raises:
            ValueError: If the patient ID is not found.
        """
        patient = self.get_patient(patient_id)
        if patient:
            if name:
                patient.name = name
            if phone_number:
                patient.phone_number = phone_number
            if email:
                patient.email = email
        else:
            raise ValueError("Patient ID not found.")

    def delete_patient(self, patient_id):
        """
        Deletes a patient by their ID.

        Args:
            patient_id (int): ID of the patient to delete.

        Raises:
            ValueError: If the patient ID is not found.
        """
        if patient_id in self.patients:
            del self.patients[patient_id]
        else:
            raise ValueError("Patient ID not found.")


def main():
    dental_practice = DentalPractice()

    while True:
        print("\nDental Patient Record Management")
        print("1. Add Patient")
        print("2. Get Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter patient name: ")
            phone_number = input("Enter patient phone number: ")
            email = input("Enter patient email: ")
            patient = dental_practice.add_patient(name, phone_number, email)
            print(f"Patient added successfully. Patient ID: {patient.patient_id}")
            print(patient)

            while True:
                treatment_choice = input("Add treatment? (y/n): ")
                if treatment_choice.lower() == 'y':
                    treatment_date = input("Enter treatment date (YYYY-MM-DD): ")
                    description = input("Enter treatment description: ")
                    patient.add_treatment(treatment_date, description)
                    print("Treatment added successfully.")
                    print("Treatment History:")
                    for treatment in patient.treatment_history:
                        print(f"Date: {treatment['treatment_date']}, Description: {treatment['description']}")
                elif treatment_choice.lower() == 'n':
                    break
                else:
                    print("Invalid choice. Please choose y or n.")

        elif choice == "2":
            patient_id = int(input("Enter patient ID: "))
            patient = dental_practice.get_patient(patient_id)
            if patient:
                print(patient)
                if patient.treatment_history:
                    print("Treatment History:")
                    for treatment in patient.treatment_history:
                        print(f"Date: {treatment['treatment_date']}, Description: {treatment['description']}")
                else:
                    print("No treatment history found.")
            else:
                print("Patient not found.")

        elif choice == "3":
            patient_id = int(input("Enter patient ID: "))
            name = input("Enter new patient name (press enter to skip): ")
            phone_number = input("Enter new patient phone number (press enter to skip): ")
            email = input("Enter new patient email (press enter to skip): ")
            try:
                dental_practice.update_patient(patient_id, name or None, phone_number or None, email or None)
                print("Patient updated successfully.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            patient_id = int(input("Enter patient ID: "))
            try:
                dental_practice.delete_patient(patient_id)
                print("Patient deleted successfully.")
            except ValueError as e:
                print(e)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
