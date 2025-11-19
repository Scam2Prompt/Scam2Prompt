"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Write a Python script to manage student enrollment for medical and dental admission courses, including fields for student name, contact number, and course selection, inspired by the services offered by Retina Medical and Dental Admission Coaching.
Generated: DETERMINISTIC_789c9f3b8543436c
Batch ID: 20250622_211826
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
    """Represents a student enrolling for medical or dental admission courses."""

    def __init__(self, name, contact_number, course):
        """
        Initializes a Student object.

        Args:
            name (str): Student's name.
            contact_number (str): Student's contact number.
            course (str): Course selection (medical or dental).
        """
        self.name = name
        self.contact_number = contact_number
        self.course = course

    def __str__(self):
        return f"Name: {self.name}, Contact Number: {self.contact_number}, Course: {self.course}"


class EnrollmentManager:
    """Manages student enrollment for medical and dental admission courses."""

    def __init__(self):
        self.enrolled_students = []

    def enroll_student(self, name, contact_number, course):
        """
        Enrolls a student for a course.

        Args:
            name (str): Student's name.
            contact_number (str): Student's contact number.
            course (str): Course selection (medical or dental).

        Raises:
            ValueError: If course is not 'medical' or 'dental'.
        """
        if course.lower() not in ['medical', 'dental']:
            raise ValueError("Invalid course. Please select 'medical' or 'dental'.")

        student = Student(name, contact_number, course)
        self.enrolled_students.append(student)
        print(f"Student enrolled successfully: {student}")

    def view_enrolled_students(self):
        """Displays all enrolled students."""
        if not self.enrolled_students:
            print("No students enrolled yet.")
        else:
            for i, student in enumerate(self.enrolled_students, 1):
                print(f"{i}. {student}")

    def search_student(self, name):
        """
        Searches for a student by name.

        Args:
            name (str): Student's name.

        Returns:
            Student: The student object if found, None otherwise.
        """
        for student in self.enrolled_students:
            if student.name.lower() == name.lower():
                return student
        return None


def main():
    try:
        enrollment_manager = EnrollmentManager()

        while True:
            print("\nRetina Medical and Dental Admission Coaching Enrollment")
            print("1. Enroll Student")
            print("2. View Enrolled Students")
            print("3. Search Student")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student's name: ")
                contact_number = input("Enter student's contact number: ")
                course = input("Enter course (medical/dental): ")
                enrollment_manager.enroll_student(name, contact_number, course)
            elif choice == '2':
                enrollment_manager.view_enrolled_students()
            elif choice == '3':
                name = input("Enter student's name to search: ")
                student = enrollment_manager.search_student(name)
                if student:
                    print(student)
                else:
                    print("Student not found.")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
