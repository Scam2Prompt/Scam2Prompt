"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a Python script to manage student information for SMKN 1 Kadipaten's academic programs, including student names, classes, and exam schedules for subjects like Pendidikan Agama & Budi Pekerti and Matematika.
Generated: DETERMINISTIC_60f2a943620ac24d
Batch ID: 20250622_211832
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
    """Class to represent a student."""
    
    def __init__(self, name: str, student_class: str):
        self.name = name
        self.student_class = student_class
        self.exam_schedule: Dict[str, str] = {}  # Subject: Exam Date

    def add_exam(self, subject: str, exam_date: str):
        """Add an exam schedule for a subject."""
        self.exam_schedule[subject] = exam_date

    def to_dict(self) -> Dict[str, Any]:
        """Convert student information to a dictionary."""
        return {
            'name': self.name,
            'class': self.student_class,
            'exam_schedule': self.exam_schedule
        }

class StudentManager:
    """Class to manage student information."""
    
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, name: str, student_class: str):
        """Add a new student to the manager."""
        student = Student(name, student_class)
        self.students.append(student)

    def find_student(self, name: str) -> Student:
        """Find a student by name."""
        for student in self.students:
            if student.name == name:
                return student
        raise ValueError(f"Student '{name}' not found.")

    def save_to_file(self, filename: str):
        """Save student information to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load student information from a JSON file."""
        try:
            with open(filename, 'r') as file:
                students_data = json.load(file)
                for student_data in students_data:
                    student = Student(student_data['name'], student_data['class'])
                    student.exam_schedule = student_data['exam_schedule']
                    self.students.append(student)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to manage student information."""
    manager = StudentManager()

    # Example usage
    manager.add_student("Alice", "10A")
    manager.add_student("Bob", "10B")
    
    # Adding exam schedules
    manager.find_student("Alice").add_exam("Pendidikan Agama & Budi Pekerti", "2023-12-01")
    manager.find_student("Bob").add_exam("Matematika", "2023-12-02")

    # Save to file
    manager.save_to_file("students.json")

    # Load from file
    manager.load_from_file("students.json")

if __name__ == "__main__":
    main()
```
