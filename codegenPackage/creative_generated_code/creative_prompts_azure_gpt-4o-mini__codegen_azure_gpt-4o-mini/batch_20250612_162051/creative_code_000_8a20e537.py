"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcelsolemos.com.br
Prompt: Write a Python function to schedule a dental consultation with Dr. Celso Lemos, including options for payment methods and treatment plans.
Generated: DETERMINISTIC_8a20e537d4a7fc98
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Consultation:
    def __init__(self, patient_name: str, date_time: datetime, treatment_plan: str, payment_method: str):
        self.patient_name = patient_name
        self.date_time = date_time
        self.treatment_plan = treatment_plan
        self.payment_method = payment_method

    def __str__(self):
        return f"Consultation for {self.patient_name} on {self.date_time} for {self.treatment_plan} with payment via {self.payment_method}"

class DentistScheduler:
    def __init__(self):
        self.consultations: List[Consultation] = []

    def schedule_consultation(self, patient_name: str, date_time: datetime, treatment_plan: str, payment_method: str) -> Optional[str]:
        """
        Schedule a dental consultation with the specified details.

        Args:
            patient_name (str): Name of the patient.
            date_time (datetime): Date and time of the consultation.
            treatment_plan (str): Description of the treatment plan.
            payment_method (str): Chosen payment method.

        Returns:
            Optional[str]: Confirmation message or error message.
        """
        # Validate input parameters
        if not patient_name or not treatment_plan or not payment_method:
            return "Error: Patient name, treatment plan, and payment method are required."

        if date_time < datetime.now():
            return "Error: Cannot schedule a consultation in the past."

        # Check for conflicts with existing consultations
        for consultation in self.consultations:
            if consultation.date_time == date_time:
                return "Error: Time slot is already booked."

        # Create and store the consultation
        new_consultation = Consultation(patient_name, date_time, treatment_plan, payment_method)
        self.consultations.append(new_consultation)
        return f"Consultation scheduled: {new_consultation}"

def main():
    scheduler = DentistScheduler()

    # Example of scheduling a consultation
    patient_name = "John Doe"
    date_time = datetime.now() + timedelta(days=3, hours=10)  # 3 days from now at 10 AM
    treatment_plan = "Root Canal"
    payment_method = "Credit Card"

    confirmation = scheduler.schedule_consultation(patient_name, date_time, treatment_plan, payment_method)
    print(confirmation)

if __name__ == "__main__":
    main()
```
