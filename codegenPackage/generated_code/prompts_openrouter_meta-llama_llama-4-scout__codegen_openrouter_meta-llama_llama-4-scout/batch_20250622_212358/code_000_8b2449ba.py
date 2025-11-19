"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Write a Python script to manage student admissions for the Escuela de Suboficiales de la Fuerza Aérea del Perú, including tasks for registration and evaluation.
Generated: DETERMINISTIC_8b2449baa923df02
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_admissions.py

class Student:
    """Represents a student applying for admission."""

    def __init__(self, name, age, grade):
        """
        Initializes a Student object.

        Args:
            name (str): Student's name.
            age (int): Student's age.
            grade (float): Student's grade.
        """
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.name}, {self.age} years old, Grade: {self.grade}"


class AdmissionSystem:
    """Manages student admissions."""

    def __init__(self):
        """Initializes an AdmissionSystem object."""
        self.students = []
        self.min_age = 17
        self.min_grade = 10.0

    def register_student(self, name, age, grade):
        """
        Registers a new student.

        Args:
            name (str): Student's name.
            age (int): Student's age.
            grade (float): Student's grade.

        Raises:
            ValueError: If age or grade is invalid.
        """
        if age < self.min_age:
            raise ValueError(f"Age must be at least {self.min_age}")
        if grade < self.min_grade:
            raise ValueError(f"Grade must be at least {self.min_grade}")

        student = Student(name, age, grade)
        self.students.append(student)
        return student

    def evaluate_students(self):
        """
        Evaluates registered students and returns those who meet the requirements.

        Returns:
            list[Student]: List of students who meet the requirements.
        """
        return [student for student in self.students if student.grade >= self.min_grade and student.age >= self.min_age]

    def print_students(self, students):
        """
        Prints a list of students.

        Args:
            students (list[Student]): List of students to print.
        """
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student}")


def main():
    admission_system = AdmissionSystem()

    while True:
        print("\nEscuela de Suboficiales de la Fuerza Aérea del Perú Admission System")
        print("1. Register Student")
        print("2. Evaluate Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter student's name: ")
                age = int(input("Enter student's age: "))
                grade = float(input("Enter student's grade: "))
                student = admission_system.register_student(name, age, grade)
                print(f"Student registered: {student}")
            elif choice == "2":
                eligible_students = admission_system.evaluate_students()
                print("\nEligible Students:")
                admission_system.print_students(eligible_students)
            elif choice == "3":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
