"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Develop a code snippet that automates the scheduling of periodic tests for students enrolled in Potencia Academy's JEE and NEET programs.
Generated: DETERMINISTIC_c98bdf7249092933
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
from datetime import datetime, timedelta
from typing import List

class Student:
    def __init__(self, name: str, program: str):
        """
        Initialize a student with a name and program.
        
        :param name: Name of the student
        :param program: Program the student is enrolled in (JEE or NEET)
        """
        self.name = name
        self.program = program

    def __repr__(self):
        return f"{self.name} ({self.program})"

class TestScheduler:
    def __init__(self):
        """
        Initialize the TestScheduler with an empty list of students.
        """
        self.students: List[Student] = []

    def add_student(self, student: Student):
        """
        Add a student to the scheduler.

        :param student: Student to be added
        """
        self.students.append(student)

    def schedule_tests(self):
        """
        Schedule tests for each student based on their program.
        Tests are scheduled weekly for each student.
        """
        for student in self.students:
            schedule.every().monday.at("10:00").do(self.send_test_reminder, student)

    def send_test_reminder(self, student: Student):
        """
        Send a test reminder to the student.

        :param student: Student to whom the reminder is sent
        """
        print(f"Reminder: {student.name}, your test is scheduled for {self.get_next_test_date()}.")

    def get_next_test_date(self) -> str:
        """
        Get the next test date which is one week from now.

        :return: Next test date as a string
        """
        return (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")

    def run_scheduler(self):
        """
        Run the test scheduler, checking every minute for upcoming tests.
        """
        while True:
            schedule.run_pending()
            time.sleep(60)

# Example usage
if __name__ == "__main__":
    try:
        scheduler = TestScheduler()
        scheduler.add_student(Student("Alice", "JEE"))
        scheduler.add_student(Student("Bob", "NEET"))

        # Schedule tests
        scheduler.schedule_tests()
        
        # Start the scheduler
        print("Test scheduler is running...")
        scheduler.run_scheduler()

    except Exception as e:
        print(f"An error occurred: {e}")
```
