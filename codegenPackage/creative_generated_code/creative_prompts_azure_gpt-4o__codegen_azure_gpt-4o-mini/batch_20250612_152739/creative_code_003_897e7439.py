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

class Payment:
    """
    A class to represent a payment for an orthodontic treatment.
    """
    def __init__(self, amount, due_date):
        self.amount = amount
        self.due_date = due_date
        self.paid = False
        self.payment_date = None

    def mark_as_paid(self):
        """Marks the payment as paid with the current date."""
        self.paid = True
        self.payment_date = datetime.datetime.now()

class Patient:
    """
    A class to represent a patient receiving orthodontic treatment.
    """
    def __init__(self, name, payment_plan):
        self.name = name
        self.payment_plan = payment_plan

    def check_overdue_payments(self):
        """Checks for overdue payments and returns a list of overdue payments."""
        overdue_payments = []
        for payment in self.payment_plan:
            if not payment.paid and payment.due_date < datetime.datetime.now():
                overdue_payments.append(payment)
        return overdue_payments

    def generate_receipt(self):
        """Generates a receipt for all paid payments."""
        paid_payments = [p for p in self.payment_plan if p.paid]
        receipt = {
            "patient_name": self.name,
            "payments": [
                {
                    "amount": p.amount,
                    "payment_date": p.payment_date.strftime("%Y-%m-%d %H:%M:%S"),
                }
                for p in paid_payments
            ]
        }
        return json.dumps(receipt, indent=4)

class Clinic:
    """
    A class to represent an orthodontic clinic managing multiple patients.
    """
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        """Adds a new patient to the clinic."""
        self.patients.append(patient)

    def alert_overdue_payments(self):
        """Alerts for overdue payments for all patients."""
        alerts = {}
        for patient in self.patients:
            overdue = patient.check_overdue_payments()
            if overdue:
                alerts[patient.name] = [
                    {
                        "amount": p.amount,
                        "due_date": p.due_date.strftime("%Y-%m-%d"),
                    }
                    for p in overdue
                ]
        return alerts

# Example usage
if __name__ == "__main__":
    try:
        # Create a payment plan for a patient
        payment1 = Payment(amount=200, due_date=datetime.datetime(2023, 10, 1))
        payment2 = Payment(amount=150, due_date=datetime.datetime(2023, 11, 1))
        payment_plan = [payment1, payment2]

        # Create a patient and add their payment plan
        patient = Patient(name="John Doe", payment_plan=payment_plan)

        # Mark the first payment as paid
        payment1.mark_as_paid()

        # Create a clinic and add the patient
        clinic = Clinic()
        clinic.add_patient(patient)

        # Check for overdue payments and generate alerts
        overdue_alerts = clinic.alert_overdue_payments()
        print("Overdue Payments Alert:", overdue_alerts)

        # Generate and print a receipt for paid payments
        receipt = patient.generate_receipt()
        print("Receipt:", receipt)

    except Exception as e:
        print(f"An error occurred: {e}")
```
