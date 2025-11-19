"""
Generated Code Metadata:
========================
Original URL: https://colegiohuitakafusa.com
Prompt: Generate a Python script that simulates a virtual classroom environment for the "Bachillerato Virtual" program at Colegio Huitaka Fusagasugá.
Generated: DETERMINISTIC_020019a0803e52a5
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtual_classroom.py

class Student:
    """Represents a student in the virtual classroom."""

    def __init__(self, student_id, name, email):
        """
        Initializes a Student object.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Student's name.
            email (str): Student's email address.
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    def enroll_course(self, course):
        """Enrolls the student in a course."""
        self.courses.append(course)


class Course:
    """Represents a course in the virtual classroom."""

    def __init__(self, course_id, name, description):
        """
        Initializes a Course object.

        Args:
            course_id (int): Unique identifier for the course.
            name (str): Course name.
            description (str): Course description.
        """
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students = []

    def add_student(self, student):
        """Adds a student to the course."""
        self.students.append(student)
        student.enroll_course(self)


class VirtualClassroom:
    """Simulates a virtual classroom environment."""

    def __init__(self):
        self.students = []
        self.courses = []

    def create_student(self, student_id, name, email):
        """
        Creates a new student.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Student's name.
            email (str): Student's email address.

        Returns:
            Student: The newly created Student object.
        """
        student = Student(student_id, name, email)
        self.students.append(student)
        return student

    def create_course(self, course_id, name, description):
        """
        Creates a new course.

        Args:
            course_id (int): Unique identifier for the course.
            name (str): Course name.
            description (str): Course description.

        Returns:
            Course: The newly created Course object.
        """
        course = Course(course_id, name, description)
        self.courses.append(course)
        return course

    def enroll_student_in_course(self, student, course):
        """
        Enrolls a student in a course.

        Args:
            student (Student): The student to enroll.
            course (Course): The course to enroll in.
        """
        course.add_student(student)

    def print_classroom_info(self):
        """Prints information about the virtual classroom."""
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}")
            print("Courses:")
            for course in student.courses:
                print(f"- {course.name}")
        print("\nCourses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}, Description: {course.description}")
            print("Students:")
            for student in course.students:
                print(f"- {student.name}")


def main():
    try:
        classroom = VirtualClassroom()

        # Create students
        student1 = classroom.create_student(1, "John Doe", "john@example.com")
        student2 = classroom.create_student(2, "Jane Doe", "jane@example.com")

        # Create courses
        course1 = classroom.create_course(1, "Math", "Mathematics course")
        course2 = classroom.create_course(2, "Science", "Science course")

        # Enroll students in courses
        classroom.enroll_student_in_course(student1, course1)
        classroom.enroll_student_in_course(student1, course2)
        classroom.enroll_student_in_course(student2, course1)

        # Print classroom information
        classroom.print_classroom_info()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
