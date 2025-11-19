"""
Generated Code Metadata:
========================
Original URL: https://cuicalli.edu.mx
Prompt: What are the best practices for developing a student feedback system for a college, inspired by the community engagement at Tecnológico Cuicalli?
Generated: DETERMINISTIC_30632774f33842c8
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_feedback_system.py

"""
Student Feedback System for a college, inspired by the community engagement at Tecnológico Cuicalli.

This system allows students to provide feedback on courses and professors.
"""

import datetime
import json
from typing import Dict, List

class Course:
    """Represents a course with its name and professor."""

    def __init__(self, name: str, professor: str):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            professor (str): The name of the professor.
        """
        self.name = name
        self.professor = professor

class Feedback:
    """Represents a student's feedback on a course."""

    def __init__(self, course: Course, rating: int, comment: str):
        """
        Initializes a Feedback object.

        Args:
            course (Course): The course being evaluated.
            rating (int): The student's rating (1-5).
            comment (str): The student's comment.
        """
        self.course = course
        self.rating = rating
        self.comment = comment
        self.timestamp = datetime.datetime.now()

class StudentFeedbackSystem:
    """Manages student feedback for a college."""

    def __init__(self):
        """
        Initializes the StudentFeedbackSystem.

        Attributes:
            courses (Dict[str, Course]): A dictionary of courses.
            feedback (List[Feedback]): A list of feedback submissions.
        """
        self.courses = {}
        self.feedback = []

    def add_course(self, course: Course):
        """
        Adds a course to the system.

        Args:
            course (Course): The course to add.
        """
        self.courses[course.name] = course

    def submit_feedback(self, course_name: str, rating: int, comment: str):
        """
        Submits feedback for a course.

        Args:
            course_name (str): The name of the course.
            rating (int): The student's rating (1-5).
            comment (str): The student's comment.

        Raises:
            ValueError: If the course does not exist or the rating is invalid.
        """
        if course_name not in self.courses:
            raise ValueError("Course not found")
        if rating < 1 or rating > 5:
            raise ValueError("Invalid rating")

        course = self.courses[course_name]
        feedback = Feedback(course, rating, comment)
        self.feedback.append(feedback)

    def get_feedback(self, course_name: str = None) -> List[Feedback]:
        """
        Retrieves feedback for a course or all courses.

        Args:
            course_name (str, optional): The name of the course. Defaults to None.

        Returns:
            List[Feedback]: A list of feedback submissions.
        """
        if course_name:
            return [f for f in self.feedback if f.course.name == course_name]
        return self.feedback

    def save_feedback(self, filename: str):
        """
        Saves feedback to a JSON file.

        Args:
            filename (str): The filename to save to.
        """
        data = []
        for feedback in self.feedback:
            data.append({
                "course": feedback.course.name,
                "professor": feedback.course.professor,
                "rating": feedback.rating,
                "comment": feedback.comment,
                "timestamp": str(feedback.timestamp)
            })

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_feedback(self, filename: str):
        """
        Loads feedback from a JSON file.

        Args:
            filename (str): The filename to load from.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    course = Course(item["course"], item["professor"])
                    feedback = Feedback(course, item["rating"], item["comment"])
                    feedback.timestamp = datetime.datetime.strptime(item["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
                    self.feedback.append(feedback)
        except FileNotFoundError:
            print("File not found")

def main():
    system = StudentFeedbackSystem()

    # Add courses
    system.add_course(Course("Math 101", "John Doe"))
    system.add_course(Course("Science 202", "Jane Smith"))

    # Submit feedback
    system.submit_feedback("Math 101", 4, "Great course!")
    system.submit_feedback("Science 202", 5, "Excellent professor!")

    # Get feedback
    feedback = system.get_feedback("Math 101")
    for f in feedback:
        print(f"Course: {f.course.name}, Rating: {f.rating}, Comment: {f.comment}")

    # Save feedback
    system.save_feedback("feedback.json")

    # Load feedback
    system.load_feedback("feedback.json")
    feedback = system.get_feedback()
    for f in feedback:
        print(f"Course: {f.course.name}, Rating: {f.rating}, Comment: {f.comment}")

if __name__ == "__main__":
    main()
```
