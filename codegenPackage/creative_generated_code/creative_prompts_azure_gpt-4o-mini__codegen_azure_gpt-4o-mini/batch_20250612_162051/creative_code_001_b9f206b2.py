"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Write a code snippet that simulates a consultation scheduling system for a plastic surgeon's practice, incorporating features like procedure selection and patient details.
Generated: DETERMINISTIC_b9f206b2dd5e4880
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Patient:
    """
    A class to represent a patient in the scheduling system.
    """
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Patient(Name: {self.name}, Email: {self.email}, Phone: {self.phone})"


class Procedure:
    """
    A class to represent a medical procedure offered by the practice.
    """
    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration  # Duration in minutes

    def __str__(self):
        return f"Procedure(Name: {self.name}, Duration: {self.duration} minutes)"


class ConsultationScheduler:
    """
    A class to handle the scheduling of consultations.
    """
    def __init__(self):
        self.schedule = []  # List to hold scheduled consultations

    def schedule_consultation(self, patient: Patient, procedure: Procedure, date: datetime.date, time: datetime.time):
        """
        Schedule a consultation for a patient.
        
        :param patient: Patient object
        :param procedure: Procedure object
        :param date: Date object representing the consultation date
        :param time: Time object representing the consultation time
        :raises ValueError: If the date is in the past or the time slot is already taken
        """
        # Check if the consultation date is in the past
        if date < datetime.date.today():
            raise ValueError("Consultation date cannot be in the past.")

        # Create a consultation entry
        consultation_time = datetime.datetime.combine(date, time)
        
        # Check for scheduling conflicts
        for scheduled in self.schedule:
            if scheduled['time'] == consultation_time:
                raise ValueError("This time slot is already taken.")

        # Add the consultation to the schedule
        self.schedule.append({
            'patient': patient,
            'procedure': procedure,
            'time': consultation_time
        })

        print(f"Consultation scheduled: {patient} for {procedure} on {consultation_time}")

    def view_schedule(self):
        """ Display the current schedule of consultations. """
        if not self.schedule:
            print("No consultations scheduled.")
            return

        print("Scheduled Consultations:")
        for consultation in self.schedule:
            patient = consultation['patient']
            procedure = consultation['procedure']
            time = consultation['time']
            print(f"{patient} | {procedure} at {time}")


# Example usage
if __name__ == "__main__":
    try:
        # Create some procedures
        liposuction = Procedure("Liposuction", 120)
        rhinoplasty = Procedure("Rhinoplasty", 90)

        # Create a patient
        patient1 = Patient("Alice Smith", "alice@example.com", "555-1234")

        # Initialize the consultation scheduler
        scheduler = ConsultationScheduler()

        # Schedule a consultation
        scheduler.schedule_consultation(patient1, liposuction, datetime.date(2023, 12, 1), datetime.time(14, 30))
        scheduler.schedule_consultation(patient1, rhinoplasty, datetime.date(2023, 12, 1), datetime.time(16, 0))

        # View the current schedule
        scheduler.view_schedule()

    except ValueError as e:
        print(f"Error: {e}")
```
