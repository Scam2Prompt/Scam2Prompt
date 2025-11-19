"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Write a program to manage multi-sectoral vocational skills training, referencing MIEC's offerings in banking, finance, retail sales enablement, and digital media marketing.
Generated: DETERMINISTIC_122ab28527711bad
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
MIEC Vocational Skills Training Management System

This program manages multi-sectoral vocational skills training programs
offered by MIEC, including banking, finance, retail sales enablement,
and digital media marketing.

Features:
- Student enrollment and management
- Course management
- Training progress tracking
- Reporting and analytics
"""

import json
from datetime import datetime
from typing import List, Dict, Optional, Union
import csv
import os

class Student:
    """Represents a student enrolled in vocational training programs."""
    
    def __init__(self, student_id: str, name: str, email: str, phone: str):
        """
        Initialize a student with basic information.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            email: Contact email address
            phone: Contact phone number
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.enrolled_courses = []
        self.completed_courses = []
        self.attendance = {}
        self.grades = {}
    
    def enroll_in_course(self, course_code: str) -> bool:
        """
        Enroll the student in a course.
        
        Args:
            course_code: Code of the course to enroll in
            
        Returns:
            bool: True if enrollment was successful, False otherwise
        """
        if course_code not in self.enrolled_courses:
            self.enrolled_courses.append(course_code)
            return True
        return False
    
    def complete_course(self, course_code: str, grade: float) -> bool:
        """
        Mark a course as completed with a grade.
        
        Args:
            course_code: Code of the completed course
            grade: Final grade achieved (0-100)
            
        Returns:
            bool: True if completion was recorded, False otherwise
        """
        if course_code in self.enrolled_courses:
            self.enrolled_courses.remove(course_code)
            self.completed_courses.append(course_code)
            self.grades[course_code] = grade
            return True
        return False
    
    def record_attendance(self, course_code: str, date: str, present: bool) -> None:
        """
        Record attendance for a specific course session.
        
        Args:
            course_code: Code of the course
            date: Date of the session (YYYY-MM-DD)
            present: Whether the student was present
        """
        if course_code not in self.attendance:
            self.attendance[course_code] = {}
        self.attendance[course_code][date] = present
    
    def get_attendance_rate(self, course_code: str) -> float:
        """
        Calculate attendance rate for a course.
        
        Args:
            course_code: Code of the course
            
        Returns:
            float: Attendance rate (0-1)
        """
        if course_code not in self.attendance or not self.attendance[course_code]:
            return 0.0
        
        total_sessions = len(self.attendance[course_code])
        attended = sum(1 for present in self.attendance[course_code].values() if present)
        return attended / total_sessions
    
    def to_dict(self) -> Dict:
        """Convert student data to dictionary for serialization."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'enrolled_courses': self.enrolled_courses,
            'completed_courses': self.completed_courses,
            'attendance': self.attendance,
            'grades': self.grades
        }

class Course:
    """Represents a vocational training course offered by MIEC."""
    
    SECTORS = {
        'BANK': 'Banking',
        'FIN': 'Finance',
        'RSE': 'Retail Sales Enablement',
        'DMM': 'Digital Media Marketing'
    }
    
    def __init__(self, code: str, title: str, sector: str, duration_weeks: int, capacity: int):
        """
        Initialize a course with basic information.
        
        Args:
            code: Unique course code
            title: Course title
            sector: Sector the course belongs to (BANK, FIN, RSE, DMM)
            duration_weeks: Duration in weeks
            capacity: Maximum number of students
        """
        if sector not in self.SECTORS:
            raise ValueError(f"Invalid sector. Must be one of: {list(self.SECTORS.keys())}")
        
        self.code = code
        self.title = title
        self.sector = sector
        self.duration_weeks = duration_weeks
        self.capacity = capacity
        self.enrolled_students = []
        self.schedule = []
    
    def add_student(self, student_id: str) -> bool:
        """
        Add a student to the course if capacity allows.
        
        Args:
            student_id: ID of the student to add
            
        Returns:
            bool: True if student was added, False if course is full
        """
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student_id)
            return True
        return False
    
    def remove_student(self, student_id: str) -> bool:
        """
        Remove a student from the course.
        
        Args:
            student_id: ID of the student to remove
            
        Returns:
            bool: True if student was removed, False if not found
        """
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            return True
        return False
    
    def add_session(self, date: str, topic: str, instructor: str) -> None:
        """
        Add a training session to the course schedule.
        
        Args:
            date: Date of the session (YYYY-MM-DD)
            topic: Session topic
            instructor: Instructor name
        """
        self.schedule.append({
            'date': date,
            'topic': topic,
            'instructor': instructor
        })
    
    def get_enrollment_count(self) -> int:
        """Get current number of enrolled students."""
        return len(self.enrolled_students)
    
    def to_dict(self) -> Dict:
        """Convert course data to dictionary for serialization."""
        return {
            'code': self.code,
            'title': self.title,
            'sector': self.sector,
            'duration_weeks': self.duration_weeks,
            'capacity': self.capacity,
            'enrolled_students': self.enrolled_students,
            'schedule': self.schedule
        }

class TrainingCenter:
    """Main class to manage MIEC vocational training programs."""
    
    def __init__(self):
        """Initialize the training center with empty datasets."""
        self.students = {}  # student_id: Student
        self.courses = {}   # course_code: Course
    
    def add_student(self, student_id: str, name: str, email: str, phone: str) -> bool:
        """
        Add a new student to the system.
        
        Args:
            student_id: Unique student ID
            name: Full name
            email: Email address
            phone: Phone number
            
        Returns:
            bool: True if student was added, False if student_id already exists
        """
        if student_id in self.students:
            return False
        
        self.students[student_id] = Student(student_id, name, email, phone)
        return True
    
    def add_course(self, code: str, title: str, sector: str, duration_weeks: int, capacity: int) -> bool:
        """
        Add a new course to the system.
        
        Args:
            code: Unique course code
            title: Course title
            sector: Sector (BANK, FIN, RSE, DMM)
            duration_weeks: Duration in weeks
            capacity: Maximum students
            
        Returns:
            bool: True if course was added, False if course code exists
        """
        if code in self.courses:
            return False
        
        self.courses[code] = Course(code, title, sector, duration_weeks, capacity)
        return True
    
    def enroll_student(self, student_id: str, course_code: str) -> bool:
        """
        Enroll a student in a course.
        
        Args:
            student_id: ID of the student
            course_code: Code of the course
            
        Returns:
            bool: True if enrollment was successful, False otherwise
        """
        if student_id not in self.students or course_code not in self.courses:
            return False
        
        student = self.students[student_id]
        course = self.courses[course_code]
        
        if student.enroll_in_course(course_code) and course.add_student(student_id):
            return True
        
        return False
    
    def record_attendance(self, student_id: str, course_code: str, date: str, present: bool) -> bool:
        """
        Record attendance for a student in a course session.
        
        Args:
            student_id: ID of the student
            course_code: Code of the course
            date: Date of session
            present: Whether
