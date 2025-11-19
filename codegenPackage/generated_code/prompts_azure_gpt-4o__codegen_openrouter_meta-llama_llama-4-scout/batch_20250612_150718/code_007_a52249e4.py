"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Write code to generate a timetable for SOMTU's MBA program, incorporating semester schedules and key dates mentioned on the website.
Generated: DETERMINISTIC_a52249e4660d051c
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Semester:
    def __init__(self, name, start_date, end_date):
        """
        Initialize a Semester object.

        Args:
            name (str): Name of the semester.
            start_date (str): Start date of the semester in 'YYYY-MM-DD' format.
            end_date (str): End date of the semester in 'YYYY-MM-DD' format.
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    def __str__(self):
        return f"{self.name}: {self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}"


class Course:
    def __init__(self, name, semester, days, time):
        """
        Initialize a Course object.

        Args:
            name (str): Name of the course.
            semester (Semester): Semester the course belongs to.
            days (list): List of days the course is held (e.g., ['Monday', 'Wednesday']).
            time (str): Time the course is held (e.g., '10:00 AM - 11:15 AM').
        """
        self.name = name
        self.semester = semester
        self.days = days
        self.time = time

    def __str__(self):
        return f"{self.name} ({self.semester.name}): {', '.join(self.days)} {self.time}"


class Timetable:
    def __init__(self):
        """
        Initialize a Timetable object.
        """
        self.semesters = []
        self.courses = []

    def add_semester(self, semester):
        """
        Add a semester to the timetable.

        Args:
            semester (Semester): Semester to add.
        """
        self.semesters.append(semester)

    def add_course(self, course):
        """
        Add a course to the timetable.

        Args:
            course (Course): Course to add.
        """
        self.courses.append(course)

    def print_timetable(self):
        """
        Print the timetable.
        """
        for semester in self.semesters:
            print(semester)
            semester_courses = [course for course in self.courses if course.semester == semester]
            for course in semester_courses:
                print(f"  {course}")
            print()


def main():
    # Define key dates
    try:
        fall_semester_start = '2024-09-02'
        fall_semester_end = '2024-12-13'
        spring_semester_start = '2025-01-21'
        spring_semester_end = '2025-05-09'

        # Create semesters
        fall_semester = Semester('Fall', fall_semester_start, fall_semester_end)
        spring_semester = Semester('Spring', spring_semester_start, spring_semester_end)

        # Create timetable
        timetable = Timetable()
        timetable.add_semester(fall_semester)
        timetable.add_semester(spring_semester)

        # Create courses
        course1 = Course('MBA 501', fall_semester, ['Monday', 'Wednesday'], '10:00 AM - 11:15 AM')
        course2 = Course('MBA 502', fall_semester, ['Tuesday', 'Thursday'], '2:00 PM - 3:15 PM')
        course3 = Course('MBA 503', spring_semester, ['Monday', 'Wednesday'], '10:00 AM - 11:15 AM')
        course4 = Course('MBA 504', spring_semester, ['Tuesday', 'Thursday'], '2:00 PM - 3:15 PM')

        # Add courses to timetable
        timetable.add_course(course1)
        timetable.add_course(course2)
        timetable.add_course(course3)
        timetable.add_course(course4)

        # Print timetable
        timetable.print_timetable()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
