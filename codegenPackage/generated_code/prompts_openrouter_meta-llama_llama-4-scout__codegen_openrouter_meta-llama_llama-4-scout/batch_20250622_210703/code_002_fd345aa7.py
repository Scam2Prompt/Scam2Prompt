"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Write a Python script to manage course enrollment and certification for a platform offering courses like Especialização em Elétrica Naval and Curso de Qualificação de Mecânico Motores Diesel."
Generated: DETERMINISTIC_fd345aa705940580
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_enrollment.py

class Course:
    """Represents a course on the platform."""

    def __init__(self, id, name):
        """
        Initializes a Course object.

        Args:
            id (int): Unique course ID.
            name (str): Course name.
        """
        self.id = id
        self.name = name
        self.enrolled_students = []
        self.certified_students = []

    def enroll_student(self, student_id):
        """
        Enrolls a student in the course.

        Args:
            student_id (int): ID of the student to enroll.

        Raises:
            ValueError: If the student is already enrolled.
        """
        if student_id in self.enrolled_students:
            raise ValueError("Student is already enrolled in this course.")
        self.enrolled_students.append(student_id)

    def certify_student(self, student_id):
        """
        Certifies a student who has completed the course.

        Args:
            student_id (int): ID of the student to certify.

        Raises:
            ValueError: If the student is not enrolled or already certified.
        """
        if student_id not in self.enrolled_students:
            raise ValueError("Student is not enrolled in this course.")
        if student_id in self.certified_students:
            raise ValueError("Student is already certified.")
        self.certified_students.append(student_id)


class CoursePlatform:
    """Represents the course platform."""

    def __init__(self):
        """
        Initializes a CoursePlatform object.
        """
        self.courses = {}

    def add_course(self, course_id, course_name):
        """
        Adds a course to the platform.

        Args:
            course_id (int): Unique course ID.
            course_name (str): Course name.

        Raises:
            ValueError: If a course with the same ID already exists.
        """
        if course_id in self.courses:
            raise ValueError("Course with this ID already exists.")
        self.courses[course_id] = Course(course_id, course_name)

    def get_course(self, course_id):
        """
        Retrieves a course by ID.

        Args:
            course_id (int): ID of the course to retrieve.

        Returns:
            Course: The course object, or None if not found.
        """
        return self.courses.get(course_id)

    def enroll_student_in_course(self, course_id, student_id):
        """
        Enrolls a student in a course.

        Args:
            course_id (int): ID of the course.
            student_id (int): ID of the student to enroll.

        Raises:
            ValueError: If the course or student ID is invalid.
        """
        course = self.get_course(course_id)
        if course is None:
            raise ValueError("Course not found.")
        course.enroll_student(student_id)

    def certify_student_in_course(self, course_id, student_id):
        """
        Certifies a student who has completed a course.

        Args:
            course_id (int): ID of the course.
            student_id (int): ID of the student to certify.

        Raises:
            ValueError: If the course or student ID is invalid.
        """
        course = self.get_course(course_id)
        if course is None:
            raise ValueError("Course not found.")
        course.certify_student(student_id)


def main():
    platform = CoursePlatform()

    # Add courses
    platform.add_course(1, "Especialização em Elétrica Naval")
    platform.add_course(2, "Curso de Qualificação de Mecânico Motores Diesel")

    # Enroll students
    platform.enroll_student_in_course(1, 101)
    platform.enroll_student_in_course(1, 102)
    platform.enroll_student_in_course(2, 103)

    # Certify students
    platform.certify_student_in_course(1, 101)
    platform.certify_student_in_course(2, 103)

    # Print course information
    for course_id, course in platform.courses.items():
        print(f"Course ID: {course.id}, Name: {course.name}")
        print(f"Enrolled Students: {course.enrolled_students}")
        print(f"Certified Students: {course.certified_students}")
        print()


if __name__ == "__main__":
    main()
```
