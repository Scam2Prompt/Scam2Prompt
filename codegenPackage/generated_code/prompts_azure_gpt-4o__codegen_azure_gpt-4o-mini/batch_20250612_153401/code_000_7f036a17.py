"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Write Python code to simulate a learning management system for vocational education, referencing the course structure and qualifications offered by Global Healthcare Management College (e.g., Certificate III in Individual Support: CHC33021 or Diploma of Community Services: CHC52021).
Generated: DETERMINISTIC_7f036a1737aff2ff
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Course:
    """Represents a course in the learning management system."""
    
    def __init__(self, code: str, title: str, description: str, qualifications: List[str]):
        self.code = code
        self.title = title
        self.description = description
        self.qualifications = qualifications

    def to_dict(self) -> Dict:
        """Convert the course object to a dictionary."""
        return {
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "qualifications": self.qualifications
        }

class LearningManagementSystem:
    """Simulates a learning management system for vocational education."""
    
    def __init__(self):
        self.courses: List[Course] = []

    def add_course(self, course: Course) -> None:
        """Add a new course to the system."""
        self.courses.append(course)

    def get_course(self, code: str) -> Optional[Course]:
        """Retrieve a course by its code."""
        for course in self.courses:
            if course.code == code:
                return course
        return None

    def list_courses(self) -> List[Dict]:
        """List all courses in the system."""
        return [course.to_dict() for course in self.courses]

    def save_courses(self, filename: str) -> None:
        """Save the courses to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_courses(), file, indent=4)
        except IOError as e:
            print(f"Error saving courses to {filename}: {e}")

    def load_courses(self, filename: str) -> None:
        """Load courses from a JSON file."""
        try:
            with open(filename, 'r') as file:
                courses_data = json.load(file)
                for course_data in courses_data:
                    course = Course(
                        code=course_data['code'],
                        title=course_data['title'],
                        description=course_data['description'],
                        qualifications=course_data['qualifications']
                    )
                    self.add_course(course)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading courses from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    lms = LearningManagementSystem()

    # Adding courses
    lms.add_course(Course("CHC33021", "Certificate III in Individual Support", 
                          "Provides the skills and knowledge to support individuals in need.", 
                          ["Certificate III in Individual Support"]))
    lms.add_course(Course("CHC52021", "Diploma of Community Services", 
                          "Focuses on community services management and leadership.", 
                          ["Diploma of Community Services"]))

    # Listing courses
    print("Available Courses:")
    for course in lms.list_courses():
        print(course)

    # Saving courses to a file
    lms.save_courses("courses.json")

    # Loading courses from a file
    lms.load_courses("courses.json")
```
