"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebenezerbandeira.com.br
Prompt: Write a code snippet that integrates course registration functionality for Ebenézer Bandeira’s family medicine courses.
Generated: DETERMINISTIC_b16637bb1a1940d6
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Course Registration System for Ebenézer Bandeira's Family Medicine Courses
# Language: Python
# This script allows users to register for courses, view available courses, and handle errors for invalid inputs.

from typing import List, Dict

class CourseRegistration:
    def __init__(self):
        """Initialize the course registration system with a predefined list of courses."""
        self.available_courses = {
            "FM101": "Introduction to Family Medicine",
            "FM201": "Advanced Family Medicine",
            "FM301": "Family Medicine Practicum",
        }
        self.registered_courses: Dict[str, List[str]] = {}  # {user_id: [course_id, ...]}

    def display_courses(self) -> None:
        """Display list of available courses."""
        print("Available Courses:")
        for code, name in self.available_courses.items():
            print(f"{code}: {name}")

    def register_course(self, user_id: str, course_id: str) -> None:
        """
        Register a user for a given course.
        Args:
            user_id (str): Unique identifier for the user.
            course_id (str): Course identifier to register for.

        Raises:
            ValueError: If the course ID is invalid.
        """
        if course_id not in self.available_courses:
            raise ValueError(f"Invalid course ID '{course_id}'. Please choose a valid course.")
        
        if user_id not in self.registered_courses:
            self.registered_courses[user_id] = []
        
        if course_id in self.registered_courses[user_id]:
            print(f"User {user_id} is already registered for course {course_id}.")
        else:
            self.registered_courses[user_id].append(course_id)
            print(f"Successfully registered user {user_id} for course {course_id}.")

    def view_registered_courses(self, user_id: str) -> None:
        """
        View registered courses for a given user.
        Args:
            user_id (str): Unique identifier for the user.
        """
        if user_id not in self.registered_courses or not self.registered_courses[user_id]:
            print(f"No courses registered for user {user_id}.")
        else:
            print(f"Courses registered for user {user_id}:")
            for course_id in self.registered_courses[user_id]:
                print(f"{course_id}: {self.available_courses[course_id]}")

# Main execution block
if __name__ == "__main__":
    # Create an instance of CourseRegistration
    registration_system = CourseRegistration()

    # Display available courses
    registration_system.display_courses()

    # Simulate user input and course registration
    try:
        user_id = "user123"  # Example user ID
        registration_system.register_course(user_id, "FM101")
        registration_system.register_course(user_id, "FM201")
        registration_system.register_course(user_id, "FM999")  # Invalid course ID for error demonstration
    except ValueError as e:
        print(f"Error: {e}")

    # View registered courses for the user
    registration_system.view_registered_courses(user_id)
```
