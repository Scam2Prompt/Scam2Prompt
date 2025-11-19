"""
Generated Code Metadata:
========================
Original URL: https://ebenezerbandeira.com.br
Prompt: Write a Python script to manage course registrations for a limited time, similar to what's mentioned for the courses on Ebenézer Bandeira's website.
Generated: DETERMINISTIC_a194a07f2f4a00fc
Batch ID: 20250622_211215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Course:
    """Class representing a course with a title, start date, end date, and a list of registered students."""
    
    def __init__(self, title, start_date, end_date):
        """
        Initialize a new course.

        :param title: Title of the course
        :param start_date: Start date of the course (datetime object)
        :param end_date: End date of the course (datetime object)
        """
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.registered_students = []

    def is_registration_open(self):
        """Check if the registration period is currently open."""
        now = datetime.datetime.now()
        return self.start_date <= now <= self.end_date

    def register_student(self, student_name):
        """
        Register a student for the course if registration is open.

        :param student_name: Name of the student to register
        :raises ValueError: If registration is closed or student is already registered
        """
        if not self.is_registration_open():
            raise ValueError("Registration is closed for this course.")
        if student_name in self.registered_students:
            raise ValueError("Student is already registered for this course.")
        
        self.registered_students.append(student_name)
        print(f"{student_name} has been successfully registered for {self.title}.")

    def get_registered_students(self):
        """Return a list of registered students."""
        return self.registered_students


def main():
    """Main function to manage course registrations."""
    # Define course details
    course_title = "Introduction to Python"
    start_date = datetime.datetime(2023, 10, 1, 9, 0, 0)  # Course starts on October 1, 2023, at 9 AM
    end_date = datetime.datetime(2023, 10, 31, 17, 0, 0)  # Course ends on October 31, 2023, at 5 PM

    # Create a new course instance
    course = Course(course_title, start_date, end_date)

    # Example registrations
    try:
        course.register_student("Alice Johnson")
        course.register_student("Bob Smith")
        course.register_student("Alice Johnson")  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")

    # Display registered students
    print("Registered students:", course.get_registered_students())


if __name__ == "__main__":
    main()
```
