"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Write code to simulate the allocation of students into ENAFO's folklore modules based on their preferences and available slots.
Generated: DETERMINISTIC_c7683e6b53868c1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

class Student:
    """Represents a student with their preferences."""

    def __init__(self, student_id: int, preferences: List[str]):
        """
        Initializes a Student object.

        Args:
        - student_id (int): Unique identifier for the student.
        - preferences (List[str]): List of folklore module preferences.
        """
        self.student_id = student_id
        self.preferences = preferences


class Module:
    """Represents a folklore module with available slots."""

    def __init__(self, module_name: str, available_slots: int):
        """
        Initializes a Module object.

        Args:
        - module_name (str): Name of the folklore module.
        - available_slots (int): Number of available slots in the module.
        """
        self.module_name = module_name
        self.available_slots = available_slots
        self.enrolled_students = []

    def enroll_student(self, student: Student) -> bool:
        """
        Enrolls a student in the module if there are available slots.

        Args:
        - student (Student): Student to be enrolled.

        Returns:
        - bool: True if the student is enrolled successfully, False otherwise.
        """
        if self.available_slots > 0:
            self.enrolled_students.append(student)
            self.available_slots -= 1
            return True
        return False


def allocate_students_to_modules(students: List[Student], modules: Dict[str, Module]) -> Dict[str, List[Student]]:
    """
    Allocates students to folklore modules based on their preferences and available slots.

    Args:
    - students (List[Student]): List of students with their preferences.
    - modules (Dict[str, Module]): Dictionary of folklore modules with their available slots.

    Returns:
    - Dict[str, List[Student]]: Dictionary of enrolled students in each module.
    """
    # Create a dictionary to store enrolled students in each module
    enrolled_students = {module_name: [] for module_name in modules}

    # Iterate over each student
    for student in students:
        # Iterate over each preference of the student
        for preference in student.preferences:
            # Check if the preferred module exists and has available slots
            if preference in modules and modules[preference].available_slots > 0:
                # Enroll the student in the preferred module
                if modules[preference].enroll_student(student):
                    enrolled_students[preference].append(student)
                    break  # Move to the next student

    return enrolled_students


def main():
    # Example usage
    try:
        # Create students with their preferences
        students = [
            Student(1, ["Module A", "Module B", "Module C"]),
            Student(2, ["Module B", "Module A", "Module D"]),
            Student(3, ["Module C", "Module D", "Module A"]),
            Student(4, ["Module A", "Module C", "Module B"]),
            Student(5, ["Module D", "Module B", "Module C"]),
        ]

        # Create folklore modules with available slots
        modules = {
            "Module A": Module("Module A", 2),
            "Module B": Module("Module B", 2),
            "Module C": Module("Module C", 1),
            "Module D": Module("Module D", 1),
        }

        # Allocate students to modules
        enrolled_students = allocate_students_to_modules(students, modules)

        # Print enrolled students in each module
        for module_name, students_in_module in enrolled_students.items():
            print(f"Enrolled students in {module_name}:")
            for student in students_in_module:
                print(f"Student ID: {student.student_id}, Preferences: {student.preferences}")
            print()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
