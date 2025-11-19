"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Generate a Python script to manage student enrollment for a dental hygiene program with a duration of 2 years, similar to the Técnico Superior Universitario en Higienista Dental offered by INESO."
Generated: DETERMINISTIC_40dc1f7fc2250cfd
Batch ID: 20250622_212433
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
    """Class representing a student in the dental hygiene program."""
    
    def __init__(self, student_id: int, name: str, age: int, email: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self) -> Dict[str, Any]:
        """Convert the student object to a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

class EnrollmentManager:
    """Class to manage student enrollment for the dental hygiene program."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.students: List[Student] = []
        self.load_students()

    def load_students(self) -> None:
        """Load students from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                students_data = json.load(file)
                self.students = [Student(**data) for data in students_data]
        except FileNotFoundError:
            print("No existing enrollment data found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting fresh.")
        except Exception as e:
            print(f"An error occurred while loading students: {e}")

    def save_students(self) -> None:
        """Save students to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving students: {e}")

    def enroll_student(self, student_id: int, name: str, age: int, email: str) -> None:
        """Enroll a new student in the program."""
        if any(student.student_id == student_id for student in self.students):
            print(f"Student with ID {student_id} is already enrolled.")
            return
        
        new_student = Student(student_id, name, age, email)
        self.students.append(new_student)
        self.save_students()
        print(f"Student {name} enrolled successfully.")

    def list_students(self) -> None:
        """List all enrolled students."""
        if not self.students:
            print("No students enrolled.")
            return
        
        print("Enrolled Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Email: {student.email}")

def main():
    """Main function to run the enrollment manager."""
    enrollment_manager = EnrollmentManager('students.json')

    while True:
        print("\nDental Hygiene Program Enrollment")
        print("1. Enroll Student")
        print("2. List Students")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                age = int(input("Enter Student Age: "))
                email = input("Enter Student Email: ")
                enrollment_manager.enroll_student(student_id, name, age, email)
            except ValueError:
                print("Invalid input. Please enter the correct data types.")
        elif choice == '2':
            enrollment_manager.list_students()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
