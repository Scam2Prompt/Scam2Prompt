"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Develop a simple automation script using Mecatrónica Automotriz principles to streamline student registration processes for the Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa".
Generated: DETERMINISTIC_79e8466998a3fdf7
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_registration.py

"""
Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa" Student Registration Script

This script automates the student registration process using Mecatrónica Automotriz principles.

Author: [Your Name]
Date: [Today's Date]
"""

import csv
import datetime
import os

# Define a class for Student
class Student:
    def __init__(self, student_id, name, email, phone_number):
        """
        Initialize a Student object.

        Args:
            student_id (str): Unique student ID
            name (str): Student name
            email (str): Student email
            phone_number (str): Student phone number
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

# Define a class for RegistrationSystem
class RegistrationSystem:
    def __init__(self, registration_file):
        """
        Initialize a RegistrationSystem object.

        Args:
            registration_file (str): Path to the registration CSV file
        """
        self.registration_file = registration_file
        self.students = []

    def register_student(self, student):
        """
        Register a new student.

        Args:
            student (Student): Student object to register

        Returns:
            bool: True if registration is successful, False otherwise
        """
        try:
            # Check if student already exists
            existing_student = next((s for s in self.students if s.student_id == student.student_id), None)
            if existing_student:
                print(f"Student with ID {student.student_id} already exists.")
                return False

            # Add student to the list
            self.students.append(student)

            # Save to CSV file
            self.save_to_csv()

            print(f"Student {student.name} registered successfully.")
            return True

        except Exception as e:
            print(f"Error registering student: {str(e)}")
            return False

    def save_to_csv(self):
        """
        Save the registered students to a CSV file.
        """
        with open(self.registration_file, 'w', newline='') as csvfile:
            fieldnames = ['student_id', 'name', 'email', 'phone_number']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for student in self.students:
                writer.writerow({
                    'student_id': student.student_id,
                    'name': student.name,
                    'email': student.email,
                    'phone_number': student.phone_number
                })

    def load_from_csv(self):
        """
        Load registered students from a CSV file.
        """
        if os.path.exists(self.registration_file):
            with open(self.registration_file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student = Student(
                        row['student_id'],
                        row['name'],
                        row['email'],
                        row['phone_number']
                    )
                    self.students.append(student)

def main():
    registration_file = 'student_registrations.csv'
    registration_system = RegistrationSystem(registration_file)
    registration_system.load_from_csv()

    while True:
        print("\nInstituto de Educación Superior Tecnológico Público 'San Martín de Pangoa' Student Registration")
        print("1. Register a new student")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            phone_number = input("Enter student phone number: ")

            student = Student(student_id, name, email, phone_number)
            registration_system.register_student(student)
        elif choice == '2':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
