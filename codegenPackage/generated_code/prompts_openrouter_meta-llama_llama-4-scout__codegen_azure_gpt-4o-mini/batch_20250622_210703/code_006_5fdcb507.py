"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Develop a system to track student progress and provide recommendations for courses like Especialização em Construção Naval and NR-33."
Generated: DETERMINISTIC_5fdcb507597938f2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Student:
    """Class to represent a student and their course progress."""
    
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.completed_courses: List[str] = []
        self.recommended_courses: List[str] = []

    def complete_course(self, course_name: str):
        """Mark a course as completed for the student."""
        if course_name not in self.completed_courses:
            self.completed_courses.append(course_name)
        else:
            raise ValueError(f"Course '{course_name}' already completed.")

    def recommend_courses(self, all_courses: List[str]):
        """Generate course recommendations based on completed courses."""
        # Example logic for recommendations
        self.recommended_courses = [course for course in all_courses if course not in self.completed_courses]

    def to_dict(self) -> Dict[str, Any]:
        """Convert student data to a dictionary for easy serialization."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "completed_courses": self.completed_courses,
            "recommended_courses": self.recommended_courses
        }

class CourseTracker:
    """Class to manage student progress and course recommendations."""
    
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.all_courses: List[str] = ["Especialização em Construção Naval", "NR-33", "Course A", "Course B"]

    def add_student(self, student_id: str, name: str):
        """Add a new student to the tracker."""
        if student_id in self.students:
            raise ValueError(f"Student ID '{student_id}' already exists.")
        self.students[student_id] = Student(student_id, name)

    def complete_course(self, student_id: str, course_name: str):
        """Mark a course as completed for a specific student."""
        if student_id not in self.students:
            raise ValueError(f"Student ID '{student_id}' not found.")
        self.students[student_id].complete_course(course_name)

    def generate_recommendations(self, student_id: str):
        """Generate course recommendations for a specific student."""
        if student_id not in self.students:
            raise ValueError(f"Student ID '{student_id}' not found.")
        self.students[student_id].recommend_courses(self.all_courses)

    def save_progress(self, filename: str):
        """Save all student progress to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({student_id: student.to_dict() for student_id, student in self.students.items()}, file, indent=4)
        except IOError as e:
            raise Exception(f"Error saving progress to file: {e}")

    def load_progress(self, filename: str):
        """Load student progress from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for student_id, student_data in data.items():
                    student = Student(student_data['student_id'], student_data['name'])
                    student.completed_courses = student_data['completed_courses']
                    self.students[student_id] = student
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading progress from file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = CourseTracker()
    
    # Adding students
    tracker.add_student("001", "Alice")
    tracker.add_student("002", "Bob")
    
    # Completing courses
    tracker.complete_course("001", "Especialização em Construção Naval")
    
    # Generating recommendations
    tracker.generate_recommendations("001")
    
    # Saving progress
    tracker.save_progress("student_progress.json")
    
    # Loading progress
    tracker.load_progress("student_progress.json")
```
