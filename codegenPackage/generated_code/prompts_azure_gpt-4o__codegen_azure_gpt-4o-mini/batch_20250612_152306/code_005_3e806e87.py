"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: Create a program to manage course durations and schedules for vocational training programs like "Cloud Computing and Storage Basics" and "Diploma in Industrial Safety" listed on the RSP Bharat website.
Generated: DETERMINISTIC_3e806e87c87d63a8
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class Course:
    """
    A class to represent a vocational training course.
    """

    def __init__(self, name, duration_days, start_date):
        """
        Initializes a new course with a name, duration, and start date.

        :param name: str - The name of the course
        :param duration_days: int - The duration of the course in days
        :param start_date: str - The start date of the course in 'YYYY-MM-DD' format
        """
        self.name = name
        self.duration_days = duration_days
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = self.start_date + timedelta(days=self.duration_days)

    def get_schedule(self):
        """
        Returns the schedule of the course.

        :return: dict - A dictionary containing course name, start date, and end date
        """
        return {
            'course_name': self.name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d')
        }

class CourseManager:
    """
    A class to manage multiple courses.
    """

    def __init__(self):
        """
        Initializes the CourseManager with an empty course list.
        """
        self.courses = []

    def add_course(self, course):
        """
        Adds a new course to the manager.

        :param course: Course - The course object to be added
        """
        if not isinstance(course, Course):
            raise ValueError("Invalid course object")
        self.courses.append(course)

    def get_all_courses(self):
        """
        Returns a list of all courses with their schedules.

        :return: list - A list of dictionaries containing course schedules
        """
        return [course.get_schedule() for course in self.courses]

    def save_courses_to_file(self, filename):
        """
        Saves the course schedules to a JSON file.

        :param filename: str - The name of the file to save the courses
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_all_courses(), file, indent=4)
        except IOError as e:
            print(f"Error saving courses to file: {e}")

    def load_courses_from_file(self, filename):
        """
        Loads courses from a JSON file.

        :param filename: str - The name of the file to load the courses from
        """
        try:
            with open(filename, 'r') as file:
                courses_data = json.load(file)
                for course_data in courses_data:
                    course = Course(course_data['course_name'], 
                                    (datetime.strptime(course_data['end_date'], '%Y-%m-%d') - 
                                     datetime.strptime(course_data['start_date'], '%Y-%m-%d')).days, 
                                    course_data['start_date'])
                    self.add_course(course)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading courses from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = CourseManager()
    
    # Adding courses
    try:
        course1 = Course("Cloud Computing and Storage Basics", 30, "2023-11-01")
        course2 = Course("Diploma in Industrial Safety", 45, "2023-12-01")
        
        manager.add_course(course1)
        manager.add_course(course2)
        
        # Display all courses
        print(manager.get_all_courses())
        
        # Save courses to a file
        manager.save_courses_to_file('courses.json')
        
        # Load courses from a file
        manager.load_courses_from_file('courses.json')
        
        # Display loaded courses
        print(manager.get_all_courses())
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
