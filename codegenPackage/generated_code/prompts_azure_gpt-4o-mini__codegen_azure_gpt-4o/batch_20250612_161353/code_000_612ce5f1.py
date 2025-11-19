"""
Generated Code Metadata:
========================
Original URL: https://iedeoccidente.edu.co
Prompt: Generate a Python script that uses the educational resources from the Institución Educativa de Occidente to create a student performance tracking system.
Generated: DETERMINISTIC_612ce5f13fbef66e
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Student Performance Tracking System
This script allows tracking and managing student performance using educational resources
from the Institución Educativa de Occidente.

Features:
- Add new students
- Record grades for subjects
- Calculate average grades
- Display student performance summary
"""

import json

class StudentPerformanceTracker:
    def __init__(self):
        """
        Initialize the tracker with an empty student database.
        """
        self.students = {}

    def add_student(self, student_id, name):
        """
        Add a new student to the tracker.

        Args:
            student_id (str): Unique identifier for the student.
            name (str): Name of the student.
        """
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = {
            "name": name,
            "grades": {}
        }

    def record_grade(self, student_id, subject, grade):
        """
        Record a grade for a specific subject for a student.

        Args:
            student_id (str): Unique identifier for the student.
            subject (str): Name of the subject.
            grade (float): Grade for the subject (0-100).
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        self.students[student_id]["grades"][subject] = grade

    def calculate_average(self, student_id):
        """
        Calculate the average grade for a student.

        Args:
            student_id (str): Unique identifier for the student.

        Returns:
            float: Average grade of the student.
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        grades = self.students[student_id]["grades"].values()
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

    def display_summary(self, student_id):
        """
        Display a performance summary for a student.

        Args:
            student_id (str): Unique identifier for the student.
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        student = self.students[student_id]
        print(f"Performance Summary for {student['name']} (ID: {student_id})")
        print("Grades:")
        for subject, grade in student["grades"].items():
            print(f"  {subject}: {grade}")
        average = self.calculate_average(student_id)
        print(f"Average Grade: {average:.2f}")

    def save_to_file(self, filename):
        """
        Save the student database to a file.

        Args:
            filename (str): Name of the file to save the data.
        """
        with open(filename, 'w') as file:
            json.dump(self.students, file, indent=4)

    def load_from_file(self, filename):
        """
        Load the student database from a file.

        Args:
            filename (str): Name of the file to load the data from.
        """
        try:
            with open(filename, 'r') as file:
                self.students = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"File {filename} contains invalid JSON.")

# Example usage
if __name__ == "__main__":
    tracker = StudentPerformanceTracker()

    # Add students
    tracker.add_student("001", "Alice")
    tracker.add_student("002", "Bob")

    # Record grades
    tracker.record_grade("001", "Math", 85)
    tracker.record_grade("001", "Science", 90)
    tracker.record_grade("002", "Math", 78)
    tracker.record_grade("002", "Science", 88)

    # Display summaries
    tracker.display_summary("001")
    tracker.display_summary("002")

    # Save to file
    tracker.save_to_file("students.json")

    # Load from file
    tracker.load_from_file("students.json")
    tracker.display_summary("001")
```
