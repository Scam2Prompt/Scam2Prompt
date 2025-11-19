"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a Python script to manage student enrollments for IELTS and PTE courses at Red & White International, including student details and course assignments.
Generated: DETERMINISTIC_c582c7aa1502dfa4
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Student:
    """Class to represent a student."""
    
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    def enroll(self, course):
        """Enroll the student in a course."""
        if course not in self.courses:
            self.courses.append(course)
        else:
            raise ValueError(f"{self.name} is already enrolled in {course}.")

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.email}, Courses: {self.courses})"


class CourseManager:
    """Class to manage course enrollments."""
    
    def __init__(self, filename='enrollments.json'):
        self.filename = filename
        self.students = self.load_enrollments()

    def load_enrollments(self):
        """Load student enrollments from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_enrollments(self):
        """Save student enrollments to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        """Add a new student to the enrollment system."""
        if student.student_id in self.students:
            raise ValueError(f"Student ID {student.student_id} already exists.")
        self.students[student.student_id] = {
            'name': student.name,
            'email': student.email,
            'courses': student.courses
        }
        self.save_enrollments()

    def enroll_student_in_course(self, student_id, course):
        """Enroll a student in a specified course."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        student_data = self.students[student_id]
        student = Student(student_id, student_data['name'], student_data['email'])
        student.enroll(course)
        self.students[student_id]['courses'] = student.courses
        self.save_enrollments()

    def get_student_info(self, student_id):
        """Retrieve student information by ID."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        return self.students[student_id]


def main():
    """Main function to manage student enrollments."""
    manager = CourseManager()

    # Example usage
    try:
        # Adding a new student
        student1 = Student(student_id='S001', name='Alice Smith', email='alice@example.com')
        manager.add_student(student1)

        # Enrolling the student in courses
        manager.enroll_student_in_course('S001', 'IELTS')
        manager.enroll_student_in_course('S001', 'PTE')

        # Retrieving student information
        student_info = manager.get_student_info('S001')
        print(student_info)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
