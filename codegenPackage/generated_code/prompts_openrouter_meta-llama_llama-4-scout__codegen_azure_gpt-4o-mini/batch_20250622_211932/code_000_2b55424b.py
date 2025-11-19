"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: Write a Python script to manage course bookings for a vocational training provider like CoLa Training Services, including features for online training programs and machinery-based courses.
Generated: DETERMINISTIC_2b55424b23c68c96
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class Course:
    """Class representing a course offered by the training provider."""
    
    def __init__(self, course_id, name, description, max_students, course_type):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.max_students = max_students
        self.enrolled_students = []
        self.course_type = course_type  # 'online' or 'machinery'

    def enroll_student(self, student_name):
        """Enroll a student in the course if there is space available."""
        if len(self.enrolled_students) < self.max_students:
            self.enrolled_students.append(student_name)
            return True
        else:
            return False

    def get_enrollment_info(self):
        """Return the current enrollment status of the course."""
        return {
            "course_id": self.course_id,
            "name": self.name,
            "enrolled_students": self.enrolled_students,
            "available_spots": self.max_students - len(self.enrolled_students)
        }

class CourseManager:
    """Class to manage course bookings and data persistence."""
    
    def __init__(self, data_file='courses.json'):
        self.courses = []
        self.data_file = data_file
        self.load_courses()

    def load_courses(self):
        """Load courses from a JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                courses_data = json.load(file)
                for course in courses_data:
                    self.courses.append(Course(**course))
        except FileNotFoundError:
            print("Data file not found. Starting with an empty course list.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the data file. Starting with an empty course list.")

    def save_courses(self):
        """Save the current courses to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([course.__dict__ for course in self.courses], file)

    def add_course(self, course):
        """Add a new course to the manager."""
        self.courses.append(course)
        self.save_courses()

    def enroll_student_in_course(self, course_id, student_name):
        """Enroll a student in a specified course by course ID."""
        for course in self.courses:
            if course.course_id == course_id:
                if course.enroll_student(student_name):
                    self.save_courses()
                    return True
                else:
                    return False
        return False

    def get_course_info(self, course_id):
        """Get information about a specific course."""
        for course in self.courses:
            if course.course_id == course_id:
                return course.get_enrollment_info()
        return None

def main():
    """Main function to run the course management system."""
    manager = CourseManager()

    # Example usage
    # Adding courses
    manager.add_course(Course(course_id='C001', name='Python Programming', description='Learn Python from scratch.', max_students=30, course_type='online'))
    manager.add_course(Course(course_id='C002', name='Welding Basics', description='Introduction to welding techniques.', max_students=15, course_type='machinery'))

    # Enrolling students
    if manager.enroll_student_in_course('C001', 'Alice Johnson'):
        print("Alice Johnson enrolled in Python Programming.")
    else:
        print("Failed to enroll Alice Johnson.")

    if manager.enroll_student_in_course('C002', 'Bob Smith'):
        print("Bob Smith enrolled in Welding Basics.")
    else:
        print("Failed to enroll Bob Smith.")

    # Display course information
    course_info = manager.get_course_info('C001')
    print(course_info)

if __name__ == "__main__":
    main()
```
