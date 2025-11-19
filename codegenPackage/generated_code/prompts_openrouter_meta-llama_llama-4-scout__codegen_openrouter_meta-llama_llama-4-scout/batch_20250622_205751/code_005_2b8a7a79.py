"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Write a function to calculate the number of available spots for a free business training course and send notifications when the course is fully booked.
Generated: DETERMINISTIC_2b8a7a796c41431c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class Course:
    def __init__(self, name: str, capacity: int):
        """
        Initialize a Course object.

        Args:
        - name (str): The name of the course.
        - capacity (int): The maximum number of spots available for the course.
        """
        self.name = name
        self.capacity = capacity
        self.spots_taken = 0
        self.notifications_sent = False

    def calculate_available_spots(self) -> int:
        """
        Calculate the number of available spots for the course.

        Returns:
        - int: The number of available spots.
        """
        return self.capacity - self.spots_taken

    def book_spot(self) -> bool:
        """
        Book a spot for the course.

        Returns:
        - bool: True if the spot was booked successfully, False otherwise.
        """
        if self.calculate_available_spots() > 0:
            self.spots_taken += 1
            if self.calculate_available_spots() == 0:
                self.send_notification()
            return True
        return False

    def send_notification(self) -> None:
        """
        Send a notification when the course is fully booked.
        """
        if not self.notifications_sent:
            print(f"Notification: Course '{self.name}' is fully booked.")
            self.notifications_sent = True


class CourseManager:
    def __init__(self):
        """
        Initialize a CourseManager object.
        """
        self.courses: Dict[str, Course] = {}

    def add_course(self, name: str, capacity: int) -> None:
        """
        Add a course to the course manager.

        Args:
        - name (str): The name of the course.
        - capacity (int): The maximum number of spots available for the course.
        """
        self.courses[name] = Course(name, capacity)

    def book_spot(self, course_name: str) -> bool:
        """
        Book a spot for a course.

        Args:
        - course_name (str): The name of the course.

        Returns:
        - bool: True if the spot was booked successfully, False otherwise.
        """
        if course_name in self.courses:
            return self.courses[course_name].book_spot()
        else:
            print(f"Error: Course '{course_name}' not found.")
            return False

    def get_available_spots(self, course_name: str) -> int:
        """
        Get the number of available spots for a course.

        Args:
        - course_name (str): The name of the course.

        Returns:
        - int: The number of available spots.
        """
        if course_name in self.courses:
            return self.courses[course_name].calculate_available_spots()
        else:
            print(f"Error: Course '{course_name}' not found.")
            return -1


def main() -> None:
    # Create a course manager
    course_manager = CourseManager()

    # Add a course
    course_manager.add_course("Business Training", 10)

    # Book spots
    for _ in range(10):
        course_manager.book_spot("Business Training")

    # Try to book another spot
    course_manager.book_spot("Business Training")

    # Get available spots
    print(f"Available spots: {course_manager.get_available_spots('Business Training')}")


if __name__ == "__main__":
    main()
```
