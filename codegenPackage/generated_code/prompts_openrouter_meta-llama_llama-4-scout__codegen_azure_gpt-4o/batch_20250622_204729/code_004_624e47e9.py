"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Design a Python program that manages student information for a school with multiple levels of education, including features for tracking student progress, similar to what Unidad Educativa Bilingüe de la Inmaculada might use."
Generated: DETERMINISTIC_624e47e96c2df147
Batch ID: 20250622_204729
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
    Represents a student with basic information and progress tracking.
    """
    def __init__(self, student_id, name, age, level):
        """
        Initialize a student object.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param age: Age of the student
        :param level: Education level of the student (e.g., Primary, Secondary)
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.level = level
        self.progress = {}  # Dictionary to track progress in subjects

    def update_progress(self, subject, score):
        """
        Update the student's progress in a specific subject.

        :param subject: Name of the subject
        :param score: Score achieved in the subject
        """
        self.progress[subject] = score

    def get_progress(self):
        """
        Retrieve the student's progress.

        :return: Dictionary of subjects and scores
        """
        return self.progress

    def to_dict(self):
        """
        Convert the student object to a dictionary for serialization.

        :return: Dictionary representation of the student
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "level": self.level,
            "progress": self.progress
        }


class School:
    """
    Represents a school that manages multiple students.
    """
    def __init__(self, name):
        """
        Initialize a school object.

        :param name: Name of the school
        """
        self.name = name
        self.students = {}  # Dictionary to store students by their ID

    def add_student(self, student):
        """
        Add a new student to the school.

        :param student: Student object to be added
        """
        if student.student_id in self.students:
            raise ValueError(f"Student ID {student.student_id} already exists.")
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        """
        Remove a student from the school.

        :param student_id: ID of the student to be removed
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        del self.students[student_id]

    def get_student(self, student_id):
        """
        Retrieve a student by their ID.

        :param student_id: ID of the student to retrieve
        :return: Student object
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        return self.students[student_id]

    def save_to_file(self, filename):
        """
        Save all student data to a JSON file.

        :param filename: Name of the file to save data
        """
        try:
            with open(filename, 'w') as file:
                json.dump({sid: student.to_dict() for sid, student in self.students.items()}, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Load student data from a JSON file.

        :param filename: Name of the file to load data from
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.students = {sid: Student(**info) for sid, info in data.items()}
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a school
    school = School("Unidad Educativa Bilingüe de la Inmaculada")

    # Add students
    student1 = Student(student_id="S001", name="Alice", age=10, level="Primary")
    student2 = Student(student_id="S002", name="Bob", age=15, level="Secondary")

    school.add_student(student1)
    school.add_student(student2)

    # Update progress
    student1.update_progress("Math", 95)
    student1.update_progress("English", 88)
    student2.update_progress("Science", 90)

    # Save to file
    school.save_to_file("students.json")

    # Load from file
    school.load_from_file("students.json")

    # Retrieve and display student information
    retrieved_student = school.get_student("S001")
    print(f"Student Name: {retrieved_student.name}, Progress: {retrieved_student.get_progress()}")
```
