"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Generate code for a searchable database of aviation training courses, including filters for course types like "Avsec Supervisor Course" and "Avsec Management Course," inspired by the Welwitschia Aviation offerings.
Generated: DETERMINISTIC_1e0b3135992cabae
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aviation_training_courses.py

from enum import Enum
from typing import List, Dict

class CourseType(str, Enum):
    """Enum for course types."""
    AVSEC_SUPERVISOR = "Avsec Supervisor Course"
    AVSEC_MANAGEMENT = "Avsec Management Course"
    # Add more course types as needed

class AviationTrainingCourse:
    """Represents an aviation training course."""
    
    def __init__(self, 
                 course_id: int, 
                 course_type: CourseType, 
                 course_name: str, 
                 description: str, 
                 duration: int, 
                 location: str):
        """
        Initializes an AviationTrainingCourse object.

        Args:
        course_id (int): Unique identifier for the course.
        course_type (CourseType): Type of the course.
        course_name (str): Name of the course.
        description (str): Brief description of the course.
        duration (int): Duration of the course in days.
        location (str): Location where the course is held.
        """
        self.course_id = course_id
        self.course_type = course_type
        self.course_name = course_name
        self.description = description
        self.duration = duration
        self.location = location

class AviationTrainingDatabase:
    """A searchable database of aviation training courses."""
    
    def __init__(self):
        """Initializes an empty database."""
        self.courses: Dict[int, AviationTrainingCourse] = {}

    def add_course(self, course: AviationTrainingCourse):
        """
        Adds a course to the database.

        Args:
        course (AviationTrainingCourse): The course to add.
        """
        self.courses[course.course_id] = course

    def get_course(self, course_id: int) -> AviationTrainingCourse:
        """
        Retrieves a course by its ID.

        Args:
        course_id (int): The ID of the course to retrieve.

        Returns:
        AviationTrainingCourse: The course with the specified ID, or None if not found.
        """
        return self.courses.get(course_id)

    def search_courses(self, course_type: CourseType = None, 
                       course_name: str = None, 
                       location: str = None) -> List[AviationTrainingCourse]:
        """
        Searches for courses based on the given filters.

        Args:
        course_type (CourseType): The type of course to search for.
        course_name (str): The name of the course to search for.
        location (str): The location where the course is held.

        Returns:
        List[AviationTrainingCourse]: A list of courses matching the search criteria.
        """
        results = []
        for course in self.courses.values():
            if (course_type is None or course.course_type == course_type) and \
               (course_name is None or course_name.lower() in course.course_name.lower()) and \
               (location is None or location.lower() in course.location.lower()):
                results.append(course)
        return results

def main():
    # Create a sample database
    db = AviationTrainingDatabase()

    # Add some sample courses
    db.add_course(AviationTrainingCourse(1, CourseType.AVSEC_SUPERVISOR, 
                                         "Avsec Supervisor Training", 
                                         "Training for avsec supervisors.", 
                                         5, "Windhoek"))
    db.add_course(AviationTrainingCourse(2, CourseType.AVSEC_MANAGEMENT, 
                                         "Avsec Management Course", 
                                         "Course for avsec management.", 
                                         3, "Luanda"))
    db.add_course(AviationTrainingCourse(3, CourseType.AVSEC_SUPERVISOR, 
                                         "Avsec Supervisor Refresher", 
                                         "Refresher course for avsec supervisors.", 
                                         2, "Windhoek"))

    # Search for courses
    print("All Avsec Supervisor Courses:")
    for course in db.search_courses(course_type=CourseType.AVSEC_SUPERVISOR):
        print(f"ID: {course.course_id}, Name: {course.course_name}, Location: {course.location}")

    print("\nCourses in Windhoek:")
    for course in db.search_courses(location="Windhoek"):
        print(f"ID: {course.course_id}, Name: {course.course_name}, Location: {course.location}")

if __name__ == "__main__":
    main()
```
