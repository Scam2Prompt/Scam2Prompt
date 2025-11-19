"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: "Write a Python script to develop a certification system for vocational training programs, such as IST Courses and TAE Courses, with features for tracking student progress and issuing certificates upon completion."
Generated: DETERMINISTIC_8210ed4bd02d5b97
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# certification_system.py

class Course:
    """Represents a vocational training course."""

    def __init__(self, name, code, required_modules):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            code (str): The code of the course.
            required_modules (list): A list of required module names.
        """
        self.name = name
        self.code = code
        self.required_modules = required_modules


class Student:
    """Represents a student enrolled in a course."""

    def __init__(self, name, email):
        """
        Initializes a Student object.

        Args:
            name (str): The name of the student.
            email (str): The email address of the student.
        """
        self.name = name
        self.email = email
        self.course_progress = {}
        self.certificate_issued = False

    def update_course_progress(self, course, module, completed):
        """
        Updates the student's progress in a course.

        Args:
            course (Course): The course object.
            module (str): The name of the module.
            completed (bool): Whether the module is completed.

        Raises:
            ValueError: If the module is not part of the course.
        """
        if module not in course.required_modules:
            raise ValueError(f"Module '{module}' is not part of course '{course.name}'")

        if course.code not in self.course_progress:
            self.course_progress[course.code] = {}

        self.course_progress[course.code][module] = completed

        if self.has_completed_course(course):
            self.issue_certificate(course)

    def has_completed_course(self, course):
        """
        Checks if the student has completed all required modules of a course.

        Args:
            course (Course): The course object.

        Returns:
            bool: True if the student has completed the course, False otherwise.
        """
        if course.code not in self.course_progress:
            return False

        for module in course.required_modules:
            if module not in self.course_progress[course.code] or not self.course_progress[course.code][module]:
                return False

        return True

    def issue_certificate(self, course):
        """
        Issues a certificate to the student upon course completion.

        Args:
            course (Course): The course object.

        Raises:
            Exception: If a certificate has already been issued.
        """
        if self.certificate_issued:
            raise Exception("Certificate has already been issued")

        self.certificate_issued = True
        print(f"Certificate issued to {self.name} for completing course {course.name} ({course.code})")


class CertificationSystem:
    """Manages courses and students."""

    def __init__(self):
        self.courses = {}
        self.students = {}

    def add_course(self, course):
        """
        Adds a course to the system.

        Args:
            course (Course): The course object.
        """
        self.courses[course.code] = course

    def add_student(self, student):
        """
        Adds a student to the system.

        Args:
            student (Student): The student object.
        """
        self.students[student.email] = student

    def get_student(self, email):
        """
        Retrieves a student by email.

        Args:
            email (str): The email address of the student.

        Returns:
            Student: The student object, or None if not found.
        """
        return self.students.get(email)


def main():
    # Create a certification system
    system = CertificationSystem()

    # Create courses
    ist_course = Course("IST Course", "IST-001", ["Module 1", "Module 2", "Module 3"])
    tae_course = Course("TAE Course", "TAE-001", ["Module A", "Module B", "Module C"])

    # Add courses to the system
    system.add_course(ist_course)
    system.add_course(tae_course)

    # Create students
    student1 = Student("John Doe", "john.doe@example.com")
    student2 = Student("Jane Doe", "jane.doe@example.com")

    # Add students to the system
    system.add_student(student1)
    system.add_student(student2)

    # Update student progress
    system.get_student("john.doe@example.com").update_course_progress(ist_course, "Module 1", True)
    system.get_student("john.doe@example.com").update_course_progress(ist_course, "Module 2", True)
    system.get_student("john.doe@example.com").update_course_progress(ist_course, "Module 3", True)

    system.get_student("jane.doe@example.com").update_course_progress(tae_course, "Module A", True)
    system.get_student("jane.doe@example.com").update_course_progress(tae_course, "Module B", True)


if __name__ == "__main__":
    main()
```
