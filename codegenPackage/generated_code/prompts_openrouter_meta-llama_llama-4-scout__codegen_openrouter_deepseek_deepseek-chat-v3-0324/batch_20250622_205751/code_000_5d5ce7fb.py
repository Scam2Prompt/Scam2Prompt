"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Write a Python code to manage online courses and e-learning platforms for a non-profit organization like SKI Foundation.
Generated: DETERMINISTIC_5d5ce7fb4821808b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional, Union
import uuid
import os

class Course:
    """Represents an online course with basic information and enrollment capabilities."""
    
    def __init__(self, title: str, description: str, instructor: str, duration: int, capacity: int):
        """
        Initialize a new Course instance.
        
        Args:
            title (str): Title of the course.
            description (str): Description of the course.
            instructor (str): Name of the instructor.
            duration (int): Duration of the course in weeks.
            capacity (int): Maximum number of students that can enroll.
        """
        self.course_id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.capacity = capacity
        self.enrolled_students = []
        self.start_date = None
        self.is_active = False

    def enroll_student(self, student_id: str) -> bool:
        """
        Enroll a student in the course if there is capacity.
        
        Args:
            student_id (str): Unique identifier of the student.
            
        Returns:
            bool: True if enrollment was successful, False otherwise.
        """
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student_id)
            return True
        return False

    def unenroll_student(self, student_id: str) -> bool:
        """
        Unenroll a student from the course.
        
        Args:
            student_id (str): Unique identifier of the student.
            
        Returns:
            bool: True if unenrollment was successful, False otherwise.
        """
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            return True
        return False

    def start_course(self) -> None:
        """Mark the course as active and set the start date to today."""
        self.is_active = True
        self.start_date = datetime.now().date()

    def end_course(self) -> None:
        """Mark the course as inactive."""
        self.is_active = False

    def to_dict(self) -> Dict:
        """Convert the Course instance to a dictionary for serialization."""
        return {
            "course_id": self.course_id,
            "title": self.title,
            "description": self.description,
            "instructor": self.instructor,
            "duration": self.duration,
            "capacity": self.capacity,
            "enrolled_students": self.enrolled_students,
            "start_date": str(self.start_date) if self.start_date else None,
            "is_active": self.is_active
        }

class Student:
    """Represents a student who can enroll in courses."""
    
    def __init__(self, name: str, email: str):
        """
        Initialize a new Student instance.
        
        Args:
            name (str): Name of the student.
            email (str): Email address of the student.
        """
        self.student_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.enrolled_courses = []

    def enroll_in_course(self, course_id: str) -> None:
        """
        Add a course to the student's list of enrolled courses.
        
        Args:
            course_id (str): Unique identifier of the course.
        """
        self.enrolled_courses.append(course_id)

    def unenroll_from_course(self, course_id: str) -> bool:
        """
        Remove a course from the student's list of enrolled courses.
        
        Args:
            course_id (str): Unique identifier of the course.
            
        Returns:
            bool: True if unenrollment was successful, False otherwise.
        """
        if course_id in self.enrolled_courses:
            self.enrolled_courses.remove(course_id)
            return True
        return False

    def to_dict(self) -> Dict:
        """Convert the Student instance to a dictionary for serialization."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "enrolled_courses": self.enrolled_courses
        }

class ELearningPlatform:
    """Manages courses and students for an e-learning platform."""
    
    def __init__(self, data_file: str = "elearning_data.json"):
        """
        Initialize the e-learning platform.
        
        Args:
            data_file (str): Path to the JSON file for data persistence.
        """
        self.data_file = data_file
        self.courses: Dict[str, Course] = {}
        self.students: Dict[str, Student] = {}
        self.load_data()

    def add_course(self, title: str, description: str, instructor: str, duration: int, capacity: int) -> str:
        """
        Add a new course to the platform.
        
        Args:
            title (str): Title of the course.
            description (str): Description of the course.
            instructor (str): Name of the instructor.
            duration (int): Duration of the course in weeks.
            capacity (int): Maximum number of students that can enroll.
            
        Returns:
            str: The ID of the newly created course.
        """
        course = Course(title, description, instructor, duration, capacity)
        self.courses[course.course_id] = course
        self.save_data()
        return course.course_id

    def get_course(self, course_id: str) -> Optional[Course]:
        """
        Retrieve a course by its ID.
        
        Args:
            course_id (str): Unique identifier of the course.
            
        Returns:
            Optional[Course]: The Course instance if found, None otherwise.
        """
        return self.courses.get(course_id)

    def add_student(self, name: str, email: str) -> str:
        """
        Add a new student to the platform.
        
        Args:
            name (str): Name of the student.
            email (str): Email address of the student.
            
        Returns:
            str: The ID of the newly created student.
        """
        student = Student(name, email)
        self.students[student.student_id] = student
        self.save_data()
        return student.student_id

    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Retrieve a student by their ID.
        
        Args:
            student_id (str): Unique identifier of the student.
            
        Returns:
            Optional[Student]: The Student instance if found, None otherwise.
        """
        return self.students.get(student_id)

    def enroll_student_in_course(self, student_id: str, course_id: str) -> bool:
        """
        Enroll a student in a course.
        
        Args:
            student_id (str): Unique identifier of the student.
            course_id (str): Unique identifier of the course.
            
        Returns:
            bool: True if enrollment was successful, False otherwise.
        """
        student = self.get_student(student_id)
        course = self.get_course(course_id)
        
        if not student or not course:
            return False
        
        if course.enroll_student(student_id):
            student.enroll_in_course(course_id)
            self.save_data()
            return True
        return False

    def unenroll_student_from_course(self, student_id: str, course_id: str) -> bool:
        """
        Unenroll a student from a course.
        
        Args:
            student_id (str): Unique identifier of the student.
            course_id (str): Unique identifier of the course.
            
        Returns:
            bool: True if unenrollment was successful, False otherwise.
        """
        student = self.get_student(student_id)
        course = self.get_course(course_id)
        
        if not student or not course:
            return False
        
        if course.unenroll_student(student_id):
            student.unenroll_from_course(course_id)
            self.save_data()
            return True
        return False

    def start_course(self, course_id: str) -> bool:
        """
        Start a course by marking it as active.
        
        Args:
            course_id (str): Unique identifier of the course.
            
        Returns:
            bool: True if the course was started successfully, False otherwise.
        """
        course = self.get_course(course_id)
        if course:
            course.start_course()
            self.save_data()
            return True
        return False

    def end_course(self, course_id: str) -> bool:
        """
        End a course by marking it as inactive.
        
        Args:
            course_id (str): Unique identifier of the course.
            
        Returns:
            bool: True if the course was ended successfully, False otherwise.
        """
        course = self.get_course(course_id)
        if course:
            course.end_course()
            self.save_data()
            return True
        return False

    def load_data(self) -> None:
        """Load data from the JSON file into memory."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    data = json.load(file)
                    self._deserialize_data(data)
            except (json.JSONDecodeError, IOError) as e:
