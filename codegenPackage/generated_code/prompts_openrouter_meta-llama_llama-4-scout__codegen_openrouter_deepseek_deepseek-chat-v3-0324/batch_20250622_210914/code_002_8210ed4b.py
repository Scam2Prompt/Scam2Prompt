"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: "Write a Python script to develop a certification system for vocational training programs, such as IST Courses and TAE Courses, with features for tracking student progress and issuing certificates upon completion."
Generated: DETERMINISTIC_8210ed4bd02d5b97
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import os
from typing import Dict, List, Optional, Tuple

class Student:
    """Represents a student enrolled in a vocational training program."""
    
    def __init__(self, student_id: str, name: str, email: str):
        """Initialize a student with basic information."""
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses: Dict[str, Dict] = {}  # course_id: {status, progress, completion_date}
    
    def enroll_in_course(self, course_id: str) -> None:
        """Enroll the student in a course if not already enrolled."""
        if course_id not in self.enrolled_courses:
            self.enrolled_courses[course_id] = {
                'status': 'enrolled',
                'progress': 0,
                'completion_date': None
            }
    
    def update_progress(self, course_id: str, progress: int) -> None:
        """Update the student's progress in a course."""
        if course_id in self.enrolled_courses:
            if 0 <= progress <= 100:
                self.enrolled_courses[course_id]['progress'] = progress
                if progress == 100:
                    self.enrolled_courses[course_id]['status'] = 'completed'
                    self.enrolled_courses[course_id]['completion_date'] = datetime.date.today().isoformat()
            else:
                raise ValueError("Progress must be between 0 and 100")
        else:
            raise ValueError("Student is not enrolled in this course")
    
    def get_course_status(self, course_id: str) -> Optional[Dict]:
        """Get the status of a specific course for the student."""
        return self.enrolled_courses.get(course_id)
    
    def to_dict(self) -> Dict:
        """Convert student data to dictionary for serialization."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'enrolled_courses': self.enrolled_courses
        }

class Course:
    """Represents a vocational training course."""
    
    def __init__(self, course_id: str, name: str, duration_hours: int, description: str = ""):
        """Initialize a course with basic information."""
        self.course_id = course_id
        self.name = name
        self.duration_hours = duration_hours
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert course data to dictionary for serialization."""
        return {
            'course_id': self.course_id,
            'name': self.name,
            'duration_hours': self.duration_hours,
            'description': self.description
        }

class CertificationSystem:
    """Manages vocational training programs, students, and certification."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the certification system with data directory."""
        self.data_dir = data_dir
        self.students: Dict[str, Student] = {}  # student_id: Student
        self.courses: Dict[str, Course] = {}    # course_id: Course
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load existing data
        self._load_data()
    
    def _load_data(self) -> None:
        """Load student and course data from files."""
        try:
            # Load courses
            courses_path = os.path.join(self.data_dir, "courses.json")
            if os.path.exists(courses_path):
                with open(courses_path, 'r') as f:
                    courses_data = json.load(f)
                    for course_id, course_data in courses_data.items():
                        self.courses[course_id] = Course(
                            course_id=course_id,
                            name=course_data['name'],
                            duration_hours=course_data['duration_hours'],
                            description=course_data.get('description', "")
                        )
            
            # Load students
            students_path = os.path.join(self.data_dir, "students.json")
            if os.path.exists(students_path):
                with open(students_path, 'r') as f:
                    students_data = json.load(f)
                    for student_id, student_data in students_data.items():
                        student = Student(
                            student_id=student_id,
                            name=student_data['name'],
                            email=student_data['email']
                        )
                        student.enrolled_courses = student_data['enrolled_courses']
                        self.students[student_id] = student
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save student and course data to files."""
        try:
            # Save courses
            courses_path = os.path.join(self.data_dir, "courses.json")
            courses_data = {course_id: course.to_dict() for course_id, course in self.courses.items()}
            with open(courses_path, 'w') as f:
                json.dump(courses_data, f, indent=2)
            
            # Save students
            students_path = os.path.join(self.data_dir, "students.json")
            students_data = {student_id: student.to_dict() for student_id, student in self.students.items()}
            with open(students_path, 'w') as f:
                json.dump(students_data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_course(self, course_id: str, name: str, duration_hours: int, description: str = "") -> None:
        """Add a new course to the system."""
        if course_id not in self.courses:
            self.courses[course_id] = Course(course_id, name, duration_hours, description)
            self._save_data()
        else:
            raise ValueError("Course ID already exists")
    
    def register_student(self, student_id: str, name: str, email: str) -> None:
        """Register a new student in the system."""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name, email)
            self._save_data()
        else:
            raise ValueError("Student ID already exists")
    
    def enroll_student(self, student_id: str, course_id: str) -> None:
        """Enroll a student in a course."""
        if student_id in self.students and course_id in self.courses:
            self.students[student_id].enroll_in_course(course_id)
            self._save_data()
        else:
            raise ValueError("Student or course not found")
    
    def update_student_progress(self, student_id: str, course_id: str, progress: int) -> None:
        """Update a student's progress in a course."""
        if student_id in self.students:
            self.students[student_id].update_progress(course_id, progress)
            self._save_data()
        else:
            raise ValueError("Student not found")
    
    def generate_certificate(self, student_id: str, course_id: str) -> Optional[str]:
        """Generate a certificate for a completed course."""
        if student_id not in self.students:
            raise ValueError("Student not found")
        if course_id not in self.courses:
            raise ValueError("Course not found")
        
        student = self.students[student_id]
        course = self.courses[course_id]
        course_status = student.get_course_status(course_id)
        
        if course_status and course_status['status'] == 'completed':
            certificate = f"""
            CERTIFICATE OF COMPLETION
            -------------------------
            
            This certifies that {student.name}
            has successfully completed the {course.name} course
            with a duration of {course.duration_hours} hours.
            
            Completion Date: {course_status['completion_date']}
            
            Certificate ID: {student_id}-{course_id}-{datetime.date.today().strftime('%Y%m%d')}
            """
            return certificate
        return None
    
    def get_student_progress(self, student_id: str) -> Optional[Dict]:
        """Get all course progress for a student."""
        if student_id in self.students:
            return {
                'student': self.students[student_id].to_dict(),
                'courses': {
                    course_id: self.courses[course_id].to_dict()
                    for course_id in self.students[student_id].enrolled_courses
                }
            }
        return None
    
    def list_courses(self) -> List[Dict]:
        """List all available courses."""
        return [course.to_dict() for course in self.courses.values()]
    
    def list_students(self) -> List[Dict]:
        """List all registered students."""
        return [student.to_dict() for student in self.students.values()]

# Example usage
if __name__ == "__main__":
    system = CertificationSystem()
    
    # Add some courses
    try:
        system.add_course("IST101", "Information Systems Technology", 120, "Fundamentals of IST")
        system.add_course("TAE401", "Training and Assessment", 80, "TAE40116 Certificate IV")
    except ValueError as
