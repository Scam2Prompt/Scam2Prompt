"""
Generated Code Metadata:
========================
Original URL: https://ydmc.edu.np
Prompt: Write a Python code to manage student information for a university with programs like BBS, B Ed, and MBS.
Generated: DETERMINISTIC_83e932b9094201fa
Batch ID: 20250622_205217
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
    """Represents a university student."""

    def __init__(self, student_id, name, program, semester):
        """
        Initializes a Student object.

        Args:
            student_id (str): Unique student ID.
            name (str): Student name.
            program (str): Student program (e.g., BBS, B Ed, MBS).
            semester (int): Student semester.
        """
        self.student_id = student_id
        self.name = name
        self.program = program
        self.semester = semester

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Program: {self.program}, Semester: {self.semester}"


class StudentInformationSystem:
    """Manages student information for a university."""

    def __init__(self):
        """Initializes an empty student information system."""
        self.students = {}

    def add_student(self, student_id, name, program, semester):
        """
        Adds a student to the system.

        Args:
            student_id (str): Unique student ID.
            name (str): Student name.
            program (str): Student program (e.g., BBS, B Ed, MBS).
            semester (int): Student semester.

        Raises:
            ValueError: If student ID already exists.
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = Student(student_id, name, program, semester)

    def get_student(self, student_id):
        """
        Retrieves a student by ID.

        Args:
            student_id (str): Unique student ID.

        Returns:
            Student: Student object if found, None otherwise.
        """
        return self.students.get(student_id)

    def update_student(self, student_id, name=None, program=None, semester=None):
        """
        Updates a student's information.

        Args:
            student_id (str): Unique student ID.
            name (str, optional): New student name. Defaults to None.
            program (str, optional): New student program. Defaults to None.
            semester (int, optional): New student semester. Defaults to None.

        Raises:
            ValueError: If student ID does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist.")
        student = self.students[student_id]
        if name:
            student.name = name
        if program:
            student.program = program
        if semester:
            student.semester = semester

    def delete_student(self, student_id):
        """
        Deletes a student from the system.

        Args:
            student_id (str): Unique student ID.

        Raises:
            ValueError: If student ID does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist.")
        del self.students[student_id]

    def list_students(self):
        """Returns a list of all students in the system."""
        return list(self.students.values())


def main():
    # Create a student information system
    sis = StudentInformationSystem()

    # Add students
    sis.add_student("S001", "John Doe", "BBS", 1)
    sis.add_student("S002", "Jane Doe", "B Ed", 2)
    sis.add_student("S003", "Bob Smith", "MBS", 3)

    # List students
    print("Students:")
    for student in sis.list_students():
        print(student)

    # Get a student
    student_id = "S001"
    student = sis.get_student(student_id)
    if student:
        print(f"\nStudent {student_id}:")
        print(student)
    else:
        print(f"\nStudent {student_id} not found.")

    # Update a student
    sis.update_student("S002", semester=3)
    print("\nUpdated Student S002:")
    print(sis.get_student("S002"))

    # Delete a student
    sis.delete_student("S003")
    print("\nStudents after deletion:")
    for student in sis.list_students():
        print(student)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
