"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Create a Python script to calculate the total cost for a student enrolling in multiple courses at Global Healthcare Management College, factoring in course fees and durations.
Generated: DETERMINISTIC_2c1e915993eb7647
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Course:
    """Represents a course with a name, fee, and duration in weeks."""
    
    def __init__(self, name: str, fee: float, duration_weeks: int):
        """
        Initializes a Course instance.

        :param name: Name of the course
        :param fee: Fee for the course
        :param duration_weeks: Duration of the course in weeks
        """
        self.name = name
        self.fee = fee
        self.duration_weeks = duration_weeks

class Student:
    """Represents a student enrolled in multiple courses."""
    
    def __init__(self, name: str):
        """
        Initializes a Student instance.

        :param name: Name of the student
        """
        self.name = name
        self.courses = []

    def add_course(self, course: Course):
        """
        Adds a course to the student's enrollment.

        :param course: Course to be added
        """
        self.courses.append(course)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of all enrolled courses.

        :return: Total cost as a float
        """
        total_cost = 0
        for course in self.courses:
            total_cost += course.fee
        return total_cost

def main():
    """Main function to execute the program."""
    try:
        # Create courses
        course1 = Course("Healthcare Management", 1200.00, 12)
        course2 = Course("Health Informatics", 1500.00, 10)
        course3 = Course("Public Health Policy", 900.00, 8)

        # Create a student and enroll in courses
        student = Student("John Doe")
        student.add_course(course1)
        student.add_course(course2)
        student.add_course(course3)

        # Calculate total cost for the student
        total_cost = student.calculate_total_cost()
        print(f"Total cost for {student.name} is: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
