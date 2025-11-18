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
import datetime
from typing import List, Dict

class Course:
    """
    Represents a vocational training course with a name, duration, and schedule.
    """
    def __init__(self, name: str, duration_weeks: int, start_date: str):
        """
        Initializes a new Course instance.

        :param name: Name of the course.
        :param duration_weeks: Duration of the course in weeks.
        :param start_date: Start date of the course in YYYY-MM-DD format.
        """
        self.name = name
        self.duration_weeks = duration_weeks
        try:
            self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format for start_date: {start_date}. Expected YYYY-MM-DD.")
        self.end_date = self.calculate_end_date()

    def calculate_end_date(self) -> datetime.date:
        """
        Calculates the end date based on the start date and duration.

        :return: End date of the course.
        """
        return self.start_date + datetime.timedelta(weeks=self.duration_weeks)

    def get_schedule(self) -> Dict[str, str]:
        """
        Returns the course schedule as a dictionary.

        :return: A dictionary containing the course name, start date, and end date.
        """
        return {
            "Course Name": self.name,
            "Start Date": self.start_date.strftime("%Y-%m-%d"),
            "End Date": self.end_date.strftime("%Y-%m-%d")
        }


class CourseManager:
    """
    Manages multiple vocational training courses.
    """
    def __init__(self):
        """
        Initializes the CourseManager with an empty list of courses.
        """
        self.courses: List[Course] = []

    def add_course(self, name: str, duration_weeks: int, start_date: str):
        """
        Adds a new course to the manager.

        :param name: Name of the course.
        :param duration_weeks: Duration of the course in weeks.
        :param start_date: Start date of the course in YYYY-MM-DD format.
        """
        try:
            course = Course(name, duration_weeks, start_date)
            self.courses.append(course)
        except ValueError as e:
            print(f"Error adding course: {e}")

    def list_courses(self) -> List[Dict[str, str]]:
        """
        Lists all courses managed by the CourseManager.

        :return: A list of dictionaries containing course schedules.
        """
        return [course.get_schedule() for course in self.courses]

    def find_course(self, course_name: str) -> Dict[str, str]:
        """
        Finds a course by its name.

        :param course_name: Name of the course to find.
        :return: The course schedule if found, otherwise an error message.
        """
        for course in self.courses:
            if course.name.lower() == course_name.lower():
                return course.get_schedule()
        return {"Error": f"Course '{course_name}' not found."}


# Example usage (uncomment and run to test the program):
# if __name__ == "__main__":
#     manager = CourseManager()
#     manager.add_course("Cloud Computing and Storage Basics", 12, "2023-11-01")
#     manager.add_course("Diploma in Industrial Safety", 24, "2023-10-15")
#     
#     print("Listing all courses:")
#     for course in manager.list_courses():
#         print(course)
#     
#     print("\nFinding a specific course:")
#     print(manager.find_course("Cloud Computing and Storage Basics"))
#     print(manager.find_course("Unknown Course"))
```
