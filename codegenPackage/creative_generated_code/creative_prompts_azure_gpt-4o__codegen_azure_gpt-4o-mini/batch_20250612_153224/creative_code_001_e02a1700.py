"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Recommend a system design for developing an integrated school management system for public institutions, as described in Licitare's "Solução em T.I" services.
Generated: DETERMINISTIC_e02a1700811e553e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
School Management System

This system is designed to manage various functionalities of a public school institution,
including student enrollment, course management, staff management, and reporting.
"""

class Student:
    """Class representing a student in the school management system."""

    def __init__(self, student_id, name, age):
        """
        Initialize a new student.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param age: Age of the student
        """
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        """Return a string representation of the student."""
        return f"{self.name} (ID: {self.student_id}, Age: {self.age})"


class Course:
    """Class representing a course offered at the school."""

    def __init__(self, course_id, title, credits):
        """
        Initialize a new course.

        :param course_id: Unique identifier for the course
        :param title: Title of the course
        :param credits: Number of credits for the course
        """
        self.course_id = course_id
        self.title = title
        self.credits = credits

    def __str__(self):
        """Return a string representation of the course."""
        return f"{self.title} (ID: {self.course_id}, Credits: {self.credits})"


class SchoolManagementSystem:
    """Class representing the overall school management system."""

    def __init__(self):
        """Initialize the school management system with empty data."""
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name, age):
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        
        self.students[student_id] = Student(student_id, name, age)

    def add_course(self, course_id, title, credits):
        """Add a new course to the system."""
        if course_id in self.courses:
            raise ValueError("Course ID already exists.")
        
        self.courses[course_id] = Course(course_id, title, credits)

    def enroll_student_in_course(self, student_id, course_id):
        """
        Enroll a student in a course.

        :param student_id: The ID of the student to enroll
        :param course_id: The ID of the course to enroll in
        """
        if student_id not in self.students:
            raise ValueError("Student not found.")
        if course_id not in self.courses:
            raise ValueError("Course not found.")

        if 'courses' not in vars(self.students[student_id]):
            self.students[student_id].courses = []
        
        self.students[student_id].courses.append(course_id)

    def generate_report(self):
        """Generate a report of all students and their enrolled courses."""
        report = "School Management System Report:\n"
        for student in self.students.values():
            report += str(student) + "\n"
            if hasattr(student, 'courses'):
                report += " Enrolled Courses: " + ", ".join(student.courses) + "\n"
            else:
                report += " Enrolled Courses: None\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        sms = SchoolManagementSystem()
        
        # Add students
        sms.add_student(1, "Alice Johnson", 14)
        sms.add_student(2, "Bob Smith", 15)

        # Add courses
        sms.add_course(101, "Mathematics", 3)
        sms.add_course(102, "Science", 4)

        # Enroll students in courses
        sms.enroll_student_in_course(1, 101)
        sms.enroll_student_in_course(2, 102)

        # Generate and print report
        print(sms.generate_report())

    except ValueError as e:
        print(f"Error: {e}")
```
