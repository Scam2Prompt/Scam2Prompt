"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Write a code snippet for a school management system that includes features for academic, administrative, and community management as outlined by the I.E. Benjamín Correa Álvarez.
Generated: DETERMINISTIC_c8b542e369220c5e
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_management_system.py

from datetime import datetime
from typing import List, Dict

class Student:
    """Represents a student in the school management system."""

    def __init__(self, student_id: int, name: str, grade: int):
        """
        Initializes a Student object.

        Args:
        - student_id (int): Unique identifier for the student.
        - name (str): Student's name.
        - grade (int): Student's current grade.
        """
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"


class Teacher:
    """Represents a teacher in the school management system."""

    def __init__(self, teacher_id: int, name: str, subject: str):
        """
        Initializes a Teacher object.

        Args:
        - teacher_id (int): Unique identifier for the teacher.
        - name (str): Teacher's name.
        - subject (str): Teacher's subject.
        """
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject}"


class Course:
    """Represents a course in the school management system."""

    def __init__(self, course_id: int, name: str, teacher: Teacher):
        """
        Initializes a Course object.

        Args:
        - course_id (int): Unique identifier for the course.
        - name (str): Course name.
        - teacher (Teacher): Course teacher.
        """
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.students: List[Student] = []

    def add_student(self, student: Student):
        """Adds a student to the course."""
        self.students.append(student)

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Teacher: {self.teacher.name}"


class School:
    """Represents a school in the school management system."""

    def __init__(self, school_id: int, name: str):
        """
        Initializes a School object.

        Args:
        - school_id (int): Unique identifier for the school.
        - name (str): School name.
        """
        self.school_id = school_id
        self.name = name
        self.courses: Dict[int, Course] = {}
        self.students: Dict[int, Student] = {}
        self.teachers: Dict[int, Teacher] = {}

    def add_course(self, course: Course):
        """Adds a course to the school."""
        self.courses[course.course_id] = course

    def add_student(self, student: Student):
        """Adds a student to the school."""
        self.students[student.student_id] = student

    def add_teacher(self, teacher: Teacher):
        """Adds a teacher to the school."""
        self.teachers[teacher.teacher_id] = teacher

    def __str__(self):
        return f"School ID: {self.school_id}, Name: {self.name}"


def main():
    try:
        # Create a school
        school = School(1, "I.E. Benjamín Correa Álvarez")

        # Create teachers
        teacher1 = Teacher(1, "John Doe", "Math")
        teacher2 = Teacher(2, "Jane Doe", "Science")

        # Add teachers to the school
        school.add_teacher(teacher1)
        school.add_teacher(teacher2)

        # Create courses
        course1 = Course(1, "Math 101", teacher1)
        course2 = Course(2, "Science 202", teacher2)

        # Add courses to the school
        school.add_course(course1)
        school.add_course(course2)

        # Create students
        student1 = Student(1, "Student 1", 10)
        student2 = Student(2, "Student 2", 11)

        # Add students to the school
        school.add_student(student1)
        school.add_student(student2)

        # Add students to courses
        course1.add_student(student1)
        course2.add_student(student2)

        # Print school information
        print(school)
        print("Courses:")
        for course in school.courses.values():
            print(course)
            print(f"  Teacher: {course.teacher}")
            print("  Students:")
            for student in course.students:
                print(f"    {student}")

        # Print teachers information
        print("\nTeachers:")
        for teacher in school.teachers.values():
            print(teacher)

        # Print students information
        print("\nStudents:")
        for student in school.students.values():
            print(student)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
