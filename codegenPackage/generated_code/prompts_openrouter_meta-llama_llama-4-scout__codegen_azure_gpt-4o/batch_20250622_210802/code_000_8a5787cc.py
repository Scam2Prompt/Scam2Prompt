"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: "Generate a Python script to manage student enrollment for admission exam preparation courses, including personalized classes and flexible scheduling."
Generated: DETERMINISTIC_8a5787cc828bd2ea
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Student:
    """
    Represents a student enrolling in exam preparation courses.
    """
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []

    def enroll_course(self, course):
        """
        Enroll the student in a course.
        """
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"{self.name} has been enrolled in {course.name}.")
        else:
            print(f"{self.name} is already enrolled in {course.name}.")

    def view_enrolled_courses(self):
        """
        Display all courses the student is enrolled in.
        """
        if self.enrolled_courses:
            print(f"{self.name} is enrolled in the following courses:")
            for course in self.enrolled_courses:
                print(f"- {course.name} (Schedule: {course.schedule})")
        else:
            print(f"{self.name} is not enrolled in any courses.")


class Course:
    """
    Represents an exam preparation course.
    """
    def __init__(self, course_id, name, schedule):
        self.course_id = course_id
        self.name = name
        self.schedule = schedule


class EnrollmentManager:
    """
    Manages student enrollment for courses.
    """
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name, email):
        """
        Add a new student to the system.
        """
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name, email)
            print(f"Student {name} has been added.")
        else:
            print(f"Student with ID {student_id} already exists.")

    def add_course(self, course_id, name, schedule):
        """
        Add a new course to the system.
        """
        if course_id not in self.courses:
            self.courses[course_id] = Course(course_id, name, schedule)
            print(f"Course {name} has been added.")
        else:
            print(f"Course with ID {course_id} already exists.")

    def enroll_student_in_course(self, student_id, course_id):
        """
        Enroll a student in a course.
        """
        try:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.enroll_course(course)
        except KeyError as e:
            print(f"Error: {e}. Please ensure both student and course exist.")

    def view_student_courses(self, student_id):
        """
        View all courses a student is enrolled in.
        """
        try:
            student = self.students[student_id]
            student.view_enrolled_courses()
        except KeyError:
            print(f"Error: Student with ID {student_id} does not exist.")


# Example usage
if __name__ == "__main__":
    manager = EnrollmentManager()

    # Adding students
    manager.add_student(1, "Alice", "alice@example.com")
    manager.add_student(2, "Bob", "bob@example.com")

    # Adding courses
    manager.add_course(101, "Math Preparation", "Monday 10:00 AM - 12:00 PM")
    manager.add_course(102, "Science Preparation", "Wednesday 2:00 PM - 4:00 PM")

    # Enrolling students in courses
    manager.enroll_student_in_course(1, 101)
    manager.enroll_student_in_course(1, 102)
    manager.enroll_student_in_course(2, 101)

    # Viewing enrolled courses
    manager.view_student_courses(1)
    manager.view_student_courses(2)
```
