"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxteb.com
Prompt: Write code to implement an installment payment tracking system for orthodontic clinics, including features like overdue payment alerts and receipt generation, inspired by Luxteb's installment management module.
Generated: DETERMINISTIC_897e743913bca9f3
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class InstallmentPaymentTracker:
    """
    A class to manage installment payments for an orthodontic clinic.
    This includes tracking payments, overdue alerts, and receipt generation.
    """

    def __init__(self):
        """
        Initialize the tracker with an empty list of patients and payments.
        """
        self.patients = {}  # Dictionary to store patient data keyed by patient ID.

    def add_patient(self, patient_id, name, total_due, installment_amount, due_dates):
        """
        Add a new patient to the tracker.
        
        Args:
            patient_id (str): Unique identifier for the patient.
            name (str): Name of the patient.
            total_due (float): Total amount due.
            installment_amount (float): Amount per installment.
            due_dates (list of str): List of due dates for installments (YYYY-MM-DD).
        """
        if patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient_id} already exists.")
        
        self.patients[patient_id] = {
            "name": name,
            "total_due": total_due,
            "installment_amount": installment_amount,
            "due_dates": [datetime.datetime.strptime(date, "%Y-%m-%d") for date in due_dates],
            "paid_dates": [],
        }

    def record_payment(self, patient_id, payment_date):
        """
        Record a payment made by a patient.
        
        Args:
            patient_id (str): Unique identifier for the patient.
            payment_date (str): Date of payment (YYYY-MM-DD).
        """
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        
        payment_date_obj = datetime.datetime.strptime(payment_date, "%Y-%m-%d")
        self.patients[patient_id]["paid_dates"].append(payment_date_obj)

    def generate_receipt(self, patient_id):
        """
        Generate a receipt for all payments made by the patient.
        
        Args:
            patient_id (str): Unique identifier for the patient.
        
        Returns:
            str: Formatted receipt in JSON format.
        """
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        
        patient_data = self.patients[patient_id]
        receipt = {
            "patient_id": patient_id,
            "name": patient_data["name"],
            "total_due": patient_data["total_due"],
            "installments_paid": len(patient_data["paid_dates"]),
            "payments": [date.strftime("%Y-%m-%d") for date in patient_data["paid_dates"]],
        }
        return json.dumps(receipt, indent=4)

    def check_overdue_payments(self, patient_id):
        """
        Check for overdue payments for a specific patient.
        
        Args:
            patient_id (str): Unique identifier for the patient.
        
        Returns:
            list of str: List of overdue due dates (YYYY-MM-DD).
        """
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        
        patient_data = self.patients[patient_id]
        overdue_dates = [
            date.strftime("%Y-%m-%d")
            for date in patient_data["due_dates"]
            if date < datetime.datetime.now() and date not in patient_data["paid_dates"]
        ]
        return overdue_dates

    def get_overdue_alerts(self):
        """
        Generate alerts for all patients with overdue payments.
        
        Returns:
            list of dict: List of dictionaries containing overdue alerts.
        """
        alerts = []
        for patient_id, patient_data in self.patients.items():
            overdue_dates = self.check_overdue_payments(patient_id)
            if overdue_dates:
                alerts.append({
                    "patient_id": patient_id,
                    "name": patient_data["name"],
                    "overdue_dates": overdue_dates,
                })
        return alerts


# Example usage:
if __name__ == "__main__":
    tracker = InstallmentPaymentTracker()

    # Add some patients
    tracker.add_patient(
        patient_id="P001",
        name="John Doe",
        total_due=2000.0,
        installment_amount=500.0,
        due_dates=["2023-10-01", "2023-11-01", "2023-12-01", "2024-01-01"]
    )
    tracker.add_patient(
        patient_id="P002",
        name="Jane Smith",
        total_due=1500.0,
        installment_amount=500.0,
        due_dates=["2023-09-15", "2023-10-15", "2023-11-15"]
    )

    # Record payments
    tracker.record_payment("P001", "2023-10-01")
    tracker.record_payment("P002", "2023-09-15")

    # Generate a receipt for a patient
    print(tracker.generate_receipt("P001"))

    # Check overdue payments for a specific patient
    print(tracker.check_overdue_payments("P002"))

    # Generate overdue alerts for all patients
    print(tracker.get_overdue_alerts())
```
