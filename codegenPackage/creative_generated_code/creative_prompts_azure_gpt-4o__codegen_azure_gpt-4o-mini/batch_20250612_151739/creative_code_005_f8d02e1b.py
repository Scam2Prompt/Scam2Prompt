"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Write a program to track student progress in aviation security courses, with specific modules like "Security Awareness" and "Risk Management," as outlined on the Welwitschia Aviation website.
Generated: DETERMINISTIC_f8d02e1b5dc6ac90
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

class Student:
    """
    Class representing a student in the aviation security courses.
    """
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.modules = {
            "Security Awareness": {"completed": False, "date_completed": None},
            "Risk Management": {"completed": False, "date_completed": None}
        }

    def complete_module(self, module_name):
        """
        Marks a module as completed and records the date of completion.
        
        :param module_name: Name of the module to complete.
        """
        if module_name in self.modules:
            self.modules[module_name]["completed"] = True
            self.modules[module_name]["date_completed"] = datetime.now().isoformat()
        else:
            raise ValueError(f"Module '{module_name}' does not exist.")

    def to_dict(self):
        """
        Converts the student instance to a dictionary for JSON serialization.
        
        :return: Dictionary representation of the student.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "modules": self.modules
        }

class StudentProgressTracker:
    """
    Class to track the progress of students enrolled in aviation security courses.
    """
    def __init__(self, file_path='student_progress.json'):
        self.file_path = file_path
        self.students = {}
        self.load_progress()

    def load_progress(self):
        """
        Loads student progress from a JSON file.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    self.students = json.load(file)
                except json.JSONDecodeError:
                    print("Warning: Failed to decode JSON. Starting with an empty record.")
                    self.students = {}

    def save_progress(self):
        """
        Saves the current student progress to a JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student_id, name):
        """
        Adds a new student to the tracker.

        :param student_id: Unique identifier for the student.
        :param name: Name of the student.
        """
        if student_id in self.students:
            raise ValueError(f"Student ID '{student_id}' already exists.")
        self.students[student_id] = Student(student_id, name)
        self.save_progress()

    def complete_module_for_student(self, student_id, module_name):
        """
        Marks a module as completed for a specific student.

        :param student_id: Unique identifier for the student.
        :param module_name: Name of the module to complete.
        """
        if student_id not in self.students:
            raise ValueError(f"No student found with ID '{student_id}'")
        self.students[student_id].complete_module(module_name)
        self.save_progress()

    def get_student_progress(self, student_id):
        """
        Retrieves a student's progress by their ID.

        :param student_id: Unique identifier for the student.
        :return: Dictionary containing the student's progress.
        """
        if student_id not in self.students:
            raise ValueError(f"No student found with ID '{student_id}'")
        return self.students[student_id].to_dict()

# Example usage
if __name__ == "__main__":
    tracker = StudentProgressTracker()

    try:
        tracker.add_student("123", "John Doe")
        tracker.complete_module_for_student("123", "Security Awareness")
        progress = tracker.get_student_progress("123")
        print(json.dumps(progress, indent=4))
    except ValueError as e:
        print(f"Error: {e}")
```
