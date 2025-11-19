"""
Generated Code Metadata:
========================
Original URL: https://www.ahs.edu.np
Prompt: Write a program to manage student information for a school like Ace Higher Secondary School.
Generated: DETERMINISTIC_a3390649284555f1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program to manage student information for a school.
This program allows adding, viewing, updating, and deleting student records.
"""

import sys

class Student:
    """
    A class to represent a student.
    """
    def __init__(self, student_id, name, age, grade):
        """
        Initialize a student object.
        :param student_id: Unique ID for the student
        :param name: Name of the student
        :param age: Age of the student
        :param grade: Grade of the student
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        """
        String representation of the student object.
        """
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class SchoolManagementSystem:
    """
    A class to manage student information for a school.
    """
    def __init__(self):
        """
        Initialize the school management system with an empty student database.
        """
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student to the system.
        :param student_id: Unique ID for the student
        :param name: Name of the student
        :param age: Age of the student
        :param grade: Grade of the student
        """
        if student_id in self.students:
            print(f"Error: Student ID {student_id} already exists.")
            return
        self.students[student_id] = Student(student_id, name, age, grade)
        print(f"Student {name} added successfully.")

    def view_student(self, student_id):
        """
        View details of a specific student.
        :param student_id: Unique ID of the student to view
        """
        student = self.students.get(student_id)
        if not student:
            print(f"Error: Student ID {student_id} not found.")
            return
        print(student)

    def update_student(self, student_id, name=None, age=None, grade=None):
        """
        Update details of an existing student.
        :param student_id: Unique ID of the student to update
        :param name: New name of the student (optional)
        :param age: New age of the student (optional)
        :param grade: New grade of the student (optional)
        """
        student = self.students.get(student_id)
        if not student:
            print(f"Error: Student ID {student_id} not found.")
            return
        if name:
            student.name = name
        if age:
            student.age = age
        if grade:
            student.grade = grade
        print(f"Student ID {student_id} updated successfully.")

    def delete_student(self, student_id):
        """
        Delete a student from the system.
        :param student_id: Unique ID of the student to delete
        """
        if student_id not in self.students:
            print(f"Error: Student ID {student_id} not found.")
            return
        del self.students[student_id]
        print(f"Student ID {student_id} deleted successfully.")

    def list_students(self):
        """
        List all students in the system.
        """
        if not self.students:
            print("No students found.")
            return
        for student in self.students.values():
            print(student)


def main():
    """
    Main function to interact with the school management system.
    """
    system = SchoolManagementSystem()

    while True:
        print("\n--- Ace Higher Secondary School Management System ---")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. List All Students")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                age = int(input("Enter Student Age: "))
                grade = input("Enter Student Grade: ")
                system.add_student(student_id, name, age, grade)
            elif choice == "2":
                student_id = input("Enter Student ID: ")
                system.view_student(student_id)
            elif choice == "3":
                student_id = input("Enter Student ID: ")
                name = input("Enter New Name (leave blank to keep unchanged): ")
                age = input("Enter New Age (leave blank to keep unchanged): ")
                grade = input("Enter New Grade (leave blank to keep unchanged): ")
                system.update_student(
                    student_id,
                    name=name if name else None,
                    age=int(age) if age else None,
                    grade=grade if grade else None,
                )
            elif choice == "4":
                student_id = input("Enter Student ID: ")
                system.delete_student(student_id)
            elif choice == "5":
                system.list_students()
            elif choice == "6":
                print("Exiting the system. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: Invalid input. {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
