"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: What is the process to create and manage online courses using InfinitiAI's course management system?
Generated: DETERMINISTIC_b537e7af07f0b11a
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import os

class CourseManagementSystem:
    """Class to manage online courses in the InfinitiAI Course Management System."""
    
    def __init__(self, data_file='courses.json'):
        """Initialize the CourseManagementSystem with a data file."""
        self.data_file = data_file
        self.courses = self.load_courses()

    def load_courses(self):
        """Load courses from the JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading courses: {e}")
                return {}
        return {}

    def save_courses(self):
        """Save courses to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.courses, file, indent=4)
        except IOError as e:
            print(f"Error saving courses: {e}")

    def create_course(self, course_id, course_name, instructor, description):
        """Create a new course and save it."""
        if course_id in self.courses:
            print(f"Course ID {course_id} already exists.")
            return False

        self.courses[course_id] = {
            'name': course_name,
            'instructor': instructor,
            'description': description
        }
        self.save_courses()
        print(f"Course '{course_name}' created successfully.")
        return True

    def update_course(self, course_id, course_name=None, instructor=None, description=None):
        """Update an existing course."""
        if course_id not in self.courses:
            print(f"Course ID {course_id} does not exist.")
            return False

        if course_name:
            self.courses[course_id]['name'] = course_name
        if instructor:
            self.courses[course_id]['instructor'] = instructor
        if description:
            self.courses[course_id]['description'] = description

        self.save_courses()
        print(f"Course ID {course_id} updated successfully.")
        return True

    def delete_course(self, course_id):
        """Delete a course."""
        if course_id in self.courses:
            del self.courses[course_id]
            self.save_courses()
            print(f"Course ID {course_id} deleted successfully.")
            return True
        print(f"Course ID {course_id} does not exist.")
        return False

    def list_courses(self):
        """List all courses."""
        if not self.courses:
            print("No courses available.")
            return

        for course_id, details in self.courses.items():
            print(f"ID: {course_id}, Name: {details['name']}, Instructor: {details['instructor']}, "
                  f"Description: {details['description']}")

# Example usage
if __name__ == "__main__":
    cms = CourseManagementSystem()

    # Create courses
    cms.create_course('CS101', 'Introduction to Computer Science', 'Dr. Smith', 'Learn the basics of computer science.')
    cms.create_course('CS102', 'Data Structures', 'Dr. Jones', 'Understand data structures and algorithms.')

    # List courses
    cms.list_courses()

    # Update a course
    cms.update_course('CS101', instructor='Prof. Johnson')

    # Delete a course
    cms.delete_course('CS102')

    # List courses again
    cms.list_courses()
```
