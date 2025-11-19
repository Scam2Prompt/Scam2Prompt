"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Write a program to track student progress in aviation security courses, with specific modules like "Security Awareness" and "Risk Management," as outlined on the Welwitschia Aviation website.
Generated: DETERMINISTIC_f8d02e1b5dc6ac90
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Student:
    """Class to represent a student in the aviation security course."""
    
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.modules = {}  # Dictionary to hold module progress

    def add_module(self, module_name: str):
        """Add a new module to the student's progress."""
        if module_name not in self.modules:
            self.modules[module_name] = {'completed': False, 'score': 0}
        else:
            raise ValueError(f"Module '{module_name}' already exists for student '{self.name}'.")

    def complete_module(self, module_name: str, score: int):
        """Mark a module as completed and set the score."""
        if module_name in self.modules:
            self.modules[module_name]['completed'] = True
            self.modules[module_name]['score'] = score
        else:
            raise ValueError(f"Module '{module_name}' not found for student '{self.name}'.")

    def get_progress(self) -> Dict[str, Any]:
        """Return the student's progress in all modules."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'modules': self.modules
        }

class Course:
    """Class to represent the aviation security course."""
    
    def __init__(self):
        self.students: Dict[str, Student] = {}  # Dictionary to hold students by ID

    def add_student(self, student_id: str, name: str):
        """Add a new student to the course."""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        else:
            raise ValueError(f"Student ID '{student_id}' already exists.")

    def get_student_progress(self, student_id: str) -> Dict[str, Any]:
        """Get the progress of a specific student."""
        if student_id in self.students:
            return self.students[student_id].get_progress()
        else:
            raise ValueError(f"Student ID '{student_id}' not found.")

    def save_progress(self, filename: str):
        """Save all students' progress to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({student_id: student.get_progress() for student_id, student in self.students.items()}, file, indent=4)
        except IOError as e:
            print(f"Error saving progress to file: {e}")

    def load_progress(self, filename: str):
        """Load students' progress from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for student_id, student_data in data.items():
                    self.add_student(student_id, student_data['name'])
                    for module_name, module_data in student_data['modules'].items():
                        self.students[student_id].add_module(module_name)
                        if module_data['completed']:
                            self.students[student_id].complete_module(module_name, module_data['score'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading progress from file: {e}")

# Example usage
if __name__ == "__main__":
    course = Course()
    
    # Adding students
    course.add_student("001", "Alice Smith")
    course.add_student("002", "Bob Johnson")
    
    # Adding modules
    course.students["001"].add_module("Security Awareness")
    course.students["001"].add_module("Risk Management")
    
    # Completing modules
    course.students["001"].complete_module("Security Awareness", 85)
    
    # Saving progress
    course.save_progress("student_progress.json")
    
    # Loading progress
    course.load_progress("student_progress.json")
    
    # Print student progress
    print(course.get_student_progress("001"))
```
