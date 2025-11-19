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
# student_enrollment.py

from datetime import datetime, timedelta
from typing import Dict, List

class Student:
    """Represents a student enrolled in a course."""

    def __init__(self, student_id: int, name: str, email: str):
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

    def __str__(self):
        return f"Student {self.name} ({self.student_id}) - {self.email}"


class Course:
    """Represents an admission exam preparation course."""

    def __init__(self, course_id: int, name: str, description: str):
        """
        Initializes a Course object.

        Args:
            course_id (int): Unique identifier for the course.
            name (str): Course name.
            description (str): Brief course description.
        """
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students = []
        self.schedule = []

    def __str__(self):
        return f"Course {self.name} ({self.course_id}) - {self.description}"


class EnrollmentSystem:
    """Manages student enrollment for admission exam preparation courses."""

    def __init__(self):
        self.students: Dict[int, Student] = {}
        self.courses: Dict[int, Course] = {}
        self.course_id_counter = 1
        self.student_id_counter = 1

    def create_course(self, name: str, description: str) -> Course:
        """
        Creates a new course.

        Args:
            name (str): Course name.
            description (str): Brief course description.

        Returns:
            Course: The newly created course.
        """
        course = Course(self.course_id_counter, name, description)
        self.courses[self.course_id_counter] = course
        self.course_id_counter += 1
        return course

    def create_student(self, name: str, email: str) -> Student:
        """
        Creates a new student.

        Args:
            name (str): Student's name.
            email (str): Student's email address.

        Returns:
            Student: The newly created student.
        """
        student = Student(self.student_id_counter, name, email)
        self.students[self.student_id_counter] = student
        self.student_id_counter += 1
        return student

    def enroll_student(self, student_id: int, course_id: int) -> bool:
        """
        Enrolls a student in a course.

        Args:
            student_id (int): Unique identifier for the student.
            course_id (int): Unique identifier for the course.

        Returns:
            bool: True if enrollment was successful, False otherwise.
        """
        if student_id not in self.students or course_id not in self.courses:
            return False

        student = self.students[student_id]
        course = self.courses[course_id]
        student.courses.append(course)
        course.students.append(student)
        return True

    def schedule_class(self, course_id: int, date: str, time: str) -> bool:
        """
        Schedules a class for a course.

        Args:
            course_id (int): Unique identifier for the course.
            date (str): Date of the class (YYYY-MM-DD).
            time (str): Time of the class (HH:MM).

        Returns:
            bool: True if scheduling was successful, False otherwise.
        """
        if course_id not in self.courses:
            return False

        course = self.courses[course_id]
        try:
            class_date = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            course.schedule.append(class_date)
            return True
        except ValueError:
            return False

    def print_student_info(self, student_id: int) -> None:
        """
        Prints information about a student.

        Args:
            student_id (int): Unique identifier for the student.
        """
        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]
        print(student)
        print("Courses:")
        for course in student.courses:
            print(course)

    def print_course_info(self, course_id: int) -> None:
        """
        Prints information about a course.

        Args:
            course_id (int): Unique identifier for the course.
        """
        if course_id not in self.courses:
            print("Course not found.")
            return

        course = self.courses[course_id]
        print(course)
        print("Students:")
        for student in course.students:
            print(student)
        print("Schedule:")
        for class_date in course.schedule:
            print(class_date.strftime("%Y-%m-%d %H:%M"))


def main() -> None:
    enrollment_system = EnrollmentSystem()

    while True:
        print("\n1. Create Course")
        print("2. Create Student")
        print("3. Enroll Student")
        print("4. Schedule Class")
        print("5. Print Student Info")
        print("6. Print Course Info")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter course name: ")
            description = input("Enter course description: ")
            course = enrollment_system.create_course(name, description)
            print(f"Course created: {course}")
        elif choice == "2":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            student = enrollment_system.create_student(name, email)
            print(f"Student created: {student}")
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            if enrollment_system.enroll_student(student_id, course_id):
                print("Enrollment successful.")
            else:
                print("Enrollment failed.")
        elif choice == "4":
            course_id = int(input("Enter course ID: "))
            date = input("Enter class date (YYYY-MM-DD): ")
            time = input("Enter class time (HH:MM): ")
            if enrollment_system.schedule_class(course_id, date, time):
                print("Class scheduled successfully.")
            else:
                print("Class scheduling failed.")
        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            enrollment_system.print_student_info(student_id)
        elif choice == "6":
            course_id = int(input("Enter course ID: "))
            enrollment_system.print_course_info(course_id)
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
