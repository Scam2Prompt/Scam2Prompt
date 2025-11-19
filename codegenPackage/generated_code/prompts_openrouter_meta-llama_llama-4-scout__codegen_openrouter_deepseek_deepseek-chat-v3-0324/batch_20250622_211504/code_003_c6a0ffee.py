"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Design a system for online course management, inspired by the online education programs at ISIV, including Análisis de Sistemas and Negocios Digitales."
Generated: DETERMINISTIC_c6a0ffee1ae3f1c6
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Online Course Management System
# Inspired by ISIV's online education programs

from datetime import datetime
from typing import List, Dict, Optional
import uuid
import json
from enum import Enum, auto

class CourseLevel(Enum):
    BEGINNER = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()

class CourseStatus(Enum):
    DRAFT = auto()
    PUBLISHED = auto()
    ARCHIVED = auto()

class UserRole(Enum):
    ADMIN = auto()
    INSTRUCTOR = auto()
    STUDENT = auto()

class User:
    def __init__(self, user_id: str, name: str, email: str, role: UserRole):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role
        self.enrolled_courses: List[str] = []

    def enroll_in_course(self, course_id: str) -> None:
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)

    def to_dict(self) -> Dict:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "role": self.role.name,
            "enrolled_courses": self.enrolled_courses
        }

class Course:
    def __init__(self, course_id: str, title: str, description: str, 
                 instructor_id: str, level: CourseLevel, 
                 status: CourseStatus = CourseStatus.DRAFT):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor_id = instructor_id
        self.level = level
        self.status = status
        self.modules: List[Module] = []
        self.students: List[str] = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_module(self, module: 'Module') -> None:
        self.modules.append(module)
        self.updated_at = datetime.now()

    def enroll_student(self, student_id: str) -> bool:
        if student_id not in self.students:
            self.students.append(student_id)
            self.updated_at = datetime.now()
            return True
        return False

    def publish(self) -> None:
        if self.status == CourseStatus.DRAFT:
            self.status = CourseStatus.PUBLISHED
            self.updated_at = datetime.now()

    def archive(self) -> None:
        self.status = CourseStatus.ARCHIVED
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        return {
            "course_id": self.course_id,
            "title": self.title,
            "description": self.description,
            "instructor_id": self.instructor_id,
            "level": self.level.name,
            "status": self.status.name,
            "modules": [module.to_dict() for module in self.modules],
            "students": self.students,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class Module:
    def __init__(self, module_id: str, title: str, description: str):
        self.module_id = module_id
        self.title = title
        self.description = description
        self.lessons: List[Lesson] = []

    def add_lesson(self, lesson: 'Lesson') -> None:
        self.lessons.append(lesson)

    def to_dict(self) -> Dict:
        return {
            "module_id": self.module_id,
            "title": self.title,
            "description": self.description,
            "lessons": [lesson.to_dict() for lesson in self.lessons]
        }

class Lesson:
    def __init__(self, lesson_id: str, title: str, content: str, duration_minutes: int):
        self.lesson_id = lesson_id
        self.title = title
        self.content = content
        self.duration_minutes = duration_minutes

    def to_dict(self) -> Dict:
        return {
            "lesson_id": self.lesson_id,
            "title": self.title,
            "content": self.content,
            "duration_minutes": self.duration_minutes
        }

class CourseManagementSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.courses: Dict[str, Course] = {}

    def add_user(self, name: str, email: str, role: UserRole) -> User:
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email, role)
        self.users[user_id] = user
        return user

    def create_course(self, title: str, description: str, 
                     instructor_id: str, level: CourseLevel) -> Course:
        if instructor_id not in self.users or self.users[instructor_id].role != UserRole.INSTRUCTOR:
            raise ValueError("Instructor not found or invalid role")
        
        course_id = str(uuid.uuid4())
        course = Course(course_id, title, description, instructor_id, level)
        self.courses[course_id] = course
        return course

    def enroll_student(self, course_id: str, student_id: str) -> bool:
        if course_id not in self.courses:
            raise ValueError("Course not found")
        if student_id not in self.users or self.users[student_id].role != UserRole.STUDENT:
            raise ValueError("Student not found or invalid role")
        
        success = self.courses[course_id].enroll_student(student_id)
        if success:
            self.users[student_id].enroll_in_course(course_id)
        return success

    def get_course_by_id(self, course_id: str) -> Optional[Course]:
        return self.courses.get(course_id)

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def save_to_file(self, filename: str) -> None:
        data = {
            "users": [user.to_dict() for user in self.users.values()],
            "courses": [course.to_dict() for course in self.courses.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.users.clear()
        self.courses.clear()
        
        for user_data in data.get("users", []):
            user = User(
                user_data["user_id"],
                user_data["name"],
                user_data["email"],
                UserRole[user_data["role"]]
            )
            user.enrolled_courses = user_data["enrolled_courses"]
            self.users[user.user_id] = user
        
        for course_data in data.get("courses", []):
            course = Course(
                course_data["course_id"],
                course_data["title"],
                course_data["description"],
                course_data["instructor_id"],
                CourseLevel[course_data["level"]],
                CourseStatus[course_data["status"]]
            )
            course.students = course_data["students"]
            course.created_at = datetime.fromisoformat(course_data["created_at"])
            course.updated_at = datetime.fromisoformat(course_data["updated_at"])
            
            for module_data in course_data["modules"]:
                module = Module(
                    module_data["module_id"],
                    module_data["title"],
                    module_data["description"]
                )
                for lesson_data in module_data["lessons"]:
                    lesson = Lesson(
                        lesson_data["lesson_id"],
                        lesson_data["title"],
                        lesson_data["content"],
                        lesson_data["duration_minutes"]
                    )
                    module.add_lesson(lesson)
                course.add_module(module)
            
            self.courses[course.course_id] = course

# Example usage
if __name__ == "__main__":
    system = CourseManagementSystem()
    
    # Create admin
    admin = system.add_user("Admin User", "admin@isiv.edu", UserRole.ADMIN)
    
    # Create instructor
    instructor = system.add_user("Prof. Smith", "smith@isiv.edu", UserRole.INSTRUCTOR)
    
    # Create course
    analysis_course = system.create_course(
        "Análisis de Sistemas",
        "Fundamentos de análisis de sistemas",
        instructor.user_id,
        CourseLevel.INTERMEDIATE
    )
    
    # Create module and lessons
    module1 = Module("m1", "Introducción", "Conceptos básicos")
    module1.add_lesson(Lesson("l1", "Qué es el análisis", "Contenido...", 45))
    module1.add_lesson(Lesson("l2", "Metodologías", "Contenido...", 60))
    analysis_course.add_module(module1)
    
    # Publish course
    analysis_course.publish()
    
    # Create student and enroll
    student = system.add_user("Juan Perez", "juan@student.edu", UserRole.STUDENT)
    system.enroll_student(analysis_course.c
