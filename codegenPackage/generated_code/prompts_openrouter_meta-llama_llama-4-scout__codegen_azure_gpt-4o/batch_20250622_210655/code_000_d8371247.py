"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Write a Python script to manage student information for a school like MercedariasGye, including fields for student name, grade level, and extracurricular activities.
Generated: DETERMINISTIC_d837124730ee177e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Student:
    """
    A class to represent a student.
    """
    def __init__(self, name: str, grade_level: str, activities: list):
        """
        Initialize a Student object.

        :param name: Name of the student
        :param grade_level: Grade level of the student
        :param activities: List of extracurricular activities
        """
        self.name = name
        self.grade_level = grade_level
        self.activities = activities

    def to_dict(self):
        """
        Convert the Student object to a dictionary.

        :return: Dictionary representation of the student
        """
        return {
            "name": self.name,
            "grade_level": self.grade_level,
            "activities": self.activities
        }


class StudentManager:
    """
    A class to manage student information.
    """
    def __init__(self, data_file: str = "students.json"):
        """
        Initialize the StudentManager object.

        :param data_file: File to store student data
        """
        self.data_file = data_file
        self.students = self.load_students()

    def load_students(self):
        """
        Load students from the data file.

        :return: List of students
        """
        try:
            with open(self.data_file, "r") as file:
                return [Student(**student) for student in json.load(file)]
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Unable to decode student data file.")
            return []

    def save_students(self):
        """
        Save students to the data file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save student data. {e}")

    def add_student(self, name: str, grade_level: str, activities: list):
        """
        Add a new student to the list.

        :param name: Name of the student
        :param grade_level: Grade level of the student
        :param activities: List of extracurricular activities
        """
        new_student = Student(name, grade_level, activities)
        self.students.append(new_student)
        self.save_students()

    def list_students(self):
        """
        List all students.

        :return: List of students
        """
        return [student.to_dict() for student in self.students]

    def find_student(self, name: str):
        """
        Find a student by name.

        :param name: Name of the student
        :return: Student object or None if not found
        """
        for student in self.students:
            if student.name.lower() == name.lower():
                return student.to_dict()
        return None

    def delete_student(self, name: str):
        """
        Delete a student by name.

        :param name: Name of the student
        """
        self.students = [student for student in self.students if student.name.lower() != name.lower()]
        self.save_students()


# Example usage
if __name__ == "__main__":
    manager = StudentManager()

    # Add a new student
    manager.add_student("Alice Johnson", "Grade 10", ["Basketball", "Drama Club"])

    # List all students
    print("All Students:")
    print(manager.list_students())

    # Find a specific student
    print("\nFind Student:")
    print(manager.find_student("Alice Johnson"))

    # Delete a student
    manager.delete_student("Alice Johnson")
    print("\nAfter Deletion:")
    print(manager.list_students())
```
