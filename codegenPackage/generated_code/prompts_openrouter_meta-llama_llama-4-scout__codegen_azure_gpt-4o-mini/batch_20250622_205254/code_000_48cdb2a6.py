"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Write a Python script to manage student contact information for a school like Colegio Panamericano e Instituto Libertadores, including fields for student name, grade, and contact numbers.
Generated: DETERMINISTIC_48cdb2a69851cd64
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Student:
    """Class to represent a student with contact information."""
    
    def __init__(self, name, grade, contact_numbers):
        """
        Initialize a new student instance.

        :param name: str - The name of the student
        :param grade: str - The grade of the student
        :param contact_numbers: list - A list of contact numbers for the student
        """
        self.name = name
        self.grade = grade
        self.contact_numbers = contact_numbers

    def to_dict(self):
        """Convert the student instance to a dictionary."""
        return {
            'name': self.name,
            'grade': self.grade,
            'contact_numbers': self.contact_numbers
        }

class StudentManager:
    """Class to manage student contact information."""
    
    def __init__(self, filename='students.json'):
        """
        Initialize the StudentManager with a file to store student data.

        :param filename: str - The filename where student data will be stored
        """
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        """Load students from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return [Student(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading student data: {e}")
                    return []
        return []

    def save_students(self):
        """Save the current list of students to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self, name, grade, contact_numbers):
        """
        Add a new student to the list.

        :param name: str - The name of the student
        :param grade: str - The grade of the student
        :param contact_numbers: list - A list of contact numbers for the student
        """
        new_student = Student(name, grade, contact_numbers)
        self.students.append(new_student)
        self.save_students()

    def get_students(self):
        """Return the list of students."""
        return self.students

    def find_student(self, name):
        """
        Find a student by name.

        :param name: str - The name of the student to find
        :return: Student or None - The found student or None if not found
        """
        for student in self.students:
            if student.name == name:
                return student
        return None

def main():
    """Main function to run the student manager."""
    manager = StudentManager()

    # Example usage
    try:
        manager.add_student("John Doe", "10th Grade", ["123-456-7890", "987-654-3210"])
        manager.add_student("Jane Smith", "11th Grade", ["555-555-5555"])

        print("Current students:")
        for student in manager.get_students():
            print(f"Name: {student.name}, Grade: {student.grade}, Contacts: {', '.join(student.contact_numbers)}")

        # Find a specific student
        student_name = "John Doe"
        found_student = manager.find_student(student_name)
        if found_student:
            print(f"Found student: {found_student.name}, Grade: {found_student.grade}, Contacts: {', '.join(found_student.contact_numbers)}")
        else:
            print(f"Student {student_name} not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
