"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Generate a Python code snippet to manage student enrollment and course scheduling for a music school like Московский Колледж Импровизационной Музыки, considering factors like faculty availability, room assignments, and student prerequisites.
Generated: DETERMINISTIC_81a0d6ff3ca457c6
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional, Set
from enum import Enum
from dataclasses import dataclass


class CourseLevel(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3


class InstrumentType(Enum):
    PIANO = "Piano"
    GUITAR = "Guitar"
    VIOLIN = "Violin"
    DRUMS = "Drums"
    VOCALS = "Vocals"
    SAXOPHONE = "Saxophone"


@dataclass
class Faculty:
    id: int
    name: str
    instruments: List[InstrumentType]
    availability: Dict[datetime.date, List[datetime.time]]


@dataclass
class Room:
    id: int
    name: str
    capacity: int
    instruments_available: List[InstrumentType]


@dataclass
class Student:
    id: int
    name: str
    level: CourseLevel
    instruments: List[InstrumentType]
    completed_courses: Set[int]


@dataclass
class Course:
    id: int
    name: str
    level: CourseLevel
    instrument: InstrumentType
    prerequisites: Set[int]
    faculty_id: int
    room_id: int
    schedule: Dict[datetime.date, List[datetime.time]]
    max_students: int


class EnrollmentSystem:
    def __init__(self):
        self.students: Dict[int, Student] = {}
        self.courses: Dict[int, Course] = {}
        self.faculty: Dict[int, Faculty] = {}
        self.rooms: Dict[int, Room] = {}
        self.enrollments: Dict[int, Set[int]] = {}  # course_id: set of student_ids

    def add_student(self, student: Student) -> None:
        """Add a student to the system."""
        if student.id in self.students:
            raise ValueError(f"Student with ID {student.id} already exists")
        self.students[student.id] = student

    def add_course(self, course: Course) -> None:
        """Add a course to the system."""
        if course.id in self.courses:
            raise ValueError(f"Course with ID {course.id} already exists")
        if course.faculty_id not in self.faculty:
            raise ValueError(f"Faculty with ID {course.faculty_id} does not exist")
        if course.room_id not in self.rooms:
            raise ValueError(f"Room with ID {course.room_id} does not exist")
        self.courses[course.id] = course
        self.enrollments[course.id] = set()

    def add_faculty(self, faculty: Faculty) -> None:
        """Add a faculty member to the system."""
        if faculty.id in self.faculty:
            raise ValueError(f"Faculty with ID {faculty.id} already exists")
        self.faculty[faculty.id] = faculty

    def add_room(self, room: Room) -> None:
        """Add a room to the system."""
        if room.id in self.rooms:
            raise ValueError(f"Room with ID {room.id} already exists")
        self.rooms[room.id] = room

    def enroll_student(self, student_id: int, course_id: int) -> bool:
        """
        Enroll a student in a course if prerequisites are met and there's capacity.
        Returns True if enrollment was successful, False otherwise.
        """
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist")
        if course_id not in self.courses:
            raise ValueError(f"Course with ID {course_id} does not exist")

        student = self.students[student_id]
        course = self.courses[course_id]

        # Check prerequisites
        if not course.prerequisites.issubset(student.completed_courses):
            return False

        # Check student level
        if student.level.value < course.level.value:
            return False

        # Check instrument compatibility
        if course.instrument not in student.instruments:
            return False

        # Check capacity
        if len(self.enrollments[course_id]) >= course.max_students:
            return False

        # Check faculty availability
        faculty = self.faculty[course.faculty_id]
        for date, times in course.schedule.items():
            if date not in faculty.availability or not all(t in faculty.availability[date] for t in times):
                return False

        # Check room availability (simplified - would need more complex scheduling in production)
        # In a real system, we'd need to track room bookings separately

        self.enrollments[course_id].add(student_id)
        return True

    def get_student_schedule(self, student_id: int) -> Dict[int, Course]:
        """Get all courses a student is enrolled in."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist")
        
        return {
            course_id: self.courses[course_id]
            for course_id in self.enrollments
            if student_id in self.enrollments[course_id]
        }

    def get_course_roster(self, course_id: int) -> List[Student]:
        """Get all students enrolled in a course."""
        if course_id not in self.courses:
            raise ValueError(f"Course with ID {course_id} does not exist")
        
        return [
            self.students[student_id]
            for student_id in self.enrollments.get(course_id, set())
        ]

    def check_room_availability(self, room_id: int, date: datetime.date, time: datetime.time) -> bool:
        """Check if a room is available at a given date and time."""
        if room_id not in self.rooms:
            raise ValueError(f"Room with ID {room_id} does not exist")
        
        # In a real system, we'd need to check against scheduled courses
        # This is a simplified version
        for course in self.courses.values():
            if course.room_id == room_id and date in course.schedule and time in course.schedule[date]:
                return False
        return True

    def complete_course(self, student_id: int, course_id: int) -> None:
        """Mark a course as completed for a student."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist")
        if course_id not in self.courses:
            raise ValueError(f"Course with ID {course_id} does not exist")
        if course_id not in self.enrollments or student_id not in self.enrollments[course_id]:
            raise ValueError(f"Student {student_id} is not enrolled in course {course_id}")
        
        self.students[student_id].completed_courses.add(course_id)
        self.enrollments[course_id].remove(student_id)
```
