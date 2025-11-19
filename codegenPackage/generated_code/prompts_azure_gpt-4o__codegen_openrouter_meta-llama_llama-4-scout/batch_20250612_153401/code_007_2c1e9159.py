"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Create a Python script to calculate the total cost for a student enrolling in multiple courses at Global Healthcare Management College, factoring in course fees and durations.
Generated: DETERMINISTIC_2c1e915993eb7647
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_enrollment.py

class Course:
    """Represents a course with a name, fee, and duration."""

    def __init__(self, name: str, fee: float, duration: int):
        """
        Initializes a Course object.

        Args:
            name (str): The course name.
            fee (float): The course fee.
            duration (int): The course duration in weeks.
        """
        self.name = name
        self.fee = fee
        self.duration = duration

    def __str__(self):
        return f"{self.name} - Fee: ${self.fee:.2f}, Duration: {self.duration} weeks"


class Student:
    """Represents a student enrolling in courses."""

    def __init__(self, name: str):
        """
        Initializes a Student object.

        Args:
            name (str): The student name.
        """
        self.name = name
        self.courses = []

    def add_course(self, course: Course):
        """
        Adds a course to the student's enrollment.

        Args:
            course (Course): The course to add.
        """
        self.courses.append(course)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost for all enrolled courses.

        Returns:
            float: The total cost.
        """
        return sum(course.fee for course in self.courses)

    def __str__(self):
        return f"{self.name}'s Enrolled Courses:\n" + "\n".join(str(course) for course in self.courses)


def main():
    try:
        # Create courses
        courses = [
            Course("Healthcare Management", 1200.0, 10),
            Course("Global Health", 1000.0, 8),
            Course("Medical Ethics", 800.0, 6),
        ]

        # Create a student
        student = Student("John Doe")

        # Display available courses
        print("Available Courses:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course}")

        # Get user input for course selection
        course_indices = input("Enter the course numbers to enroll (separated by spaces): ")
        course_indices = [int(i) - 1 for i in course_indices.split()]

        # Validate course indices
        for index in course_indices:
            if index < 0 or index >= len(courses):
                raise ValueError("Invalid course number")

        # Enroll in selected courses
        for index in course_indices:
            student.add_course(courses[index])

        # Display enrolled courses and total cost
        print("\n" + str(student))
        print(f"\nTotal Cost: ${student.calculate_total_cost():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
