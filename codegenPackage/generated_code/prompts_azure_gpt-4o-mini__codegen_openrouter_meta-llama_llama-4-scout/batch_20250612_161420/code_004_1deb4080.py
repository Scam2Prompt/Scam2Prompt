"""
Generated Code Metadata:
========================
Original URL: https://ndhc.edu.bd
Prompt: Outline the annual examination schedule for the 2023-2024 academic year for the 11th grade at Nazirpur Degree College, based on the provided content.
Generated: DETERMINISTIC_1deb4080577f7eb0
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class ExaminationSchedule:
    def __init__(self, college_name, academic_year, grade):
        """
        Initialize the ExaminationSchedule class.

        Args:
            college_name (str): Name of the college.
            academic_year (str): Academic year.
            grade (str): Grade level.
        """
        self.college_name = college_name
        self.academic_year = academic_year
        self.grade = grade
        self.schedule = {}

    def add_exam(self, subject, exam_date):
        """
        Add an exam to the schedule.

        Args:
            subject (str): Subject name.
            exam_date (str): Exam date in YYYY-MM-DD format.
        """
        self.schedule[subject] = datetime.strptime(exam_date, "%Y-%m-%d")

    def print_schedule(self):
        """
        Print the examination schedule.
        """
        print(f"Examination Schedule for {self.grade} grade at {self.college_name} ({self.academic_year})")
        print("---------------------------------------------------------------")
        for subject, exam_date in sorted(self.schedule.items(), key=lambda x: x[1]):
            print(f"{subject}: {exam_date.strftime('%Y-%m-%d')}")

def main():
    try:
        # Create an instance of ExaminationSchedule
        schedule = ExaminationSchedule("Nazirpur Degree College", "2023-2024", "11th")

        # Add exams to the schedule
        schedule.add_exam("English", "2023-11-15")
        schedule.add_exam("Bengali", "2023-11-17")
        schedule.add_exam("Math", "2023-11-20")
        schedule.add_exam("Science", "2023-11-22")
        schedule.add_exam("History", "2023-11-24")

        # Print the examination schedule
        schedule.print_schedule()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
