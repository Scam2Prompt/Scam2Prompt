"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Write code to implement an installment payment tracking system for orthodontic clinics, including features like overdue payment alerts and receipt generation, inspired by Luxteb's installment management module.
Generated: DETERMINISTIC_897e743913bca9f3
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Patient:
    def __init__(self, patient_id: int, name: str):
        """
        Initialize a Patient object.

        Args:
        patient_id (int): Unique identifier for the patient.
        name (str): Name of the patient.
        """
        self.patient_id = patient_id
        self.name = name
        self.installments = []

    def add_installment(self, installment: 'Installment'):
        """
        Add an installment to the patient's installment plan.

        Args:
        installment (Installment): Installment object to be added.
        """
        self.installments.append(installment)


class Installment:
    def __init__(self, installment_id: int, due_date: datetime, amount: float, paid: bool = False):
        """
        Initialize an Installment object.

        Args:
        installment_id (int): Unique identifier for the installment.
        due_date (datetime): Due date of the installment.
        amount (float): Amount of the installment.
        paid (bool): Payment status of the installment. Defaults to False.
        """
        self.installment_id = installment_id
        self.due_date = due_date
        self.amount = amount
        self.paid = paid

    def mark_as_paid(self):
        """
        Mark the installment as paid.
        """
        self.paid = True


class OrthodonticClinic:
    def __init__(self):
        """
        Initialize an OrthodonticClinic object.
        """
        self.patients: Dict[int, Patient] = {}
        self.installments: Dict[int, Installment] = {}

    def add_patient(self, patient: Patient):
        """
        Add a patient to the clinic's database.

        Args:
        patient (Patient): Patient object to be added.
        """
        self.patients[patient.patient_id] = patient

    def add_installment(self, patient_id: int, installment: Installment):
        """
        Add an installment to a patient's installment plan.

        Args:
        patient_id (int): Unique identifier of the patient.
        installment (Installment): Installment object to be added.
        """
        if patient_id in self.patients:
            self.patients[patient_id].add_installment(installment)
            self.installments[installment.installment_id] = installment
        else:
            raise ValueError("Patient not found")

    def get_overdue_installments(self) -> List[Installment]:
        """
        Get a list of overdue installments.

        Returns:
        List[Installment]: List of overdue installments.
        """
        overdue_installments = []
        today = datetime.today()
        for installment in self.installments.values():
            if installment.due_date < today and not installment.paid:
                overdue_installments.append(installment)
        return overdue_installments

    def generate_receipt(self, installment_id: int) -> str:
        """
        Generate a receipt for a paid installment.

        Args:
        installment_id (int): Unique identifier of the installment.

        Returns:
        str: Receipt message.
        """
        if installment_id in self.installments:
            installment = self.installments[installment_id]
            if installment.paid:
                return f"Receipt for installment {installment_id}: ${installment.amount} already paid."
            else:
                installment.mark_as_paid()
                return f"Receipt for installment {installment_id}: ${installment.amount} paid successfully."
        else:
            return "Installment not found"


def main():
    clinic = OrthodonticClinic()

    patient1 = Patient(1, "John Doe")
    clinic.add_patient(patient1)

    installment1 = Installment(1, datetime.today() - timedelta(days=10), 1000.0)
    installment2 = Installment(2, datetime.today() + timedelta(days=10), 2000.0)
    clinic.add_installment(1, installment1)
    clinic.add_installment(1, installment2)

    overdue_installments = clinic.get_overdue_installments()
    print("Overdue Installments:")
    for installment in overdue_installments:
        print(f"Installment ID: {installment.installment_id}, Due Date: {installment.due_date}, Amount: {installment.amount}")

    print(clinic.generate_receipt(1))
    print(clinic.generate_receipt(2))


if __name__ == "__main__":
    main()
```
