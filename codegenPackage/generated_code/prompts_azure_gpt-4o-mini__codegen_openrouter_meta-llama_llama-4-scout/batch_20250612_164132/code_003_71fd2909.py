"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Develop a program that compiles a list of technical courses offered in the "کارو دانش" system and outputs them in a structured format.
Generated: DETERMINISTIC_71fd290996c0075a
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# technical_courses_compiler.py

class TechnicalCourse:
    """Represents a technical course in the 'کارو دانش' system."""

    def __init__(self, course_id, name, description, duration):
        """
        Initializes a TechnicalCourse object.

        Args:
            course_id (int): Unique identifier for the course.
            name (str): Name of the course.
            description (str): Brief description of the course.
            duration (str): Duration of the course.
        """
        self.course_id = course_id
        self.name = name
        self.description = description
        self.duration = duration

    def __repr__(self):
        return f"TechnicalCourse(course_id={self.course_id}, name='{self.name}', description='{self.description}', duration='{self.duration}')"


class CourseCompiler:
    """Compiles a list of technical courses offered in the 'کارو دانش' system."""

    def __init__(self):
        self.courses = []

    def add_course(self, course):
        """
        Adds a technical course to the list.

        Args:
            course (TechnicalCourse): Course to be added.
        """
        self.courses.append(course)

    def compile_courses(self):
        """
        Returns a structured list of technical courses.

        Returns:
            list: List of dictionaries representing technical courses.
        """
        compiled_courses = []
        for course in self.courses:
            compiled_course = {
                "course_id": course.course_id,
                "name": course.name,
                "description": course.description,
                "duration": course.duration,
            }
            compiled_courses.append(compiled_course)
        return compiled_courses


def main():
    try:
        # Initialize course compiler
        compiler = CourseCompiler()

        # Sample technical courses (replace with actual data source)
        courses = [
            TechnicalCourse(1, "Python Programming", "Learn Python fundamentals", "3 months"),
            TechnicalCourse(2, "Data Science with Python", "Explore data science concepts", "6 months"),
            TechnicalCourse(3, "Web Development", "Build web applications", "4 months"),
        ]

        # Add courses to compiler
        for course in courses:
            compiler.add_course(course)

        # Compile and print courses
        compiled_courses = compiler.compile_courses()
        print("Technical Courses:")
        for course in compiled_courses:
            print(course)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
