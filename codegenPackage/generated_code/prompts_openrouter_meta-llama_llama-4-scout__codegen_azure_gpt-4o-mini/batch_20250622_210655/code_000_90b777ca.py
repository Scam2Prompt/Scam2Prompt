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
class ScubaDivingCourse:
    """
    A class to represent a scuba diving certification course.
    """

    def __init__(self, course_name, level, duration, price):
        """
        Initializes a new scuba diving course.

        :param course_name: Name of the course
        :param level: PADI level of the course (e.g., Open Water, Advanced)
        :param duration: Duration of the course in days
        :param price: Price of the course
        """
        self.course_name = course_name
        self.level = level
        self.duration = duration
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the course.
        """
        return f"{self.course_name} ({self.level}) - Duration: {self.duration} days, Price: ${self.price}"


class Instructor:
    """
    A class to represent a scuba diving instructor.
    """

    def __init__(self, name, certification_level, experience_years):
        """
        Initializes a new scuba diving instructor.

        :param name: Name of the instructor
        :param certification_level: PADI certification level of the instructor
        :param experience_years: Years of experience the instructor has
        """
        self.name = name
        self.certification_level = certification_level
        self.experience_years = experience_years

    def __str__(self):
        """
        Returns a string representation of the instructor.
        """
        return f"Instructor: {self.name}, Certification Level: {self.certification_level}, Experience: {self.experience_years} years"


class ScubaDivingSchool:
    """
    A class to manage scuba diving courses and instructors.
    """

    def __init__(self):
        """
        Initializes a new scuba diving school with empty lists for courses and instructors.
        """
        self.courses = []
        self.instructors = []

    def add_course(self, course):
        """
        Adds a new course to the school.

        :param course: An instance of ScubaDivingCourse
        """
        if not isinstance(course, ScubaDivingCourse):
            raise ValueError("Invalid course. Must be an instance of ScubaDivingCourse.")
        self.courses.append(course)

    def add_instructor(self, instructor):
        """
        Adds a new instructor to the school.

        :param instructor: An instance of Instructor
        """
        if not isinstance(instructor, Instructor):
            raise ValueError("Invalid instructor. Must be an instance of Instructor.")
        self.instructors.append(instructor)

    def list_courses(self):
        """
        Lists all available courses in the school.
        """
        if not self.courses:
            print("No courses available.")
        else:
            print("Available Courses:")
            for course in self.courses:
                print(course)

    def list_instructors(self):
        """
        Lists all instructors in the school.
        """
        if not self.instructors:
            print("No instructors available.")
        else:
            print("Available Instructors:")
            for instructor in self.instructors:
                print(instructor)


# Example usage
if __name__ == "__main__":
    try:
        # Create a scuba diving school
        school = ScubaDivingSchool()

        # Create courses
        open_water = ScubaDivingCourse("Open Water Diver", "Open Water", 3, 350)
        advanced_open_water = ScubaDivingCourse("Advanced Open Water Diver", "Advanced", 2, 400)

        # Create instructors
        instructor_john = Instructor("John Doe", "Master Scuba Diver Trainer", 10)
        instructor_jane = Instructor("Jane Smith", "Open Water Scuba Instructor", 5)

        # Add courses and instructors to the school
        school.add_course(open_water)
        school.add_course(advanced_open_water)
        school.add_instructor(instructor_john)
        school.add_instructor(instructor_jane)

        # List courses and instructors
        school.list_courses()
        school.list_instructors()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
