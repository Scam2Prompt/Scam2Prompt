"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Generate a Python script that demonstrates how to manage student enrollment for the Graduate Diploma of Management (Learning) at Global Healthcare Management College.
Generated: DETERMINISTIC_3706fc22b7e63889
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_enrollment.py

class Student:
    """Represents a student enrolling in the Graduate Diploma of Management (Learning)."""

    def __init__(self, student_id, name, email):
        """
        Initializes a Student object.

        Args:
            student_id (str): Unique identifier for the student.
            name (str): Student's full name.
            email (str): Student's email address.
        """
        self.student_id = student_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}"


class Course:
    """Represents the Graduate Diploma of Management (Learning) course."""

    def __init__(self, course_code, course_name):
        """
        Initializes a Course object.

        Args:
            course_code (str): Unique code for the course.
            course_name (str): Full name of the course.
        """
        self.course_code = course_code
        self.course_name = course_name
        self.enrolled_students = []

    def enroll_student(self, student):
        """
        Enrolls a student in the course.

        Args:
            student (Student): Student object to be enrolled.

        Raises:
            ValueError: If the student is already enrolled.
        """
        if student in self.enrolled_students:
            raise ValueError("Student is already enrolled in this course.")
        self.enrolled_students.append(student)

    def unenroll_student(self, student_id):
        """
        Unenrolls a student from the course.

        Args:
            student_id (str): ID of the student to be unenrolled.

        Raises:
            ValueError: If the student is not found in the enrolled students list.
        """
        for student in self.enrolled_students:
            if student.student_id == student_id:
                self.enrolled_students.remove(student)
                return
        raise ValueError("Student not found in the enrolled students list.")

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}"


class EnrollmentManager:
    """Manages student enrollment for the Graduate Diploma of Management (Learning)."""

    def __init__(self):
        self.courses = {}
        self.students = {}

    def add_course(self, course):
        """
        Adds a course to the enrollment manager.

        Args:
            course (Course): Course object to be added.

        Raises:
            ValueError: If the course already exists.
        """
        if course.course_code in self.courses:
            raise ValueError("Course already exists.")
        self.courses[course.course_code] = course

    def add_student(self, student):
        """
        Adds a student to the enrollment manager.

        Args:
            student (Student): Student object to be added.

        Raises:
            ValueError: If the student already exists.
        """
        if student.student_id in self.students:
            raise ValueError("Student already exists.")
        self.students[student.student_id] = student

    def enroll_student_in_course(self, student_id, course_code):
        """
        Enrolls a student in a course.

        Args:
            student_id (str): ID of the student to be enrolled.
            course_code (str): Code of the course.

        Raises:
            ValueError: If the student or course is not found.
        """
        if student_id not in self.students:
            raise ValueError("Student not found.")
        if course_code not in self.courses:
            raise ValueError("Course not found.")
        student = self.students[student_id]
        course = self.courses[course_code]
        course.enroll_student(student)

    def unenroll_student_from_course(self, student_id, course_code):
        """
        Unenrolls a student from a course.

        Args:
            student_id (str): ID of the student to be unenrolled.
            course_code (str): Code of the course.

        Raises:
            ValueError: If the student or course is not found.
        """
        if course_code not in self.courses:
            raise ValueError("Course not found.")
        course = self.courses[course_code]
        course.unenroll_student(student_id)

    def print_enrolled_students(self, course_code):
        """
        Prints the enrolled students for a course.

        Args:
            course_code (str): Code of the course.

        Raises:
            ValueError: If the course is not found.
        """
        if course_code not in self.courses:
            raise ValueError("Course not found.")
        course = self.courses[course_code]
        print(f"Enrolled Students for {course}:")
        for student in course.enrolled_students:
            print(student)


def main():
    enrollment_manager = EnrollmentManager()

    # Create a course
    course = Course("GDM101", "Graduate Diploma of Management (Learning)")
    enrollment_manager.add_course(course)

    # Create students
    student1 = Student("S001", "John Doe", "john.doe@example.com")
    student2 = Student("S002", "Jane Smith", "jane.smith@example.com")
    enrollment_manager.add_student(student1)
    enrollment_manager.add_student(student2)

    # Enroll students in the course
    enrollment_manager.enroll_student_in_course("S001", "GDM101")
    enrollment_manager.enroll_student_in_course("S002", "GDM101")

    # Print enrolled students
    enrollment_manager.print_enrolled_students("GDM101")

    # Unenroll a student
    enrollment_manager.unenroll_student_from_course("S001", "GDM101")

    # Print enrolled students again
    print("\nAfter unenrolling a student:")
    enrollment_manager.print_enrolled_students("GDM101")


if __name__ == "__main__":
    main()
```
