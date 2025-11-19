"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Compare the National N Diploma courses in Electrical Engineering (Heavy Current and Light Current) offered by Nzotho FET College.
Generated: DETERMINISTIC_e46e40f7f800613d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Nzotho FET College National N Diploma Courses Comparator

class Course:
    """Represents a course offered by Nzotho FET College."""

    def __init__(self, name, description, duration, credits):
        """
        Initializes a Course object.

        Args:
            name (str): Course name.
            description (str): Course description.
            duration (str): Course duration.
            credits (int): Course credits.
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.credits = credits

    def __str__(self):
        return f"{self.name}: {self.description}, Duration: {self.duration}, Credits: {self.credits}"


class NzothoFETCollege:
    """Represents Nzotho FET College with its courses."""

    def __init__(self):
        self.courses = []

    def add_course(self, course):
        """
        Adds a course to the college's course list.

        Args:
            course (Course): Course to add.
        """
        self.courses.append(course)

    def get_courses(self):
        """
        Retrieves all courses offered by the college.

        Returns:
            list[Course]: List of courses.
        """
        return self.courses

    def compare_courses(self, course_name1, course_name2):
        """
        Compares two courses by their credits and duration.

        Args:
            course_name1 (str): Name of the first course.
            course_name2 (str): Name of the second course.

        Returns:
            dict: Comparison result.

        Raises:
            ValueError: If either course is not found.
        """
        course1 = next((course for course in self.courses if course.name == course_name1), None)
        course2 = next((course for course in self.courses if course.name == course_name2), None)

        if course1 is None or course2 is None:
            raise ValueError("One or both courses not found.")

        comparison_result = {
            "course1": course1.__dict__,
            "course2": course2.__dict__,
            "credits_difference": course1.credits - course2.credits,
            "duration_difference": course1.duration != course2.duration
        }

        return comparison_result


def main():
    try:
        college = NzothoFETCollege()

        # Add Electrical Engineering (Heavy Current) course
        heavy_current_course = Course(
            "Electrical Engineering (Heavy Current)",
            "This course focuses on the practical application of electrical engineering principles in heavy current environments.",
            "2 years",
            120
        )
        college.add_course(heavy_current_course)

        # Add Electrical Engineering (Light Current) course
        light_current_course = Course(
            "Electrical Engineering (Light Current)",
            "This course focuses on the practical application of electrical engineering principles in light current environments.",
            "2 years",
            120
        )
        college.add_course(light_current_course)

        # Compare courses
        comparison_result = college.compare_courses(
            "Electrical Engineering (Heavy Current)",
            "Electrical Engineering (Light Current)"
        )

        print("Comparison Result:")
        print(f"Course 1: {comparison_result['course1']['name']}")
        print(f"Course 2: {comparison_result['course2']['name']}")
        print(f"Credits Difference: {comparison_result['credits_difference']}")
        print(f"Duration Difference: {comparison_result['duration_difference']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
