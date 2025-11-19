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
import datetime
import json

class Student:
    """
    Represents a student enrolled in a vocational training program.
    """
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}  # Dictionary to track courses and progress

    def enroll_course(self, course_name):
        """
        Enroll the student in a course.
        """
        if course_name not in self.courses:
            self.courses[course_name] = {'progress': 0, 'completed': False}
        else:
            raise ValueError(f"Student is already enrolled in {course_name}.")

    def update_progress(self, course_name, progress):
        """
        Update the progress of a course for the student.
        """
        if course_name in self.courses:
            if 0 <= progress <= 100:
                self.courses[course_name]['progress'] = progress
                if progress == 100:
                    self.courses[course_name]['completed'] = True
            else:
                raise ValueError("Progress must be between 0 and 100.")
        else:
            raise ValueError(f"Student is not enrolled in {course_name}.")

    def get_certificate(self, course_name):
        """
        Issue a certificate if the course is completed.
        """
        if course_name in self.courses and self.courses[course_name]['completed']:
            return f"Certificate of Completion\nName: {self.name}\nCourse: {course_name}\nDate: {datetime.date.today()}"
        else:
            raise ValueError(f"Certificate cannot be issued for {course_name}. Course not completed.")

    def __str__(self):
        """
        String representation of the student and their progress.
        """
        return json.dumps({
            'student_id': self.student_id,
            'name': self.name,
            'courses': self.courses
        }, indent=4)


class CertificationSystem:
    """
    Certification system to manage students and courses.
    """
    def __init__(self):
        self.students = {}  # Dictionary to store students by ID

    def add_student(self, student_id, name):
        """
        Add a new student to the system.
        """
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        else:
            raise ValueError(f"Student with ID {student_id} already exists.")

    def enroll_student_in_course(self, student_id, course_name):
        """
        Enroll a student in a course.
        """
        if student_id in self.students:
            self.students[student_id].enroll_course(course_name)
        else:
            raise ValueError(f"Student with ID {student_id} does not exist.")

    def update_student_progress(self, student_id, course_name, progress):
        """
        Update the progress of a student in a course.
        """
        if student_id in self.students:
            self.students[student_id].update_progress(course_name, progress)
        else:
            raise ValueError(f"Student with ID {student_id} does not exist.")

    def issue_certificate(self, student_id, course_name):
        """
        Issue a certificate for a student upon course completion.
        """
        if student_id in self.students:
            return self.students[student_id].get_certificate(course_name)
        else:
            raise ValueError(f"Student with ID {student_id} does not exist.")

    def __str__(self):
        """
        String representation of the certification system.
        """
        return json.dumps({
            'students': {student_id: str(student) for student_id, student in self.students.items()}
        }, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        system = CertificationSystem()

        # Add students
        system.add_student("S001", "Alice")
        system.add_student("S002", "Bob")

        # Enroll students in courses
        system.enroll_student_in_course("S001", "IST Course")
        system.enroll_student_in_course("S002", "TAE Course")

        # Update progress
        system.update_student_progress("S001", "IST Course", 50)
        system.update_student_progress("S001", "IST Course", 100)  # Completion
        system.update_student_progress("S002", "TAE Course", 100)  # Completion

        # Issue certificates
        print(system.issue_certificate("S001", "IST Course"))
        print(system.issue_certificate("S002", "TAE Course"))

        # Print system state
        print(system)

    except Exception as e:
        print(f"Error: {e}")
```
