"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Write Python code to simulate a scheduling system for medical exams like colonoscopy, endoscopy, and elastography, including options for selecting dates, times, and specialties such as gastroenterology and hepatology.
Generated: DETERMINISTIC_8cb1cd011b51504b
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

# Define an Enum for medical exam types
class ExamType(Enum):
    COLONOSCOPY = "Colonoscopy"
    ENDOSCOPY = "Endoscopy"
    ELASTOGRAPHY = "Elastography"

# Define an Enum for medical specialties
class Specialty(Enum):
    GASTROENTEROLOGY = "Gastroenterology"
    HEPATOLOGY = "Hepatology"

class MedicalExam:
    def __init__(self, exam_type, specialty, date, time):
        """
        Initialize a MedicalExam object.

        Args:
            exam_type (ExamType): The type of medical exam.
            specialty (Specialty): The medical specialty.
            date (str): The date of the exam in YYYY-MM-DD format.
            time (str): The time of the exam in HH:MM format.
        """
        self.exam_type = exam_type
        self.specialty = specialty
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.strptime(time, "%H:%M").time()

    def __str__(self):
        return f"{self.exam_type.value} - {self.specialty.value} on {self.date} at {self.time}"

class SchedulingSystem:
    def __init__(self):
        self.exams = []

    def schedule_exam(self, exam_type, specialty, date, time):
        """
        Schedule a medical exam.

        Args:
            exam_type (ExamType): The type of medical exam.
            specialty (Specialty): The medical specialty.
            date (str): The date of the exam in YYYY-MM-DD format.
            time (str): The time of the exam in HH:MM format.

        Raises:
            ValueError: If the date or time is invalid.
        """
        try:
            exam = MedicalExam(exam_type, specialty, date, time)
            self.exams.append(exam)
            print(f"Exam scheduled: {exam}")
        except ValueError as e:
            print(f"Invalid date or time: {e}")

    def view_exams(self):
        """
        View all scheduled exams.
        """
        if not self.exams:
            print("No exams scheduled.")
        else:
            for i, exam in enumerate(self.exams, 1):
                print(f"{i}. {exam}")

    def cancel_exam(self, index):
        """
        Cancel a scheduled exam.

        Args:
            index (int): The index of the exam to cancel.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            del self.exams[index - 1]
            print("Exam canceled.")
        except IndexError:
            print("Invalid exam index.")

def main():
    scheduling_system = SchedulingSystem()

    while True:
        print("\n1. Schedule Exam")
        print("2. View Exams")
        print("3. Cancel Exam")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nExam Types:")
            for i, exam_type in enumerate(ExamType, 1):
                print(f"{i}. {exam_type.value}")
            exam_type_index = int(input("Choose an exam type: ")) - 1
            exam_type = list(ExamType)[exam_type_index]

            print("\nSpecialties:")
            for i, specialty in enumerate(Specialty, 1):
                print(f"{i}. {specialty.value}")
            specialty_index = int(input("Choose a specialty: ")) - 1
            specialty = list(Specialty)[specialty_index]

            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            scheduling_system.schedule_exam(exam_type, specialty, date, time)
        elif choice == "2":
            scheduling_system.view_exams()
        elif choice == "3":
            scheduling_system.view_exams()
            index = int(input("Enter exam index to cancel: "))
            scheduling_system.cancel_exam(index)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
