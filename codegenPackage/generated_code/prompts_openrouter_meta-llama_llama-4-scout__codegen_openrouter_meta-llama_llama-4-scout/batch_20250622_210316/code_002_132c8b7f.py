"""
Generated Code Metadata:
========================
Original URL: https://cuicalli.edu.mx
Prompt: Write a Python code snippet to manage student information for a university like Universidad Tecnológico Cuicalli, including fields for student name, program, and campus location.
Generated: DETERMINISTIC_132c8b7f25ae8db4
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student.py

class Student:
    """
    Represents a student at Universidad Tecnológico Cuicalli.

    Attributes:
        name (str): The student's name.
        program (str): The student's program.
        campus_location (str): The student's campus location.
    """

    def __init__(self, name: str, program: str, campus_location: str):
        """
        Initializes a Student object.

        Args:
            name (str): The student's name.
            program (str): The student's program.
            campus_location (str): The student's campus location.

        Raises:
            ValueError: If any of the required fields are empty.
        """
        if not all([name, program, campus_location]):
            raise ValueError("Name, program, and campus location are required.")

        self.name = name
        self.program = program
        self.campus_location = campus_location

    def __str__(self):
        """
        Returns a string representation of the Student object.

        Returns:
            str: A string representation of the Student object.
        """
        return f"Name: {self.name}\nProgram: {self.program}\nCampus Location: {self.campus_location}"

    def to_dict(self):
        """
        Returns a dictionary representation of the Student object.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        return {
            "name": self.name,
            "program": self.program,
            "campus_location": self.campus_location
        }


class StudentManager:
    """
    Manages a collection of students at Universidad Tecnológico Cuicalli.
    """

    def __init__(self):
        """
        Initializes a StudentManager object.
        """
        self.students = []

    def add_student(self, student: Student):
        """
        Adds a student to the collection.

        Args:
            student (Student): The student to add.

        Raises:
            TypeError: If the student is not a Student object.
        """
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")

        self.students.append(student)

    def remove_student(self, student_name: str):
        """
        Removes a student from the collection.

        Args:
            student_name (str): The name of the student to remove.

        Raises:
            ValueError: If the student is not found.
        """
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                return

        raise ValueError("Student not found.")

    def get_students(self):
        """
        Returns a list of all students in the collection.

        Returns:
            list: A list of all students in the collection.
        """
        return self.students


def main():
    try:
        # Create a StudentManager
        manager = StudentManager()

        # Create some students
        student1 = Student("John Doe", "Computer Science", "Cuicalli Campus")
        student2 = Student("Jane Doe", "Engineering", "Cuicalli Campus")

        # Add students to the manager
        manager.add_student(student1)
        manager.add_student(student2)

        # Print all students
        print("All Students:")
        for student in manager.get_students():
            print(student)
            print("--------------------")

        # Remove a student
        manager.remove_student("John Doe")

        # Print all students again
        print("\nAll Students after removal:")
        for student in manager.get_students():
            print(student)
            print("--------------------")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
