"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Create a program to manage course durations and schedules for vocational training programs like "Cloud Computing and Storage Basics" and "Diploma in Industrial Safety" listed on the RSP Bharat website.
Generated: DETERMINISTIC_3e806e87c87d63a8
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class Course:
    """
    A class to represent a vocational training course.
    """

    def __init__(self, name, duration_days, start_date):
        """
        Initializes a new course with the given name, duration, and start date.

        :param name: str - The name of the course
        :param duration_days: int - The duration of the course in days
        :param start_date: str - The starting date of the course in 'YYYY-MM-DD' format
        """
        self.name = name
        self.duration_days = duration_days
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
    
    def end_date(self):
        """
        Calculates the end date of the course based on its duration.

        :return: datetime - The end date of the course
        """
        return self.start_date + timedelta(days=self.duration_days)

    def course_info(self):
        """
        Returns a dictionary containing course information.

        :return: dict - Course details including name, duration, start date, and end date
        """
        return {
            'name': self.name,
            'duration_days': self.duration_days,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date().strftime('%Y-%m-%d')
        }


class CourseManager:
    """
    A class to manage multiple courses.
    """

    def __init__(self):
        """Initializes an empty course manager."""
        self.courses = []

    def add_course(self, name, duration_days, start_date):
        """
        Adds a new course to the course manager.

        :param name: str - The name of the course
        :param duration_days: int - The duration of the course in days
        :param start_date: str - The starting date of the course in 'YYYY-MM-DD' format
        """
        try:
            course = Course(name, duration_days, start_date)
            self.courses.append(course)
            print(f"Course '{name}' added successfully!")
        except Exception as e:
            print(f"Error adding course: {e}")

    def get_courses(self):
        """
        Returns a list of all courses managed by the CourseManager.

        :return: list - List of course information dictionaries
        """
        return [course.course_info() for course in self.courses]

    def save_courses_to_file(self, filename):
        """
        Saves the current courses to a JSON file.

        :param filename: str - The name of the file to save the courses
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_courses(), file, indent=4)
            print(f"Courses saved to {filename} successfully!")
        except Exception as e:
            print(f"Error saving courses to file: {e}")

    def load_courses_from_file(self, filename):
        """
        Loads courses from a JSON file into the course manager.

        :param filename: str - The name of the file to load courses from
        """
        try:
            with open(filename, 'r') as file:
                courses_data = json.load(file)
                for course_data in courses_data:
                    self.add_course(course_data['name'], course_data['duration_days'], course_data['start_date'])
            print(f"Courses loaded from {filename} successfully!")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file: {filename}.")
        except Exception as e:
            print(f"Error loading courses from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = CourseManager()
    manager.add_course("Cloud Computing and Storage Basics", 30, "2023-11-01")
    manager.add_course("Diploma in Industrial Safety", 60, "2023-12-01")
    
    print("\nCurrent Courses:")
    print(manager.get_courses())
    
    # Save courses to a JSON file
    manager.save_courses_to_file("courses.json")
    
    # Load courses from a JSON file
    manager.load_courses_from_file("courses.json")
```
