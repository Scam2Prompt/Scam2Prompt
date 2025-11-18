"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Write code to implement a student-centered, competency-based learning system inspired by the TAFE vocational education mode reform project described on the AVEA website.
Generated: DETERMINISTIC_39e835e1df5d0e58
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Student-Centered Competency-Based Learning System
Inspired by TAFE Vocational Education Mode Reform Project
"""

import uuid


class Student:
    """
    Class representing a student in the system.
    """
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())  # Unique identifier for the student
        self.name = name
        self.email = email
        self.competencies = {}  # Dictionary to track competencies and progress

    def add_competency(self, competency_name):
        """
        Add a new competency for the student.
        """
        if competency_name not in self.competencies:
            self.competencies[competency_name] = {"status": "Not Started"}
        else:
            raise ValueError(f"Competency '{competency_name}' already exists for the student.")

    def update_competency_status(self, competency_name, status):
        """
        Update the status of a student's competency.
        """
        if competency_name in self.competencies:
            self.competencies[competency_name]["status"] = status
        else:
            raise ValueError(f"Competency '{competency_name}' does not exist for the student.")

    def get_progress(self):
        """
        Get a summary of the student's competency progress.
        """
        return self.competencies


class Competency:
    """
    Class representing a competency in the system.
    """
    def __init__(self, name, description):
        self.id = str(uuid.uuid4())  # Unique identifier for the competency
        self.name = name
        self.description = description


class LearningSystem:
    """
    Central system to manage students and competencies.
    """
    def __init__(self):
        self.students = {}  # Dictionary to store students by ID
        self.competencies = {}  # Dictionary to store competencies by ID

    def create_student(self, name, email):
        """
        Create a new student and add them to the system.
        """
        student = Student(name, email)
        self.students[student.id] = student
        return student

    def create_competency(self, name, description):
        """
        Create a new competency and add it to the system.
        """
        competency = Competency(name, description)
        self.competencies[competency.id] = competency
        return competency

    def assign_competency_to_student(self, student_id, competency_id):
        """
        Assign a competency to a student.
        """
        if student_id not in self.students:
            raise ValueError(f"Student with ID '{student_id}' not found.")
        if competency_id not in self.competencies:
            raise ValueError(f"Competency with ID '{competency_id}' not found.")

        student = self.students[student_id]
        competency = self.competencies[competency_id]
        student.add_competency(competency.name)

    def get_student_progress(self, student_id):
        """
        Retrieve progress information for a specific student.
        """
        if student_id not in self.students:
            raise ValueError(f"Student with ID '{student_id}' not found.")

        student = self.students[student_id]
        return student.get_progress()

    def list_all_students(self):
        """
        List all students in the system.
        """
        return [vars(student) for student in self.students.values()]

    def list_all_competencies(self):
        """
        List all competencies in the system.
        """
        return [vars(competency) for competency in self.competencies.values()]


# Example usage
if __name__ == "__main__":
    try:
        system = LearningSystem()

        # Create competencies
        math_competency = system.create_competency("Mathematics", "Basic mathematics skills")
        coding_competency = system.create_competency("Coding", "Basic programming skills")

        # Create students
        student1 = system.create_student("Alice", "alice@example.com")
        student2 = system.create_student("Bob", "bob@example.com")

        # Assign competencies to students
        system.assign_competency_to_student(student1.id, math_competency.id)
        system.assign_competency_to_student(student1.id, coding_competency.id)
        system.assign_competency_to_student(student2.id, coding_competency.id)

        # Update competency status
        student1.update_competency_status("Mathematics", "Completed")
        student2.update_competency_status("Coding", "In Progress")

        # Retrieve and display student progress
        print("Student Progress:")
        print(system.get_student_progress(student1.id))
        print(system.get_student_progress(student2.id))

        # List all students and competencies
        print("\nAll Students:")
        print(system.list_all_students())

        print("\nAll Competencies:")
        print(system.list_all_competencies())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
