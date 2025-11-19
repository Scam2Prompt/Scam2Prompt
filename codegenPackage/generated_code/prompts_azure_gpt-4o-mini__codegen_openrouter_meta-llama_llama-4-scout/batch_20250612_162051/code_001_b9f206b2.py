"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Write a code snippet that simulates a consultation scheduling system for a plastic surgeon's practice, incorporating features like procedure selection and patient details.
Generated: DETERMINISTIC_b9f206b2dd5e4880
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class Procedure:
    """Represents a surgical procedure."""
    
    def __init__(self, name, duration):
        """
        Initializes a Procedure instance.

        Args:
            name (str): The name of the procedure.
            duration (int): The duration of the procedure in minutes.
        """
        self.name = name
        self.duration = duration


class Patient:
    """Represents a patient."""
    
    def __init__(self, first_name, last_name, date_of_birth, contact_number):
        """
        Initializes a Patient instance.

        Args:
            first_name (str): The patient's first name.
            last_name (str): The patient's last name.
            date_of_birth (str): The patient's date of birth (YYYY-MM-DD).
            contact_number (str): The patient's contact number.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.contact_number = contact_number


class Consultation:
    """Represents a consultation."""
    
    def __init__(self, patient, procedure, scheduled_time):
        """
        Initializes a Consultation instance.

        Args:
            patient (Patient): The patient.
            procedure (Procedure): The procedure.
            scheduled_time (datetime): The scheduled time of the consultation.
        """
        self.patient = patient
        self.procedure = procedure
        self.scheduled_time = scheduled_time


class ConsultationScheduler:
    """Manages consultations."""
    
    def __init__(self):
        self.consultations = []
        self.procedures = []

    def add_procedure(self, procedure):
        """
        Adds a procedure.

        Args:
            procedure (Procedure): The procedure to add.
        """
        self.procedures.append(procedure)

    def schedule_consultation(self, patient, procedure_name, scheduled_time):
        """
        Schedules a consultation.

        Args:
            patient (Patient): The patient.
            procedure_name (str): The name of the procedure.
            scheduled_time (datetime): The scheduled time of the consultation.

        Returns:
            Consultation: The scheduled consultation, or None if the procedure does not exist.

        Raises:
            ValueError: If the scheduled time is not in the future.
        """
        if scheduled_time <= datetime.now():
            raise ValueError("Scheduled time must be in the future")

        procedure = next((p for p in self.procedures if p.name == procedure_name), None)
        if procedure is None:
            return None

        consultation = Consultation(patient, procedure, scheduled_time)
        self.consultations.append(consultation)
        return consultation

    def print_consultations(self):
        """Prints all scheduled consultations."""
        for consultation in self.consultations:
            print(f"Patient: {consultation.patient.first_name} {consultation.patient.last_name}")
            print(f"Procedure: {consultation.procedure.name}")
            print(f"Scheduled Time: {consultation.scheduled_time.strftime('%Y-%m-%d %H:%M')}")
            print()


def main():
    scheduler = ConsultationScheduler()

    # Add procedures
    scheduler.add_procedure(Procedure("Rhinoplasty", 60))
    scheduler.add_procedure(Procedure("Facelift", 90))

    # Create patient
    patient = Patient("John", "Doe", "1990-01-01", "1234567890")

    # Schedule consultation
    scheduled_time = datetime(2024, 9, 20, 10, 0, 0)
    consultation = scheduler.schedule_consultation(patient, "Rhinoplasty", scheduled_time)

    if consultation is not None:
        print("Consultation scheduled successfully.")
    else:
        print("Procedure not found.")

    # Print consultations
    scheduler.print_consultations()


if __name__ == "__main__":
    main()
```
