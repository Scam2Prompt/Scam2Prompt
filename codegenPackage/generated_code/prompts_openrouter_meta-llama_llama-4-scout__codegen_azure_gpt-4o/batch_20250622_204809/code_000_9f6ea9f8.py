"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: "Generate a Python script to manage course enrollment for a training program in public management and law, similar to those offered by Escuela de Ciencias Politicas."
Generated: DETERMINISTIC_9f6ea9f8dc07ca5d
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Course Enrollment Management System

This script allows users to manage course enrollment for a training program
in public management and law. It includes functionality to add courses,
enroll students, view enrolled students, and handle errors gracefully.

Author: [Your Name]
Date: [Today's Date]
"""

import sys

class CourseEnrollmentSystem:
    def __init__(self):
        # Initialize the system with empty courses and enrollments
        self.courses = {}  # Dictionary to store courses and their enrolled students

    def add_course(self, course_name):
        """
        Add a new course to the system.
        :param course_name: Name of the course to be added.
        """
        if course_name in self.courses:
            print(f"Error: Course '{course_name}' already exists.")
        else:
            self.courses[course_name] = []
            print(f"Course '{course_name}' added successfully.")

    def enroll_student(self, course_name, student_name):
        """
        Enroll a student in a specific course.
        :param course_name: Name of the course.
        :param student_name: Name of the student to enroll.
        """
        if course_name not in self.courses:
            print(f"Error: Course '{course_name}' does not exist.")
        elif student_name in self.courses[course_name]:
            print(f"Error: Student '{student_name}' is already enrolled in '{course_name}'.")
        else:
            self.courses[course_name].append(student_name)
            print(f"Student '{student_name}' enrolled in '{course_name}' successfully.")

    def view_enrolled_students(self, course_name):
        """
        View all students enrolled in a specific course.
        :param course_name: Name of the course.
        """
        if course_name not in self.courses:
            print(f"Error: Course '{course_name}' does not exist.")
        else:
            students = self.courses[course_name]
            if not students:
                print(f"No students are enrolled in '{course_name}'.")
            else:
                print(f"Students enrolled in '{course_name}':")
                for student in students:
                    print(f"- {student}")

    def list_courses(self):
        """
        List all available courses in the system.
        """
        if not self.courses:
            print("No courses available.")
        else:
            print("Available courses:")
            for course in self.courses:
                print(f"- {course}")


def main():
    """
    Main function to run the Course Enrollment System.
    """
    system = CourseEnrollmentSystem()

    while True:
        print("\nCourse Enrollment System")
        print("1. Add Course")
        print("2. Enroll Student")
        print("3. View Enrolled Students")
        print("4. List Courses")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            course_name = input("Enter course name: ").strip()
            system.add_course(course_name)
        elif choice == 2:
            course_name = input("Enter course name: ").strip()
            student_name = input("Enter student name: ").strip()
            system.enroll_student(course_name, student_name)
        elif choice == 3:
            course_name = input("Enter course name: ").strip()
            system.view_enrolled_students(course_name)
        elif choice == 4:
            system.list_courses()
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
```
