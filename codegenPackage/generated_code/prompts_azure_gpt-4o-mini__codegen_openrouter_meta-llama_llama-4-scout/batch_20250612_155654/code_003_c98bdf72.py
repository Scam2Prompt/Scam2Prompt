"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Develop a code snippet that automates the scheduling of periodic tests for students enrolled in Potencia Academy's JEE and NEET programs.
Generated: DETERMINISTIC_c98bdf7249092933
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import Dict, List

class Student:
    def __init__(self, student_id: int, name: str, program: str):
        """
        Initialize a Student object.

        Args:
        - student_id (int): Unique identifier for the student.
        - name (str): Name of the student.
        - program (str): Program the student is enrolled in (JEE or NEET).
        """
        self.student_id = student_id
        self.name = name
        self.program = program

class TestScheduler:
    def __init__(self, tests: List[Dict]):
        """
        Initialize a TestScheduler object.

        Args:
        - tests (List[Dict]): List of test schedules.
            Each test schedule is a dictionary containing:
            - test_id (int): Unique identifier for the test.
            - test_name (str): Name of the test.
            - program (str): Program the test is for (JEE or NEET).
            - frequency (str): Frequency of the test (e.g., daily, weekly).
            - time (str): Time of day to schedule the test.
        """
        self.tests = tests
        self.students = {}

    def add_student(self, student: Student):
        """
        Add a student to the scheduler.

        Args:
        - student (Student): Student object to add.
        """
        self.students[student.student_id] = student

    def schedule_tests(self):
        """
        Schedule periodic tests for all enrolled students.

        Returns:
        - A dictionary where the keys are student IDs and the values are lists of scheduled test IDs.
        """
        scheduled_tests = {}
        for student_id, student in self.students.items():
            scheduled_tests[student_id] = []
            for test in self.tests:
                if test['program'] == student.program:
                    scheduled_test = self.schedule_test(test, student)
                    if scheduled_test:
                        scheduled_tests[student_id].append(scheduled_test['test_id'])

        return scheduled_tests

    def schedule_test(self, test: Dict, student: Student):
        """
        Schedule a test for a student.

        Args:
        - test (Dict): Test schedule.
        - student (Student): Student object.

        Returns:
        - A dictionary containing the scheduled test ID and time, or None if scheduling fails.
        """
        try:
            test_time = datetime.datetime.strptime(test['time'], '%H:%M')
            test_time = test_time.replace(year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day)

            if test['frequency'] == 'daily':
                # Schedule daily test
                for i in range(7):  # Schedule for the next 7 days
                    scheduled_test_time = test_time + datetime.timedelta(days=i)
                    print(f"Scheduling test {test['test_id']} for {student.name} on {scheduled_test_time.strftime('%Y-%m-%d %H:%M')}")
                    yield {'test_id': test['test_id'], 'time': scheduled_test_time.strftime('%Y-%m-%d %H:%M')}

            elif test['frequency'] == 'weekly':
                # Schedule weekly test
                for i in range(4):  # Schedule for the next 4 weeks
                    scheduled_test_time = test_time + datetime.timedelta(weeks=i)
                    print(f"Scheduling test {test['test_id']} for {student.name} on {scheduled_test_time.strftime('%Y-%m-%d %H:%M')}")
                    yield {'test_id': test['test_id'], 'time': scheduled_test_time.strftime('%Y-%m-%d %H:%M')}

        except Exception as e:
            print(f"Error scheduling test {test['test_id']} for {student.name}: {str(e)}")
            return None

def main():
    tests = [
        {'test_id': 1, 'test_name': 'Test 1', 'program': 'JEE', 'frequency': 'daily', 'time': '08:00'},
        {'test_id': 2, 'test_name': 'Test 2', 'program': 'NEET', 'frequency': 'weekly', 'time': '14:00'},
    ]

    scheduler = TestScheduler(tests)

    students = [
        Student(1, 'John Doe', 'JEE'),
        Student(2, 'Jane Doe', 'NEET'),
    ]

    for student in students:
        scheduler.add_student(student)

    scheduled_tests = scheduler.schedule_tests()

    print("\nScheduled Tests:")
    for student_id, test_ids in scheduled_tests.items():
        print(f"Student ID: {student_id}, Test IDs: {test_ids}")

if __name__ == "__main__":
    main()
```
