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
"""
Student Admissions Management for M.Pharm Program at DBCOP

This script manages student admissions for the M.Pharm program, considering the program's specializations.
It includes functionality to add students, view student details, and filter students by specialization.
"""

# Import necessary modules
import sys

class Student:
    """
    Represents a student applying for the M.Pharm program.
    """
    def __init__(self, student_id, name, specialization):
        """
        Initialize a Student object.

        :param student_id: Unique ID for the student
        :param name: Name of the student
        :param specialization: Specialization chosen by the student
        """
        self.student_id = student_id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        """
        String representation of the Student object.
        """
        return f"ID: {self.student_id}, Name: {self.name}, Specialization: {self.specialization}"


class AdmissionsManager:
    """
    Manages student admissions for the M.Pharm program.
    """
    def __init__(self):
        """
        Initialize the AdmissionsManager with an empty list of students.
        """
        self.students = []

    def add_student(self, student_id, name, specialization):
        """
        Add a new student to the admissions list.

        :param student_id: Unique ID for the student
        :param name: Name of the student
        :param specialization: Specialization chosen by the student
        :raises ValueError: If the specialization is invalid
        """
        valid_specializations = ["Pharmacology", "Pharmaceutics", "Pharmaceutical Chemistry", "Pharmacognosy"]
        if specialization not in valid_specializations:
            raise ValueError(f"Invalid specialization: {specialization}. Valid options are: {', '.join(valid_specializations)}")
        
        new_student = Student(student_id, name, specialization)
        self.students.append(new_student)
        print(f"Student {name} added successfully!")

    def view_students(self):
        """
        View all students in the admissions list.
        """
        if not self.students:
            print("No students have been admitted yet.")
            return
        
        print("List of admitted students:")
        for student in self.students:
            print(student)

    def filter_students_by_specialization(self, specialization):
        """
        Filter students by their chosen specialization.

        :param specialization: Specialization to filter by
        :raises ValueError: If the specialization is invalid
        """
        valid_specializations = ["Pharmacology", "Pharmaceutics", "Pharmaceutical Chemistry", "Pharmacognosy"]
        if specialization not in valid_specializations:
            raise ValueError(f"Invalid specialization: {specialization}. Valid options are: {', '.join(valid_specializations)}")
        
        filtered_students = [student for student in self.students if student.specialization == specialization]
        
        if not filtered_students:
            print(f"No students found for specialization: {specialization}")
            return
        
        print(f"Students specializing in {specialization}:")
        for student in filtered_students:
            print(student)


# Main function to demonstrate the AdmissionsManager functionality
def main():
    """
    Main function to run the admissions management system.
    """
    manager = AdmissionsManager()

    try:
        # Add students
        manager.add_student(1, "Alice Johnson", "Pharmacology")
        manager.add_student(2, "Bob Smith", "Pharmaceutics")
        manager.add_student(3, "Charlie Brown", "Pharmaceutical Chemistry")

        # View all students
        manager.view_students()

        # Filter students by specialization
        manager.filter_students_by_specialization("Pharmaceutics")
        manager.filter_students_by_specialization("Pharmacognosy")  # No students in this specialization

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```
