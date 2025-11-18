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
from typing import List, Dict, Optional

class DivingCourse:
    def __init__(self, name: str, duration: int, start_date: datetime.date, capacity: int):
        self.name = name  # Name of the diving course
        self.duration = duration  # Duration of the course in days
        self.start_date = start_date  # Start date of the course
        self.capacity = capacity  # Maximum number of participants
        self.enrolled = []  # List to keep track of enrolled participants

    def enroll(self, participant: str) -> bool:
        """Enroll a participant in the course if there's space available."""
        if len(self.enrolled) < self.capacity:
            self.enrolled.append(participant)
            return True
        else:
            print(f"Enrollment failed for {participant}: Course is full.")
            return False

    def is_full(self) -> bool:
        """Check if the course is full."""
        return len(self.enrolled) >= self.capacity

    def course_info(self) -> Dict[str, Optional[int]]:
        """Return basic information about the course."""
        return {
            'name': self.name,
            'start_date': self.start_date.isoformat(),
            'duration': self.duration,
            'capacity': self.capacity,
            'enrolled_count': len(self.enrolled)
        }

class DivingSchool:
    def __init__(self):
        self.courses: List[DivingCourse] = []  # List of courses offered by the school

    def add_course(self, course: DivingCourse) -> None:
        """Add a new diving course to the schedule."""
        self.courses.append(course)

    def schedule_courses(self) -> List[Dict]:
        """Return a list of scheduled courses with their info."""
        return [course.course_info() for course in self.courses]

def main():
    school = DivingSchool()

    # Define some diving courses
    try:
        free_diving_course = DivingCourse("Фридайвинг", duration=3, start_date=datetime.date(2023, 11, 15), capacity=10)
        scuba_diving_course = DivingCourse("Дайвинг", duration=5, start_date=datetime.date(2023, 11, 20), capacity=8)

        # Add courses to the school
        school.add_course(free_diving_course)
        school.add_course(scuba_diving_course)

        # Enroll participants
        participants = ["Alice", "Bob", "Charlie", "David", "Eve"]

        for participant in participants:
            if not free_diving_course.is_full():
                free_diving_course.enroll(participant)

        # Schedule summary
        scheduled_courses = school.schedule_courses()
        for course in scheduled_courses:
            print(course)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
