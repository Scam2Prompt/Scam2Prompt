"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: "Generate a Python code snippet to manage student admissions for the M.Pharm program at DBCOP, considering the program's specializations."
Generated: DETERMINISTIC_c45b64beafc6ed0c
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class Specialization(Enum):
    """Enum for M.Pharm program specializations"""
    PHARMACOLOGY = "Pharmacology"
    PHARMACEUTICS = "Pharmaceutics"
    PHARMACOGNOSY = "Pharmacognosy"
    QUALITY_ASSURANCE = "Quality Assurance"

class Student:
    """Class representing a student"""
    def __init__(self, name: str, email: str, specialization: Specialization):
        """
        Initialize a Student object

        Args:
        - name (str): Student's name
        - email (str): Student's email
        - specialization (Specialization): Student's chosen specialization
        """
        self.name = name
        self.email = email
        self.specialization = specialization

class AdmissionManager:
    """Class responsible for managing student admissions"""
    def __init__(self):
        """Initialize an AdmissionManager object"""
        self.admitted_students: Dict[Specialization, List[Student]] = {
            specialization: [] for specialization in Specialization
        }

    def add_student(self, student: Student):
        """
        Add a student to the admission list

        Args:
        - student (Student): Student to be added

        Raises:
        - ValueError: If the student's specialization is not valid
        """
        if not isinstance(student.specialization, Specialization):
            raise ValueError("Invalid specialization")
        
        self.admitted_students[student.specialization].append(student)

    def remove_student(self, email: str, specialization: Specialization):
        """
        Remove a student from the admission list

        Args:
        - email (str): Student's email
        - specialization (Specialization): Student's specialization

        Raises:
        - ValueError: If the student's specialization is not valid
        - Exception: If the student is not found in the admission list
        """
        if not isinstance(specialization, Specialization):
            raise ValueError("Invalid specialization")
        
        self.admitted_students[specialization] = [
            student for student in self.admitted_students[specialization] 
            if student.email != email
        ]

    def get_admitted_students(self, specialization: Specialization = None):
        """
        Get admitted students for a specific specialization or all specializations

        Args:
        - specialization (Specialization, optional): Specialization to filter by. Defaults to None.

        Returns:
        - List[Student]: List of admitted students
        """
        if specialization:
            if not isinstance(specialization, Specialization):
                raise ValueError("Invalid specialization")
            return self.admitted_students[specialization]
        else:
            return [student for students in self.admitted_students.values() for student in students]

def main():
    # Example usage
    admission_manager = AdmissionManager()

    student1 = Student("John Doe", "john@example.com", Specialization.PHARMACOLOGY)
    student2 = Student("Jane Doe", "jane@example.com", Specialization.PHARMACEUTICS)

    admission_manager.add_student(student1)
    admission_manager.add_student(student2)

    print("Admitted Students:")
    for student in admission_manager.get_admitted_students():
        print(f"Name: {student.name}, Email: {student.email}, Specialization: {student.specialization.value}")

    admission_manager.remove_student("john@example.com", Specialization.PHARMACOLOGY)

    print("\nAdmitted Students after removal:")
    for student in admission_manager.get_admitted_students():
        print(f"Name: {student.name}, Email: {student.email}, Specialization: {student.specialization.value}")

if __name__ == "__main__":
    main()
```
