"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: "Generate a Python script to manage course registrations for a vocational training program like those offered on araform.org."
Generated: DETERMINISTIC_d7452815c35aecba
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_registration.py

class Course:
    """Represents a vocational training course."""

    def __init__(self, course_id, name, capacity):
        """
        Initializes a Course object.

        Args:
            course_id (str): Unique identifier for the course.
            name (str): Name of the course.
            capacity (int): Maximum number of registrations allowed.
        """
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.registrations = []

    def register(self, student):
        """
        Registers a student for the course.

        Args:
            student (Student): Student object to register.

        Raises:
            ValueError: If course is already full or student is already registered.
        """
        if len(self.registrations) >= self.capacity:
            raise ValueError("Course is already full.")
        if student in self.registrations:
            raise ValueError("Student is already registered for this course.")
        self.registrations.append(student)

    def unregister(self, student):
        """
        Unregisters a student from the course.

        Args:
            student (Student): Student object to unregister.

        Raises:
            ValueError: If student is not registered for the course.
        """
        if student not in self.registrations:
            raise ValueError("Student is not registered for this course.")
        self.registrations.remove(student)


class Student:
    """Represents a student."""

    def __init__(self, student_id, name, email):
        """
        Initializes a Student object.

        Args:
            student_id (str): Unique identifier for the student.
            name (str): Name of the student.
            email (str): Email address of the student.
        """
        self.student_id = student_id
        self.name = name
        self.email = email

    def __eq__(self, other):
        """Checks if two Student objects are equal."""
        return self.student_id == other.student_id


class CourseRegistrationSystem:
    """Manages course registrations."""

    def __init__(self):
        """Initializes the course registration system."""
        self.courses = {}
        self.students = {}

    def add_course(self, course):
        """
        Adds a course to the system.

        Args:
            course (Course): Course object to add.

        Raises:
            ValueError: If course with the same ID already exists.
        """
        if course.course_id in self.courses:
            raise ValueError("Course with the same ID already exists.")
        self.courses[course.course_id] = course

    def add_student(self, student):
        """
        Adds a student to the system.

        Args:
            student (Student): Student object to add.

        Raises:
            ValueError: If student with the same ID already exists.
        """
        if student.student_id in self.students:
            raise ValueError("Student with the same ID already exists.")
        self.students[student.student_id] = student

    def register_student_for_course(self, student_id, course_id):
        """
        Registers a student for a course.

        Args:
            student_id (str): ID of the student to register.
            course_id (str): ID of the course to register for.

        Raises:
            ValueError: If student or course does not exist.
        """
        student = self.students.get(student_id)
        course = self.courses.get(course_id)
        if not student:
            raise ValueError("Student does not exist.")
        if not course:
            raise ValueError("Course does not exist.")
        course.register(student)

    def unregister_student_from_course(self, student_id, course_id):
        """
        Unregisters a student from a course.

        Args:
            student_id (str): ID of the student to unregister.
            course_id (str): ID of the course to unregister from.

        Raises:
            ValueError: If student or course does not exist.
        """
        student = self.students.get(student_id)
        course = self.courses.get(course_id)
        if not student:
            raise ValueError("Student does not exist.")
        if not course:
            raise ValueError("Course does not exist.")
        course.unregister(student)

    def print_course_registrations(self, course_id):
        """
        Prints registrations for a course.

        Args:
            course_id (str): ID of the course to print registrations for.
        """
        course = self.courses.get(course_id)
        if not course:
            print("Course does not exist.")
            return
        print(f"Registrations for {course.name}:")
        for student in course.registrations:
            print(f"- {student.name} ({student.email})")


def main():
    # Create a course registration system
    crs = CourseRegistrationSystem()

    # Create courses
    course1 = Course("course1", "Vocational Training Course 1", 10)
    course2 = Course("course2", "Vocational Training Course 2", 15)

    # Add courses to the system
    crs.add_course(course1)
    crs.add_course(course2)

    # Create students
    student1 = Student("student1", "John Doe", "john@example.com")
    student2 = Student("student2", "Jane Doe", "jane@example.com")

    # Add students to the system
    crs.add_student(student1)
    crs.add_student(student2)

    # Register students for courses
    crs.register_student_for_course("student1", "course1")
    crs.register_student_for_course("student2", "course1")
    crs.register_student_for_course("student1", "course2")

    # Print course registrations
    crs.print_course_registrations("course1")
    crs.print_course_registrations("course2")

    # Unregister a student from a course
    crs.unregister_student_from_course("student1", "course1")

    # Print updated course registrations
    crs.print_course_registrations("course1")


if __name__ == "__main__":
    main()
```
