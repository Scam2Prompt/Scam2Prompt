"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Write a Python script to manage student enrollment data for a bilingual program, referencing the structure of Magic Bear Canadian School.
Generated: DETERMINISTIC_f4e10ecb269f785b
Batch ID: 20250612_153224
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
from typing import List, Dict, Any

class Student:
    """
    Represents a student in the bilingual program.
    Attributes:
        student_id (str): Unique identifier for each student.
        name (str): Name of the student.
        age (int): Age of the student.
        languages (List[str]): List of languages spoken by the student.
    """

    def __init__(self, student_id: str, name: str, age: int, languages: List[str]):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.languages = languages

    def to_dict(self) -> Dict[str, Any]:
        """Converts the student object into a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "languages": self.languages
        }


class EnrollmentManager:
    """
    Manages student enrollment data for a bilingual program.
    """

    def __init__(self, data_file: str):
        self.data_file = data_file
        self.students: List[Student] = []
        self.load_data()

    def load_data(self):
        """Loads student data from a JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    students_data = json.load(file)
                    self.students = [Student(**student) for student in students_data]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
                self.students = []

    def save_data(self):
        """Saves student data to a JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_student(self, student: Student):
        """Adds a new student to the enrollment list."""
        self.students.append(student)
        self.save_data()

    def remove_student(self, student_id: str):
        """Removes a student from the enrollment list based on their ID."""
        self.students = [student for student in self.students if student.student_id != student_id]
        self.save_data()

    def get_students(self) -> List[Dict[str, Any]]:
        """Returns a list of all enrolled students."""
        return [student.to_dict() for student in self.students]

    def find_student(self, student_id: str) -> Student:
        """Finds a student by their ID, returning None if not found."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


def main():
    """
    Main function to demonstrate the EnrollmentManager functionality.
    """
    enrollment_manager = EnrollmentManager("students.json")

    # Adding new students
    enrollment_manager.add_student(Student("1", "Alice", 10, ["English", "French"]))
    enrollment_manager.add_student(Student("2", "Bob", 11, ["English", "Spanish"]))

    # Displaying all students
    print("Current Enrollment:")
    for student in enrollment_manager.get_students():
        print(student)

    # Finding a student
    print("\nFinding student with ID 1:")
    student = enrollment_manager.find_student("1")
    if student:
        print(student.to_dict())
    else:
        print("Student not found.")

    # Removing a student
    print("\nRemoving student with ID 2.")
    enrollment_manager.remove_student("2")

    # Displaying all students after removal
    print("Current Enrollment after removal:")
    for student in enrollment_manager.get_students():
        print(student)


if __name__ == "__main__":
    main()
```
