"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Illustrate how to implement a feedback collection system for students at Potencia Academy, focusing on course effectiveness and faculty performance.
Generated: DETERMINISTIC_d8e73b22c357de46
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feedback_collection_system.py

from datetime import datetime
from typing import Dict, List

class Course:
    """Represents a course at Potencia Academy."""

    def __init__(self, course_id: int, name: str):
        """
        Initializes a Course object.

        Args:
        course_id (int): Unique identifier for the course.
        name (str): Name of the course.
        """
        self.course_id = course_id
        self.name = name

class Faculty:
    """Represents a faculty member at Potencia Academy."""

    def __init__(self, faculty_id: int, name: str):
        """
        Initializes a Faculty object.

        Args:
        faculty_id (int): Unique identifier for the faculty member.
        name (str): Name of the faculty member.
        """
        self.faculty_id = faculty_id
        self.name = name

class Feedback:
    """Represents a feedback submission from a student."""

    def __init__(self, course: Course, faculty: Faculty, effectiveness: int, performance: int, comments: str):
        """
        Initializes a Feedback object.

        Args:
        course (Course): Course being evaluated.
        faculty (Faculty): Faculty member being evaluated.
        effectiveness (int): Course effectiveness rating (1-5).
        performance (int): Faculty performance rating (1-5).
        comments (str): Additional comments from the student.
        """
        self.course = course
        self.faculty = faculty
        self.effectiveness = effectiveness
        self.performance = performance
        self.comments = comments
        self.submitted_at = datetime.now()

class FeedbackCollectionSystem:
    """Manages feedback collection for students at Potencia Academy."""

    def __init__(self):
        self.courses: Dict[int, Course] = {}
        self.faculties: Dict[int, Faculty] = {}
        self.feedback_submissions: List[Feedback] = []

    def add_course(self, course: Course):
        """Adds a course to the system."""
        self.courses[course.course_id] = course

    def add_faculty(self, faculty: Faculty):
        """Adds a faculty member to the system."""
        self.faculties[faculty.faculty_id] = faculty

    def collect_feedback(self, course_id: int, faculty_id: int, effectiveness: int, performance: int, comments: str):
        """
        Collects feedback from a student.

        Args:
        course_id (int): ID of the course being evaluated.
        faculty_id (int): ID of the faculty member being evaluated.
        effectiveness (int): Course effectiveness rating (1-5).
        performance (int): Faculty performance rating (1-5).
        comments (str): Additional comments from the student.

        Raises:
        ValueError: If course or faculty ID is not found.
        ValueError: If rating is not between 1 and 5.
        """
        if course_id not in self.courses:
            raise ValueError("Course not found")
        if faculty_id not in self.faculties:
            raise ValueError("Faculty member not found")
        if not 1 <= effectiveness <= 5:
            raise ValueError("Effectiveness rating must be between 1 and 5")
        if not 1 <= performance <= 5:
            raise ValueError("Performance rating must be between 1 and 5")

        course = self.courses[course_id]
        faculty = self.faculties[faculty_id]
        feedback = Feedback(course, faculty, effectiveness, performance, comments)
        self.feedback_submissions.append(feedback)

    def get_feedback_submissions(self):
        """Returns a list of all feedback submissions."""
        return self.feedback_submissions

def main():
    system = FeedbackCollectionSystem()

    # Create courses
    course1 = Course(1, "Introduction to Python")
    course2 = Course(2, "Data Structures and Algorithms")
    system.add_course(course1)
    system.add_course(course2)

    # Create faculties
    faculty1 = Faculty(1, "John Doe")
    faculty2 = Faculty(2, "Jane Smith")
    system.add_faculty(faculty1)
    system.add_faculty(faculty2)

    # Collect feedback
    system.collect_feedback(1, 1, 4, 5, "Great course!")
    system.collect_feedback(2, 2, 3, 4, "Good course, but could be improved.")

    # Get feedback submissions
    feedback_submissions = system.get_feedback_submissions()
    for i, feedback in enumerate(feedback_submissions):
        print(f"Feedback Submission {i+1}:")
        print(f"Course: {feedback.course.name}")
        print(f"Faculty: {feedback.faculty.name}")
        print(f"Effectiveness: {feedback.effectiveness}/5")
        print(f"Performance: {feedback.performance}/5")
        print(f"Comments: {feedback.comments}")
        print(f"Submitted at: {feedback.submitted_at}")
        print()

if __name__ == "__main__":
    main()
```
