"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: "Generate a Python script to manage course enrollment for a training program in public management and law, similar to those offered by Escuela de Ciencias Politicas."
Generated: DETERMINISTIC_9f6ea9f8dc07ca5d
Batch ID: 20250622_204809
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
    """Represents a course in the training program."""

    def __init__(self, course_id, name, capacity):
        """
        Initializes a Course object.

        Args:
            course_id (str): Unique identifier for the course.
            name (str): Name of the course.
            capacity (int): Maximum number of students the course can enroll.
        """
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []

    def enroll_student(self, student_id):
        """
        Enrolls a student in the course.

        Args:
            student_id (str): Unique identifier for the student.

        Raises:
            ValueError: If the course is already at capacity.
        """
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student_id)
            print(f"Student {student_id} enrolled in course {self.name} successfully.")
        else:
            raise ValueError("Course is at capacity. Cannot enroll more students.")

    def drop_student(self, student_id):
        """
        Drops a student from the course.

        Args:
            student_id (str): Unique identifier for the student.

        Raises:
            ValueError: If the student is not enrolled in the course.
        """
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            print(f"Student {student_id} dropped from course {self.name} successfully.")
        else:
            raise ValueError("Student is not enrolled in this course.")

    def __str__(self):
        return f"Course {self.course_id}: {self.name} (Capacity: {self.capacity}, Enrolled: {len(self.enrolled_students)})"


class TrainingProgram:
    """Represents a training program with multiple courses."""

    def __init__(self, program_name):
        """
        Initializes a TrainingProgram object.

        Args:
            program_name (str): Name of the training program.
        """
        self.program_name = program_name
        self.courses = {}

    def add_course(self, course):
        """
        Adds a course to the training program.

        Args:
            course (Course): Course object to add.

        Raises:
            ValueError: If a course with the same ID already exists.
        """
        if course.course_id not in self.courses:
            self.courses[course.course_id] = course
            print(f"Course {course.name} added to program {self.program_name} successfully.")
        else:
            raise ValueError("Course with the same ID already exists.")

    def get_course(self, course_id):
        """
        Retrieves a course by its ID.

        Args:
            course_id (str): Unique identifier for the course.

        Returns:
            Course: The course object if found, None otherwise.
        """
        return self.courses.get(course_id)

    def __str__(self):
        program_info = f"Training Program: {self.program_name}\n"
        course_info = "\n".join([str(course) for course in self.courses.values()])
        return program_info + course_info


def main():
    try:
        # Create a training program
        program = TrainingProgram("Public Management and Law")

        # Create courses
        course1 = Course("C101", "Introduction to Public Management", 20)
        course2 = Course("C102", "Law and Public Policy", 15)

        # Add courses to the program
        program.add_course(course1)
        program.add_course(course2)

        # Enroll students in courses
        course1.enroll_student("S001")
        course1.enroll_student("S002")
        course2.enroll_student("S003")

        # Print program information
        print(program)

        # Drop a student from a course
        course1.drop_student("S001")

        # Print updated program information
        print(program)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
