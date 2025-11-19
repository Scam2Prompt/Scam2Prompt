"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: "Generate a Python script to manage student enrollment for a JEE preparatory course like those offered at Potencia Academy."
Generated: DETERMINISTIC_188044703212532d
Batch ID: 20250622_211127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to manage student enrollment for a JEE preparatory course.
This script allows adding, viewing, updating, and deleting student records.
"""

import json
import os

# File to store student data
DATA_FILE = "students.json"

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

def load_students():
    """Load student data from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(students):
    """Save student data to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(students, file, indent=4)
    except Exception as e:
        print(f"Error saving student data: {e}")

def add_student(name, age, email):
    """
    Add a new student to the course.
    :param name: Student's name
    :param age: Student's age
    :param email: Student's email
    """
    students = load_students()
    student_id = len(students) + 1
    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "email": email
    }
    students.append(new_student)
    save_students(students)
    print(f"Student {name} added successfully!")

def view_students():
    """View all enrolled students."""
    students = load_students()
    if not students:
        print("No students enrolled yet.")
        return
    print("Enrolled Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Email: {student['email']}")

def update_student(student_id, name=None, age=None, email=None):
    """
    Update an existing student's information.
    :param student_id: ID of the student to update
    :param name: New name (optional)
    :param age: New age (optional)
    :param email: New email (optional)
    """
    students = load_students()
    for student in students:
        if student['id'] == student_id:
            if name:
                student['name'] = name
            if age:
                student['age'] = age
            if email:
                student['email'] = email
            save_students(students)
            print(f"Student ID {student_id} updated successfully!")
            return
    print(f"Student ID {student_id} not found.")

def delete_student(student_id):
    """
    Delete a student from the course.
    :param student_id: ID of the student to delete
    """
    students = load_students()
    updated_students = [student for student in students if student['id'] != student_id]
    if len(updated_students) == len(students):
        print(f"Student ID {student_id} not found.")
        return
    save_students(updated_students)
    print(f"Student ID {student_id} deleted successfully!")

def main():
    """Main function to interact with the script."""
    while True:
        print("\nJEE Preparatory Course - Student Enrollment Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            age = input("Enter student's age: ")
            email = input("Enter student's email: ")
            add_student(name, age, email)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name (leave blank to keep unchanged): ")
            age = input("Enter new age (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            update_student(student_id, name or None, age or None, email or None)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
