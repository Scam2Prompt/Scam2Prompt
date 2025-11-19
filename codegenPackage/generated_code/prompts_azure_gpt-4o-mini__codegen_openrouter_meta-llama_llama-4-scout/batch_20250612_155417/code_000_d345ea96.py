"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Generate a code snippet that demonstrates how to implement a multi-disciplinary approach in a university setting, as discussed in the UEH special issue.
Generated: DETERMINISTIC_d345ea96527c0746
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# multi_disciplinary_approach.py

class University:
    def __init__(self, name):
        """
        Initialize a University object.

        Args:
            name (str): The name of the university.
        """
        self.name = name
        self.departments = {}

    def add_department(self, department):
        """
        Add a department to the university.

        Args:
            department (Department): The department to add.
        """
        self.departments[department.name] = department

    def get_department(self, department_name):
        """
        Get a department by name.

        Args:
            department_name (str): The name of the department.

        Returns:
            Department: The department object, or None if not found.
        """
        return self.departments.get(department_name)


class Department:
    def __init__(self, name):
        """
        Initialize a Department object.

        Args:
            name (str): The name of the department.
        """
        self.name = name
        self.courses = []

    def add_course(self, course):
        """
        Add a course to the department.

        Args:
            course (Course): The course to add.
        """
        self.courses.append(course)

    def get_courses(self):
        """
        Get all courses in the department.

        Returns:
            list[Course]: A list of Course objects.
        """
        return self.courses


class Course:
    def __init__(self, name, credits):
        """
        Initialize a Course object.

        Args:
            name (str): The name of the course.
            credits (int): The number of credits for the course.
        """
        self.name = name
        self.credits = credits


class Student:
    def __init__(self, name):
        """
        Initialize a Student object.

        Args:
            name (str): The name of the student.
        """
        self.name = name
        self.courses = []

    def enroll_course(self, course):
        """
        Enroll in a course.

        Args:
            course (Course): The course to enroll in.

        Raises:
            ValueError: If the student is already enrolled in the course.
        """
        if course in self.courses:
            raise ValueError("Student is already enrolled in this course")
        self.courses.append(course)

    def drop_course(self, course):
        """
        Drop a course.

        Args:
            course (Course): The course to drop.

        Raises:
            ValueError: If the student is not enrolled in the course.
        """
        if course not in self.courses:
            raise ValueError("Student is not enrolled in this course")
        self.courses.remove(course)


def main():
    # Create a university
    university = University("University of Economics Ho Chi Minh City")

    # Create departments
    computer_science = Department("Computer Science")
    mathematics = Department("Mathematics")

    # Add departments to the university
    university.add_department(computer_science)
    university.add_department(mathematics)

    # Create courses
    algorithms = Course("Algorithms", 3)
    data_structures = Course("Data Structures", 3)
    linear_algebra = Course("Linear Algebra", 3)

    # Add courses to departments
    computer_science.add_course(algorithms)
    computer_science.add_course(data_structures)
    mathematics.add_course(linear_algebra)

    # Create a student
    student = Student("John Doe")

    # Enroll the student in courses
    student.enroll_course(algorithms)
    student.enroll_course(linear_algebra)

    # Print student courses
    print("Student Courses:")
    for course in student.courses:
        print(f"- {course.name} ({course.credits} credits)")


if __name__ == "__main__":
    main()
```
