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
"""
Student Enrollment Management System for a Dental Hygiene Program
Duration: 2 years
"""

import json
import os

# File to store student data
DATA_FILE = "students.json"

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

class Student:
    """
    Represents a student in the dental hygiene program.
    """
    def __init__(self, student_id, name, age, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        """
        Converts the student object to a dictionary for storage.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

class EnrollmentManager:
    """
    Manages student enrollment for the dental hygiene program.
    """
    def __init__(self, data_file):
        self.data_file = data_file

    def load_students(self):
        """
        Loads student data from the file.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self, students):
        """
        Saves student data to the file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(students, file, indent=4)
        except Exception as e:
            print(f"Error saving students: {e}")

    def add_student(self, student):
        """
        Adds a new student to the program.
        """
        students = self.load_students()
        # Check for duplicate student ID
        if any(s["student_id"] == student.student_id for s in students):
            print("Error: Student ID already exists.")
            return
        students.append(student.to_dict())
        self.save_students(students)
        print(f"Student {student.name} added successfully.")

    def list_students(self):
        """
        Lists all enrolled students.
        """
        students = self.load_students()
        if not students:
            print("No students enrolled.")
            return
        print("Enrolled Students:")
        for student in students:
            print(f"ID: {student['student_id']}, Name: {student['name']}, Age: {student['age']}, Email: {student['email']}")

    def remove_student(self, student_id):
        """
        Removes a student by their ID.
        """
        students = self.load_students()
        updated_students = [s for s in students if s["student_id"] != student_id]
        if len(students) == len(updated_students):
            print("Error: Student ID not found.")
            return
        self.save_students(updated_students)
        print(f"Student with ID {student_id} removed successfully.")

def main():
    """
    Main function to interact with the enrollment system.
    """
    manager = EnrollmentManager(DATA_FILE)

    while True:
        print("\nDental Hygiene Program Enrollment System")
        print("1. Add Student")
        print("2. List Students")
        print("3. Remove Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                age = int(input("Enter Student Age: "))
                email = input("Enter Student Email: ")
                student = Student(student_id, name, age, email)
                manager.add_student(student)
            except ValueError:
                print("Error: Invalid input. Age must be a number.")
        elif choice == "2":
            manager.list_students()
        elif choice == "3":
            student_id = input("Enter Student ID to remove: ")
            manager.remove_student(student_id)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
