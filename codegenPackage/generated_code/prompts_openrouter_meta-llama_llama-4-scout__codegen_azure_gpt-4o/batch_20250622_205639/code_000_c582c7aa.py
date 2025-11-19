"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a Python script to manage student enrollments for IELTS and PTE courses at Red & White International, including student details and course assignments.
Generated: DETERMINISTIC_c582c7aa1502dfa4
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class EnrollmentManager:
    """
    A class to manage student enrollments for IELTS and PTE courses at Red & White International.
    """

    def __init__(self):
        """
        Initializes the EnrollmentManager with empty student and course data.
        """
        self.students = {}  # Dictionary to store student details
        self.courses = {"IELTS": [], "PTE": []}  # Dictionary to store course assignments

    def add_student(self, student_id, name, email):
        """
        Adds a new student to the system.

        Args:
            student_id (str): Unique ID for the student.
            name (str): Name of the student.
            email (str): Email address of the student.

        Raises:
            ValueError: If the student ID already exists.
        """
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = {"name": name, "email": email}
        print(f"Student {name} added successfully.")

    def enroll_student(self, student_id, course_name):
        """
        Enrolls a student in a specified course.

        Args:
            student_id (str): Unique ID of the student.
            course_name (str): Name of the course ("IELTS" or "PTE").

        Raises:
            ValueError: If the student ID does not exist or the course name is invalid.
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} does not exist.")
        if course_name not in self.courses:
            raise ValueError(f"Invalid course name: {course_name}.")
        if student_id in self.courses[course_name]:
            print(f"Student {student_id} is already enrolled in {course_name}.")
            return
        self.courses[course_name].append(student_id)
        print(f"Student {student_id} enrolled in {course_name} successfully.")

    def get_student_details(self, student_id):
        """
        Retrieves details of a specific student.

        Args:
            student_id (str): Unique ID of the student.

        Returns:
            dict: Details of the student.

        Raises:
            ValueError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} does not exist.")
        return self.students[student_id]

    def get_course_enrollments(self, course_name):
        """
        Retrieves a list of students enrolled in a specific course.

        Args:
            course_name (str): Name of the course ("IELTS" or "PTE").

        Returns:
            list: List of student IDs enrolled in the course.

        Raises:
            ValueError: If the course name is invalid.
        """
        if course_name not in self.courses:
            raise ValueError(f"Invalid course name: {course_name}.")
        return self.courses[course_name]

    def save_data(self, file_name):
        """
        Saves student and course data to a JSON file.

        Args:
            file_name (str): Name of the file to save data.
        """
        data = {"students": self.students, "courses": self.courses}
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {file_name} successfully.")

    def load_data(self, file_name):
        """
        Loads student and course data from a JSON file.

        Args:
            file_name (str): Name of the file to load data.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                self.students = data.get("students", {})
                self.courses = data.get("courses", {"IELTS": [], "PTE": []})
            print(f"Data loaded from {file_name} successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_name} not found.")

# Example usage
if __name__ == "__main__":
    manager = EnrollmentManager()

    # Adding students
    manager.add_student("S001", "Alice Johnson", "alice@example.com")
    manager.add_student("S002", "Bob Smith", "bob@example.com")

    # Enrolling students in courses
    manager.enroll_student("S001", "IELTS")
    manager.enroll_student("S002", "PTE")

    # Retrieving student details
    print(manager.get_student_details("S001"))

    # Retrieving course enrollments
    print(manager.get_course_enrollments("IELTS"))

    # Saving data to a file
    manager.save_data("enrollment_data.json")

    # Loading data from a file
    manager.load_data("enrollment_data.json")
```
