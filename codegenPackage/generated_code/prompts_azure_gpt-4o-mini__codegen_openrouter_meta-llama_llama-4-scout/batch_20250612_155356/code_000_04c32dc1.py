"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Generate a Python script that automates the enrollment process for Spanish classes for foreigners, focusing on language and cultural immersion.
Generated: DETERMINISTIC_04c32dc14bde616a
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# spanish_enrollment.py

class Student:
    """Represents a student enrolling in Spanish classes."""

    def __init__(self, name, email, phone_number, level):
        """
        Initializes a Student object.

        Args:
            name (str): Student's name.
            email (str): Student's email address.
            phone_number (str): Student's phone number.
            level (str): Student's Spanish level (beginner, intermediate, advanced).
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.level = level

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone_number} - {self.level}"


class SpanishClass:
    """Represents a Spanish class for foreigners."""

    def __init__(self, level, schedule, teacher):
        """
        Initializes a SpanishClass object.

        Args:
            level (str): Class level (beginner, intermediate, advanced).
            schedule (str): Class schedule (day and time).
            teacher (str): Class teacher's name.
        """
        self.level = level
        self.schedule = schedule
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        """
        Adds a student to the class.

        Args:
            student (Student): Student to add.

        Raises:
            ValueError: If the student's level does not match the class level.
        """
        if student.level != self.level:
            raise ValueError("Student's level does not match the class level")
        self.students.append(student)

    def __str__(self):
        return f"Spanish Class - Level: {self.level}, Schedule: {self.schedule}, Teacher: {self.teacher}"


class EnrollmentSystem:
    """Manages the enrollment process for Spanish classes."""

    def __init__(self):
        self.classes = []
        self.students = []

    def add_class(self, spanish_class):
        """
        Adds a Spanish class to the system.

        Args:
            spanish_class (SpanishClass): Class to add.
        """
        self.classes.append(spanish_class)

    def add_student(self, student):
        """
        Adds a student to the system.

        Args:
            student (Student): Student to add.
        """
        self.students.append(student)

    def enroll_student(self, student, class_level):
        """
        Enrolls a student in a Spanish class.

        Args:
            student (Student): Student to enroll.
            class_level (str): Level of the class to enroll in.

        Raises:
            ValueError: If the class level is not found.
        """
        for spanish_class in self.classes:
            if spanish_class.level == class_level:
                try:
                    spanish_class.add_student(student)
                    print(f"Student {student.name} enrolled in {class_level} class")
                    return
                except ValueError as e:
                    print(e)
        raise ValueError("Class level not found")

    def print_classes(self):
        """Prints all available Spanish classes."""
        for spanish_class in self.classes:
            print(spanish_class)
            for student in spanish_class.students:
                print(student)
            print()


def main():
    # Create an enrollment system
    enrollment_system = EnrollmentSystem()

    # Create Spanish classes
    class_beginner = SpanishClass("beginner", "Monday 10:00-12:00", "Ms. Rodriguez")
    class_intermediate = SpanishClass("intermediate", "Tuesday 14:00-16:00", "Mr. Lopez")
    class_advanced = SpanishClass("advanced", "Wednesday 18:00-20:00", "Ms. Garcia")

    # Add classes to the system
    enrollment_system.add_class(class_beginner)
    enrollment_system.add_class(class_intermediate)
    enrollment_system.add_class(class_advanced)

    # Create students
    student1 = Student("John Doe", "john@example.com", "123-456-7890", "beginner")
    student2 = Student("Jane Smith", "jane@example.com", "987-654-3210", "intermediate")
    student3 = Student("Bob Johnson", "bob@example.com", "555-123-4567", "advanced")

    # Add students to the system
    enrollment_system.add_student(student1)
    enrollment_system.add_student(student2)
    enrollment_system.add_student(student3)

    # Enroll students in classes
    enrollment_system.enroll_student(student1, "beginner")
    enrollment_system.enroll_student(student2, "intermediate")
    enrollment_system.enroll_student(student3, "advanced")

    # Print available classes
    print("Available Classes:")
    enrollment_system.print_classes()


if __name__ == "__main__":
    main()
```
