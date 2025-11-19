"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Write a Python code to manage online courses and e-learning platforms for a non-profit organization like SKI Foundation.
Generated: DETERMINISTIC_5d5ce7fb4821808b
Batch ID: 20250622_205751
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
    """Class to represent a course in the e-learning platform."""
    
    def __init__(self, title: str, description: str, instructor: str, course_id: Optional[int] = None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.course_id = course_id

    def to_dict(self) -> Dict:
        """Convert the course object to a dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "instructor": self.instructor,
            "course_id": self.course_id
        }

class CourseManager:
    """Class to manage a collection of courses."""
    
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.courses: List[Course] = []
        self.load_courses()

    def load_courses(self):
        """Load courses from a JSON file."""
        try:
            with open(self.storage_file, 'r') as file:
                courses_data = json.load(file)
                self.courses = [Course(**course) for course in courses_data]
        except FileNotFoundError:
            print("Storage file not found. Starting with an empty course list.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the storage file. Starting with an empty course list.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_courses(self):
        """Save courses to a JSON file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([course.to_dict() for course in self.courses], file, indent=4)
        except Exception as e:
            print(f"Failed to save courses: {e}")

    def add_course(self, course: Course):
        """Add a new course to the collection."""
        if any(c.title == course.title for c in self.courses):
            print(f"Course with title '{course.title}' already exists.")
            return
        course.course_id = len(self.courses) + 1  # Simple ID assignment
        self.courses.append(course)
        self.save_courses()
        print(f"Course '{course.title}' added successfully.")

    def remove_course(self, course_id: int):
        """Remove a course from the collection by its ID."""
        course_to_remove = next((c for c in self.courses if c.course_id == course_id), None)
        if course_to_remove:
            self.courses.remove(course_to_remove)
            self.save_courses()
            print(f"Course '{course_to_remove.title}' removed successfully.")
        else:
            print(f"Course with ID '{course_id}' not found.")

    def list_courses(self) -> List[Dict]:
        """List all courses in the collection."""
        return [course.to_dict() for course in self.courses]

# Example usage
if __name__ == "__main__":
    manager = CourseManager('courses.json')
    
    # Adding courses
    manager.add_course(Course("Python Programming", "Learn Python from scratch", "John Doe"))
    manager.add_course(Course("Data Science", "Introduction to Data Science", "Jane Smith"))
    
    # Listing courses
    print("Current Courses:")
    for course in manager.list_courses():
        print(course)
    
    # Removing a course
    manager.remove_course(1)
    
    # Listing courses after removal
    print("Courses after removal:")
    for course in manager.list_courses():
        print(course)
```
