"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Write a program to manage multi-sectoral vocational skills training, referencing MIEC's offerings in banking, finance, retail sales enablement, and digital media marketing.
Generated: DETERMINISTIC_122ab28527711bad
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to manage multi-sectoral vocational skills training based on MIEC's offerings.

This program allows administrators to add courses, enroll students, and view course and student information.
The offerings include training in banking, finance, retail sales enablement, and digital media marketing.
"""

import sys

class TrainingProgramManager:
    def __init__(self):
        # Initialize the courses and enrolled students
        self.courses = {}  # Format: {course_name: {description: str, students: list}}
    
    def add_course(self, name, description):
        """Add a new vocational skills training course.

        Args:
            name (str): Name of the course.
            description (str): Description of the course.

        Raises:
            ValueError: If a course with the given name already exists.
        """
        if name in self.courses:
            raise ValueError(f"Course '{name}' already exists.")
        self.courses[name] = {"description": description, "students": []}
        print(f"Course '{name}' added successfully.")

    def enroll_student(self, course_name, student_name):
        """Enroll a student in a specific course.

        Args:
            course_name (str): Name of the course.
            student_name (str): Name of the student.

        Raises:
            ValueError: If the course does not exist or if the student is already enrolled.
        """
        if course_name not in self.courses:
            raise ValueError(f"Course '{course_name}' does not exist.")
        if student_name in self.courses[course_name]["students"]:
            raise ValueError(f"Student '{student_name}' is already enrolled in '{course_name}'.")
        self.courses[course_name]["students"].append(student_name)
        print(f"Student '{student_name}' enrolled in '{course_name}' successfully.")
    
    def view_courses(self):
        """View all available courses with descriptions and enrolled students."""
        if not self.courses:
            print("No courses available.")
            return
        print("Available Courses:")
        for course_name, details in self.courses.items():
            print(f"- {course_name}: {details['description']}")
            print(f"  Enrolled Students: {', '.join(details['students']) if details['students'] else 'None'}")
    
    def view_students_in_course(self, course_name):
        """View all students enrolled in a specific course.

        Args:
            course_name (str): Name of the course.

        Raises:
            ValueError: If the course does not exist.
        """
        if course_name not in self.courses:
            raise ValueError(f"Course '{course_name}' does not exist.")
        students = self.courses[course_name]["students"]
        if not students:
            print(f"No students enrolled in '{course_name}'.")
        else:
            print(f"Students enrolled in '{course_name}': {', '.join(students)}")


def main():
    """Main function to manage user interaction."""
    manager = TrainingProgramManager()

    while True:
        print("\n===== Multi-Sectoral Vocational Skills Training Management =====")
        print("1. Add Course")
        print("2. Enroll Student")
        print("3. View Courses")
        print("4. View Students in a Course")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter course name: ")
                description = input("Enter course description: ")
                manager.add_course(name, description)
            elif choice == "2":
                course_name = input("Enter course name: ")
                student_name = input("Enter student name: ")
                manager.enroll_student(course_name, student_name)
            elif choice == "3":
                manager.view_courses()
            elif choice == "4":
                course_name = input("Enter course name: ")
                manager.view_students_in_course(course_name)
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
