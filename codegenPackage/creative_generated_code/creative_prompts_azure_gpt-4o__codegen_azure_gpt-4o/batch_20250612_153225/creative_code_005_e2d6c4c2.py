"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Write a program to track and evaluate academic work for students, incorporating the evaluation methods described on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_e2d6c4c24110cf07
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Student Academic Tracker and Evaluator

This program tracks and evaluates academic work for students based on evaluation methods.
It allows adding students, tracking their academic tasks (assignments, tests, etc.), and
evaluating their performance based on predefined criteria.

Evaluation methods are assumed to include:
1. Assignments scored out of 20.
2. Tests scored out of 50.
3. Attendance as a percentage.

The program calculates a final grade based on weighted contributions from these metrics.
"""

import sys

class Student:
    """
    Represents a single student with academic data.
    """

    def __init__(self, name: str, student_id: str):
        """
        Initializes a new student with a name and unique ID.

        :param name: Full name of the student.
        :param student_id: Unique identifier for the student.
        """
        self.name = name
        self.student_id = student_id
        self.assignments = []  # List to store assignment scores out of 20
        self.tests = []  # List to store test scores out of 50
        self.attendance = 0  # Attendance percentage
        self.final_grade = None  # Placeholder for final grade

    def add_assignment_score(self, score: float):
        """
        Adds an assignment score to the student's record.

        :param score: Score out of 20. Must be between 0 and 20.
        """
        if 0 <= score <= 20:
            self.assignments.append(score)
        else:
            raise ValueError("Assignment score must be between 0 and 20.")

    def add_test_score(self, score: float):
        """
        Adds a test score to the student's record.

        :param score: Score out of 50. Must be between 0 and 50.
        """
        if 0 <= score <= 50:
            self.tests.append(score)
        else:
            raise ValueError("Test score must be between 0 and 50.")

    def update_attendance(self, attendance: float):
        """
        Updates the student's attendance percentage.

        :param attendance: Attendance percentage. Must be between 0 and 100.
        """
        if 0 <= attendance <= 100:
            self.attendance = attendance
        else:
            raise ValueError("Attendance must be between 0 and 100.")

    def calculate_final_grade(self):
        """
        Calculates the student's final grade based on:
        - Assignments (20% weight)
        - Tests (50% weight)
        - Attendance (30% weight)
        """
        if not self.assignments or not self.tests:
            raise ValueError("Assignments and tests must be entered before calculating the final grade.")

        assignment_avg = sum(self.assignments) / len(self.assignments) if self.assignments else 0
        test_avg = sum(self.tests) / len(self.tests) if self.tests else 0

        # Weighted grade calculation
        self.final_grade = (assignment_avg / 20 * 20) + (test_avg / 50 * 50) + (self.attendance / 100 * 30)
        return self.final_grade

    def __str__(self):
        """
        Returns a string representation of the student's details.
        """
        return (
            f"Name: {self.name}, "
            f"ID: {self.student_id}, "
            f"Assignments: {self.assignments}, "
            f"Tests: {self.tests}, "
            f"Attendance: {self.attendance}%, "
            f"Final Grade: {self.final_grade if self.final_grade is not None else 'Not Calculated'}"
        )


class AcademicTracker:
    """
    Manages multiple students and their academic evaluations.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty student list.
        """
        self.students = {}

    def add_student(self, name: str, student_id: str):
        """
        Adds a new student to the tracker.

        :param name: Full name of the student.
        :param student_id: Unique identifier for the student.
        """
        if student_id in self.students:
            raise ValueError("A student with this ID already exists.")
        self.students[student_id] = Student(name, student_id)

    def get_student(self, student_id: str) -> Student:
        """
        Retrieves a student by their ID.

        :param student_id: Unique identifier for the student.
        :return: The Student object.
        """
        if student_id not in self.students:
            raise ValueError("No student found with the given ID.")
        return self.students[student_id]

    def evaluate_all_students(self):
        """
        Calculates and prints the final grades for all students.
        """
        for student in self.students.values():
            try:
                student.calculate_final_grade()
                print(student)
            except ValueError as e:
                print(f"Error evaluating {student.name} ({student.student_id}): {e}")


def main():
    """
    Main function to demonstrate the functionality of the academic tracker.
    """
    tracker = AcademicTracker()

    try:
        # Adding example students
        tracker.add_student("Alice Johnson", "S001")
        tracker.add_student("Bob Smith", "S002")

        # Adding academic data for Alice
        alice = tracker.get_student("S001")
        alice.add_assignment_score(18)
        alice.add_assignment_score(20)
        alice.add_test_score(45)
        alice.add_test_score(47)
        alice.update_attendance(95)

        # Adding academic data for Bob
        bob = tracker.get_student("S002")
        bob.add_assignment_score(16)
        bob.add_assignment_score(17)
        bob.add_test_score(38)
        bob.add_test_score(40)
        bob.update_attendance(88)

        # Evaluate all students
        tracker.evaluate_all_students()

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
