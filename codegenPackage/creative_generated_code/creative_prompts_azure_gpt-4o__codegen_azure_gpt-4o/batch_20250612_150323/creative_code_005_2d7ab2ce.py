"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Write code to automate the scheduling of diving courses, including фридайвинг and дайвинг, as described in the training section of the Открытое море website.
Generated: DETERMINISTIC_2d7ab2ce3e4019a2
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional


class Course:
    """
    Represents a diving course.
    Attributes:
        name (str): Name of the course.
        duration_days (int): Duration of the course in days.
        start_date (datetime.date): Start date of the course.
        end_date (datetime.date): End date of the course.
    """
    def __init__(self, name: str, duration_days: int, start_date: Optional[datetime.date] = None):
        self.name = name
        self.duration_days = duration_days
        self.start_date = start_date
        self.end_date = None
        if start_date:
            self.set_schedule(start_date)

    def set_schedule(self, start_date: datetime.date):
        """
        Sets the schedule for the course based on the start date.
        Args:
            start_date (datetime.date): The date when the course starts.
        """
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=self.duration_days)


class DivingScheduler:
    """
    Scheduler for managing diving courses.
    Attributes:
        courses (List[Course]): List of scheduled courses.
    """
    def __init__(self):
        self.courses: List[Course] = []

    def add_course(self, name: str, duration_days: int, start_date: datetime.date):
        """
        Adds a new course to the schedule.
        Args:
            name (str): Name of the course.
            duration_days (int): Duration of the course in days.
            start_date (datetime.date): Start date of the course.
        Raises:
            ValueError: If the course overlaps with an existing course.
        """
        new_course = Course(name, duration_days, start_date)
        for course in self.courses:
            if self._check_overlap(course, new_course):
                raise ValueError(f"Course '{name}' overlaps with an existing course '{course.name}' scheduled from {course.start_date} to {course.end_date}.")
        self.courses.append(new_course)

    def _check_overlap(self, existing_course: Course, new_course: Course) -> bool:
        """
        Checks if two courses overlap in their schedules.
        Args:
            existing_course (Course): An existing scheduled course.
            new_course (Course): A new course being scheduled.
        Returns:
            bool: True if the courses overlap, otherwise False.
        """
        return not (new_course.end_date <= existing_course.start_date or new_course.start_date >= existing_course.end_date)

    def view_schedule(self) -> List[str]:
        """
        Returns a formatted view of the schedule.
        Returns:
            List[str]: List of scheduled courses in human-readable format.
        """
        schedule = []
        for course in sorted(self.courses, key=lambda c: c.start_date):
            schedule.append(f"{course.name}: {course.start_date} to {course.end_date}")
        return schedule


# Example usage of the DivingScheduler
if __name__ == "__main__":
    scheduler = DivingScheduler()
    try:
        # Adding courses
        scheduler.add_course("Фридайвинг", 3, datetime.date(2023, 10, 1))
        scheduler.add_course("Дайвинг", 5, datetime.date(2023, 10, 5))
        
        # Attempting to add an overlapping course (will raise an error)
        scheduler.add_course("Advanced Фридайвинг", 4, datetime.date(2023, 10, 3))  # Overlaps with Фридайвинг
        
    except ValueError as e:
        print(f"Error: {e}")
    
    # Viewing the schedule
    for entry in scheduler.view_schedule():
        print(entry)
```
