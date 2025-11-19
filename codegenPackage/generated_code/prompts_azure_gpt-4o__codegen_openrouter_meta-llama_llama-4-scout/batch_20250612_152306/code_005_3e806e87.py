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
# course_scheduler.py

from datetime import datetime, timedelta

class Course:
    """Represents a vocational training course."""

    def __init__(self, name, duration):
        """
        Initializes a Course object.

        Args:
            name (str): Name of the course.
            duration (int): Duration of the course in days.
        """
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"{self.name} - {self.duration} days"


class Schedule:
    """Manages course schedules."""

    def __init__(self):
        self.courses = {}

    def add_course(self, course, start_date):
        """
        Adds a course to the schedule.

        Args:
            course (Course): Course to add.
            start_date (datetime): Start date of the course.

        Raises:
            ValueError: If the course already exists in the schedule.
        """
        if course.name in self.courses:
            raise ValueError(f"Course '{course.name}' already exists in the schedule.")

        end_date = start_date + timedelta(days=course.duration)
        self.courses[course.name] = {"start_date": start_date, "end_date": end_date}

    def update_course(self, course_name, new_start_date):
        """
        Updates the start date of a course in the schedule.

        Args:
            course_name (str): Name of the course to update.
            new_start_date (datetime): New start date of the course.

        Raises:
            ValueError: If the course does not exist in the schedule.
        """
        if course_name not in self.courses:
            raise ValueError(f"Course '{course_name}' does not exist in the schedule.")

        course = next((c for c in self.courses if c == course_name), None)
        course_obj = Course(course_name, self.get_course_duration(course_name))
        end_date = new_start_date + timedelta(days=course_obj.duration)
        self.courses[course_name] = {"start_date": new_start_date, "end_date": end_date}

    def delete_course(self, course_name):
        """
        Deletes a course from the schedule.

        Args:
            course_name (str): Name of the course to delete.

        Raises:
            ValueError: If the course does not exist in the schedule.
        """
        if course_name not in self.courses:
            raise ValueError(f"Course '{course_name}' does not exist in the schedule.")

        del self.courses[course_name]

    def get_course_schedule(self, course_name):
        """
        Gets the schedule of a course.

        Args:
            course_name (str): Name of the course.

        Returns:
            dict: Course schedule with start and end dates.

        Raises:
            ValueError: If the course does not exist in the schedule.
        """
        if course_name not in self.courses:
            raise ValueError(f"Course '{course_name}' does not exist in the schedule.")

        return self.courses[course_name]

    def get_course_duration(self, course_name):
        """
        Gets the duration of a course.

        Args:
            course_name (str): Name of the course.

        Returns:
            int: Duration of the course in days.

        Raises:
            ValueError: If the course does not exist in the schedule.
        """
        if course_name not in self.courses:
            raise ValueError(f"Course '{course_name}' does not exist in the schedule.")

        for course in courses:
            if course.name == course_name:
                return course.duration


def main():
    # List of courses
    global courses
    courses = [
        Course("Cloud Computing and Storage Basics", 30),
        Course("Diploma in Industrial Safety", 90),
    ]

    schedule = Schedule()

    # Add courses to the schedule
    schedule.add_course(courses[0], datetime(2024, 9, 16))
    schedule.add_course(courses[1], datetime(2024, 10, 1))

    # Print course schedules
    for course in courses:
        try:
            schedule_info = schedule.get_course_schedule(course.name)
            print(f"Course: {course.name}")
            print(f"Start Date: {schedule_info['start_date'].strftime('%Y-%m-%d')}")
            print(f"End Date: {schedule_info['end_date'].strftime('%Y-%m-%d')}")
            print("------------------------")
        except ValueError as e:
            print(e)

    # Update course schedule
    schedule.update_course("Cloud Computing and Storage Basics", datetime(2024, 9, 20))

    # Print updated course schedule
    try:
        schedule_info = schedule.get_course_schedule("Cloud Computing and Storage Basics")
        print(f"Updated Course: Cloud Computing and Storage Basics")
        print(f"Start Date: {schedule_info['start_date'].strftime('%Y-%m-%d')}")
        print(f"End Date: {schedule_info['end_date'].strftime('%Y-%m-%d')}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
