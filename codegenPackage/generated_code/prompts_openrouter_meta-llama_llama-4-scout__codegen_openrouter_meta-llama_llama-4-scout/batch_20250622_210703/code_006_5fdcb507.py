"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Develop a system to track student progress and provide recommendations for courses like Especialização em Construção Naval and NR-33."
Generated: DETERMINISTIC_5fdcb507597938f2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_progress_tracker.py

class Student:
    """Represents a student with their progress and course recommendations."""

    def __init__(self, student_id, name):
        """
        Initializes a Student object.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Student's name.
        """
        self.student_id = student_id
        self.name = name
        self.courses = {}
        self.recommendations = []

    def add_course(self, course_name, completed):
        """
        Adds a course to the student's record.

        Args:
            course_name (str): Name of the course.
            completed (bool): Whether the course is completed.
        """
        self.courses[course_name] = completed

    def add_recommendation(self, course_name):
        """
        Adds a course recommendation for the student.

        Args:
            course_name (str): Name of the recommended course.
        """
        self.recommendations.append(course_name)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}"


class Course:
    """Represents a course with its name and description."""

    def __init__(self, name, description):
        """
        Initializes a Course object.

        Args:
            name (str): Name of the course.
            description (str): Description of the course.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class StudentProgressTracker:
    """Tracks student progress and provides course recommendations."""

    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name):
        """
        Adds a student to the tracker.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Student's name.
        """
        self.students[student_id] = Student(student_id, name)

    def add_course(self, course_name, description):
        """
        Adds a course to the tracker.

        Args:
            course_name (str): Name of the course.
            description (str): Description of the course.
        """
        self.courses[course_name] = Course(course_name, description)

    def update_student_course(self, student_id, course_name, completed):
        """
        Updates a student's course completion status.

        Args:
            student_id (int): Unique identifier for the student.
            course_name (str): Name of the course.
            completed (bool): Whether the course is completed.

        Raises:
            ValueError: If the student or course does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student not found")
        if course_name not in self.courses:
            raise ValueError("Course not found")
        self.students[student_id].add_course(course_name, completed)

    def add_recommendation(self, student_id, course_name):
        """
        Adds a course recommendation for a student.

        Args:
            student_id (int): Unique identifier for the student.
            course_name (str): Name of the recommended course.

        Raises:
            ValueError: If the student or course does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student not found")
        if course_name not in self.courses:
            raise ValueError("Course not found")
        self.students[student_id].add_recommendation(course_name)

    def get_student_progress(self, student_id):
        """
        Retrieves a student's progress.

        Args:
            student_id (int): Unique identifier for the student.

        Returns:
            dict: Student's course completion status and recommendations.

        Raises:
            ValueError: If the student does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student not found")
        student = self.students[student_id]
        return {
            "courses": student.courses,
            "recommendations": student.recommendations,
        }


def main():
    tracker = StudentProgressTracker()

    # Add courses
    tracker.add_course("Especialização em Construção Naval", "Course description")
    tracker.add_course("NR-33", "Course description")

    # Add students
    tracker.add_student(1, "John Doe")
    tracker.add_student(2, "Jane Doe")

    # Update student courses
    tracker.update_student_course(1, "Especialização em Construção Naval", True)
    tracker.update_student_course(1, "NR-33", False)
    tracker.update_student_course(2, "Especialização em Construção Naval", False)
    tracker.update_student_course(2, "NR-33", True)

    # Add recommendations
    tracker.add_recommendation(1, "NR-33")
    tracker.add_recommendation(2, "Especialização em Construção Naval")

    # Get student progress
    try:
        progress = tracker.get_student_progress(1)
        print("Student 1 Progress:")
        print("Courses:", progress["courses"])
        print("Recommendations:", progress["recommendations"])
    except ValueError as e:
        print(e)

    try:
        progress = tracker.get_student_progress(2)
        print("\nStudent 2 Progress:")
        print("Courses:", progress["courses"])
        print("Recommendations:", progress["recommendations"])
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
