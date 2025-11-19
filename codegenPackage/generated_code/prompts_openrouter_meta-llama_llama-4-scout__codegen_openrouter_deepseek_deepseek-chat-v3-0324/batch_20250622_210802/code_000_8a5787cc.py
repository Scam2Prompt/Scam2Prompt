"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: "Generate a Python script to manage student enrollment for admission exam preparation courses, including personalized classes and flexible scheduling."
Generated: DETERMINISTIC_8a5787cc828bd2ea
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class Student:
    """Represents a student enrolled in the preparation course."""
    
    def __init__(self, student_id: str, name: str, email: str, phone: str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.enrolled_courses: List[str] = []
        self.schedule: Dict[str, List[Tuple[datetime, datetime]]] = {}

    def enroll_in_course(self, course_id: str) -> None:
        """Enrolls the student in a course."""
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)

    def schedule_class(self, course_id: str, start_time: datetime, end_time: datetime) -> bool:
        """Schedules a class for the student."""
        if course_id not in self.enrolled_courses:
            return False
        
        if course_id not in self.schedule:
            self.schedule[course_id] = []
        
        # Check for schedule conflicts
        for scheduled_start, scheduled_end in self.schedule[course_id]:
            if not (end_time <= scheduled_start or start_time >= scheduled_end):
                return False
        
        self.schedule[course_id].append((start_time, end_time))
        return True

    def to_dict(self) -> Dict:
        """Converts the student object to a dictionary for serialization."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'enrolled_courses': self.enrolled_courses,
            'schedule': {
                course_id: [
                    (start.isoformat(), end.isoformat()) 
                    for start, end in times
                ] 
                for course_id, times in self.schedule.items()
            }
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        """Creates a student object from a dictionary."""
        student = cls(
            data['student_id'],
            data['name'],
            data['email'],
            data['phone']
        )
        student.enrolled_courses = data.get('enrolled_courses', [])
        
        schedule = data.get('schedule', {})
        for course_id, times in schedule.items():
            student.schedule[course_id] = [
                (datetime.fromisoformat(start), datetime.fromisoformat(end))
                for start, end in times
            ]
        
        return student

class Course:
    """Represents an admission exam preparation course."""
    
    def __init__(self, course_id: str, name: str, description: str, duration_hours: int):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.duration_hours = duration_hours
        self.students_enrolled: List[str] = []

    def add_student(self, student_id: str) -> None:
        """Adds a student to the course."""
        if student_id not in self.students_enrolled:
            self.students_enrolled.append(student_id)

    def to_dict(self) -> Dict:
        """Converts the course object to a dictionary for serialization."""
        return {
            'course_id': self.course_id,
            'name': self.name,
            'description': self.description,
            'duration_hours': self.duration_hours,
            'students_enrolled': self.students_enrolled
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Course':
        """Creates a course object from a dictionary."""
        return cls(
            data['course_id'],
            data['name'],
            data['description'],
            data['duration_hours']
        )

class EnrollmentSystem:
    """Manages student enrollment and scheduling for exam preparation courses."""
    
    def __init__(self, data_file: str = 'enrollment_data.json'):
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}
        self.load_data()

    def add_student(self, student_id: str, name: str, email: str, phone: str) -> bool:
        """Adds a new student to the system."""
        if student_id in self.students:
            return False
        
        self.students[student_id] = Student(student_id, name, email, phone)
        self.save_data()
        return True

    def add_course(self, course_id: str, name: str, description: str, duration_hours: int) -> bool:
        """Adds a new course to the system."""
        if course_id in self.courses:
            return False
        
        self.courses[course_id] = Course(course_id, name, description, duration_hours)
        self.save_data()
        return True

    def enroll_student(self, student_id: str, course_id: str) -> bool:
        """Enrolls a student in a course."""
        if student_id not in self.students or course_id not in self.courses:
            return False
        
        self.students[student_id].enroll_in_course(course_id)
        self.courses[course_id].add_student(student_id)
        self.save_data()
        return True

    def schedule_class(
        self, 
        student_id: str, 
        course_id: str, 
        start_time: datetime, 
        duration: timedelta
    ) -> bool:
        """Schedules a class for a student in a course."""
        if student_id not in self.students or course_id not in self.courses:
            return False
        
        end_time = start_time + duration
        return self.students[student_id].schedule_class(course_id, start_time, end_time)

    def get_student_schedule(self, student_id: str) -> Optional[Dict]:
        """Retrieves a student's schedule."""
        if student_id not in self.students:
            return None
        
        student = self.students[student_id]
        return {
            'student_id': student.student_id,
            'name': student.name,
            'schedule': {
                course_id: [
                    (start.strftime('%Y-%m-%d %H:%M'), end.strftime('%Y-%m-%d %H:%M'))
                    for start, end in times
                ]
                for course_id, times in student.schedule.items()
            }
        }

    def load_data(self) -> None:
        """Loads data from the storage file."""
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.students = {
                    student_id: Student.from_dict(student_data)
                    for student_id, student_data in data.get('students', {}).items()
                }
                self.courses = {
                    course_id: Course.from_dict(course_data)
                    for course_id, course_data in data.get('courses', {}).items()
                }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")

    def save_data(self) -> None:
        """Saves data to the storage file."""
        data = {
            'students': {
                student_id: student.to_dict()
                for student_id, student in self.students.items()
            },
            'courses': {
                course_id: course.to_dict()
                for course_id, course in self.courses.items()
            }
        }
        
        try:
            with open(self.data_file, 'w') as file:
                json.dump(data, file, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

def main():
    """Example usage of the enrollment system."""
    system = EnrollmentSystem()
    
    # Add some courses
    system.add_course('math101', 'Mathematics Basics', 'Fundamental math concepts', 20)
    system.add_course('eng101', 'English Fundamentals', 'Basic English skills', 15)
    
    # Add some students
    system.add_student('s001', 'John Doe', 'john@example.com', '1234567890')
    system.add_student('s002', 'Jane Smith', 'jane@example.com', '0987654321')
    
    # Enroll students in courses
    system.enroll_student('s001', 'math101')
    system.enroll_student('s001', 'eng101')
    system.enroll_student('s002', 'math101')
    
    # Schedule classes
    now = datetime.now()
    system.schedule_class('s001', 'math101', now, timedelta(hours=1))
    system.schedule_class('s001', 'eng101', now + timedelta(days=1), timedelta(hours=1.5))
    system.schedule_class('s002', 'math101', now + timedelta(days=2), timedelta(hours=2))
    
    # Print a student's schedule
    print(json.dumps(system.get_student_schedule('s
