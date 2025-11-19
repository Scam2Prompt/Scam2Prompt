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
# student_information_system.py

class Student:
    """Represents a student with their information."""

    def __init__(self, student_id, name, email, phone, address):
        """
        Initializes a Student object.

        Args:
            student_id (str): Unique ID of the student.
            name (str): Name of the student.
            email (str): Email address of the student.
            phone (str): Phone number of the student.
            address (str): Address of the student.
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        """Returns a string representation of the Student object."""
        return f"ID: {self.student_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"


class StudentInformationSystem:
    """Manages student information for a school."""

    def __init__(self):
        """Initializes an empty student information system."""
        self.students = {}

    def add_student(self, student_id, name, email, phone, address):
        """
        Adds a new student to the system.

        Args:
            student_id (str): Unique ID of the student.
            name (str): Name of the student.
            email (str): Email address of the student.
            phone (str): Phone number of the student.
            address (str): Address of the student.

        Raises:
            ValueError: If a student with the same ID already exists.
        """
        if student_id in self.students:
            raise ValueError("Student with the same ID already exists.")
        self.students[student_id] = Student(student_id, name, email, phone, address)

    def remove_student(self, student_id):
        """
        Removes a student from the system.

        Args:
            student_id (str): Unique ID of the student.

        Raises:
            ValueError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist.")
        del self.students[student_id]

    def update_student(self, student_id, name=None, email=None, phone=None, address=None):
        """
        Updates a student's information.

        Args:
            student_id (str): Unique ID of the student.
            name (str, optional): New name of the student. Defaults to None.
            email (str, optional): New email address of the student. Defaults to None.
            phone (str, optional): New phone number of the student. Defaults to None.
            address (str, optional): New address of the student. Defaults to None.

        Raises:
            ValueError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist.")
        student = self.students[student_id]
        if name:
            student.name = name
        if email:
            student.email = email
        if phone:
            student.phone = phone
        if address:
            student.address = address

    def get_student(self, student_id):
        """
        Retrieves a student's information.

        Args:
            student_id (str): Unique ID of the student.

        Returns:
            Student: The Student object if found, otherwise None.

        Raises:
            ValueError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist.")
        return self.students[student_id]

    def list_students(self):
        """Returns a list of all students in the system."""
        return list(self.students.values())


def main():
    # Create a student information system
    sis = StudentInformationSystem()

    while True:
        print("\nAce Higher Secondary School Student Information System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Get Student")
        print("5. List Students")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                email = input("Enter student email: ")
                phone = input("Enter student phone: ")
                address = input("Enter student address: ")
                sis.add_student(student_id, name, email, phone, address)
                print("Student added successfully.")
            elif choice == "2":
                student_id = input("Enter student ID: ")
                sis.remove_student(student_id)
                print("Student removed successfully.")
            elif choice == "3":
                student_id = input("Enter student ID: ")
                name = input("Enter new student name (press Enter to skip): ")
                email = input("Enter new student email (press Enter to skip): ")
                phone = input("Enter new student phone (press Enter to skip): ")
                address = input("Enter new student address (press Enter to skip): ")
                sis.update_student(student_id, name or None, email or None, phone or None, address or None)
                print("Student updated successfully.")
            elif choice == "4":
                student_id = input("Enter student ID: ")
                student = sis.get_student(student_id)
                print(student)
            elif choice == "5":
                students = sis.list_students()
                for student in students:
                    print(student)
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
