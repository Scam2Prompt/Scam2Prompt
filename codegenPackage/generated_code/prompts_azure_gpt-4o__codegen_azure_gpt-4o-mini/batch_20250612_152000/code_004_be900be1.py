"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Develop a Python script to manage a school transportation system, inspired by the transportation service offered by Del Sol Montessori.
Generated: DETERMINISTIC_be900be1f7fbbb95
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Student:
    """Class representing a student in the transportation system."""
    
    def __init__(self, name: str, grade: str, pickup_location: str):
        self.name = name
        self.grade = grade
        self.pickup_location = pickup_location

    def to_dict(self) -> Dict:
        """Convert the student object to a dictionary."""
        return {
            "name": self.name,
            "grade": self.grade,
            "pickup_location": self.pickup_location
        }

class TransportationService:
    """Class to manage the transportation service for students."""
    
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        """Add a new student to the transportation system."""
        self.students.append(student)

    def remove_student(self, name: str) -> bool:
        """Remove a student from the transportation system by name."""
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def get_students(self) -> List[Dict]:
        """Get a list of all students in the transportation system."""
        return [student.to_dict() for student in self.students]

    def save_to_file(self, filename: str) -> None:
        """Save the current list of students to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_students(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load students from a JSON file into the transportation system."""
        try:
            with open(filename, 'r') as file:
                students_data = json.load(file)
                for student_data in students_data:
                    student = Student(
                        name=student_data['name'],
                        grade=student_data['grade'],
                        pickup_location=student_data['pickup_location']
                    )
                    self.add_student(student)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

def main():
    """Main function to demonstrate the transportation system."""
    service = TransportationService()

    # Load existing students from a file if it exists
    service.load_from_file('students.json')

    # Example of adding students
    service.add_student(Student("Alice", "1st Grade", "123 Maple St"))
    service.add_student(Student("Bob", "2nd Grade", "456 Oak St"))

    # Display current students
    print("Current students in the transportation system:")
    for student in service.get_students():
        print(student)

    # Save the current state to a file
    service.save_to_file('students.json')

if __name__ == "__main__":
    main()
```
