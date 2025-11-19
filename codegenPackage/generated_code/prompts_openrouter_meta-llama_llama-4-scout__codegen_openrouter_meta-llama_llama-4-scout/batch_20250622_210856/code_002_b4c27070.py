"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Generate a registration process for Endeavor Plus programs, assuming a parent wants to enroll their child in a school within the Endeavor Schools network."
Generated: DETERMINISTIC_b4c270700485d68d
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# endeavor_plus_registration.py

from enum import Enum
from typing import Dict

class ProgramStatus(str, Enum):
    """Program status enumeration."""
    AVAILABLE = "available"
    FULL = "full"
    CLOSED = "closed"

class School:
    """School class representation."""
    def __init__(self, name: str, program: str, capacity: int, status: ProgramStatus):
        """
        Initialize a School object.

        Args:
        - name (str): School name.
        - program (str): Program name.
        - capacity (int): Program capacity.
        - status (ProgramStatus): Program status.
        """
        self.name = name
        self.program = program
        self.capacity = capacity
        self.status = status
        self.enrolled_students = []

    def enroll_student(self, student_name: str) -> bool:
        """
        Enroll a student in the school program.

        Args:
        - student_name (str): Student name.

        Returns:
        - bool: True if enrollment is successful, False otherwise.
        """
        if self.status != ProgramStatus.AVAILABLE:
            return False
        if len(self.enrolled_students) >= self.capacity:
            return False
        self.enrolled_students.append(student_name)
        return True

    def __str__(self):
        return f"{self.name} - {self.program} ({self.status.value})"


class Parent:
    """Parent class representation."""
    def __init__(self, name: str, email: str):
        """
        Initialize a Parent object.

        Args:
        - name (str): Parent name.
        - email (str): Parent email.
        """
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class Student:
    """Student class representation."""
    def __init__(self, name: str, parent: Parent):
        """
        Initialize a Student object.

        Args:
        - name (str): Student name.
        - parent (Parent): Parent object.
        """
        self.name = name
        self.parent = parent

    def __str__(self):
        return f"{self.name} ({self.parent})"


class EndeavorPlusRegistration:
    """Endeavor Plus registration process."""
    def __init__(self):
        self.schools: Dict[str, School] = {}

    def add_school(self, school: School):
        """
        Add a school to the registration process.

        Args:
        - school (School): School object.
        """
        self.schools[school.name] = school

    def register_student(self, student_name: str, parent_name: str, parent_email: str, school_name: str) -> bool:
        """
        Register a student in a school program.

        Args:
        - student_name (str): Student name.
        - parent_name (str): Parent name.
        - parent_email (str): Parent email.
        - school_name (str): School name.

        Returns:
        - bool: True if registration is successful, False otherwise.
        """
        if school_name not in self.schools:
            print(f"School '{school_name}' not found.")
            return False

        school = self.schools[school_name]
        parent = Parent(parent_name, parent_email)
        student = Student(student_name, parent)

        if school.enroll_student(student_name):
            print(f"Student '{student_name}' enrolled in '{school_name}' successfully.")
            return True
        else:
            print(f"Failed to enroll student '{student_name}' in '{school_name}'.")
            return False


def main():
    registration = EndeavorPlusRegistration()

    # Create schools
    school1 = School("Endeavor Academy", "Endeavor Plus", 10, ProgramStatus.AVAILABLE)
    school2 = School("Endeavor High", "Endeavor Plus", 5, ProgramStatus.AVAILABLE)

    # Add schools to registration
    registration.add_school(school1)
    registration.add_school(school2)

    # Register students
    registration.register_student("John Doe", "Jane Doe", "jane.doe@example.com", "Endeavor Academy")
    registration.register_student("Jane Smith", "John Smith", "john.smith@example.com", "Endeavor High")
    registration.register_student("Bob Johnson", "Alice Johnson", "alice.johnson@example.com", "Non-Existent School")


if __name__ == "__main__":
    main()
```
