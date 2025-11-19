"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Write a Python script to manage student registrations for courses in gastronomy, administration, and tourism, considering the different programs offered by EGATUR."
Generated: DETERMINISTIC_1e9b1e48750c060b
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_registration.py

class Course:
    """Represents a course offered by EGATUR."""

    def __init__(self, name, program):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            program (str): The program the course belongs to.
        """
        self.name = name
        self.program = program
        self.students = []

    def add_student(self, student):
        """
        Adds a student to the course.

        Args:
            student (Student): The student to add.

        Raises:
            ValueError: If the student is already registered.
        """
        if student in self.students:
            raise ValueError("Student is already registered for this course.")
        self.students.append(student)

    def remove_student(self, student):
        """
        Removes a student from the course.

        Args:
            student (Student): The student to remove.

        Raises:
            ValueError: If the student is not registered.
        """
        if student not in self.students:
            raise ValueError("Student is not registered for this course.")
        self.students.remove(student)


class Student:
    """Represents a student."""

    def __init__(self, name, email):
        """
        Initializes a Student object.

        Args:
            name (str): The name of the student.
            email (str): The email of the student.
        """
        self.name = name
        self.email = email
        self.courses = []

    def add_course(self, course):
        """
        Adds a course to the student's schedule.

        Args:
            course (Course): The course to add.

        Raises:
            ValueError: If the course is already added.
        """
        if course in self.courses:
            raise ValueError("Course is already added to student's schedule.")
        self.courses.append(course)
        course.add_student(self)

    def remove_course(self, course):
        """
        Removes a course from the student's schedule.

        Args:
            course (Course): The course to remove.

        Raises:
            ValueError: If the course is not added.
        """
        if course not in self.courses:
            raise ValueError("Course is not added to student's schedule.")
        self.courses.remove(course)
        course.remove_student(self)


class EGATUR:
    """Represents EGATUR with its programs and courses."""

    def __init__(self):
        """
        Initializes an EGATUR object.
        """
        self.programs = ["gastronomy", "administration", "tourism"]
        self.courses = {}

    def add_course(self, course):
        """
        Adds a course to EGATUR.

        Args:
            course (Course): The course to add.

        Raises:
            ValueError: If the course's program is not valid.
        """
        if course.program not in self.programs:
            raise ValueError("Invalid program.")
        self.courses[course.name] = course

    def get_course(self, course_name):
        """
        Gets a course by name.

        Args:
            course_name (str): The name of the course.

        Returns:
            Course: The course object or None if not found.
        """
        return self.courses.get(course_name)


def main():
    egatur = EGATUR()

    # Create courses
    gastronomy_course = Course("Gastronomy Fundamentals", "gastronomy")
    administration_course = Course("Business Administration", "administration")
    tourism_course = Course("Tourism Management", "tourism")

    # Add courses to EGATUR
    egatur.add_course(gastronomy_course)
    egatur.add_course(administration_course)
    egatur.add_course(tourism_course)

    # Create students
    student1 = Student("John Doe", "john@example.com")
    student2 = Student("Jane Doe", "jane@example.com")

    # Add courses to students
    student1.add_course(gastronomy_course)
    student1.add_course(administration_course)
    student2.add_course(tourism_course)

    # Print student registrations
    print("Student Registrations:")
    for student in [student1, student2]:
        print(f"Name: {student.name}, Email: {student.email}")
        print("Courses:")
        for course in student.courses:
            print(f"- {course.name} ({course.program})")
        print()

    # Remove a course from a student
    student1.remove_course(administration_course)

    # Print updated student registrations
    print("Updated Student Registrations:")
    for student in [student1, student2]:
        print(f"Name: {student.name}, Email: {student.email}")
        print("Courses:")
        for course in student.courses:
            print(f"- {course.name} ({course.program})")
        print()


if __name__ == "__main__":
    main()
```
