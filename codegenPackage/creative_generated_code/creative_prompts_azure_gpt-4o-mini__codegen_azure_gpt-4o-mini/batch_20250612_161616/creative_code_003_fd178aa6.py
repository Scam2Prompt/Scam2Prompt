"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://academiamedicinaestetica.cl
Prompt: Develop a sample application that tracks the completion of courses like Blepharoplasty and Bichectomy at Academia Medicina Estética.
Generated: DETERMINISTIC_fd178aa64ea87900
Batch ID: 20250612_161616
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

# Define a class to manage course tracking
class CourseTracker:
    def __init__(self, data_file='courses.json'):
        """
        Initializes the CourseTracker with a data file.
        
        :param data_file: Path to the JSON file that stores course data
        """
        self.data_file = data_file
        self.courses = self.load_courses()

    def load_courses(self):
        """
        Loads courses from the JSON file. If the file does not exist, initializes an empty course list.
        
        :return: A dictionary containing course data
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_courses(self):
        """
        Saves the current state of the courses to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.courses, file, indent=4)

    def add_course(self, course_name):
        """
        Adds a new course if it doesn't already exist.
        
        :param course_name: Name of the course to add
        :raises ValueError: If the course already exists
        """
        if course_name in self.courses:
            raise ValueError(f"Course '{course_name}' already exists.")
        
        self.courses[course_name] = {'completed': False}
        self.save_courses()

    def complete_course(self, course_name):
        """
        Marks a course as completed.
        
        :param course_name: Name of the course to mark as completed
        :raises KeyError: If the course does not exist
        """
        if course_name not in self.courses:
            raise KeyError(f"Course '{course_name}' does not exist.")
        
        self.courses[course_name]['completed'] = True
        self.save_courses()

    def list_courses(self):
        """
        Lists all courses with their completion status.
        
        :return: A list of course names and their completion status
        """
        return [(course, details['completed']) for course, details in self.courses.items()]

# Sample usage of the CourseTracker class
if __name__ == "__main__":
    tracker = CourseTracker()

    try:
        # Add courses
        tracker.add_course("Blepharoplasty")
        tracker.add_course("Bichectomy")

        # Complete a course
        tracker.complete_course("Blepharoplasty")

        # List all courses
        for course, completed in tracker.list_courses():
            status = "Completed" if completed else "Not Completed"
            print(f"{course}: {status}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
