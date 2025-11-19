"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Generate a Python script to manage student enrollment data for an educational institution like I.E Politécnico Municipal Cali, focusing on handling multiple campuses and student levels.
Generated: DETERMINISTIC_07585f23b5f809c4
Batch ID: 20250612_161301
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
    
    def __init__(self, student_id: str, name: str, level: str, campus: str):
        self.student_id = student_id
        self.name = name
        self.level = level
        self.campus = campus

    def to_dict(self) -> Dict[str, Any]:
        """Convert student object to dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "level": self.level,
            "campus": self.campus
        }

class EnrollmentManager:
    """Class to manage student enrollment data."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.students: List[Student] = []
        self.load_data()

    def load_data(self) -> None:
        """Load student data from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.students = [Student(**student) for student in data]
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty student list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {self.filename}. Starting with an empty student list.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_data(self) -> None:
        """Save student data to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def add_student(self, student_id: str, name: str, level: str, campus: str) -> None:
        """Add a new student to the enrollment list."""
        new_student = Student(student_id, name, level, campus)
        self.students.append(new_student)
        self.save_data()

    def remove_student(self, student_id: str) -> None:
        """Remove a student from the enrollment list by student ID."""
        self.students = [student for student in self.students if student.student_id != student_id]
        self.save_data()

    def get_students_by_campus(self, campus: str) -> List[Student]:
        """Get a list of students enrolled in a specific campus."""
        return [student for student in self.students if student.campus == campus]

    def get_students_by_level(self, level: str) -> List[Student]:
        """Get a list of students enrolled in a specific level."""
        return [student for student in self.students if student.level == level]

    def display_students(self) -> None:
        """Display all enrolled students."""
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Level: {student.level}, Campus: {student.campus}")

if __name__ == "__main__":
    # Example usage
    enrollment_manager = EnrollmentManager("students.json")
    
    # Adding students
    enrollment_manager.add_student("001", "Alice Smith", "Undergraduate", "Main Campus")
    enrollment_manager.add_student("002", "Bob Johnson", "Graduate", "Downtown Campus")
    
    # Display all students
    enrollment_manager.display_students()
    
    # Get students by campus
    downtown_students = enrollment_manager.get_students_by_campus("Downtown Campus")
    print("\nStudents in Downtown Campus:")
    for student in downtown_students:
        print(student.to_dict())
    
    # Remove a student
    enrollment_manager.remove_student("001")
    
    # Display all students after removal
    print("\nStudents after removal:")
    enrollment_manager.display_students()
```
