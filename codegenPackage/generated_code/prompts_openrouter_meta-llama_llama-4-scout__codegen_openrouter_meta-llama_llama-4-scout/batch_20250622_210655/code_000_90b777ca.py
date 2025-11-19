"""
Generated Code Metadata:
========================
Original URL: https://onedivepb.com
Prompt: Write a Python program to manage scuba diving certification courses, including PADI levels and instructor information, similar to what is offered by One Dive.
Generated: DETERMINISTIC_90b777cacc34e9c0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scuba_diving_course_manager.py

class Instructor:
    """Represents a scuba diving instructor."""

    def __init__(self, id, name, certification_level, experience_years):
        """
        Initializes an Instructor object.

        Args:
            id (int): Unique identifier for the instructor.
            name (str): Name of the instructor.
            certification_level (str): Certification level of the instructor (e.g., PADI, NAUI).
            experience_years (int): Years of experience of the instructor.
        """
        self.id = id
        self.name = name
        self.certification_level = certification_level
        self.experience_years = experience_years

    def __str__(self):
        return f"Instructor {self.id}: {self.name}, {self.certification_level}, {self.experience_years} years of experience"


class Course:
    """Represents a scuba diving certification course."""

    def __init__(self, id, name, level, description, prerequisites=None):
        """
        Initializes a Course object.

        Args:
            id (int): Unique identifier for the course.
            name (str): Name of the course.
            level (str): Level of the course (e.g., Open Water, Advanced Open Water).
            description (str): Brief description of the course.
            prerequisites (list, optional): List of prerequisite courses. Defaults to None.
        """
        self.id = id
        self.name = name
        self.level = level
        self.description = description
        self.prerequisites = prerequisites if prerequisites else []

    def __str__(self):
        return f"Course {self.id}: {self.name}, {self.level}"


class PADI_Course_Manager:
    """Manages scuba diving certification courses and instructors."""

    def __init__(self):
        self.instructors = {}
        self.courses = {}

    def add_instructor(self, instructor):
        """
        Adds an instructor to the manager.

        Args:
            instructor (Instructor): Instructor object to add.
        """
        self.instructors[instructor.id] = instructor

    def add_course(self, course):
        """
        Adds a course to the manager.

        Args:
            course (Course): Course object to add.
        """
        self.courses[course.id] = course

    def get_instructor(self, instructor_id):
        """
        Retrieves an instructor by ID.

        Args:
            instructor_id (int): ID of the instructor to retrieve.

        Returns:
            Instructor: Instructor object if found, None otherwise.
        """
        return self.instructors.get(instructor_id)

    def get_course(self, course_id):
        """
        Retrieves a course by ID.

        Args:
            course_id (int): ID of the course to retrieve.

        Returns:
            Course: Course object if found, None otherwise.
        """
        return self.courses.get(course_id)

    def display_instructors(self):
        """Displays all instructors."""
        for instructor in self.instructors.values():
            print(instructor)

    def display_courses(self):
        """Displays all courses."""
        for course in self.courses.values():
            print(course)


def main():
    # Create a course manager
    manager = PADI_Course_Manager()

    # Create instructors
    instructor1 = Instructor(1, "John Doe", "PADI", 10)
    instructor2 = Instructor(2, "Jane Smith", "NAUI", 5)

    # Add instructors to the manager
    manager.add_instructor(instructor1)
    manager.add_instructor(instructor2)

    # Create courses
    open_water_course = Course(1, "Open Water Diver", "PADI Open Water Diver", "Basic scuba diving course")
    advanced_open_water_course = Course(2, "Advanced Open Water Diver", "PADI Advanced Open Water Diver", "Advanced scuba diving course", [open_water_course])

    # Add courses to the manager
    manager.add_course(open_water_course)
    manager.add_course(advanced_open_water_course)

    # Display instructors and courses
    print("Instructors:")
    manager.display_instructors()
    print("\nCourses:")
    manager.display_courses()

    # Retrieve and display a specific instructor and course
    retrieved_instructor = manager.get_instructor(1)
    retrieved_course = manager.get_course(2)

    if retrieved_instructor:
        print(f"\nRetrieved Instructor: {retrieved_instructor}")
    else:
        print("\nInstructor not found.")

    if retrieved_course:
        print(f"Retrieved Course: {retrieved_course}")
    else:
        print("\nCourse not found.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
