"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Write a Python script that automates the scheduling of occupational health exams, referencing the types of exams offered by Medicid IPS.
Generated: DETERMINISTIC_a5e39aad367c8aef
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# occupational_health_exam_scheduler.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class ExamType(str, Enum):
    """Types of occupational health exams offered by Medicid IPS"""
    MEDICAL_EXAM = "Medical Exam"
    PSYCHOLOGICAL_EVALUATION = "Psychological Evaluation"
    OCCUPATIONAL_HEALTH_SCREENING = "Occupational Health Screening"

class Patient:
    """Represents a patient"""
    def __init__(self, patient_id: int, name: str, email: str, phone: str):
        self.patient_id = patient_id
        self.name = name
        self.email = email
        self.phone = phone

class ExamScheduler:
    """Schedules occupational health exams"""
    def __init__(self):
        self.exams: Dict[ExamType, List[datetime]] = {
            ExamType.MEDICAL_EXAM: [],
            ExamType.PSYCHOLOGICAL_EVALUATION: [],
            ExamType.OCCUPATIONAL_HEALTH_SCREENING: []
        }
        self.patients: Dict[int, Patient] = {}

    def add_patient(self, patient: Patient):
        """Adds a patient to the scheduler"""
        self.patients[patient.patient_id] = patient

    def schedule_exam(self, patient_id: int, exam_type: ExamType, exam_date: datetime):
        """Schedules an exam for a patient"""
        if patient_id not in self.patients:
            raise ValueError("Patient not found")

        if exam_date < datetime.now():
            raise ValueError("Exam date cannot be in the past")

        self.exams[exam_type].append(exam_date)
        print(f"Exam scheduled for {self.patients[patient_id].name} on {exam_date} - {exam_type}")

    def get_scheduled_exams(self, exam_type: ExamType = None):
        """Gets scheduled exams"""
        if exam_type:
            return self.exams.get(exam_type, [])
        return self.exams

def main():
    scheduler = ExamScheduler()

    # Create patients
    patient1 = Patient(1, "John Doe", "john@example.com", "1234567890")
    patient2 = Patient(2, "Jane Doe", "jane@example.com", "9876543210")

    # Add patients to scheduler
    scheduler.add_patient(patient1)
    scheduler.add_patient(patient2)

    # Schedule exams
    try:
        scheduler.schedule_exam(1, ExamType.MEDICAL_EXAM, datetime.now() + timedelta(days=7))
        scheduler.schedule_exam(2, ExamType.PSYCHOLOGICAL_EVALUATION, datetime.now() + timedelta(days=14))
        scheduler.schedule_exam(1, ExamType.OCCUPATIONAL_HEALTH_SCREENING, datetime.now() - timedelta(days=1))  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")

    # Get scheduled exams
    scheduled_exams = scheduler.get_scheduled_exams()
    for exam_type, exam_dates in scheduled_exams.items():
        print(f"Scheduled {exam_type} exams:")
        for exam_date in exam_dates:
            print(exam_date)

if __name__ == "__main__":
    main()
```
